# Trust Boundaries

Axiom is designed around strict trust boundaries.

The most important rule is:

The AI agent must never be the source of truth for user intent.

## Trusted Input

- User-confirmed intent through trusted Axiom or Amex surface
- Axiom-signed Intent Mandate

## Untrusted Input

- Agent-submitted Cart Mandate
- Merchant page content
- Agent-provided explanations
- External callbacks until verified

## Safe Failure Rule

If Axiom cannot verify intent, signature, key status, policy, or audit state, it must fail closed.

Fail closed means:

- decline
- pause
- require step-up
- return safe error

It must not approve an unsafe transaction.