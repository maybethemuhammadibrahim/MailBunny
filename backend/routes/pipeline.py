# backend/routes/pipeline.py
# ---------------------------------------------------------------
# Exposes the AI pipeline (classify, summarize, draft) as REST
# endpoints. Also provides a convenience endpoint that runs all
# three stages in sequence. Phase 3 will implement the full logic.
# ---------------------------------------------------------------

from fastapi import APIRouter

router = APIRouter()


@router.post("/classify")
def classify_email():
    """
    Placeholder for the email classification endpoint.
    Will call GPT-4o-mini to categorise an email and assign
    a priority score.

    Returns:
        dict: placeholder message
    """
    return {"message": "Classify email — not yet implemented (Phase 3)"}


@router.post("/summarize")
def summarize_email():
    """
    Placeholder for the email summarization endpoint.
    Will call GPT-4o-mini to produce a one-line summary
    and key facts.

    Returns:
        dict: placeholder message
    """
    return {"message": "Summarize email — not yet implemented (Phase 3)"}


@router.post("/draft")
def draft_reply():
    """
    Placeholder for the email draft endpoint.
    Will call GPT-4o to generate a professional reply.

    Returns:
        dict: placeholder message
    """
    return {"message": "Draft reply — not yet implemented (Phase 3)"}


@router.post("/process-email")
def process_email():
    """
    Placeholder for the combined pipeline endpoint.
    Will run classify → summarize → draft in sequence
    and return the merged result.

    Returns:
        dict: placeholder message
    """
    return {"message": "Process email (full pipeline) — not yet implemented (Phase 3)"}
