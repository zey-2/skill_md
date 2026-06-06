---
type: concept
created: 2026-04-26
updated: 2026-06-06
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
  - "raw/Equipping agents for the real world with Agent Skills.md"
  - "raw/Agent Skills Overview.md"
  - "raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md"
tags: [agent-skills, progressive-disclosure, context-management]
---

# Progressive Disclosure

## Summary

Progressive disclosure means giving the agent only the information it needs at each stage. First the agent sees short metadata. If the skill looks relevant, it reads the main `SKILL.md`. If more detail is needed, it opens references, scripts, or assets.

This matters because agent context is limited. A skill that dumps everything into one file may be complete, but it can be harder to route, harder to read, and more expensive to load.

Sources: `raw/skill.md for AI Agents.md`, `raw/VoltAgentawesome-agent-skills`, `raw/Equipping agents for the real world with Agent Skills.md`, and `raw/Agent Skills Overview.md`.

## Key Ideas and Evidence

The original synthesis describes a three-level loading model: metadata first, then the `SKILL.md` body, then bundled resources only when needed. It also says OpenAI guidance recommends keeping the body to essentials and splitting larger reference material into separate files.

The newer curated source adds more concrete heuristics. It recommends keeping top-level metadata under about 100 tokens, keeping the skill body under about 500 lines, and loading large docs or schemas on demand instead of inlining them.

The key design rule is simple: the main skill file should explain the task, trigger conditions, steps, and constraints. Long schemas, examples, background docs, and detailed references should live elsewhere.

The agentskills.io open standard gives the three stages canonical names: **Discovery** (metadata at startup), **Activation** (reading `SKILL.md` when a task matches), and **Execution** (following instructions, loading referenced files or running scripts on demand). Anthropic's engineering article illustrates this with a context window diagram showing how the window grows as each level is loaded.

Anthropic's internal skill model uses the same three-layer structure with different names: (1) **description** — what Claude checks to decide whether to use the skill, (2) **instructions** — the step-by-step playbook, (3) **tools** — code scripts, API calls, reference files. The description maps to Discovery, instructions to Activation, and tools to Execution. Source: `raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md`.

## Where Sources Agree

The sources agree that the main skill file should be concise. They also agree that supporting resources are useful and should not be copied into the main file just because they are related.

They agree on the reason: agent skills are loaded into working context. Context should be reserved for what helps the task succeed right now.

## Where Sources Disagree

The sources differ more in precision than in principle. The earlier synthesis says "keep it lean" and notes a rough 500-line target from Anthropic-style guidance. The curated list turns that into a more operational checklist, including a token budget for top-level metadata.

Those numeric limits are best read as practical heuristics, not as a universal standard. A small workflow skill and a large technical reference skill may need different boundaries.

## Connections

- [[SKILL.md Package Anatomy]] describes the files used in progressive disclosure.
- [[Skill Authoring Workflow]] explains how to split a draft into core instructions and resources.
- [[Validation and Evaluation]] explains how to catch broken references.
- [[Skill Governance and Metrics]] includes token footprint and reference hit rate as quality metrics.
- [[concepts/Agent Legibility]] extends progressive disclosure to the repository level, with AGENTS.md as the table of contents.
- [[concepts/Replacing Code with Skills]] — Commands load prompts only when invoked, a just-in-time disclosure pattern that avoids context bloat while keeping instructions available when needed.
- [[Prompting Skills Not Prompts]] — the three-layer skill architecture (description, instructions, tools) maps directly to progressive disclosure stages.
- [[sources/How Anthropic Engineers ACTUALLY Prompt Claude Code]] — source for Anthropic's three-layer skill model.

## Open Questions

- What is the best target length for `SKILL.md` across different agent runtimes?
- Should skill repositories measure whether references are actually opened during successful tasks?
