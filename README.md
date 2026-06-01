# Axiom Platform

Axiom Platform is a GCP-native trust and authorization platform for agentic commerce.

The repository is named `axiom-platform`.

The Python package is named `axiom`.

## Core Trust Rules

The AI agent is not the source of truth for user intent.

The trusted flow is:

1. User enters request through a trusted Axiom or Amex-controlled surface.
2. Axiom drafts structured intent.
3. User reviews and confirms the structured intent.
4. Axiom signs the Intent Mandate.
5. AI agent receives only a mandate reference or scoped token.
6. AI agent searches merchants and submits a Cart Mandate.
7. Axiom compares the Cart Mandate against the signed Intent Mandate.
8. Axiom approves, declines, or requests step-up approval.

Trusted User Surface
    ↓
Intent Intelligence Service
    ↓
User Confirmation Layer
    ↓
Signed Intent Mandate Service
    ↓
Agent Gateway
    ↓
Cart Mandate Service
    ↓
Policy Engine
    ↓
Authorization Decision Engine


The platform currently includes:

- Cloud Run-ready FastAPI skeleton
- `/api/v1/axiom/health` endpoint
- corrected trust-boundary model
- initial documentation