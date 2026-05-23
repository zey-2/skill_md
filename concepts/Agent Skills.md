---
type: concept
created: 2026-04-26
updated: 2026-05-20
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/openaiskills Skills Catalog for Codex.md"
  - "raw/anthropicsskills Public repository for Agent Skills.md"
  - "raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md"
  - "raw/mattpocockskills Skills for Real Engineers. Straight from my .claude directory.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
  - "raw/2026-04-26 MCP architecture and Agent Skills integration source.md"
  - "raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md"
  - "raw/2026-04-26 OpenAI Codex SDK and App Server source.md"
  - "raw/2026-04-26 Claude Agent SDK source.md"
  - "raw/2026-04-26 OpenAI Codex Plugins docs.md"
  - "raw/2026-04-26 Claude Code Plugins docs.md"
  - "raw/Equipping agents for the real world with Agent Skills.md"
  - "raw/Agent Skills Overview.md"
  - "raw/Agent Skills.md"
  - "raw/Introduction to Claude Skills.md"
  - "raw/Superpowers How Jesse Built the 1 AI Claude Code  Codex Plugin — and Stopped Writing Code.md"
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

The Superpowers video strengthens this operating-procedure view. Jesse Vincent describes skills as a way to encode the development habits he learned from managing junior engineers: clarify intent, write a spec, break work into small tasks, require tests, use fresh reviewers, and verify real behavior. This is evidence that mature skills can package a whole method of work, not merely a reusable prompt or tool wrapper. Source: [[sources/Superpowers How Jesse Built the 1 AI Claude Code Codex Plugin]].

## Where Sources Agree

The sources agree on the broad purpose: skills make agent behavior more repeatable by packaging instructions and resources. They also agree that the core file should contain routing metadata plus instructions, and that optional supporting files are useful for deeper reference material or executable help.

They also converge on another useful idea: a good skill changes how the agent works in practice. That can mean helping with a domain task, but it can also mean enforcing a disciplined workflow such as planning, testing, or code review.

## Where Sources Disagree

The sources disagree on how tightly the term "skill" should be defined. The package-oriented sources emphasize `SKILL.md` directories, optional resources, and installable catalogs. The `CLAUDE.md` source shows a nearby but different pattern: one behavior-shaping file that is merged into project instructions rather than distributed as a portable skill package.

They also differ in granularity. Some repositories publish many small skills for narrow activities. Others publish larger systems that bundle a whole development method and dispatch multiple sub-skills behind the scenes.

The likely reason is that each platform has a different runtime, UI, and installation model. A portable concept exists, but the operational boundaries are still settling.

## Skill Development Guidelines

Anthropic's engineering article outlines four practical guidelines for authoring and testing skills:

- **Start with evaluation**: Run agents on representative tasks, observe where they struggle, and build skills incrementally to address specific gaps.
- **Structure for scale**: Split unwieldy `SKILL.md` files into separate referenced files. Keep mutually exclusive contexts separate to reduce token usage. Make it clear whether code should be run or read as reference.
- **Think from Claude's perspective**: Monitor real usage for unexpected trajectories. Pay special attention to `name` and `description` quality — these are the routing signals that determine when the skill triggers.
- **Iterate with Claude**: Ask Claude to capture its own successful approaches and common mistakes into reusable skill content. If it goes off-track, ask it to self-reflect on what went wrong. This discovers what context Claude actually needs rather than guessing upfront.

The article also frames building a skill as "putting together an onboarding guide for a new hire" — a useful mental model for skill authors.

## Connections

- [[SKILL.md Package Anatomy]] explains the file and folder structure.
- [[Portable Skill Core]] explains the shared metadata center.
- [[Progressive Disclosure]] explains why skills are split into metadata, core instructions, and resources.
- [[Skill Authoring Workflow]] explains how recurring tasks become reusable skills.
- [[Skill Distribution and Installation]] explains how skills reach different agent runtimes.
- [[Plugin-Based Agent Extensions]] explains why plugins matter as a packaging, distribution, and integration layer around skills.
- [[MCP and Tool-Integration Architecture]] explains how skills relate to tools, resources, prompts, and MCP servers.
- [[Agent Frameworks and Orchestration]] explains when skills should be combined with subagents, handoffs, or graph workflows.
- [[concepts/Replacing Code with Skills]] — Cursor replaced ~15K lines of application code with skills, demonstrating skills as a substitute for hardcoded features.
- [[Agent SDKs and Codex Automation]] explains how skills relate to OpenAI Agents SDK, Codex SDK/App Server, and Claude Agent SDK.
- [[concepts/Claude Code Architecture Deep Dive]] provides the source-level analysis of where skills sit in Claude Code's extensibility spectrum (Hooks → Skills → Plugins → MCP) and how SkillTool vs AgentTool differ in context cost.
- [[concepts/LLM Fundamentals]] explains how LLMs work under the hood — why skills need precise wording, why context matters, and why evaluation is necessary.
- [[concepts/OpenAI Responses API]] explains OpenAI's stateful API primitive for agentic tool use and reasoning models.
- [[sources/Equipping Agents for the Real World with Agent Skills]] Anthropic's engineering article: the official narrative introducing skills, with the PDF skill walk-through and development guidelines.
- [[sources/Agent Skills Overview (agentskills.io)]] The open standard homepage: concise definition, three-stage loading (Discovery, Activation, Execution), and cross-product reuse.
- [[sources/Agent Skills (platform docs)]] Official platform docs: VM architecture, beta API requirements, runtime constraints per surface, and ZDR notice.
- [[sources/Introduction to Claude Skills (cookbook)]] Official cookbook: Excel/PPT/PDF examples, token optimization (98% savings), and versioning strategy.
- [[concepts/Skill Security and Supply Chain Risk]] Security landscape: 36% of skills have flaws, 76 confirmed malicious payloads, and the convergence of prompt injection with traditional malware.
- [[sources/Superpowers How Jesse Built the 1 AI Claude Code Codex Plugin]] Jesse Vincent on Superpowers as a skill-driven agentic development workflow built around specs, TDD, ephemeral review agents, and end-to-end validation.

## Open Questions

- Will the ecosystem converge on one cross-vendor schema beyond `name` and `description`?
- Will the boundary between installable skills and project-level behavior files stay separate, or blur further?
