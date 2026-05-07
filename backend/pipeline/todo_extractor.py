# backend/pipeline/todo_extractor.py
# ---------------------------------------------------------------
# Extracts actionable to-do items from emails using GPT-4o-mini.
# Returns structured todo objects with title, due date, and
# priority. Full implementation in Phase 4.
# ---------------------------------------------------------------


def extract_todos(subject, body, sender):
    """
    Extracts to-do items from an email using GPT-4o-mini.

    Args:
        subject (str): the email subject line
        body (str): the plain-text email body
        sender (str): the sender's email address

    Returns:
        dict: extraction result with key:
              - todos (list[dict]): each with title, due_date,
                priority (high/medium/low), source_email_subject
    """
    # Placeholder — will use openai.chat.completions.create() in Phase 4
    print("[TodoExtractor] Not yet implemented — returning empty list")

    return {"todos": []}
