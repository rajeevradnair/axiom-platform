from decimal import Decimal
from pydantic import BaseModel, Field

from axiom.domain.enums import IntentType, DecisionStatus
from axiom.domain.models import CartLeg
from axiom.domain.models import PolicyDecision
from axiom.domain.models import (CartMandate, 
                                 IntentMandate, 
                                 SignedIntentMandate)

# Request, Response contracts for Intent Draft service
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

# Request, Response contracts for Cart Draft service
class CartDraftRequest(BaseModel):
    intent_mandate_id: str
    agent_id: str
    cart_legs: list[CartLeg] = Field(min_length=1)

class CartDraftResponse(BaseModel):
    cart_draft_id: str
    status: str
    message: str
    cart: CartDraftRequest

# Request, Response contracts for Authorization Service
class AuthorizationEvaluateRequest(BaseModel):
    intent: IntentMandate
    cart: CartMandate
    agent_id: str | None = None

class AuthorizationEvaluateByIdRequest(BaseModel):
    intent_mandate_id: str
    cart_mandate_id: str
    agent_id: str | None = None

class AuthorizationEvaluateResponse(BaseModel):
    authorization_id: str
    decision: PolicyDecision
    message: str

# Response contracts for Store Service
class StoreIntentMandateResponse(BaseModel):
    status: str
    message: str
    intent: IntentMandate

class StoreCartMandateResponse(BaseModel):
    status: str
    message: str
    cart: CartMandate

class SignIntentMandateResponse(BaseModel):
    status: str
    message: str
    signed_intent: SignedIntentMandate