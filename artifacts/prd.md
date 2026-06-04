## Overview
- Build a Freudian dream interpretation website that guides users through a multi-step workflow: dream input → 5–7 open-ended follow-up questions → analysis.
- Use Freudian concepts (manifest vs. latent content, wish fulfillment, free association) to generate therapeutic, professional interpretations and well-being suggestions.
- Store user sessions containing the dream description, generated questions, user answers, and final analysis for later review, export, or deletion.
- Provide clear consent, privacy controls, and safety-oriented language that supports reflection without presenting as medical diagnosis.

## Goals
- Help Dreamers capture manifest dream material and explore latent content through guided free association questions.
- Generate a coherent Freudian interpretation emphasizing hypotheses about wish fulfillment and unconscious conflict, with practical well-being suggestions.
- Enable secure session persistence and retrieval so users can track themes across multiple dreams over time.
- Maintain a consistently therapeutic and professional tone in all user-facing copy and AI outputs.

## Non-Goals
- Provide psychotherapy, clinical diagnosis, crisis counseling, or replace professional mental health care.
- Guarantee “correct” interpretations or claims of factual accuracy about the user’s unconscious motives.
- Perform identity verification beyond standard account/session security needs or share session content with third parties by default.
- Support non-Freudian schools of interpretation as primary frameworks (e.g., Jungian, cognitive, spiritual), except as optional disclaimers.

## User Personas (brief)
- Dreamer: Wants a safe, private place to describe dreams, answer 5–7 prompts, receive a gentle interpretation, and revisit or delete saved sessions.
- Freudian AI Analyst: Needs structured context (dream + answers + optional prior sessions) to differentiate manifest/latent content and form non-overreaching wish-fulfillment hypotheses.
- Administrator: Needs tools for secure storage, access control, retention/deletion workflows, and monitoring for safety, quality, and compliance.

## Key Features
- Dream intake form with supportive guidance, consent language, and optional tagging (date, emotions, recurring themes) to anchor later reflection.
- Automated generation of 5–7 Freudian-theory-based open-ended questions designed to elicit free association and probe latent content.
- Interpretation page that summarizes manifest content, proposes latent themes and wish-fulfillment hypotheses, and offers well-being suggestions and reflection prompts.
- Session library with secure storage of dream, questions, answers, and analysis plus controls to view, export, and delete sessions.

## User Flows
- Dream input: User enters dream narrative, confirms consent/privacy, and submits to begin the interpretation workflow.
- Follow-up questions: System presents 5–7 prompts sequentially, allowing edits and encouraging free association with gentle, non-leading language.
- Analysis: System synthesizes dream + answers into a Freudian interpretation (manifest vs. latent content, wish fulfillment) and provides well-being suggestions.
- Review later: User opens the session library to revisit prior sessions, compare themes, and export or delete data.

## Functional Requirements
- The system must generate 5–7 open-ended, Freudian-aligned questions that adapt to dream content and prior answers without making diagnostic claims.
- The system must produce an analysis that explicitly separates manifest content from hypothesized latent content and frames wish-fulfillment interpretations as tentative.
- The system must store per-session objects (dream text, questions, answers, analysis, timestamps) and support retrieval, update (edits), export, and deletion.
- The system must present therapeutic, professional UI copy and safety prompts, including clear disclaimers and escalation guidance for distressing content.

## Non-Functional Requirements
- Security and privacy: Encrypt data in transit and at rest, enforce access control, and minimize exposure of sensitive session content in logs.
- Reliability: Ensure session saves are durable and recoverable, with graceful handling of timeouts during multi-step Q&A.
- Performance: Provide responsive interactions where question generation and analysis complete within acceptable UX thresholds for web apps.
- Quality and safety: Maintain consistent tone, reduce harmful or shaming content, and provide monitoring/feedback loops for improving outputs.

## Constraints/Assumptions
- Interpretations are psychoanalytic hypotheses and must be framed as reflective content, not medical advice or factual determinations.
- Users may provide highly sensitive personal material, so the product assumes strict data minimization, explicit consent, and user-controlled deletion.
- The workflow assumes a minimum viable experience without requiring user accounts, but persistent session storage may require authentication for cross-device access.
- Model outputs may vary, so the product assumes ongoing prompt/guardrail tuning and admin review processes for safety and consistency.

## Success Metrics
- Completion rate for the multi-step workflow (dream input → questions answered → analysis viewed) and drop-off points per step.
- User-reported helpfulness and tone ratings for questions and analysis, including perceived safety and non-judgment.
- Session retention behaviors: percentage of users returning to review saved sessions and frequency of theme-tracking across multiple dreams.
- Safety and compliance indicators: rate of flagged outputs, time-to-resolution for incidents, and successful fulfillment of export/delete requests.

## Open Questions
- Should sessions be available without accounts (device-based) and how will cross-device access work while maintaining privacy guarantees?
- What level of prior-session context should the AI use by default to identify recurring themes without overfitting or exposing sensitive history?
- What specific guardrails and refusal patterns are needed for content involving trauma, self-harm, or abuse while preserving a therapeutic tone?
- What data retention defaults (e.g., auto-delete after X days) best balance user value with privacy and compliance requirements?