---
type: concept
created: 2026-05-04
updated: 2026-06-14
status: active
sources:
  - "raw/Context Is the New Code — Patrick Debois, Tessl.md"
  - "raw/Reflecting on a year of Claude Code.md"
tags: [context, agent-skills, devops, lifecycle, context-minimalism]
---

# Context Development Lifecycle

## Summary

As AI coding agents become more capable, context (prompts, rules, skills, memory) matters as much as code. But while code has version control, review, testing, CI/CD, and production observability, context is still often managed as ad hoc hacks. Patrick Debois argues that context needs its own engineering discipline, modeled on the software development lifecycle and DevOps movement.

The **Context Development Lifecycle** has four stages forming an infinity loop: **Generate** → **Evaluate** → **Distribute** → **Observe**. This runs in two nested loops: an individual "library authoring loop" for crafting and testing context, and an "organizational loop" for sharing, monitoring, and improving context across teams.

Source: `raw/Context Is the New Code — Patrick Debois, Tessl.md`.

## The Analogy to DevOps

Debois draws a direct parallel to his 2009 DevOps work ("what if ops looked more like dev?"). The question now is: "if context is the new code, what does its lifecycle look like?" Code went through decades of discipline around SDLC, version control, testing, CI/CD, and observability. Context is at a much earlier stage but is shifting from an individual activity to a team and organizational concern.

## The Four Stages

### Generate

Context is created through prompting, reusable instructions (`CLAUDE.md`, `agent.md`, `SKILL.md`), pulling in documentation, MCP servers, Slack, tickets, and spec-driven development where agents break specifications into step-by-step plans. Even converting large code helpers into skills is a form of code transforming back into context. See [[Skill Authoring Workflow]] for detailed patterns.

### Evaluate

Context changes need testing. You cannot know the impact of changing two lines in `CLAUDE.md` without running evals. The evaluation ladder ranges from linting (structural checks) through Grammarly-style comprehension feedback, LLM-as-judge rule checking, unit-test-like criterion suites, to end-to-end tests where a judge agent executes the generated code in a sandbox. See [[Validation and Evaluation]] for detailed patterns.

A key difference from code testing: LLMs are non-deterministic. Running an eval once is weak evidence. Instead, run it multiple times and track pass rates. Error budgets are a useful mental model — some test suites matter more than others and should have stricter failure tolerances.

### Distribute

Context can be checked into repos for zero-friction sharing, but reusable context across projects needs packaging — like libraries. Skills are emerging as a standard package format containing context, scripts, documents, and MCP configurations. Registries enable discovery. Dependencies between context packages create dependency hell. Security scanning (credential exposure, prompt injection) and AI SBOM (tracking who built a skill, with what model) become necessary. See [[Skill Distribution and Installation]] for detailed patterns.

### Observe

Once distributed, context needs feedback channels: agent logs showing what context is missing, PR review feedback that points back to context gaps, production failures from incorrectly generated code, sandbox testing for security, and context filters to block prompt injections before they reach the agent. See [[Context Observability and Feedback]] for detailed patterns.

## Two Nested Loops

Debois frames the lifecycle as running at two scales:

| Loop | Scope | Analogy |
|---|---|---|
| Library authoring loop | Individual or small team crafting and testing context | SonarQube + CI/CD for a single library |
| Organizational loop | Sharing, monitoring, and improving context across teams | Enterprise library governance + feedback aggregation |

The individual loop focuses on creating good context for yourself. The organizational loop asks: "if everyone is missing this piece of context, how do we create it once and distribute it to everybody?"

## The Context Flywheel

Better context → better agent output → better observations → better context. Each stage of the lifecycle feeds the next, and the Observe stage closes the loop by feeding improvements back into Generate. Over time, this creates a compounding improvement cycle where shared context makes every agent in the organization more effective.

## Context as Fuel

Debois's framing: LLMs and coding agents are just the engine. Context is the fuel. If you give the engine the wrong fuel, it will not perform. Most engineers cannot change the LLM itself, but they can optimize their context. The practical implication is that engineering rigor applied to context — systematic generation, testing, distribution, and observation — matters more than tweaking prompts ad hoc.

## Context Minimalism: A Counterpoint

Boris Cherny (Head of Claude Code) and Cat Wu (Head of Product, Claude Code) advocate for **context minimalism**: "With the models of today, you don't do any of this [context engineering]. You give it the minimal possible system prompt, the minimal possible tools, and then you let the model figure it out. You just have to give the model some way to pull in the context."

Cat: "I'm a context minimalist. Tell the model only what it needs to know and let it figure out the rest. When you give the model too much context, it's kind of like you're micromanaging it."

This tensions with Debois's systematic context engineering. The resolution: context engineering applies to the **retrieval and tools layer** (how the agent pulls in context on demand), not to **verbose instructions** (telling the agent everything upfront). The shift is from "more context" to "better retrieval" — progressive disclosure via the file system, skills that point to references, and tools that fetch context when needed.

This is consistent with [[concepts/Progressive Disclosure]]: the skill's description field activates the skill, the instructions guide behavior, and the tools/references provide detail on demand. The context minimalist puts less in the system prompt and more in the skill's file structure.

Source: `raw/Reflecting on a year of Claude Code.md`.

## Connections

- [[Skill Authoring Workflow]] covers the Generate stage in detail.
- [[Validation and Evaluation]] covers the Evaluate stage, including non-determinism and error budgets.
- [[Skill Distribution and Installation]] covers the Distribute stage, including registries and dependency management.
- [[Context Observability and Feedback]] covers the Observe stage, including agent logs, production monitoring, and context filters.
- [[Harness Engineering Principles]] connects to the broader observability and feedback patterns.
- [[Skill Governance and Metrics]] connects to organizational-loop concerns about quality and trust at scale.
- [[sources/Reflecting on a year of Claude Code]] — Boris Cherny and Cat Wu on context minimalism: minimal system prompt, minimal tools, let the model figure it out.
- [[Progressive Disclosure]] — Context minimalism is consistent with progressive disclosure: less in the prompt, more in the file structure.

## Open Questions

- What are the right error-budget thresholds for different categories of context (safety-critical vs. convenience)?
- How should context dependency conflicts be resolved when packages from different teams specify contradictory rules?
- What does a mature AI SBOM look like, and should it be standardized across organizations?
- Can context filters block malicious patterns without also blocking legitimate context from third-party skills?
