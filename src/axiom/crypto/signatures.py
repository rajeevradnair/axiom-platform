import base64

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

from axiom.crypto.hashing import hash_canonical_payload


def sign_payload_hash(
    payload_hash: str,
    private_key: ec.EllipticCurvePrivateKey,
) -> str:
    signature = private_key.sign(
        payload_hash.encode("utf-8"),
        ec.ECDSA(hashes.SHA256()),
    )

    return base64.b64encode(signature).decode("utf-8")


def sign_payload(
    payload: object,
    private_key: ec.EllipticCurvePrivateKey,
) -> tuple[str, str]:
    payload_hash = hash_canonical_payload(payload)
    signature = sign_payload_hash(payload_hash, private_key)

    return payload_hash, signature


def verify_payload_signature(
    payload: object,
    signature_base64: str,
    public_key: ec.EllipticCurvePublicKey,
) -> bool:
    payload_hash = hash_canonical_payload(payload)
    signature = base64.b64decode(signature_base64.encode("utf-8"))

    try:
        public_key.verify(
            signature,
            payload_hash.encode("utf-8"),
            ec.ECDSA(hashes.SHA256()),
        )
        return True
    except InvalidSignature:
        return False