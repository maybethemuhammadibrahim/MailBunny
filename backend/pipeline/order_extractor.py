# backend/pipeline/order_extractor.py
# ---------------------------------------------------------------
# Extracts order and purchase information from shipping/order
# confirmation emails using GPT-4o-mini. Only called when the
# classifier flags is_order_email = true. Full implementation
# in Phase 5.
# ---------------------------------------------------------------


def extract_order(subject, body, sender):
    """
    Extracts order/purchase data from an email using GPT-4o-mini.

    Args:
        subject (str): the email subject line
        body (str): the plain-text email body
        sender (str): the sender's email address

    Returns:
        dict: order data with keys:
              - retailer (str)
              - order_number (str or None)
              - item_description (str, max 15 words)
              - order_date (str or None)
              - estimated_delivery (str or None)
              - status (str): one of ordered, processing, shipped,
                out-for-delivery, delivered, cancelled
              - tracking_number (str or None)
              - tracking_url (str or None)
              - price (str or None, includes currency symbol)
    """
    # Placeholder — will use openai.chat.completions.create() in Phase 5
    print("[OrderExtractor] Not yet implemented — returning default order")

    return {
        "retailer": "Unknown",
        "order_number": None,
        "item_description": "Unknown item",
        "order_date": None,
        "estimated_delivery": None,
        "status": "processing",
        "tracking_number": None,
        "tracking_url": None,
        "price": None
    }
