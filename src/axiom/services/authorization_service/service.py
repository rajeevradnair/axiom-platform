

from uuid import uuid4

from axiom.domain.contracts import (
    AuthorizationEvaluateRequest,
    AuthorizationEvaluateByIdRequest,
    AuthorizationEvaluateResponse,
)
from axiom.domain.enums import DecisionStatus
from axiom.services.policy_service.service import evaluate_policy
from axiom.repositories.in_memory_store import (
    get_cart_mandate,
    get_intent_mandate,
    save_policy_decision,
)

from axiom.repositories.in_memory_store import get_signed_intent_mandate
from axiom.services.signed_intent_verification_service.service import verify_signed_intent

def evaluate_authorization(
    request: AuthorizationEvaluateRequest,
) -> AuthorizationEvaluateResponse:
    
    authorization_id=f"auth_{uuid4().hex}"
    decision_id=f"pd_{uuid4().hex}"

    # Deterministic policy engine
    decision = evaluate_policy(
        decision_id=decision_id,
        intent=request.intent,
        cart=request.cart,
    )

    return AuthorizationEvaluateResponse(
        authorization_id=authorization_id,
        decision=decision,
        message="Authorization request accepted. Policy evaluation is not implemented yet.",
    )

def evaluate_authorization_by_id(
    request: AuthorizationEvaluateByIdRequest,
) -> AuthorizationEvaluateResponse:
    
    signed_intent = get_signed_intent_mandate(request.intent_mandate_id)
    cart = get_cart_mandate(request.cart_mandate_id)
    
    if signed_intent is None:
        raise ValueError(
            f"Signed intent mandate not found: {request.intent_mandate_id}"
        )
    
    if cart is None:
        raise ValueError(f"Cart Mandate not found: {request.cart_mandate_id}")

    if not verify_signed_intent(signed_intent=signed_intent):
        raise ValueError(
            f"Signed Intent Mandate verification failed: {request.intent_mandate_id}"
        )

    intent = signed_intent.payload

    authorization_id = f"auth_{uuid4().hex}"
    decision_id = f"pd_{uuid4().hex}"

    decision = evaluate_policy(
        decision_id=decision_id,
        intent=intent,
        cart=cart,
    )

    save_policy_decision(decision)

    print("Evaluated authorization by ID:", decision)

    return AuthorizationEvaluateResponse(
        authorization_id=authorization_id,
        decision=decision,
        message="Authorization evaluated from stored local mandates.",
    )


def evaluate_authorization_by_id_unsignedmandate(
    request: AuthorizationEvaluateByIdRequest,
) -> AuthorizationEvaluateResponse:
    
    intent = get_intent_mandate(request.intent_mandate_id)
    cart = get_cart_mandate(request.cart_mandate_id)

    if intent is None:
        raise ValueError(f"Intent Mandate not found: {request.intent_mandate_id}")

    if cart is None:
        raise ValueError(f"Cart Mandate not found: {request.cart_mandate_id}")

    authorization_id = f"auth_{uuid4().hex}"
    decision_id = f"pd_{uuid4().hex}"

    decision = evaluate_policy(
        decision_id=decision_id,
        intent=intent,
        cart=cart,
    )

    save_policy_decision(decision)

    print("Evaluated authorization by ID:", decision)

    return AuthorizationEvaluateResponse(
        authorization_id=authorization_id,
        decision=decision,
        message="Authorization evaluated from stored local mandates.",
    )