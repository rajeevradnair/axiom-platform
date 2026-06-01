from fastapi import APIRouter

from axiom.domain.contracts import (
    CartDraftRequest,
    CartDraftResponse,
    IntentDraftRequest,
    IntentDraftResponse,
)
from axiom.services.cart_service.service import create_cart_draft
from axiom.services.intent_service.service import create_intent_draft


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