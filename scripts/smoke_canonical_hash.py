from datetime import datetime, timezone
from decimal import Decimal

from axiom.crypto.canonical_json import to_canonical_json
from axiom.crypto.hashing import hash_canonical_payload
from axiom.domain.enums import IntentType
from axiom.domain.models import IntentMandate

intent = IntentMandate(
    mandate_id="im_hash_001",
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

canonical = to_canonical_json(intent)
payload_hash = hash_canonical_payload(canonical)

print("Canonical JSON:")
print(canonical)
print()
print("SHA-256 hash:")
print(payload_hash)


payload1 = {
    "user_id": "usr_456",
    "mandate_id": "im_hash_001",
    "intent_type": "purchase",
    "item_description": "black carry-on suitcase",
    "currency": "USD",
    "max_amount": Decimal("250.00"),
    "allowed_categories": ["travel_accessories"],
    "expires_at": datetime(2099, 1, 1, tzinfo=timezone.utc),
    "approval_required": False,
    "per_order_approval_threshold": None,
}
payload2 = {
    "max_amount": Decimal("250.00"),
    "user_id": "usr_456",
    "mandate_id": "im_hash_001",
    "per_order_approval_threshold": None,
    "item_description": "black carry-on suitcase",
    "currency": "USD",
    "intent_type": "purchase",
    "allowed_categories": ["travel_accessories"],
    "approval_required": False,
    "expires_at": datetime(2099, 1, 1, tzinfo=timezone.utc),
}
payload_tampered = {
    "mandate_id": "im_hash_001",
    "user_id": "usr_456",
    "intent_type": "purchase",
    "item_description": "black carry-on suitcase",
    "allowed_categories": ["travel_accessories"],
    "max_amount": Decimal("2500.00"),
    "currency": "USD",
    "expires_at": datetime(2099, 1, 1, tzinfo=timezone.utc),
    "approval_required": False,
    "per_order_approval_threshold": None,
}

print(to_canonical_json(payload1) == to_canonical_json(payload2))
print(hash_canonical_payload(to_canonical_json(payload1)) == hash_canonical_payload(to_canonical_json(payload2)))
print(hash_canonical_payload(to_canonical_json(payload1)) == hash_canonical_payload(to_canonical_json(payload_tampered)))