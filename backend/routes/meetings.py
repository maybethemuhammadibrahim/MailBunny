# backend/routes/meetings.py
# ---------------------------------------------------------------
# Endpoints for managing meeting events extracted from emails.
# Supports listing upcoming meetings. Phase 4 will implement
# the full logic.
# ---------------------------------------------------------------

from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_meetings():
    """
    Placeholder for listing all upcoming meetings.
    Will return meetings ordered by date.

    Returns:
        dict: placeholder message
    """
    return {"message": "Get meetings — not yet implemented (Phase 4)"}


@router.post("/extract")
def extract_meetings():
    """
    Placeholder for extracting meetings from an email body.
    Called by n8n after the classification step.

    Returns:
        dict: placeholder message
    """
    return {"message": "Extract meetings — not yet implemented (Phase 4)"}
