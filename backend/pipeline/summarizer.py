# backend/pipeline/summarizer.py
# ---------------------------------------------------------------
# Summarises emails using GPT-4o-mini. Produces a one-line
# summary, key facts, and action items. Full implementation
# in Phase 3.
# ---------------------------------------------------------------


def summarize_email(subject, body):
    """
    Summarises an email using GPT-4o-mini.

    Args:
        subject (str): the email subject line
        body (str): the plain-text email body

    Returns:
        dict: summary result with keys:
              - one_line_summary (str): max 20 words
              - key_facts (list[str]): up to 5 bullet points
              - action_items (list[str])
    """
    # Placeholder — will use openai.chat.completions.create() in Phase 3
    print("[Summarizer] Not yet implemented — returning default summary")

    return {
        "one_line_summary": "Email summary pending implementation.",
        "key_facts": [],
        "action_items": []
    }
