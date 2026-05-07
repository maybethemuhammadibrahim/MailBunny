# backend/routes/todos.py
# ---------------------------------------------------------------
# Endpoints for managing to-do items extracted from emails.
# Supports listing incomplete todos and marking them as done.
# Phase 4 will implement the full logic.
# ---------------------------------------------------------------

from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_todos():
    """
    Placeholder for listing all incomplete to-do items.
    Will return todos ordered by priority (high → medium → low).

    Returns:
        dict: placeholder message
    """
    return {"message": "Get todos — not yet implemented (Phase 4)"}


@router.patch("/{todo_id}/done")
def mark_todo_done(todo_id: int):
    """
    Placeholder for marking a to-do item as complete.

    Args:
        todo_id: the database ID of the todo to complete

    Returns:
        dict: placeholder message
    """
    return {"message": f"Mark todo {todo_id} done — not yet implemented (Phase 4)"}


@router.post("/extract")
def extract_todos():
    """
    Placeholder for extracting todos from an email body.
    Called by n8n after the classification step.

    Returns:
        dict: placeholder message
    """
    return {"message": "Extract todos — not yet implemented (Phase 4)"}
