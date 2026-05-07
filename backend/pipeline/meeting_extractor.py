# backend/pipeline/meeting_extractor.py
# ---------------------------------------------------------------
# Extracts meeting/call/event information from emails using
# GPT-4o-mini. Returns structured meeting objects with title,
# date, time, location, and attendees. Full implementation
# in Phase 4.
# ---------------------------------------------------------------


def extract_meetings(subject, body, sender):
    """
    Extracts meeting events from an email using GPT-4o-mini.

    Args:
        subject (str): the email subject line
        body (str): the plain-text email body
        sender (str): the sender's email address

    Returns:
        dict: extraction result with key:
              - meetings (list[dict]): each with title, date,
                time, location_or_link, attendees (list[str]),
                source_email_subject
    """
    # Placeholder — will use openai.chat.completions.create() in Phase 4
    print("[MeetingExtractor] Not yet implemented — returning empty list")

    return {"meetings": []}
