from datetime import datetime, timedelta, timezone
from decimal import Decimal

from axiom.domain.enums import DecisionStatus, IntentType
from axiom.domain.models import CartLeg, CartMandate, IntentMandate, PolicyDecision
from axiom.domain.reason_codes import ReasonCode


intent = IntentMandate(
    mandate_id="im_123",
    user_id="usr_456",
    intent_type=IntentType.PURCHASE,
    item_description="black carry-on suitcase",
    allowed_categories=["travel_accessories"],
    max_amount=Decimal("250.00"),
    currency="USD",
    expires_at=datetime.now(timezone.utc) + timedelta(hours=24),
    approval_required=False,
)

cart = CartMandate(
    cart_mandate_id="cm_789",
    intent_mandate_id="im_123",
    agent_id="agent_001",
    cart_legs=[
        CartLeg(
            leg_id="leg_001",
            merchant_name="Luxury Luggage Co",
            item_description="checked luggage set",
            amount=Decimal("620.00"),
            currency="USD",
            category="travel_accessories",
        )
    ],
)

decision = PolicyDecision(
    decision_id="pd_001",
    intent_mandate_id=intent.mandate_id,
    cart_mandate_id=cart.cart_mandate_id,
    status=DecisionStatus.DECLINED,
    reason_codes=[
        ReasonCode.AMOUNT_EXCEEDS_LIMIT,
        ReasonCode.ITEM_MISMATCH,
    ],
    risk_score=0.91,
)

print(intent.model_dump())
print(cart.model_dump())
print(decision.model_dump())