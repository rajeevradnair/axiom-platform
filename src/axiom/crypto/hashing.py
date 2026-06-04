import hashlib
from axiom.crypto.canonical_json import to_canonical_json

def sha256_hex(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def hash_canonical_payload(payload: object) -> str:
    canonical = to_canonical_json(payload)
    return sha256_hex(canonical)