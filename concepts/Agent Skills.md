---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/openaiskills Skills Catalog for Codex.md"
  - "raw/anthropicsskills Public repository for Agent Skills.md"
  - "raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
  - "raw/2026-04-26 MCP architecture and Agent Skills integration source.md"
  - "raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md"
  - "raw/2026-04-26 OpenAI Codex SDK and App Server source.md"
  - "raw/2026-04-26 Claude Agent SDK source.md"
  - "raw/2026-04-26 OpenAI Codex Plugins docs.md"
  - "raw/2026-04-26 Claude Code Plugins docs.md"
tags: [agent-skills, ai-agents]
---

# Agent Skills

## Summary

An agent skill is a packaged capability that helps an AI agent do a recurring kind of work more reliably. In plain language, it is a reusable instruction bundle: it tells the agent when to use it, what steps to follow, what files or scripts are available, and what constraints matter.

The earlier synthesis in `raw/skill.md for AI Agents.md` frames skills as a directory with a required `SKILL.md` file and optional supporting folders such as `scripts/`, `references/`, and `assets/`. The newer raw sources make that picture more concrete. They show that real skills are not limited to one narrow type of task. Some are domain helpers such as document editing or framework guidance. Others are workflow skills for planning, TDD, code review, debugging, safety guardrails, or multi-agent coordination. Sources: `raw/skill.md for AI Agents.md`, `raw/openaiskills Skills Catalog for Codex.md`, `raw/anthropicsskills Public repository for Agent Skills.md`, `raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md`, and `raw/obrasuperpowers An agentic skills framework & software development methodology that works.md`.

## Key Ideas and Evidence

- A skill is not just human documentation with a new filename. It is agent-facing operational guidance.
- A skill usually has a short routing layer, especially `name` and `description`.
- The main instruction file should stay concise enough for an agent to load without wasting context.
- Larger details belong in supporting resources, not in the core file.
- Repeatable or fragile tasks can be moved into scripts.
- Skills can package process knowledge, not just domain knowledge. The new raw sources include skills for PRD writing, issue slicing, TDD, interface design, git guardrails, debugging, and code review.
- Some ecosystems also use adjacent instruction surfaces, such as a project-level `CLAUDE.md`, to shape agent behavior. That serves a similar purpose, but it is not the same packaging model as a portable `SKILL.md` directory.
- Skills sit beside tools and orchestration, not inside them. A useful boundary is that skills package reusable operating knowledge, MCP servers and tools expose actions or context, and frameworks coordinate agents, state, control flow, and approvals.
- Plugins are the distribution and bundling layer above many skills. A local skill can guide one workflow, while a plugin can package that skill with app integrations, MCP server configuration, subagents, hooks, assets, marketplace metadata, and install policy.
- SDKs turn skills into automatable runtime assets. Codex SDK can invoke Codex programmatically, Codex App Server can embed rich Codex client behavior, and Claude Agent SDK can load filesystem skills alongside commands, memory, plugins, MCP servers, and sessions.

The combined sources suggest a practical mental model for a curious beginner: a skill is a reusable operating procedure for an agent. Sometimes that procedure is "use this API correctly." Sometimes it is "plan before coding," "write tests first," or "stay inside a safe editing boundary."

## Where Sources Agree

The sources agree on the broad purpose: skills make agent behavior more repeatable by packaging instructions and resources. They also agree that the core file should contain routing metadata plus instructions, and that optional supporting files are useful for deeper reference material or executable help.

They also converge on another useful idea: a good skill changes how the agent works in practice. That can mean helping with a domain task, but it can also mean enforcing a disciplined workflow such as planning, testing, or code review.

## Where Sources Disagree

The sources disagree on how tightly the term "skill" should be defined. The package-oriented sources emphasize `SKILL.md` directories, optional resources, and installable catalogs. The `CLAUDE.md` source shows a nearby but different pattern: one behavior-shaping file that is merged into project instructions rather than distributed as a portable skill package.

They also differ in granularity. Some repositories publish many small skills for narrow activities. Others publish larger systems that bundle a whole development method and dispatch multiple sub-skills behind the scenes.

The likely reason is that each platform has a different runtime, UI, and installation model. A portable concept exists, but the operational boundaries are still settling.

## Connections

- [[SKILL.md Package Anatomy]] explains the file and folder structure.
- [[Portable Skill Core]] explains the shared metadata center.
- [[Progressive Disclosure]] explains why skills are split into metadata, core instructions, and resources.
- [[Skill Authoring Workflow]] explains how recurring tasks become reusable skills.
- [[Skill Distribution and Installation]] explains how skills reach different agent runtimes.
- [[Plugin-Based Agent Extensions]] explains why plugins matter as a packaging, distribution, and integration layer around skills.
- [[MCP and Tool-Integration Architecture]] explains how skills relate to tools, resources, prompts, and MCP servers.
- [[Agent Frameworks and Orchestration]] explains when skills should be combined with subagents, handoffs, or graph workflows.
- [[Agent SDKs and Codex Automation]] explains how skills relate to OpenAI Agents SDK, Codex SDK/App Server, and Claude Agent SDK.

## Open Questions

- Will the ecosystem converge on one cross-vendor schema beyond `name` and `description`?
- Will the boundary between installable skills and project-level behavior files stay separate, or blur further?
