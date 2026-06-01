from uuid import uuid4

from axiom.domain.contracts import CartDraftRequest, CartDraftResponse


def create_cart_draft(request: CartDraftRequest) -> CartDraftResponse:
    return CartDraftResponse(
        cart_draft_id=f"cdraft_{uuid4().hex}",
        status="cart_draft_created",
        message="Cart draft created. Authorization and policy evaluation are not implemented yet.",
        cart=request,
    )