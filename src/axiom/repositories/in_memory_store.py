from axiom.domain.models import CartMandate, IntentMandate, PolicyDecision, SignedIntentMandate

# Key will be the mandate_id for mandates and decision_id for policy decisions
INTENT_MANDATES: dict[str, IntentMandate] = {}
SIGNED_INTENT_MANDATES: dict[str, SignedIntentMandate] = {}
CART_MANDATES: dict[str, CartMandate] = {}
POLICY_DECISIONS: dict[str, PolicyDecision] = {}

def save_intent_mandate(intent: IntentMandate) -> IntentMandate:
    INTENT_MANDATES[intent.mandate_id] = intent
    return intent


def get_intent_mandate(mandate_id: str) -> IntentMandate | None:
    return INTENT_MANDATES.get(mandate_id)


def save_cart_mandate(cart: CartMandate) -> CartMandate:
    CART_MANDATES[cart.cart_mandate_id] = cart
    return cart


def get_cart_mandate(cart_mandate_id: str) -> CartMandate | None:
    return CART_MANDATES.get(cart_mandate_id)


def save_policy_decision(decision: PolicyDecision) -> PolicyDecision:
    POLICY_DECISIONS[decision.decision_id] = decision
    return decision

def save_signed_intent_mandate(signed_intent: SignedIntentMandate) -> SignedIntentMandate:
    SIGNED_INTENT_MANDATES[signed_intent.mandate_id] = signed_intent
    return signed_intent


def get_signed_intent_mandate(mandate_id: str) -> SignedIntentMandate | None:
    return SIGNED_INTENT_MANDATES.get(mandate_id)