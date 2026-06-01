from datetime import datetime, timezone
from decimal import Decimal

from axiom.domain.enums import DecisionStatus
from axiom.domain.models import CartMandate, IntentMandate, PolicyDecision
from axiom.domain.reason_codes import ReasonCode


def calculate_cart_total(cart: CartMandate) -> Decimal:
    return sum((leg.amount for leg in cart.cart_legs), Decimal("0.00"))

from datetime import datetime, timezone
from decimal import Decimal

from axiom.domain.enums import DecisionStatus
from axiom.domain.models import CartMandate, IntentMandate, PolicyDecision
from axiom.domain.reason_codes import ReasonCode


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


def item_matches_intent(intent_description: str | None, cart_description: str) -> bool:
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

    cart_total = calculate_cart_total(cart)

    # Check for all kinds of rules here - amount limits, category restrictions, time windows, etc.

    if cart_total > intent.max_amount:
        reason_codes.append(ReasonCode.AMOUNT_EXCEEDS_LIMIT)

    for leg in cart.cart_legs:
        if not item_matches_intent(intent.item_description, leg.item_description):
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

    status = (
        DecisionStatus.APPROVED
        if not reason_codes
        else DecisionStatus.DECLINED
    )

    return PolicyDecision(
        decision_id=decision_id,
        intent_mandate_id=intent.mandate_id,
        cart_mandate_id=cart.cart_mandate_id,
        status=status,
        reason_codes=reason_codes,
    )