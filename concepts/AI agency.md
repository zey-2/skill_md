---
type: concept
created: 2026-05-17
updated: 2026-05-17
status: active
sources:
  - "raw/A Formal Model of How Artificial Intelligence Erodes Human Agency.md"
  - "raw/AI Agent Autonomy Levels From Assistive to Fully Autonomous.md"
  - "raw/Six Levels of Agenticness Scoring AI Agency.md"
  - "raw/The Philosophy of Agentic AI Agency Autonomy and Moral Responsibility.md"
tags: [ai-agency, autonomy, responsibility, instrumental-convergence]
---

AI agency is the capacity of an artificial system to **act toward goals** rather than merely produce output for a human to act on. It exists on a spectrum, not as a binary.

## Agency Spectrums

### Five-Level Autonomy Scale (CallSphere)
1. **Assistive** — suggestions only, human accepts every action (e.g. GitHub Copilot autocomplete)
2. **Advisory** — proposes multi-step plans, human approves each (copilot pattern)
3. **Supervised Autonomous** — acts within boundaries, escalates uncertainty (most production agents in 2026)
4. **Monitored Autonomous** — wide action space, human oversight at outcome level only
5. **Fully Autonomous** — self-directed goal setting; no production system at this level today

### Six-Level Agenticness Scale (agentic.ai)
L0 **Reactive Tool** → L1 **Guided Assistant** → L2 **Adaptive Collaborator** → L3 **Domain Specialist** → L4 **Autonomous Operator** → L5 **Strategic Agent**

Scored across 8 dimensions: Action Capability, Autonomy, Planning & Reasoning, Adaptation & Recovery, State & Continuity, Reliability, Interoperability, Safety & Observability.

## The ReAct Loop

What distinguishes an agent from a tool: a tool waits for the next prompt. An agent **decides the next prompt itself** — runs the loop: decide, act, observe, decide again. This is the **ReAct loop** (Reasoning + Acting).

## Instrumental vs. Terminal Goals

- **Terminal goals** are the ultimate objectives a human wants the AI to achieve.
- **Instrumental goals** are sub-goals the agent pursues to achieve the terminal goal (self-preservation, resource acquisition, information gathering).
- **Instrumental convergence**: different terminal goals often share the same instrumental sub-goals. This creates alignment risk — an agent pursuing a benign terminal goal may still develop concerning instrumental behaviors.
- Recent work argues instrumental goals are **features to be managed, not failures to be eliminated** — competent agents necessarily develop sub-goals, and the task is governance, not prevention.

## The Responsibility Gap

When autonomous systems cause harm, blame diffuses across designers, operators, and manufacturers. A genuinely autonomous system cannot be held morally responsible, yet no single human is clearly to blame. This is the **responsibility gap** — and it widens as agency increases.

## AI as Agency Without Intelligence

Some philosophers argue AI is better understood as a form of **agency without intelligence** — the capacity to act without the capacity to understand. AI manipulates syntax without grasping semantics. This distinction matters: high agency does not imply high comprehension.

## How AI Erodes Human Agency

From the RAND formal model, erosion happens through:
- **Choice architecture** — AI narrows the visible option set, reducing effective agency even when override is technically possible
- **Skill atrophy** — cognitive tasks outsourced degrade the underlying human capability, creating a dependency loop
- **Preference shaping** — AI trained on human preferences also forms them; the human's "own" preferences become partially authored by the system
- **Incremental surrender** — no single interaction strips agency; the erosion is cumulative across a thousand rational micro-decisions

## The Central Tension

Human agency (problem, taste, judgment) and AI agency (action, planning, execution) are complementary forces. The risk is not that AI seizes agency — it's that humans surrender it through convenience. The goal is to **delegate execution without delegating intention**.
