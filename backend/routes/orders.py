# backend/routes/orders.py
# ---------------------------------------------------------------
# Endpoints for order and purchase tracking. Supports listing
# all orders and computing spending statistics. Phase 5 will
# implement the full logic.
# ---------------------------------------------------------------

from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_orders():
    """
    Placeholder for listing all orders, most recent first.

    Returns:
        dict: placeholder message
    """
    return {"message": "Get orders — not yet implemented (Phase 5)"}


@router.get("/stats")
def get_order_stats():
    """
    Placeholder for order statistics (total orders, total spent,
    orders by status, monthly average).

    Returns:
        dict: placeholder message
    """
    return {"message": "Get order stats — not yet implemented (Phase 5)"}


@router.post("/extract")
def extract_order():
    """
    Placeholder for extracting order data from an email body.
    Only called when the classifier flags is_order_email = true.

    Returns:
        dict: placeholder message
    """
    return {"message": "Extract order — not yet implemented (Phase 5)"}
