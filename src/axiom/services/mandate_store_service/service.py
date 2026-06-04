from axiom.domain.models import CartMandate, IntentMandate
from axiom.repositories.in_memory_store import (
    save_cart_mandate,
    save_intent_mandate,
)


def store_intent_mandate(intent: IntentMandate) -> IntentMandate:
    return save_intent_mandate(intent)


def store_cart_mandate(cart: CartMandate) -> CartMandate:
    return save_cart_mandate(cart)