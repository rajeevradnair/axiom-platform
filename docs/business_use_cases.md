# Business Use Cases

Axiom is a trusted authorization platform for agentic commerce.

It supports many commerce workflows through one REUSABLE pattern:

1. A user defines an authorized boundary.
2. Axiom captures and signs that boundary as an Intent Mandate.
3. An AI agent searches, compares, and submits a Cart Mandate.
4. Axiom evaluates the Cart Mandate against the signed Intent Mandate.
5. Axiom returns APPROVED, DECLINED, or STEP_UP_REQUIRED.

The AI agent is never the source of truth for user intent.

## Universal Axiom Pattern

Every Axiom business flow reduces to the same structure.

| Stage | Meaning |
|---|---|
| User Instruction | Natural-language request from the user |
| Intent Draft | Structured draft created by Intent Intelligence |
| User Confirmation | User reviews and confirms the draft |
| Intent Mandate | Signed representation of what the user authorized |
| Agent Search | Agent searches merchants, offers, inventory, or services |
| Cart Mandate | Agent-submitted proposed purchase |
| Policy Evaluation | Deterministic comparison against signed intent |
| Risk Scoring | Fraud, misuse, mismatch, or escalation risk |
| Authorization Decision | APPROVED, DECLINED, or STEP_UP_REQUIRED |
| Evidence | Audit trail explaining why the decision happened |

## Use Case 1: AI Travel Booking Agent

### User Instruction

Find me a nonstop flight to New York next Friday under $500.
Use my premium travel card if benefits apply.
Ask me before checkout.

### Trusted Intent Mandate

| Field | Value |
|---|---|
| intent_type | travel_booking |
| destination | New York |
| origin | user_profile_default_airport |
| max_amount | 500 |
| currency | USD |
| flight_preference | nonstop |
| approval_required | true |
| benefit_preference | premium_travel_card |

### Agent Cart Mandate

| Field | Value |
|---|---|
| merchant | Delta |
| route | LAX to JFK |
| amount | 472 |
| currency | USD |
| category | travel |
| flight_type | nonstop |

### Policy Checks

- Amount must be less than or equal to 500.
- Destination must match New York.
- Flight must be nonstop.
- Category must be travel.
- User approval is required before checkout.

### Expected Decision

STEP_UP_REQUIRED

### Why

The cart appears compliant, but the user explicitly requested confirmation before checkout.

## Use Case 2: AI Dining Reservation and Payment Agent

### User Instruction

Book dinner for 4 in Santa Monica this Saturday.
Vegetarian-friendly.
Budget: $250.
Use restaurants where I may have dining benefits.

### Trusted Intent Mandate

| Field | Value |
|---|---|
| intent_type | dining_reservation |
| location | Santa Monica |
| party_size | 4 |
| max_amount | 250 |
| currency | USD |
| dietary_preference | vegetarian_friendly |
| benefit_preference | dining_benefits |

### Agent Cart Mandate

| Field | Value |
|---|---|
| merchant | Vegetarian-friendly restaurant |
| location | Santa Monica |
| amount | 80 |
| currency | USD |
| category | dining |
| party_size | 4 |
| charge_type | reservation_deposit |

### Policy Checks

- Location must match Santa Monica.
- Category must be dining.
- Amount must be within budget.
- Party size must match.
- Restaurant must satisfy vegetarian-friendly preference.
- Dining benefit eligibility should be checked if available.

### Expected Decision

APPROVED_PENDING_VCC

### Why

The proposed reservation deposit fits the user-authorized dining boundary.

## Use Case 3: Small-Business Inventory Refill Agent

### User Instruction

Every Friday, reorder printer paper and shipping labels from approved vendors.
Monthly cap: $2,000.
No single order above $400 without approval.
Approved vendors only.

### Trusted Intent Mandate

| Field | Value |
|---|---|
| intent_type | recurring_business_purchase |
| allowed_categories | office_supplies |
| approved_vendors_only | true |
| monthly_cap | 2000 |
| per_order_step_up_threshold | 400 |
| schedule | weekly_friday |

### Agent Cart Mandate: Attempt 1

| Field | Value |
|---|---|
| merchant | Office Depot |
| amount | 385 |
| category | office_supplies |
| currency | USD |

### Expected Decision: Attempt 1

APPROVED_PENDING_VCC

### Agent Cart Mandate: Attempt 2

| Field | Value |
|---|---|
| merchant | Unknown Electronics Store |
| amount | 875 |
| category | electronics |
| currency | USD |

### Expected Decision: Attempt 2

DECLINED

### Reason Codes

- MERCHANT_NOT_APPROVED
- CATEGORY_NOT_ALLOWED
- AMOUNT_REQUIRES_APPROVAL

### Why

The second attempt violates vendor, category, and approval-threshold constraints.

## Use Case 4: AI Subscription Renewal Agent

### User Instruction

Review my annual subscriptions.
Renew only the ones I used at least 3 times in the last 90 days.
Cancel duplicates.
Ask before anything over $100.

### Trusted Intent Mandate

| Field | Value |
|---|---|
| intent_type | subscription_renewal |
| usage_threshold_90d | 3 |
| duplicate_detection_required | true |
| step_up_threshold | 100 |
| currency | USD |

### Policy Checks

- Subscription must have been used at least 3 times in the last 90 days.
- Duplicate subscriptions must be declined.
- Renewals over $100 require step-up.
- Merchant identity must match known subscription merchant.

### Decision Examples

| Agent Proposal | Decision | Reason |
|---|---|---|
| $79 productivity app renewal | APPROVED_PENDING_VCC | Used frequently and under threshold |
| $149 software renewal | STEP_UP_REQUIRED | Amount exceeds confirmation threshold |
| Duplicate streaming subscription | DECLINED | Duplicate subscription detected |

## Use Case 5: AI Merchant-Offer Shopping Agent

### User Instruction

I need a laptop bag, noise-canceling headphones, and travel shoes.
Find options where I can use eligible merchant offers or bonus rewards.
Total budget: $700.

### Trusted Intent Mandate

| Field | Value |
|---|---|
| intent_type | multi_item_purchase |
| requested_items | laptop_bag, headphones, travel_shoes |
| max_total_amount | 700 |
| offer_preference | merchant_offer_or_bonus_rewards |
| currency | USD |

### Agent Cart Mandate

| Item | Amount |
|---|---|
| Laptop bag | 120 |
| Headphones | 329 |
| Travel shoes | 180 |
| Total | 629 |

Additional cart fields:

| Field | Value |
|---|---|
| eligible_offer | spend_300_get_30_back |
| merchant_network | amex_network |
| currency | USD |

### Policy Checks

- Total amount must be less than or equal to 700.
- Items must match requested item categories.
- Offer eligibility must be verified.
- Cardmember eligibility must be verified.
- Merchant risk must be acceptable.

### Expected Decision

APPROVED_PENDING_VCC or STEP_UP_REQUIRED

### Why

The cart fits the budget, but Axiom may require step-up depending on risk, merchant trust, or offer rules.

## Use Case 6: Agent Purchase Protection and Dispute Evidence

### User Instruction

Buy me a black carry-on suitcase under $250.

### Trusted Intent Mandate

| Field | Value |
|---|---|
| intent_type | purchase |
| item_description | black carry-on suitcase |
| allowed_category | travel_accessories |
| max_amount | 250 |
| currency | USD |

### Agent Cart Mandate

| Field | Value |
|---|---|
| merchant | Luxury Luggage Co |
| item_description | checked luggage set |
| amount | 620 |
| currency | USD |
| category | travel_accessories |

### Policy Checks

- Amount must be less than or equal to 250.
- Item must match carry-on suitcase intent.
- Category must be allowed.
- Signed mandate must be valid.

### Expected Decision

DECLINED

### Reason Codes

- AMOUNT_EXCEEDS_LIMIT
- ITEM_MISMATCH
- INTENT_VIOLATION

### Evidence Needed Later

- Original user prompt
- Structured Intent Mandate
- Intent payload hash
- User signature verification result
- Agent Cart Mandate
- Policy violations
- Final decision
- Human-readable explanation

## Use Case 7: AI Business Travel Policy Agent

### User Instruction

Book my trip to Chicago for the client meeting.
Follow company travel policy.
Prefer flights under $600 and hotels under $250/night.
Use my corporate card.

### Trusted Intent Mandate

| Field | Value |
|---|---|
| intent_type | business_travel |
| destination | Chicago |
| flight_max_amount | 600 |
| hotel_max_nightly_amount | 250 |
| payment_instrument | corporate_card |
| policy_profile | company_travel_policy |

### Policy Checks

- Flight destination must match Chicago.
- Flight amount must be within policy or require approval.
- Hotel nightly rate must be within policy or require approval.
- Merchant category must match travel/lodging.
- Corporate card eligibility must be valid.
- Manager approval may be required for exceptions.

### Decision Examples

| Agent Proposal | Decision | Reason |
|---|---|---|
| Compliant hotel under $250/night | APPROVED_PENDING_VCC | Within policy |
| Flight above $600 | STEP_UP_REQUIRED | Exceeds preferred threshold |
| Luxury hotel outside policy | DECLINED | Policy violation |

## Use Case 8: AI Merchant-Bundle Shopping Agent

### User Instruction

Plan a weekend in Las Vegas under $1,200.
Include hotel, dinner, rideshare, and one show.
Use eligible merchant offers where available.

### Trusted Intent Mandate

| Field | Value |
|---|---|
| intent_type | bundled_commerce |
| destination | Las Vegas |
| max_total_amount | 1200 |
| required_components | hotel, dinner, rideshare, show |
| offer_preference | eligible_merchant_offers |
| currency | USD |

### Agent Cart Mandate

| Component | Merchant Type | Amount |
|---|---|---|
| Hotel | lodging | 650 |
| Dinner | dining | 180 |
| Rideshare | transportation | 90 |
| Show | entertainment | 220 |
| Total | multi_merchant_total | 1140 |

### Policy Checks

- Total bundle amount must be less than or equal to 1200.
- Required components must be present.
- Each merchant category must match the component.
- Each merchant must pass risk checks.
- Offer eligibility should be verified where claimed.
- Partial failure rules must be defined.

### Expected Decision

APPROVED_PENDING_MULTI_MERCHANT_CREDENTIALS

### Why

The bundle fits the total budget and required categories, but Axiom may issue separate scoped credentials for each merchant leg.

## Shared Reason Codes

Axiom should use standardized reason codes across all use cases.

| Reason Code | Meaning |
|---|---|
| AMOUNT_EXCEEDS_LIMIT | Cart amount exceeds authorized amount |
| CATEGORY_NOT_ALLOWED | Cart category is outside user authorization |
| ITEM_MISMATCH | Cart item does not match user intent |
| MERCHANT_NOT_APPROVED | Merchant is not in allowed merchant set |
| MERCHANT_RISK_TOO_HIGH | Merchant risk exceeds acceptable threshold |
| OFFER_NOT_ELIGIBLE | Claimed offer is not valid for the cardmember or merchant |
| CARDMEMBER_NOT_ELIGIBLE | User is not eligible for the requested benefit |
| TIME_WINDOW_EXPIRED | Intent Mandate is expired |
| APPROVAL_REQUIRED | User confirmation is required |
| POLICY_VIOLATION | Corporate or user policy was violated |
| DUPLICATE_SUBSCRIPTION | Subscription appears to duplicate an existing one |
| USAGE_THRESHOLD_NOT_MET | Renewal usage requirement was not satisfied |
| INTENT_VIOLATION | Agent proposal violates the signed user intent |


## Shared Decision Outcomes

| Decision | Meaning |
|---|---|
| APPROVED | The cart is allowed immediately |
| APPROVED_PENDING_VCC | The cart is allowed and requires scoped payment credential issuance |
| APPROVED_PENDING_MULTI_MERCHANT_CREDENTIALS | The bundle is allowed but requires separate scoped credentials |
| DECLINED | The cart violates intent, policy, risk, or trust rules |
| STEP_UP_REQUIRED | The user or manager must approve before payment |
| HUMAN_CLARIFICATION_REQUIRED | The original intent is too ambiguous to safely authorize |

## Shared Object Summary

Across all use cases, Axiom repeatedly uses the same objects.

| Object | Purpose |
|---|---|
| Intent Draft | Structured but unconfirmed version of user request |
| Intent Mandate | User-confirmed signed authorization boundary |
| Cart Mandate | Agent-submitted purchase proposal |
| Policy Decision | Deterministic result of rule evaluation |
| Risk Score | ML or heuristic estimate of misuse/fraud/mismatch |
| Virtual Card Controls | Payment-rail constraints derived from the mandate |
| Evidence Packet | Cryptographic and human-readable proof of the decision |

The most important design lesson is:

Business workflows differ, but the authorization pattern stays the same.