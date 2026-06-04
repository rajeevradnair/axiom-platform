from datetime import datetime, timezone
from decimal import Decimal

from axiom.domain.enums import DecisionStatus
from axiom.domain.models import CartMandate, IntentMandate, PolicyDecision
from axiom.domain.enums import ReasonCode


def calculate_cart_total(cart: CartMandate) -> Decimal:
    return sum((leg.amount for leg in cart.cart_legs), Decimal("0.00"))

from datetime import datetime, timezone
from decimal import Decimal

from axiom.domain.enums import DecisionStatus
from axiom.domain.models import CartMandate, IntentMandate, PolicyDecision
from axiom.domain.enums import ReasonCode
from axiom.services.merchant_policy_service.service import is_approved_merchant, is_blocked_merchant


def calculate_cart_total(cart: CartMandate) -> Decimal:
    return sum((leg.amount for leg in cart.cart_legs), Decimal("0.00"))


def normalize_text(value: str) -> set[str]:
    cleaned = (
        value.lower()
        .replace("-", " ")
        .replace("/", " ")
        .replace(",", " ")
        .replace(".", " ")
    )
    return {word for word in cleaned.split() if word}


def cartmandate_matches_intentmandate(intent_description: str | None, cart_description: str) -> bool:
    if not intent_description:
        return True

    intent_words = normalize_text(intent_description)
    cart_words = normalize_text(cart_description)

    if not intent_words:
        return True

    overlap = intent_words.intersection(cart_words)

    # Even if a single word matches, we consider it a match. This is a very basic heuristic and can be improved with more sophisticated NLP techniques.
    return len(overlap) > 0


def evaluate_policy(
    decision_id: str,
    intent: IntentMandate,
    cart: CartMandate,
) -> PolicyDecision:
    
    reason_codes: list[ReasonCode] = []

    step_up_required = False

    cart_total = calculate_cart_total(cart)

    '''
    Check for all kinds of rules here - amount limits, 
    item match based on overlapping words in descriptions, 
    category restrictions, time windows, etc.
    '''

    if cart_total > intent.max_amount:
        reason_codes.append(ReasonCode.AMOUNT_EXCEEDS_LIMIT)

    for leg in cart.cart_legs:
        if not cartmandate_matches_intentmandate(intent.item_description, leg.item_description):
            reason_codes.append(ReasonCode.ITEM_MISMATCH)
            break

    for leg in cart.cart_legs:
        if leg.currency != intent.currency:
            reason_codes.append(ReasonCode.CURRENCY_MISMATCH)
            break

    for leg in cart.cart_legs:
        if leg.category not in intent.allowed_categories:
            reason_codes.append(ReasonCode.CATEGORY_NOT_ALLOWED)
            break

    now = datetime.now(timezone.utc)

    if intent.expires_at < now:
        reason_codes.append(ReasonCode.TIME_WINDOW_EXPIRED)

    for leg in cart.cart_legs:
        if is_blocked_merchant(leg.merchant_name):
            reason_codes.append(ReasonCode.MERCHANT_BLOCKED)
            break

    for leg in cart.cart_legs:
        if not is_approved_merchant(leg.merchant_name):
            reason_codes.append(ReasonCode.MERCHANT_NOT_APPROVED)
            break

    if intent.approval_required:
        step_up_required = True
        reason_codes.append(ReasonCode.APPROVAL_REQUIRED)

    if intent.per_order_approval_threshold is not None:
        for leg in cart.cart_legs:
            if leg.amount > intent.per_order_approval_threshold:
                step_up_required = True
                reason_codes.append(ReasonCode.AMOUNT_REQUIRES_APPROVAL)
                break

    hard_decline_reasons = {
        ReasonCode.AMOUNT_EXCEEDS_LIMIT,
        ReasonCode.CURRENCY_MISMATCH,
        ReasonCode.CATEGORY_NOT_ALLOWED,
        ReasonCode.ITEM_MISMATCH,
        ReasonCode.TIME_WINDOW_EXPIRED,
        ReasonCode.MERCHANT_BLOCKED,
        ReasonCode.MERCHANT_NOT_APPROVED,
    }

    if any(reason in hard_decline_reasons for reason in reason_codes):
        status = DecisionStatus.DECLINED
    elif step_up_required:
        status = DecisionStatus.STEP_UP_REQUIRED
    else:
        status = DecisionStatus.APPROVED

    return PolicyDecision(
        decision_id=decision_id,
        intent_mandate_id=intent.mandate_id,
        cart_mandate_id=cart.cart_mandate_id,
        status=status,
        reason_codes=reason_codes,
    )