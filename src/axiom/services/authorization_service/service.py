

from uuid import uuid4

from axiom.domain.contracts import (
    AuthorizationEvaluateRequest,
    AuthorizationEvaluateResponse,
)
from axiom.domain.enums import DecisionStatus
from axiom.services.policy_service.service import evaluate_policy


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
        status=decision,
        message="Authorization request accepted. Policy evaluation is not implemented yet.",
    )