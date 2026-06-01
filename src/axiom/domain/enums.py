from enum import StrEnum, IntEnum


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
