# Problem Statement

AI agents are becoming capable of searching, comparing, booking, renewing, reordering, and purchasing on behalf of users.

This creates a trust problem.

The user owns the money, liability, payment credential, and consequences, but the AI agent performs the action.

Axiom solves this by acting as a trusted authorization firewall between AI agents and payment systems.

## Core Business Problem

How can a financial platform allow AI agents to act on behalf of users without allowing those agents to exceed user intent?

## Core Security Problem

The AI agent must not be trusted to create the final user authorization object.

If the agent creates or controls the Intent Mandate, a compromised agent could change the user's true intent before authorization.

## Correct Principle

The user's intent must be captured through a trusted Axiom, Amex, wallet, browser extension, or device-controlled surface.

The AI agent may search and submit a cart, but it cannot be the source of truth for user intent.