from enum import StrEnum


class IntentType(StrEnum):
    PURCHASE = "purchase"
    TRAVEL_BOOKING = "travel_booking"
    DINING_RESERVATION = "dining_reservation"
    BUSINESS_PURCHASE = "business_purchase"
    SUBSCRIPTION_RENEWAL = "subscription_renewal"
    BUNDLED_COMMERCE = "bundled_commerce"

class DecisionStatus(StrEnum):
    PROCESSING = "processing"
    APPROVED = "approved"
    APPROVED_PENDING_VCC = "approved_pending_vcc"
    APPROVED_PENDING_MULTI_MERCHANT_CREDENTIALS = "approved_pending_multi_merchant_credentials"
    DECLINED = "declined"
    STEP_UP_REQUIRED = "step_up_required"
    HUMAN_CLARIFICATION_REQUIRED = "human_clarification_required"

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