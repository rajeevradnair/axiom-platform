from decimal import Decimal
from pydantic import BaseModel, Field

from axiom.domain.enums import IntentType, DecisionStatus
from axiom.domain.models import CartLeg
from axiom.domain.models import PolicyDecision
from axiom.domain.models import CartMandate, IntentMandate

class IntentDraftRequest(BaseModel):
    user_id: str
    prompt: str
    intent_type: IntentType = IntentType.PURCHASE
    item_description: str | None = None
    allowed_categories: list[str] = Field(default_factory=list)
    max_amount: Decimal
    currency: str = "USD"
    approval_required: bool = False


class IntentDraftResponse(BaseModel):
    draft_id: str
    status: str
    message: str
    intent: IntentDraftRequest


class CartDraftRequest(BaseModel):
    intent_mandate_id: str
    agent_id: str
    cart_legs: list[CartLeg] = Field(min_length=1)


class CartDraftResponse(BaseModel):
    cart_draft_id: str
    status: str
    message: str
    cart: CartDraftRequest

class AuthorizationEvaluateRequest(BaseModel):
    intent: IntentMandate
    cart: CartMandate
    agent_id: str | None = None

class AuthorizationEvaluateResponse(BaseModel):
    authorization_id: str
    status: PolicyDecision
    message: str