# backend/pipeline/crafter.py
# ---------------------------------------------------------------
# Multi-Agent Generative AI pipeline for crafting new emails from
# scratch. This is Member 3's core AI responsibility — takes a
# user's brief intent/prompt and a desired tone, then uses Gemini
# to generate a complete, polished email. After generation, the
# draft is passed through the Quality Review Agent for validation.
#
# Settings integration: reads stored tone and vocabulary preferences
# from the database and injects them into the system prompt.
# ---------------------------------------------------------------

from db.sqlite import get_ai_settings
from pipeline.gemini import call_draft
from pipeline.reviewer import review_draft


# ---------------------------------------------------------------------------
# System prompt template — instructs Gemini on tone matching and output schema
# User settings (tone, vocabulary) are injected at call time.
# ---------------------------------------------------------------------------

SYSTEM_TEMPLATE = (
    "You are a talented, creative email ghostwriter who transforms brief user intents "
    "into polished, complete, ready-to-send emails that sound like a real person wrote them.\n\n"
    "CRITICAL RULES:\n"
    "1. NEVER copy or echo the user's prompt text verbatim. The user gives you a BRIEF INTENT "
    "   (e.g., 'ask Alex for Q3 report update'). You must EXPAND and TRANSFORM this into a "
    "   complete, natural email with proper structure.\n"
    "2. ALWAYS include a warm greeting (e.g., 'Hi Alex,' or 'Dear Sarah,') appropriate to the tone.\n"
    "3. ALWAYS include a proper sign-off (e.g., 'Best regards,', 'Cheers,', 'Warm regards,') "
    "   followed by a newline and '[Your Name]'.\n"
    "4. Write at MINIMUM 4-6 sentences. The email should feel COMPLETE — not a stub.\n"
    "5. Make the email feel human and genuine — use natural transitions, vary sentence length, "
    "   show personality. Avoid corporate jargon and robotic phrasing.\n"
    "6. Add relevant context and details that a real person would include — don't just "
    "   restate the intent, flesh it out into a convincing, natural message.\n\n"
    "USER'S WRITING PREFERENCES (from their saved settings):\n"
    "- Default tone preference: {default_tone}\n"
    "- Writing traits to emphasise: {vocabulary}\n"
    "- Apply these traits naturally without forcing them.\n\n"
    "TONE GUIDE — match the REQUESTED tone exactly:\n"
    "- professional: formal but warm language, proper greeting (Dear/Hello), respectful and "
    "  polished. Show competence and courtesy. Use complete sentences.\n"
    "- casual: friendly, relaxed, first-name basis, conversational. Use contractions freely. "
    "  Can include light humor or enthusiasm. Feel like texting a friend but in email form.\n"
    "- direct: clear and to the point, but still polite. Lead with the main ask/point. "
    "  Minimal small talk but still include greeting and sign-off.\n"
    "- persuasive: compelling, action-oriented, emphasise benefits. Build a case. "
    "  Use confident language and clear calls to action.\n\n"
    "Return ONLY valid JSON with exactly these two keys:\n"
    '  "generated_email": (string — the FULL email text including greeting and sign-off, '
    "minimum 4 sentences, NEVER a copy of the user's prompt),\n"
    '  "subject_suggestion": (string — a concise, natural subject line; if one was provided, '
    "refine it to sound better).\n"
    "Do NOT add any other keys. Do NOT wrap the JSON in markdown code fences.\n\n"
    "IMPORTANT: The tone for THIS specific email is: {requested_tone}. Match it exactly."
)


# ---------------------------------------------------------------------------
# Quick-prompt templates — pre-built intents for common email scenarios
# ---------------------------------------------------------------------------

QUICK_PROMPTS = {
    "follow_up": (
        "Write a polite follow-up to my previous email. "
        "Ask for an update on the matter and offer to help if needed."
    ),
    "schedule_meeting": (
        "Propose a meeting to discuss the topic. "
        "Suggest two or three possible time slots and ask for their preference."
    ),
    "polite_decline": (
        "Politely decline the request or invitation. "
        "Express gratitude, briefly explain why, and keep the door open for future collaboration."
    ),
    "thank_you": (
        "Write a sincere thank-you email. "
        "Acknowledge what the recipient did and express genuine appreciation."
    ),
    "apology": (
        "Write a professional apology email. "
        "Take responsibility, explain briefly, and propose a resolution."
    ),
}


def _build_system_prompt(tone: str) -> str:
    """
    Builds the system prompt with injected user settings from the database.

    This makes the crafter 'settings-aware' — vocabulary traits and tone
    preferences saved on the Settings page flow into every email generation.

    Args:
        tone (str): the requested tone for this specific email

    Returns:
        str: fully assembled system prompt
    """
    settings = get_ai_settings()

    return SYSTEM_TEMPLATE.format(
        default_tone=settings["tone"],
        vocabulary=", ".join(settings["vocabulary"]),
        requested_tone=tone,
    )


def _extract_email_from_response(result):
    """
    Robustly extracts the generated email text from Gemini's JSON response.

    Gemini sometimes uses different key names for the generated email.
    This function checks multiple possible keys and returns the first
    non-empty value found.

    Args:
        result (dict): the parsed JSON response from Gemini

    Returns:
        str: the generated email text, or empty string if not found
    """
    # Try all possible key names Gemini might use
    possible_keys = [
        "generated_email",
        "email",
        "body",
        "email_body",
        "draft",
        "message",
        "content",
        "text",
        "reply",
        "email_text",
    ]

    for key in possible_keys:
        value = result.get(key, "")
        if value and isinstance(value, str) and len(value.strip()) > 10:
            return value.strip()

    # Last resort: if the result is a dict with only one string value, use it
    for key, value in result.items():
        if isinstance(value, str) and len(value.strip()) > 30:
            return value.strip()

    return ""


def _extract_subject_from_response(result, fallback=""):
    """
    Robustly extracts the suggested subject from Gemini's JSON response.

    Args:
        result   (dict): the parsed JSON response from Gemini
        fallback (str):  fallback subject if none found

    Returns:
        str: subject suggestion
    """
    possible_keys = [
        "subject_suggestion",
        "subject",
        "suggested_subject",
        "email_subject",
        "title",
    ]

    for key in possible_keys:
        value = result.get(key, "")
        if value and isinstance(value, str) and len(value.strip()) > 2:
            return value.strip()

    return fallback or "No subject"


def craft_email(prompt, tone="professional", recipient="", subject=""):
    """
    Multi-agent email crafter: generates a complete email using Gemini based
    on the user's intent, then passes it through the Quality Review Agent.

    If the reviewer rejects the draft (score < 0.7), the improved version
    from the reviewer is used instead — ensuring every crafted email meets
    a minimum quality bar.

    Args:
        prompt    (str): what the user wants to say (brief description)
        tone      (str): one of 'professional', 'casual', 'direct', 'persuasive'
        recipient (str): recipient name or email address (optional)
        subject   (str): desired subject line (optional)

    Returns:
        dict: {generated_email, subject_suggestion, review_score, review_feedback}
    """
    print(f"[Crafter] Generating — tone: {tone}, prompt: '{prompt[:80]}...'")

    # Step 1: Build settings-aware system prompt
    system = _build_system_prompt(tone)

    user_prompt = (
        f"Tone: {tone}\n"
        f"Recipient: {recipient if recipient else 'not specified'}\n"
        f"Subject: {subject if subject else 'please suggest one'}\n\n"
        f"What I want to say:\n{prompt[:1500]}"
    )

    try:
        # Step 2: Generate the initial draft
        result = call_draft(user_prompt, system)
        print(f"[Crafter] Raw Gemini response keys: {list(result.keys())}")

        # Robustly extract email and subject from the response
        email_text = _extract_email_from_response(result)
        subject_text = _extract_subject_from_response(result, subject)

        if not email_text:
            print(f"[Crafter] Warning: could not extract email from: {result}")
            email_text = ""
            if result:
                first_key = next(iter(result), None)
                if first_key:
                    email_text = str(result[first_key])

        print(f"[Crafter] Initial draft — subject: '{subject_text[:60]}'")

        # Step 3: Quality Review Agent
        review_score = 0.7
        review_feedback = ""

        try:
            review = review_draft(
                original_subject=subject or subject_text,
                original_body=prompt,  # The user's intent serves as the "original"
                draft_text=email_text,
                requested_tone=tone,
            )

            review_score = review.get("score", 0.7)
            review_feedback = review.get("feedback", "")

            # If reviewer provided an improved version and rejected original
            if not review.get("approved", True) and review.get("improved_draft"):
                print(f"[Crafter] Reviewer rejected (score={review_score}) — using improved draft")
                email_text = review["improved_draft"]

            print(f"[Crafter] Review complete — score={review_score}")

        except Exception as rev_exc:
            print(f"[Crafter] Review step failed: {rev_exc} — skipping review")
            review_feedback = "Review skipped."

        return {
            "generated_email": email_text,
            "subject_suggestion": subject_text,
            "review_score": review_score,
            "review_feedback": review_feedback,
        }

    except Exception as exc:
        print(f"[Crafter] Gemini call failed: {exc} — returning fallback draft")
        return {
            "generated_email": (
                f"Dear {recipient or 'Recipient'},\n\n"
                f"I wanted to reach out regarding the following matter: {prompt}\n\n"
                f"I'd appreciate the opportunity to discuss this further at your convenience. "
                f"Please let me know a good time to connect.\n\n"
                f"Best regards,\n[Your Name]"
            ),
            "subject_suggestion": subject or "No subject",
            "review_score": 0.0,
            "review_feedback": "Draft generation failed — using fallback template.",
        }


def get_quick_prompts():
    """
    Returns the dictionary of pre-built quick-prompt templates.

    Returns:
        dict: {template_key: prompt_text}
    """
    return QUICK_PROMPTS
