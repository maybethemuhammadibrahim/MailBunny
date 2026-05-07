# backend/routes/emails.py
# ---------------------------------------------------------------
# Handles fetching emails from Gmail via the API. Provides
# endpoints for retrieving unread emails and checking/marking
# processed status. Phase 2 will implement the full logic.
# ---------------------------------------------------------------

from fastapi import APIRouter

router = APIRouter()


@router.get("/unread")
def get_unread_emails():
    """
    Placeholder for fetching unread emails from Gmail.
    Will return a list of email dicts with subject, sender,
    body, thread_id, and timestamp.

    Returns:
        dict: placeholder message
    """
    return {"message": "Fetch unread emails — not yet implemented (Phase 2)"}


@router.get("/check/{email_id}")
def check_processed(email_id: str):
    """
    Placeholder for checking if an email has been processed.
    Used by n8n to skip already-processed emails.

    Args:
        email_id: the unique Gmail message ID

    Returns:
        dict: placeholder message
    """
    return {"message": f"Check email {email_id} — not yet implemented (Phase 2)"}


@router.post("/mark-processed")
def mark_email_processed():
    """
    Placeholder for marking an email as processed in the database.

    Returns:
        dict: placeholder message
    """
    return {"message": "Mark processed — not yet implemented (Phase 2)"}
