## Overview
- Build a Freudian dream interpretation website that guides users through a multi-step workflow: dream input → follow-up questions → analysis, using a therapeutic professional tone throughout.
- The system generates 5–7 open-ended Freudian-theory-based questions, then produces an interpretation highlighting manifest vs. latent content, wish fulfillment, and free association cues.
- Each interaction is stored as a user session containing the dream text, generated questions, user answers, and final analysis for later review.

## Goals
- Help Dreamers explore possible latent content and unconscious conflict by prompting free association and reflective self-inquiry in a supportive, non-judgmental manner.
- Deliver a structured Freudian interpretation plus practical well-being suggestions that avoid clinical diagnosis and encourage thoughtful reflection.
- Provide reliable session storage and retrieval so users can track themes and revisit prior analyses over time.

## Non-Goals
- Not a substitute for psychotherapy, crisis services, or medical/psychiatric diagnosis; the product must not claim clinical certainty or treatment outcomes.
- Not intended to provide dream “predictions,” supernatural explanations, or non-Freudian frameworks as primary interpretations.
- Not designed for real-time therapist-patient communication, billing, or regulated clinical record-keeping workflows.

## User Personas (brief)
- Dreamer: Submits dream narratives and answers 5–7 open-ended prompts, seeking a safe experience, consent clarity, and privacy controls for stored sessions.
- Freudian AI Analyst: Produces psychoanalytically grounded questions and interpretations, maintaining a professional therapeutic tone while avoiding overclaiming and harm.
- Administrator: Manages users, access, retention/deletion, audit logs, and monitoring to protect sensitive content and ensure reliability and safety.

## Key Features
- Guided multi-step interaction that separates manifest content capture (dream narrative) from latent content exploration (follow-up questions) before generating analysis.
- Question generation engine that outputs 5–7 open-ended prompts grounded in Freudian concepts (wish fulfillment, defenses, symbolism, free association).
- Interpretation report that summarizes themes, distinguishes manifest vs. latent content, notes possible conflicts/defenses, and offers gentle well-being suggestions and resources.
- Session library with search/filter and privacy controls to view, export, or delete saved sessions containing dream, questions, answers, and analysis.

## User Flows
- Dream input flow: User enters dream narrative, confirms consent and privacy expectations, and starts a new session with saved draft state.
- Follow-up questions flow: System generates 5–7 prompts, user answers in sequence (with optional skip), and progress is saved to the session.
- Analysis flow: System synthesizes dream + answers into a Freudian interpretation and suggestions, then saves and presents the final report for review and later access.

## Functional Requirements
- The system must create a session record that stores dream text, the exact set/order of generated questions, user answers, timestamps, and the final analysis output.
- The system must generate 5–7 open-ended Freudian prompts per dream, including at least one free association prompt and at least one wish-fulfillment/latent-content prompt.
- The system must produce an analysis that explicitly differentiates manifest vs. latent content, proposes hypotheses (not facts), and maintains a therapeutic professional tone.
- The system must provide authenticated access for users to list, open, export, and delete their sessions, and provide admin tools for moderation and audit review.

## Non-Functional Requirements
- Privacy and security: encrypt data in transit and at rest, enforce least-privilege access, and provide clear user controls for retention and deletion.
- Safety: include crisis/safety guidance for self-harm or acute distress disclosures and ensure content policies prevent harmful, shaming, or coercive language.
- Reliability and performance: autosave answers, support resumable sessions, and return question generation and analysis within defined latency targets.
- Accessibility and usability: responsive design, keyboard navigation, readable typography, and language that is empathetic, professional, and non-pathologizing.

## Constraints/Assumptions
- Interpretations are probabilistic and reflective, assuming limited context; the product must present outputs as exploratory hypotheses rather than definitive conclusions.
- The guided workflow assumes users can provide sufficient narrative detail and follow-up answers; the system must handle sparse input gracefully.
- Data storage assumes user accounts or anonymous session tokens; retention policies must be configurable by region and compliance needs.
- Freudian framing is the primary lens; the product assumes users consent to psychoanalytic language (e.g., latent content, wish fulfillment, defenses).

## Success Metrics
- Completion rate across steps (dream input → questions → analysis) and drop-off by step, indicating whether the guided flow is understandable and supportive.
- User-reported helpfulness and tone ratings for questions and analysis, including perceived safety, clarity, and therapeutic professionalism.
- Session return rate and session review frequency, showing that stored sessions provide ongoing reflective value over time.
- Safety and quality indicators: low rate of policy violations, high successful crisis-routing when needed, and low incidence of user reports about harmful output.

## Open Questions
- What level of anonymity is required (accountless sessions vs. accounts), and how will session recovery work without compromising privacy?
- What are the required compliance targets (e.g., GDPR deletion SLAs, data residency), and what default retention period should be used?
- How should the system adapt question sets for sensitive topics (trauma, sexuality, violence) while staying within a Freudian framework and maintaining safety?
- What evaluation rubric will define “Freudian quality” (e.g., explicit latent/manifest distinction, free association prompts, avoidance of overclaiming) for ongoing model tuning?