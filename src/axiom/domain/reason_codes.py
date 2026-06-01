from enum import StrEnum


class ReasonCode(StrEnum):
    AMOUNT_EXCEEDS_LIMIT = "amount_exceeds_limit"
    CATEGORY_NOT_ALLOWED = "category_not_allowed"
    ITEM_MISMATCH = "item_mismatch"
    MERCHANT_NOT_APPROVED = "merchant_not_approved"
    MERCHANT_RISK_TOO_HIGH = "merchant_risk_too_high"
    OFFER_NOT_ELIGIBLE = "offer_not_eligible"
    CARDMEMBER_NOT_ELIGIBLE = "cardmember_not_eligible"
    TIME_WINDOW_EXPIRED = "time_window_expired"
    APPROVAL_REQUIRED = "approval_required"
    POLICY_VIOLATION = "policy_violation"
    DUPLICATE_SUBSCRIPTION = "duplicate_subscription"
    USAGE_THRESHOLD_NOT_MET = "usage_threshold_not_met"
    INTENT_VIOLATION = "intent_violation"
    CURRENCY_MISMATCH = "currency_mismatch"