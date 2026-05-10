# backend/routes/crafter.py
# ---------------------------------------------------------------
# API endpoints for the AI Email Crafter page. Provides email
# generation from tone + prompt via Gemini, and quick-prompt
# template retrieval. Sending uses the existing Gmail send logic.
# ---------------------------------------------------------------

from fastapi import APIRouter
from pipeline.crafter import craft_email, get_quick_prompts
from pydantic import BaseModel

router = APIRouter()


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------


class CraftRequest(BaseModel):
    """
    Request body for POST /api/crafter/generate.

    Only 'prompt' is required — the rest have sensible defaults.
    The frontend collects these from the crafter page UI elements.
    """

    prompt: str                       # What the user wants to say
    tone: str = "professional"        # professional | casual | direct | persuasive
    recipient: str = ""               # Optional: recipient name or email
    subject: str = ""                 # Optional: desired subject line


class CraftSendRequest(BaseModel):
    """
    Request body for POST /api/crafter/send.

    All three fields are required to send an email.
    """

    to: str
    subject: str
    body: str


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.post("/generate")
def generate_email(req: CraftRequest):
    """
    Generates a complete email using the Gemini AI pipeline.

    Takes the user's brief intent/prompt and desired tone, then returns
    a polished, send-ready email body with a suggested subject line.

    Args:
        req (CraftRequest): prompt, tone, optional recipient and subject

    Returns:
        dict: {generated_email: str, subject_suggestion: str}
              or {error: str} on failure
    """
    # Validate that the prompt is not empty
    if not req.prompt.strip():
        return {"error": "Prompt cannot be empty. Describe what you want to say."}

    try:
        result = craft_email(
            prompt=req.prompt.strip(),
            tone=req.tone.strip(),
            recipient=req.recipient.strip(),
            subject=req.subject.strip(),
        )
        return result

    except Exception as exc:
        print(f"[Crafter API] generate failed: {exc}")
        return {"error": f"Failed to generate email: {str(exc)}"}


@router.get("/quick-prompts")
def list_quick_prompts():
    """
    Returns the available quick-prompt templates.

    These are pre-built prompt texts that the frontend injects
    into the AI prompt textarea when a quick-prompt chip is clicked.

    Returns:
        dict: {template_key: prompt_text} for each available template
    """
    return get_quick_prompts()
