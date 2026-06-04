from fastapi import APIRouter

from fastapi import HTTPException

from axiom.domain.contracts import (
    CartDraftRequest,
    CartDraftResponse,
    IntentDraftRequest,
    IntentDraftResponse,
)
from axiom.services.cart_service.service import create_cart_draft
from axiom.services.intent_service.service import create_intent_draft
from axiom.repositories.in_memory_store import get_intent_mandate
from axiom.services.mandate_signing_service.service import sign_intent_mandate

from axiom.domain.models import CartMandate, IntentMandate, SignedIntentMandate
from axiom.domain.contracts import (
    StoreCartMandateResponse,
    StoreIntentMandateResponse,
    SignIntentMandateResponse
)
from axiom.services.mandate_store_service.service import (
    store_cart_mandate,
    store_intent_mandate,
)

router = APIRouter(tags=["mandates"])

@router.get("/api/v1/mandates/ping")
def ping_authorizations() -> dict[str, str]:
    return {
        "status": "ok",
        "route": "mandates",
        "purpose": "mandate service for creating intent and cart drafts",
    }

@router.post("/api/v1/mandates/intent/draft", response_model=IntentDraftResponse)
def draft_intent(request: IntentDraftRequest) -> IntentDraftResponse:
    return create_intent_draft(request)


@router.post("/api/v1/mandates/cart/draft", response_model=CartDraftResponse)
def draft_cart(request: CartDraftRequest) -> CartDraftResponse:
    return create_cart_draft(request)


@router.post("/api/v1/mandates/intent", response_model=StoreIntentMandateResponse)
def create_intent_mandate(intent: IntentMandate) -> StoreIntentMandateResponse:
    stored_intent = store_intent_mandate(intent)
    return StoreIntentMandateResponse(
        status="stored",
        message="Intent Mandate stored in local repository.",
        intent=stored_intent,
    )

@router.post("/api/v1/mandates/cart", response_model=StoreCartMandateResponse)
def create_cart_mandate(cart: CartMandate) -> StoreCartMandateResponse:
    stored_cart = store_cart_mandate(cart)
    return StoreCartMandateResponse(
        status="stored",
        message="Cart Mandate stored in local repository.",
        cart=stored_cart,
    )

@router.post("/api/v1/mandates/intent/{mandate_id}/sign", response_model=SignIntentMandateResponse)
def sign_stored_intent_mandate(mandate_id: str) -> SignIntentMandateResponse:
    
    intent = get_intent_mandate(mandate_id)

    if intent is None:
        raise HTTPException(
            status_code=404,
            detail=f"Intent Mandate not found: {mandate_id}",
        )

    signed_intent = sign_intent_mandate(intent)

    return SignIntentMandateResponse(
        status="signed",
        message="Intent Mandate signed and stored locally.",
        signed_intent=signed_intent,
    )