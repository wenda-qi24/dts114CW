## Overview
- A Freudian dream interpretation website that guides users through a multi-step workflow: dream input (manifest content) → 5–7 open-ended follow-up questions → therapeutic analysis.  
- The system uses Freudian concepts (free association, latent content, wish fulfillment, condensation/displacement) to generate insights and well-being suggestions in a professional, nonjudgmental tone.  
- User sessions persistently store the dream, generated questions, user answers, and the final interpretation for later review and continuity.  

## Goals
- Help Dreamers explore possible latent content and wish fulfillment themes through structured free-association prompts and reflective analysis.  
- Deliver a safe, therapeutic, professional user experience with clear consent and gentle language around sensitive material.  
- Provide reliable session storage and retrieval so users and admins can review prior dreams, questions, answers, and interpretations.  

## Non-Goals
- The product does not provide diagnosis, crisis counseling, or replace psychotherapy, and it avoids definitive claims about the user’s unconscious.  
- The product does not offer real-time clinician chat or guarantee clinical accuracy of interpretations.  
- The product does not monetize or share user dream content for advertising or third-party profiling.  

## User Personas (brief)
- Dreamer: Shares dream manifest content, answers 5–7 open-ended questions, and reviews interpretation and well-being suggestions with strong privacy controls.  
- Freudian AI Analyst: Generates theory-based questions and produces structured interpretations referencing latent content, wish fulfillment, and free association while maintaining clinical-style boundaries.  
- Administrator: Manages session data, auditing, retention/deletion requests, and policy enforcement to maintain safety, privacy, and compliance.  

## Key Features
- Guided multi-step flow with dream entry, 5–7 open-ended follow-up questions, and a final analysis grounded in Freudian theory (latent vs. manifest content, wish fulfillment, condensation/displacement).  
- Session management that saves and organizes dream text, question set, answers, and analysis with timestamps for later review.  
- Therapeutic, professional UX copy with consent prompts, content warnings when appropriate, and gentle reflection suggestions for well-being.  

## User Flows
- Dreamer starts a session, enters the dream (manifest content), and confirms consent and privacy preferences before proceeding.  
- System generates 5–7 open-ended Freudian follow-up questions, the Dreamer answers them, and can edit responses before analysis.  
- System produces an interpretation (linking answers to free associations and possible latent themes) plus well-being suggestions, then saves the complete session for later access.  

## Functional Requirements
- The system must generate 5–7 open-ended questions per dream that encourage free association and clarify affect, symbols, relationships, and conflicts.  
- The system must produce a structured interpretation referencing manifest content, hypothesized latent content, and wish fulfillment, with supportive well-being suggestions in a professional tone.  
- The system must store and retrieve sessions containing dream input, generated questions, user answers, and the final analysis, with user access controls and admin tools for auditing/export/deletion.  

## Non-Functional Requirements
- Privacy and security: encrypt data in transit and at rest, enforce least-privilege access, and log access to stored sessions for auditing.  
- Safety and quality: apply content policies to avoid harmful or sexualized speculation, include disclaimers, and provide escalation guidance for self-harm indicators without claiming clinical authority.  
- Performance and reliability: load core pages quickly, generate questions and analysis within acceptable latency, and ensure high availability with backups for stored sessions.  

## Constraints/Assumptions
- Interpretations are reflective and probabilistic, explicitly framed as exploratory rather than factual, and consistently use therapeutic/professional language.  
- Users may provide highly sensitive content; the system assumes strict consent, clear deletion options, and configurable retention policies are required.  
- The AI must operate within policy constraints that limit explicit content, reduce risk of coercive conclusions, and avoid diagnosing mental health conditions.  

## Success Metrics
- Completion rate of the multi-step workflow (dream input → questions → analysis) and percentage of sessions saved successfully without errors.  
- User-reported helpfulness and perceived safety of questions and interpretations (e.g., post-session ratings and qualitative feedback).  
- Retention and return usage for session review (e.g., users revisiting saved sessions) alongside low incidence of safety-policy violations.  

## Open Questions
- What retention defaults and deletion flows (immediate vs. scheduled purge) best balance user control, safety auditing, and compliance requirements?  
- Should the analysis be presented as a single narrative or segmented sections (manifest summary, free associations, latent hypotheses, wish fulfillment, well-being suggestions) for clarity and safety?  
- What administrator capabilities are necessary beyond retrieval (e.g., redaction tools, consent logs, export formats) while minimizing exposure to sensitive content?