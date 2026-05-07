# backend/pipeline/classifier.py
# ---------------------------------------------------------------
# Classifies incoming emails using GPT-4o-mini. Assigns a category
# (urgent, action-required, newsletter, spam, etc.), a priority
# score (1-10), and flags for reply-needed, spam, and orders.
# Full implementation in Phase 3.
# ---------------------------------------------------------------


def classify_email(subject, sender, body):
    """
    Classifies an email using GPT-4o-mini with few-shot prompting.

    Args:
        subject (str): the email subject line
        sender (str): the sender's email address
        body (str): the plain-text email body

    Returns:
        dict: classification result with keys:
              - category (str): one of urgent, action-required,
                meeting-request, order-update, newsletter, spam, fyi
              - priority_score (int): 1-10
              - requires_reply (bool)
              - is_spam (bool)
              - is_order_email (bool)
              - action_items (list[str])
    """
    # Placeholder — will use openai.chat.completions.create() in Phase 3
    print("[Classifier] Not yet implemented — returning default classification")

    return {
        "category": "fyi",
        "priority_score": 5,
        "requires_reply": False,
        "is_spam": False,
        "is_order_email": False,
        "action_items": []
    }
