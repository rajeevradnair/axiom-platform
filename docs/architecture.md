# Architecture

Axiom is a trusted authorization layer for agentic commerce.

It does not browse merchant sites.

It does not act as the shopping agent.

It verifies that an AI agent's proposed cart matches a user-confirmed, Axiom-signed Intent Mandate.

## Trust Flow

User
  ↓
Trusted Axiom / Amex Surface
  ↓
Intent Intelligence Service
  ↓
User Confirmation Layer
  ↓
Mandate Signing Service
  ↓
Signed Intent Store
  ↓
AI Agent receives mandate_id or scoped token
  ↓
AI Agent searches merchants
  ↓
AI Agent submits Cart Mandate
  ↓
Axiom Policy Engine evaluates cart
  ↓
APPROVED / DECLINED / STEP_UP_REQUIRED

## Core Architecture Rule

The AI agent can:

- search merchants
- compare products
- propose a cart
- submit a Cart Mandate

The AI agent cannot:

- create the final Intent Mandate
- alter the signed Intent Mandate
- approve payments
- override policy
- mutate user authorization