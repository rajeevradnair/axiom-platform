from axiom.crypto.ecdsa_keys import (
    generate_private_key,
    public_key_to_pem,
)
from axiom.crypto.signatures import sign_payload
from axiom.domain.models import IntentMandate, SignedIntentMandate
from axiom.repositories.in_memory_store import save_signed_intent_mandate


def sign_intent_mandate(intent: IntentMandate) -> SignedIntentMandate:
    private_key = generate_private_key()
    public_key_pem = public_key_to_pem(private_key).decode("utf-8")

    payload_hash, signature = sign_payload(
        payload=intent,
        private_key=private_key,
    )

    signed_intent = SignedIntentMandate(
        mandate_id=intent.mandate_id,
        payload=intent,
        payload_hash=payload_hash,
        signature=signature,
        signing_key_id=f"local_demo_key_{intent.user_id}",
        public_key_pem=public_key_pem,
    )

    return save_signed_intent_mandate(signed_intent)