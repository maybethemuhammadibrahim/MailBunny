# backend/pipeline/gemini.py
# ---------------------------------------------------------------
# Shared Google Gemini client used by all three pipeline modules
# (classifier, summarizer, drafter). Keeps the API key, model
# names, and retry logic in one place so each pipeline function
# stays short and focused on its prompt.
# ---------------------------------------------------------------

import json
import time

from config import AI_MODEL_DRAFT, AI_MODEL_FAST, GEMINI_API_KEY
from google import genai
from google.genai import types


def get_client():
    """
    Returns an authenticated Gemini client using the key from .env.
    The client is lightweight — creating one per call is fine.

    Returns:
        genai.Client: ready-to-use Gemini client
    """
    return genai.Client(api_key=GEMINI_API_KEY)


def call_gemini(prompt: str, system: str, model: str = None, temperature: float = None) -> dict:
    """
    Makes a single JSON-mode Gemini call with one automatic retry.

    response_mime_type='application/json' tells Gemini to always
    return valid JSON — no markdown fences, no extra text.
    If the first attempt fails (network glitch, rate-limit, etc.)
    we wait 2 seconds and try once more before raising.

    Args:
        prompt      (str):   the user-facing message (email content, etc.)
        system      (str):   the system instruction that shapes the output
        model       (str):   override the default model (uses AI_MODEL_FAST)
        temperature (float): controls randomness/creativity (0.0=deterministic,
                             1.0=very creative). Higher values produce more
                             natural, human-sounding text. Default None lets
                             the model use its own default (~0.4).

    Returns:
        dict: parsed JSON from Gemini's response

    Raises:
        Exception: re-raised after the second failed attempt
    """
    model = model or AI_MODEL_FAST
    client = get_client()

    # Build the generation config — optionally include temperature
    # Higher temperature = more creative, varied, human-like language
    config_kwargs = {
        "system_instruction": system,
        # Forces the model to return well-formed JSON every time
        "response_mime_type": "application/json",
    }
    if temperature is not None:
        config_kwargs["temperature"] = temperature

    config = types.GenerateContentConfig(**config_kwargs)

    # 3 attempts with increasing backoff — handles rate limits on free tier
    delays = [2, 12, 20]

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=config,
            )
            return json.loads(response.text)

        except Exception as exc:
            error_str = str(exc)
            is_rate_limit = "429" in error_str or "RESOURCE_EXHAUSTED" in error_str

            if attempt < 2:
                wait = delays[attempt]
                if is_rate_limit:
                    wait = max(wait, 12)  # Google says retry in ~11s
                print(f"[Gemini] Attempt {attempt+1} failed ({error_str[:80]}). Retrying in {wait}s…")
                time.sleep(wait)
            else:
                print(f"[Gemini] All 3 attempts failed: {error_str[:120]}")
                raise


# Convenience aliases so pipeline modules can import by intent
def call_fast(prompt: str, system: str) -> dict:
    """Calls the fast model (gemini-2.0-flash) — use for classify + summarize."""
    return call_gemini(prompt, system, model=AI_MODEL_FAST)


def call_draft(prompt: str, system: str) -> dict:
    """Calls the draft model with high temperature for natural, human-like text.
    Temperature 0.9 ensures the output sounds warm and conversational,
    not robotic or formulaic."""
    return call_gemini(prompt, system, model=AI_MODEL_DRAFT, temperature=0.9)


def call_review(prompt: str, system: str) -> dict:
    """Calls the fast model with LOW temperature for consistent, analytical
    review output. Temperature 0.2 keeps reviews factual and reproducible —
    we don't want creative freedom when grading quality."""
    return call_gemini(prompt, system, model=AI_MODEL_FAST, temperature=0.2)
