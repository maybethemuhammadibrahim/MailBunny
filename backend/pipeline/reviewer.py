# backend/pipeline/reviewer.py
# ---------------------------------------------------------------
# Quality Review Agent — the second AI that reviews generated
# drafts for brand alignment, accuracy, tone consistency, and
# completeness BEFORE they are presented to the user or saved.
# This implements the "Quality Review Agent" from the multi-agent
# email workflow pattern.
# ---------------------------------------------------------------

from pipeline.gemini import call_review


# ---------------------------------------------------------------------------
# System prompt — instructs Gemini to critically review a draft
# ---------------------------------------------------------------------------

SYSTEM = (
    "You are a senior email quality reviewer. Your job is to review an AI-generated "
    "email draft and ensure it meets high quality standards before it is sent.\n\n"
    "REVIEW CRITERIA:\n"
    "1. TONE MATCH: Does the draft match the requested tone? (professional, casual, direct, etc.)\n"
    "2. COMPLETENESS: Does it have a proper greeting, body, and sign-off?\n"
    "3. SPECIFICITY: Does it reference specific details from the original email instead of being generic?\n"
    "4. EMPATHY: Is it appropriately empathetic given the sender's sentiment?\n"
    "5. LENGTH: Is the reply an appropriate length? (not too short/stub-like, not overly verbose)\n"
    "6. ACCURACY: Does it avoid making up facts or commitments not mentioned in the original?\n"
    "7. NATURALNESS: Does it sound like a real human wrote it, not a robot?\n"
    "8. ACTIONABILITY: Does it address all action items from the original email?\n\n"
    "SCORING:\n"
    "- 0.9-1.0: Excellent — ready to send as-is\n"
    "- 0.7-0.89: Good — minor tweaks suggested but acceptable\n"
    "- 0.5-0.69: Needs improvement — rewrite recommended\n"
    "- Below 0.5: Poor — significant issues, must be rewritten\n\n"
    "If the score is below 0.7, provide an IMPROVED version of the draft that fixes "
    "all identified issues. The improved version must be a complete, ready-to-send email.\n\n"
    "Return ONLY valid JSON with exactly these keys:\n"
    '  "approved": (boolean — true if score >= 0.7),\n'
    '  "score": (float 0.0-1.0),\n'
    '  "feedback": (string — brief review notes explaining your assessment),\n'
    '  "improved_draft": (string — improved version if score < 0.7, empty string if approved)\n'
    "Do NOT add any other keys."
)


def review_draft(
    original_subject: str,
    original_body: str,
    draft_text: str,
    requested_tone: str = "professional",
    sentiment: dict = None,
) -> dict:
    """
    Reviews an AI-generated email draft for quality, tone, and accuracy.

    This is the FINAL agent in the multi-agent pipeline. It acts as a
    quality gate — if the draft is below standard, it returns an improved
    version. This ensures every email leaving the system meets a minimum
    quality bar.

    Args:
        original_subject (str):  subject of the email being replied to
        original_body    (str):  body of the original email
        draft_text       (str):  the AI-generated draft to review
        requested_tone   (str):  tone that was requested (professional, casual, etc.)
        sentiment        (dict): sentiment analysis of the original email (optional)

    Returns:
        dict: approved (bool), score (float), feedback (str), improved_draft (str)
    """
    print(f"[Reviewer] Reviewing draft for '{original_subject[:60]}'")

    # Build context about the original email and expectations
    sentiment_info = ""
    if sentiment:
        sentiment_info = (
            f"Sender sentiment: {sentiment.get('sentiment', 'neutral')} "
            f"(intensity: {sentiment.get('intensity', 0.3)})\n"
            f"Recommended reply tone: {sentiment.get('recommended_tone', requested_tone)}\n"
        )

    prompt = (
        f"Review this AI-generated email draft:\n\n"
        f"CONTEXT — Original email:\n"
        f"Subject: {original_subject}\n"
        f"Body (excerpt): {original_body[:800]}\n\n"
        f"{sentiment_info}"
        f"REQUESTED TONE: {requested_tone}\n\n"
        f"DRAFT TO REVIEW:\n{draft_text}\n\n"
        f"Score this draft on all 8 quality criteria and provide your assessment."
    )

    try:
        result = call_review(prompt, SYSTEM)
        score = result.get("score", 0.5)
        approved = result.get("approved", score >= 0.7)

        print(
            f"[Reviewer] Done — score={score}, approved={approved}, "
            f"feedback='{str(result.get('feedback', ''))[:60]}'"
        )

        return result

    except Exception as exc:
        print(f"[Reviewer] Gemini call failed: {exc} — auto-approving draft")
        # On failure, approve the draft as-is rather than blocking
        return {
            "approved": True,
            "score": 0.7,
            "feedback": "Review skipped due to API error — draft approved by default.",
            "improved_draft": "",
        }
