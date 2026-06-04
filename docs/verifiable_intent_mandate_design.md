# Verifiable Intent Design

Axiom uses signed Intent Mandates to prove that a user confirmed a specific authorization boundary before an AI agent attempted a purchase.

The trusted flow is:

1. User enters a request through a trusted Axiom-controlled surface (app, web).
2. Intent Intelligence drafts structured intent.
3. User reviews and confirms the structured intent.
4. Axiom canonicalizes the confirmed Intent Mandate.
5. Axiom hashes the canonical payload.
6. Axiom signs the hash using a user-device or simulated private key.
7. Axiom stores the signed Intent Mandate.
8. Later, Axiom verifies the signature before policy evaluation.

## Threat Model

Axiom must defend against the following failures:

| Threat | Defense |
|---|---|
| Agent changes user intent | Signature verification fails |
| Merchant prompt injection changes mandate | Signed payload hash changes |
| User denies authorization | Signature + audit evidence prove confirmation |
| Stale or expired key signs a mandate | Key status check fails |
| Mandate payload is modified in storage | Recomputed hash does not match stored hash |
| Agent submits cart without valid mandate | Authorization fails closed |

## Canonical JSON

Before signing, Axiom must convert the Intent Mandate into a deterministic JSON representation.

Canonicalization rules include:

- Sort keys consistently.
- Remove unnecessary whitespace.
- Use stable date formats.
- Use stable decimal/money formatting.
- Exclude fields that should not be signed.

## ECDSA Signature

Axiom uses an ECDSA-style signature model.


## Signed Intent Mandate Shape

A future `SignedIntentMandate` object should include:

```json
{
  "mandate_id": "im_123",
  "payload": {
    "user_id": "usr_456",
    "intent_type": "purchase",
    "item_description": "black carry-on suitcase",
    "allowed_categories": ["travel_accessories"],
    "max_amount": "250.00",
    "currency": "USD",
    "expires_at": "2099-01-01T00:00:00Z",
    "approval_required": false,
    "per_order_approval_threshold": null
  },
  "payload_hash": "sha256_hex_value",
  "signature": "base64_signature_value",
  "signing_key_id": "key_user_device_001",
  "signature_algorithm": "ECDSA_P256_SHA256",
  "signed_at": "2026-06-03T00:00:00Z"
}
```

## Fail-Closed Verification Rules

Axiom must fail closed when any critical verification step fails.

| Condition | Result |
|---|---|
| Missing signed mandate | DECLINED |
| Payload hash mismatch | DECLINED |
| Invalid signature | DECLINED |
| Unknown signing key | DECLINED |
| Revoked key | DECLINED |
| Expired key | DECLINED |
| Compromised key | DECLINED |
| Signature verification service unavailable | DECLINED or 503 fail-closed |

## Authorization Integration

Before policy evaluation, Axiom must verify the signed intent.

Future authorization flow:

```text
POST /authorizations/evaluate-by-id
  ↓
load SignedIntentMandate
  ↓
verify payload hash
  ↓
verify signature
  ↓
check key status
  ↓
load CartMandate
  ↓
evaluate deterministic policy
  ↓
store PolicyDecision
  ↓
generate audit evidence