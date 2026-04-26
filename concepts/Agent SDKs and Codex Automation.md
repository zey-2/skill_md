---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/2026-04-26 OpenAI Agents SDK official source.md"
  - "raw/2026-04-26 OpenAI Codex SDK and App Server source.md"
  - "raw/2026-04-26 Claude Agent SDK source.md"
tags: [agent-skills, agent-sdks, codex, claude, openai]
---

# Agent SDKs and Codex Automation

## Summary

Agent SDKs and automation protocols let developers embed agent behavior into products, CI/CD, internal tools, and custom workflows. Around Agent Skills, they are the runtime and integration layer: skills describe reusable operating knowledge, while SDKs and app servers execute, stream, approve, resume, and observe agent work.

The current important surfaces in this wiki are:

- OpenAI Agents SDK for code-first agent applications.
- OpenAI Codex SDK for programmatically controlling local Codex agents.
- OpenAI Codex App Server for rich Codex client integrations.
- Claude Agent SDK for custom Claude Code-powered agents.

Sources: `raw/2026-04-26 OpenAI Agents SDK official source.md`, `raw/2026-04-26 OpenAI Codex SDK and App Server source.md`, and `raw/2026-04-26 Claude Agent SDK source.md`.

## Comparison

| Surface | Primary role | How it relates to Agent Skills |
| --- | --- | --- |
| OpenAI Agents SDK | Build application-owned agents with orchestration, tools, handoffs, approvals, state, and traces. | Skills are reusable knowledge/procedure that can guide agents, but the SDK is the runtime that owns execution and control flow. |
| OpenAI Codex SDK | Programmatically control local Codex agents from CI/CD, internal tools, workflows, and applications. | Lets a skill-guided Codex workflow be invoked from another system instead of only from CLI, IDE, app, or web UI. |
| Codex App Server | Deep protocol for embedding Codex-style client behavior: auth, conversation history, approvals, streamed events. | Makes skills and subagents usable inside custom rich clients, but should be treated as a Codex client protocol rather than a generic tool protocol. |
| Claude Agent SDK | Build custom agents with Claude Code's harness, tools, sessions, permissions, MCP, and filesystem configuration. | Directly supports filesystem skills such as `.claude/skills/*/SKILL.md` alongside commands, memory, plugins, MCP servers, and SDK session logic. |

## Design Boundaries

Use an Agent Skill when the reusable asset is an operating procedure, domain guide, workflow checklist, reference bundle, or deterministic helper script.

Use an agent SDK when you need to embed the agent in an application, control sessions, stream events, handle approvals, constrain tools, or integrate with product logic.

Use Codex SDK when the thing being automated is specifically local Codex agent work.

Use Codex App Server when building a rich Codex client or product integration that needs Codex-like conversation history, approvals, and streamed agent events.

Use MCP when the agent needs a reusable external tool or data source that should not be locked to one SDK or client.

## Skill-Centered Implications

SDKs make skill packaging more valuable because they create repeatable entry points. A team can define the workflow in a skill, distribute it through the relevant client or plugin mechanism, then invoke the agent through an SDK or app protocol.

They also increase governance needs. Once skills can be invoked from CI, production tools, or internal applications, skill descriptions, tool permissions, approval boundaries, and source provenance become operational controls rather than documentation niceties.

The most important maintenance question is: where does each part of behavior live?

| Behavior | Best home |
| --- | --- |
| Reusable human/agent procedure | `SKILL.md` |
| Installable reusable package | Plugin or skill catalog |
| External action/data integration | MCP server or function tool |
| App-specific session and approval loop | Agent SDK or app server |
| Parallel specialist work | Subagents, agents-as-tools, or handoffs |
| Fixed control flow | Workflow/graph code |

## Connections

- [[Agent Skills]] explains the reusable instruction-package layer.
- [[MCP and Tool-Integration Architecture]] explains tools, resources, prompts, MCP, and approval boundaries.
- [[Agent Frameworks and Orchestration]] explains subagents, handoffs, workflows, state, and runtime ownership.
- [[Tools Supporting Agent Skills]] compares client-level Agent Skills support.
- [[Skill Governance and Metrics]] explains why SDK-triggered skills need review, provenance, and metrics.

## Open Questions

- Will OpenAI Agents SDK expose a first-class portable Agent Skills loading path, or stay primarily a runtime/tool orchestration SDK?
- Will Codex SDK and Codex App Server become stable enough to treat as long-term automation infrastructure, especially outside TypeScript?
- How should a skill declare expected SDK/runtime dependencies without becoming non-portable?
