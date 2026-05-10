# backend/routes/settings.py
# ---------------------------------------------------------------
# Handles user preference storage and account management actions.
# Settings are stored as key-value pairs in the SQLite settings
# table. This module provides GET (read all), PATCH (update AI
# preferences), and DELETE (wipe all user data) endpoints.
# ---------------------------------------------------------------

from db.sqlite import delete_all_data, get_all_settings, set_setting
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


# Default settings — seeded on first GET if the table is empty.
# These represent the initial AI personality configuration.
DEFAULTS = {
    "tone": "professional",                # casual | balanced | professional
    "auto_draft": "true",                  # true | false
    "vocabulary": "Concise,Action-oriented",  # comma-separated writing traits
}


class AISettingsRequest(BaseModel):
    """
    Request body for PATCH /api/settings/ai.

    All fields are optional — only the fields present in the request
    are updated. This lets the frontend send partial updates (e.g.
    just changing the tone without touching vocabulary).
    """

    tone: str | None = None
    auto_draft: str | None = None
    vocabulary: str | None = None


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.get("")
def read_settings():
    """
    Returns all user settings as a flat JSON object.

    On first call (empty table), seeds the default values so the
    settings page always has something to display.

    Returns:
        dict: {tone, auto_draft, vocabulary, ...}
    """
    try:
        settings = get_all_settings()

        # Seed defaults if the settings table is empty (first run)
        if not settings:
            print("[Settings] No settings found — seeding defaults.")
            for key, value in DEFAULTS.items():
                set_setting(key, value)
            settings = DEFAULTS.copy()

        return settings

    except Exception as exc:
        print(f"[Settings] Failed to read settings: {exc}")
        return {"error": f"Failed to read settings: {str(exc)}"}


@router.patch("/ai")
def update_ai_settings(req: AISettingsRequest):
    """
    Updates one or more AI preference keys in the settings table.

    Only non-None fields from the request body are written. This
    allows the frontend to send partial updates (e.g. just the tone).

    Args:
        req (AISettingsRequest): optional tone, auto_draft, vocabulary

    Returns:
        dict: {success: True, updated: [list of keys that changed]}
    """
    try:
        updated_keys = []

        # Only update fields that were actually sent in the request
        if req.tone is not None:
            set_setting("tone", req.tone)
            updated_keys.append("tone")

        if req.auto_draft is not None:
            set_setting("auto_draft", req.auto_draft)
            updated_keys.append("auto_draft")

        if req.vocabulary is not None:
            set_setting("vocabulary", req.vocabulary)
            updated_keys.append("vocabulary")

        print(f"[Settings] Updated: {updated_keys}")
        return {"success": True, "updated": updated_keys}

    except Exception as exc:
        print(f"[Settings] Failed to update AI settings: {exc}")
        return {"error": f"Failed to update settings: {str(exc)}"}


@router.delete("/data")
def wipe_all_data():
    """
    Deletes all user data from the database (emails, todos, meetings,
    orders, processed_emails). Settings are intentionally preserved.

    This is a destructive action — the frontend must show a confirmation
    dialog before calling this endpoint.

    Returns:
        dict: {success: True, message: str}
    """
    try:
        delete_all_data()
        return {
            "success": True,
            "message": "All processed data has been deleted. Your settings were preserved.",
        }

    except Exception as exc:
        print(f"[Settings] Failed to delete data: {exc}")
        return {"error": f"Failed to delete data: {str(exc)}"}
