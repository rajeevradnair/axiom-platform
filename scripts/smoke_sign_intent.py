from datetime import datetime, timezone
from decimal import Decimal

from axiom.crypto.ecdsa_keys import (
    generate_private_key,
    private_key_to_pem,
    public_key_to_pem,
    load_private_key_from_pem,
    load_public_key_from_pem,
)
from axiom.crypto.signatures import sign_payload, verify_payload_signature
from axiom.domain.enums import IntentType
from axiom.domain.models import IntentMandate

intent = IntentMandate(
    mandate_id="im_signed_001",
    user_id="usr_456",
    intent_type=IntentType.PURCHASE,
    item_description="black carry-on suitcase",
    allowed_categories=["travel_accessories"],
    max_amount=Decimal("250.00"),
    currency="USD",
    expires_at=datetime(2099, 1, 1, tzinfo=timezone.utc),
    approval_required=False,
    per_order_approval_threshold=None,
)

private_key = generate_private_key()

private_key_pem = private_key_to_pem(private_key)
public_key_pem = public_key_to_pem(private_key)

loaded_private_key = load_private_key_from_pem(private_key_pem)
loaded_public_key = load_public_key_from_pem(public_key_pem)

payload_hash, signature = sign_payload(
    payload=intent,
    private_key=loaded_private_key,
)

print("Payload hash:")
print(payload_hash)
print()

print("Signature:")
print(signature)
print()

is_valid = verify_payload_signature(
    payload=intent,
    signature_base64=signature,
    public_key=loaded_public_key,
)

print("Valid signature verifies: ", is_valid)
print()


tampered_intent = IntentMandate(
    mandate_id="im_signed_001",
    user_id="usr_456",
    intent_type=IntentType.PURCHASE,
    item_description="black carry-on suitcase",
    allowed_categories=["travel_accessories"],
    max_amount=Decimal("2500.00"),
    currency="USD",
    expires_at=datetime(2099, 1, 1, tzinfo=timezone.utc),
    approval_required=False,
    per_order_approval_threshold=None,
)

tampered_is_valid = verify_payload_signature(
    payload=tampered_intent,
    signature_base64=signature,
    public_key=loaded_public_key,
)

print("Tampered signature verifies: ", tampered_is_valid)
