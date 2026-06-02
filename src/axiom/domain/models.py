from datetime import datetime, timezone
from decimal import Decimal
from pydantic import BaseModel, Field

from axiom.domain.enums import DecisionStatus, IntentType
from axiom.domain.enums import ReasonCode

class IntentMandate(BaseModel):
    mandate_id: str
    user_id: str
    intent_type: IntentType
    item_description: str | None = None
    allowed_categories: list[str] = Field(default_factory=list)
    max_amount: Decimal
    currency: str = "USD"
    expires_at: datetime
    approval_required: bool = False

class CartLeg(BaseModel):
    leg_id: str
    merchant_name: str
    item_description: str
    amount: Decimal
    currency: str = "USD"
    category: str

class CartMandate(BaseModel):
    cart_mandate_id: str
    intent_mandate_id: str
    agent_id: str
    cart_legs: list[CartLeg]

class PolicyDecision(BaseModel):
    decision_id: str
    intent_mandate_id: str
    cart_mandate_id: str
    status: DecisionStatus
    reason_codes: list[ReasonCode] = Field(default_factory=list)
    risk_score: float | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))