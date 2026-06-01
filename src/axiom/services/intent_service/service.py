from uuid import uuid4

from axiom.domain.contracts import IntentDraftRequest, IntentDraftResponse


def create_intent_draft(request: IntentDraftRequest) -> IntentDraftResponse:
    return IntentDraftResponse(
        draft_id=f"idraft_{uuid4().hex}",
        status="draft_created",
        message="Intent draft created. User confirmation and signing are not implemented yet.",
        intent=request,
    )