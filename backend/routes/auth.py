# backend/routes/auth.py
# ---------------------------------------------------------------
# Handles Gmail OAuth2 authentication. Provides endpoints to
# initiate the Google login flow and handle the callback with
# the authorization code. Phase 2 will implement the full logic.
# ---------------------------------------------------------------

from fastapi import APIRouter

# Create a router instance — this gets registered in main.py
router = APIRouter()


@router.get("/login")
def login():
    """
    Placeholder for the Gmail OAuth login endpoint.
    Will redirect the user to Google's OAuth consent screen.

    Returns:
        dict: placeholder message
    """
    return {"message": "Gmail OAuth login — not yet implemented (Phase 2)"}


@router.get("/callback")
def callback():
    """
    Placeholder for the OAuth callback endpoint.
    Google redirects here after the user grants permission.
    Will exchange the auth code for access + refresh tokens.

    Returns:
        dict: placeholder message
    """
    return {"message": "OAuth callback — not yet implemented (Phase 2)"}
