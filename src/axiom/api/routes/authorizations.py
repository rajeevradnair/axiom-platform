from copy import error
from urllib import request

from fastapi import APIRouter
from fastapi import HTTPException


from axiom.domain.contracts import (
    AuthorizationEvaluateByIdRequest,
    AuthorizationEvaluateRequest,
    AuthorizationEvaluateResponse,
)
from axiom.services.authorization_service.service import evaluate_authorization, evaluate_authorization_by_id

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


@router.post("/api/v1/authorizations/evaluate-by-id", response_model=AuthorizationEvaluateResponse)
def evaluate(
    request: AuthorizationEvaluateByIdRequest,
) -> AuthorizationEvaluateResponse:
    
    try:
        return evaluate_authorization_by_id(request)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error