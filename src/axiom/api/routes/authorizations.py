from fastapi import APIRouter

from axiom.domain.contracts import (
    AuthorizationEvaluateRequest,
    AuthorizationEvaluateResponse,
)
from axiom.services.authorization_service.service import evaluate_authorization

router = APIRouter(tags=["authorizations"])


@router.get("/api/v1/authorizations/ping")
def ping_authorizations() -> dict[str, str]:
    return {
        "status": "ok",
        "route": "authorizations",
        "purpose": "agent cart evaluation and authorization decisions",
    }

@router.post("/api/v1/authorizations/evaluate", response_model=AuthorizationEvaluateResponse)
def evaluate(
    request: AuthorizationEvaluateRequest,
) -> AuthorizationEvaluateResponse:
    return evaluate_authorization(request)