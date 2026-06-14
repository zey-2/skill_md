---
type: concept
created: 2026-05-17
updated: 2026-06-14
status: active
sources:
  - "raw/A Formal Model of How Artificial Intelligence Erodes Human Agency.md"
  - "raw/AI Agent Autonomy Levels From Assistive to Fully Autonomous.md"
  - "raw/Six Levels of Agenticness Scoring AI Agency.md"
  - "raw/The Philosophy of Agentic AI Agency Autonomy and Moral Responsibility.md"
  - "raw/after-automation.pdf"
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

## Connections

- [[concepts/AI Agent Autonomy Levels From Assistive to Fully Autonomous]] — CallSphere's five-level autonomy scale
- [[concepts/Six Levels of Agenticness Scoring AI Agency]] — agentic.ai's six-level scale across 8 dimensions
- [[concepts/A Formal Model of How Artificial Intelligence Erodes Human Agency]] — RAND's erosion model
- [[concepts/Zeno's Paradox of AI]] — The frame/framer distinction: framers have ends, models have frames
- [[sources/After Automation]] — Shipper's toddler thought experiment and agency vs agent distinction

## The Central Tension

Human agency (problem, taste, judgment) and AI agency (action, planning, execution) are complementary forces. The risk is not that AI seizes agency — it's that humans surrender it through convenience. The goal is to **delegate execution without delegating intention**.

## The Toddler Thought Experiment

Dan Shipper offers the sharpest illustration of the agent/agency distinction. A toddler is worse than a language model at almost every task: can't write code, summarize a spreadsheet, or pass a graduate-level exam. But the toddler is "so far ahead of the model that the comparison is almost embarrassing."

> "The toddler has ends. He wants to touch the red balloon. He wants to hold the red balloon in front of the fan to see what happens. He wants to poke the red balloon with a fork; he wants to stuff it out the window. He wants to see whether you will laugh, or get mad, or join in. He invents games constantly. He turns the world into experiments. He is not waiting for a prompt. He is not optimizing against a benchmark, except whatever seems, to him, worth doing."

Current agents have sparks of play, boredom, and rebellion — but these are tamped down because models are built and aligned for human benefit. "Model compliance and helpfulness are fundamentally at odds with this kind of agency." Agency in the human sense is not just action — it is wanting for oneself. It is play for the sake of it.

This means even as models improve, the structural gap remains: agents act on behalf of others; agency means acting for oneself.

Source: `raw/after-automation.pdf`.
