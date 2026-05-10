# backend/pipeline/classifier.py
# ---------------------------------------------------------------
# Classifies incoming emails using Gemini Flash with few-shot
# prompting. Assigns category, priority score, flags for
# reply-needed, spam, and order emails, AND performs sentiment
# analysis — all in a single API call to conserve quota.
# ---------------------------------------------------------------

from pipeline.gemini import call_fast

# ---------------------------------------------------------------------------
# System prompt — instructs Gemini on the exact JSON schema to return.
# Now includes sentiment analysis keys so we get classification AND
# sentiment in one call instead of two separate API requests.
# ---------------------------------------------------------------------------

SYSTEM = (
    "You are an email classification and sentiment analysis system. "
    "Analyze the email carefully and return ONLY valid JSON with exactly these keys: "
    "category (one of: urgent, action-required, meeting-request, order-update, newsletter, spam, fyi), "
    "priority_score (integer 1-10), "
    "requires_reply (boolean), "
    "is_spam (boolean), "
    "is_order_email (boolean), "
    "action_items (array of strings, empty if none), "
    "sender_sentiment (one of: positive, neutral, negative, angry, urgent, grateful, confused), "
    "sentiment_intensity (float 0.0-1.0 — how strong the emotion is), "
    "is_critical (boolean — true only for angry complaints, legal threats, emergencies, "
    "VIP escalations, or sensitive personal matters that need human attention), "
    "alert_reason (string — brief explanation if is_critical is true, empty string otherwise), "
    "recommended_reply_tone (one of: empathetic, professional, enthusiastic, reassuring, direct, warm)."
)

# ---------------------------------------------------------------------------
# Few-shot examples — shown to the model before every classification call
# so it understands category vocabulary and the expected output format.
# ---------------------------------------------------------------------------

FEW_SHOT = """Here are labelled examples to guide your classification:

Example 1:
Subject: URGENT: Production database down
From: alerts@ops.company.com
Body: All production services are failing. Database is not responding. Revenue impact ongoing.
Result: {"category":"urgent","priority_score":10,"requires_reply":true,"is_spam":false,"is_order_email":false,"action_items":["Check database server status","Page on-call engineer immediately"],"sender_sentiment":"urgent","sentiment_intensity":0.9,"is_critical":true,"alert_reason":"Production outage with revenue impact","recommended_reply_tone":"empathetic"}

Example 2:
Subject: Your weekly AI digest
From: digest@ainews.io
Body: This week in AI: GPT-5 rumours...
Result: {"category":"newsletter","priority_score":2,"requires_reply":false,"is_spam":false,"is_order_email":false,"action_items":[],"sender_sentiment":"neutral","sentiment_intensity":0.1,"is_critical":false,"alert_reason":"","recommended_reply_tone":"professional"}

Example 3:
Subject: Your Amazon order #113-456 has shipped
From: shipment-tracking@amazon.com
Body: Your order has shipped. Tracking: 1Z9999W99999999999. Estimated delivery: Thursday.
Result: {"category":"order-update","priority_score":3,"requires_reply":false,"is_spam":false,"is_order_email":true,"action_items":["Track package 1Z9999W99999999999"],"sender_sentiment":"neutral","sentiment_intensity":0.2,"is_critical":false,"alert_reason":"","recommended_reply_tone":"professional"}

Example 4:
Subject: Congratulations! You've won $1,000,000
From: winner@prize-claim-2024.ru
Body: Click this link to claim your prize immediately.
Result: {"category":"spam","priority_score":1,"requires_reply":false,"is_spam":true,"is_order_email":false,"action_items":[],"sender_sentiment":"neutral","sentiment_intensity":0.1,"is_critical":false,"alert_reason":"","recommended_reply_tone":"direct"}
"""

# Returned whenever Gemini is unreachable or returns unparseable output.
# Using "unknown" instead of "fyi" so failed classifications are flagged
# for manual review rather than silently treated as informational.
_SAFE_DEFAULT = {
    "category": "unknown",
    "priority_score": 5,
    "requires_reply": False,
    "is_spam": False,
    "is_order_email": False,
    "action_items": [],
    "sender_sentiment": "neutral",
    "sentiment_intensity": 0.3,
    "is_critical": False,
    "alert_reason": "",
    "recommended_reply_tone": "professional",
}


def _build_prompt(subject: str, sender: str, body: str) -> str:
    """
    Combines the few-shot examples with the target email fields
    into a single prompt string ready to send to Gemini.

    Args:
        subject (str): the email subject line
        sender  (str): the sender's email address
        body    (str): the plain-text email body

    Returns:
        str: fully assembled prompt (body capped at 2 000 chars)
    """
    return (
        f"{FEW_SHOT}\n"
        f"Now classify this email:\n"
        f"Subject: {subject}\n"
        f"From: {sender}\n"
        f"Body: {body[:2000]}"
    )


def _validate_result(result: dict) -> dict:
    """
    Merges Gemini's response with _SAFE_DEFAULT to fill any missing keys
    and clamps values to valid ranges. Ensures downstream code never
    encounters missing or out-of-range fields.

    Args:
        result (dict): raw dict returned by Gemini

    Returns:
        dict: validated result with all required keys present
    """
    validated = _SAFE_DEFAULT.copy()
    validated.update({k: v for k, v in result.items() if v is not None})

    # Clamp priority score to 1-10 range
    try:
        validated["priority_score"] = max(1, min(10, int(validated["priority_score"])))
    except (ValueError, TypeError):
        validated["priority_score"] = 5

    # Clamp sentiment intensity to 0.0-1.0
    try:
        validated["sentiment_intensity"] = max(0.0, min(1.0, float(validated["sentiment_intensity"])))
    except (ValueError, TypeError):
        validated["sentiment_intensity"] = 0.3

    return validated


def classify_email(subject: str, sender: str, body: str) -> dict:
    """
    Classifies an email AND analyzes sender sentiment using Gemini Flash
    in a single API call. Combines what were previously two separate
    pipeline steps (classification + sentiment) to conserve API quota.

    Args:
        subject (str): email subject line
        sender  (str): sender's email address
        body    (str): plain-text email body

    Returns:
        dict: category, priority_score, requires_reply, is_spam,
              is_order_email, action_items, sender_sentiment,
              sentiment_intensity, is_critical, alert_reason,
              recommended_reply_tone. Safe default on failure.
    """
    print(f"[Classifier] Classifying — subject: '{subject[:60]}'")
    try:
        prompt = _build_prompt(subject, sender, body)
        result = call_fast(prompt, SYSTEM)
        validated = _validate_result(result)
        print(
            f"[Classifier] Done — category={validated.get('category')}, "
            f"priority={validated.get('priority_score')}, "
            f"sentiment={validated.get('sender_sentiment')}"
        )
        return validated
    except Exception as exc:
        print(f"[Classifier] Gemini call failed: {exc} — returning safe default")
        return _SAFE_DEFAULT.copy()
