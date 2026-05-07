# backend/pipeline/drafter.py
# ---------------------------------------------------------------
# Drafts professional email replies using GPT-4o. Takes the
# classification and summary as context to produce a relevant
# reply. Full implementation in Phase 3.
# ---------------------------------------------------------------


def draft_reply(subject, body, classification, summary):
    """
    Drafts a reply to an email using GPT-4o.

    Args:
        subject (str): the original email subject line
        body (str): the original email body
        classification (dict): output from classify_email()
        summary (dict): output from summarize_email()

    Returns:
        dict: draft result with keys:
              - draft_reply (str): full reply text ready to send
              - confidence_score (float): 0.0 to 1.0
              - suggested_subject (str): reply subject line
    """
    # Placeholder — will use openai.chat.completions.create() in Phase 3
    print("[Drafter] Not yet implemented — returning default draft")

    return {
        "draft_reply": "Thank you for your email. I will review and get back to you shortly.",
        "confidence_score": 0.0,
        "suggested_subject": f"Re: {subject}"
    }
