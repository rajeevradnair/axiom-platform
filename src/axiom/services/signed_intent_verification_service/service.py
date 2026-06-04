from axiom.crypto.hashing import hash_canonical_payload
from axiom.crypto.ecdsa_keys import load_public_key_from_pem
from axiom.crypto.signatures import verify_payload_signature
from axiom.domain.models import SignedIntentMandate

def verify_signed_intent(signed_intent: SignedIntentMandate) -> bool:
    recomputed_hash = hash_canonical_payload(signed_intent.payload)

    if recomputed_hash != signed_intent.payload_hash:
        return False

    public_key = load_public_key_from_pem(
        signed_intent.public_key_pem.encode("utf-8")
    )

    return verify_payload_signature(
        payload=signed_intent.payload,
        signature_base64=signed_intent.signature,
        public_key=public_key,
    )