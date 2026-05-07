# backend/routes/analytics.py
# ---------------------------------------------------------------
# Endpoints for computing email analytics and security stats.
# Powers the dashboard charts on the Home page. Phase 6 will
# implement the full logic.
# ---------------------------------------------------------------

from fastapi import APIRouter

router = APIRouter()


@router.get("/overview")
def get_overview():
    """
    Placeholder for the analytics overview endpoint.
    Will return email counts by category, by sender domain,
    hourly volume, spam count, and flagged senders.

    Returns:
        dict: placeholder message
    """
    return {"message": "Analytics overview — not yet implemented (Phase 6)"}


@router.get("/security")
def get_security():
    """
    Placeholder for the security analytics endpoint.
    Will return spam rate, suspicious senders, and safe percentage.

    Returns:
        dict: placeholder message
    """
    return {"message": "Security analytics — not yet implemented (Phase 6)"}
