---
type: concept
created: 2026-04-26
updated: 2026-05-11
status: active
sources:
  - "raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md"
  - "raw/2026-04-26 Agent orchestration frameworks source.md"
  - "raw/2026-04-26 MCP architecture and Agent Skills integration source.md"
  - "raw/2026-04-26 OpenAI Agents SDK official source.md"
  - "raw/2026-04-26 OpenAI Codex SDK and App Server source.md"
  - "raw/2026-04-26 Claude Agent SDK source.md"
  - "raw/Agent Development Kit (ADK).md"
tags: [agent-frameworks, orchestration, agent-skills]
---

# Agent Frameworks and Orchestration

## Summary

Agent frameworks and orchestration systems decide how agents, tools, state, memory, humans, and workflows run together. Around Agent Skills, the important boundary is: skills package reusable operating knowledge, while frameworks run the system that applies that knowledge.

Skills can guide a single agent, specialize a subagent, or teach an agent to build a framework workflow. Frameworks can provide the runtime pieces that skills do not own: state, events, tool execution, human approval, graph flow, deployment, tracing, and recovery.

Sources: `raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md`, `raw/2026-04-26 Agent orchestration frameworks source.md`, and `raw/2026-04-26 MCP architecture and Agent Skills integration source.md`.

## Key Patterns

| Pattern | What controls the flow? | Best fit | Skill relationship |
| --- | --- | --- | --- |
| Single agent with skills | One agent plus skill routing | Recurring tasks where instructions and references are enough | Skills are the main abstraction. |
| Function tools or scripts | Agent chooses; code executes | Deterministic operations inside the local app/runtime | Skills can explain when to run the tool or script. |
| MCP server tools | Agent chooses; MCP host/client/server executes | Shared external systems, remote APIs, cross-client tools, or large tool surfaces | Skills can guide use or construction of the MCP server. |
| Manager / agents as tools | A manager agent keeps user-facing control | Specialist agents help with bounded subtasks | A skill can define the manager's operating procedure or each specialist's domain method. |
| Handoffs | A triage or peer agent delegates control | A specialist should own the next conversational turn | A skill can define routing criteria, handoff summaries, or specialist constraints. |
| Graph or workflow orchestration | Code/workflow graph controls order | Defined processes, approvals, long-running jobs, auditability | Skills provide reusable procedure inside nodes, agents, or development guidance. |

## Framework Landscape

The OpenAI Agents SDK frames agents as LLMs with instructions, tools, handoffs, guardrails, structured outputs, hooks, sessions, and MCP servers. Its docs highlight two common multi-agent patterns: manager agents that call specialists as tools, and handoffs where a specialist takes over.

LangGraph emphasizes low-level orchestration for long-running, stateful agents, including durable execution, streaming, human-in-the-loop control, memory, debugging, and deployment.

Microsoft Agent Framework distinguishes agents from workflows. Agents fit open-ended conversational work and autonomous tool use; workflows fit defined steps, explicit execution order, multi-agent coordination, and business processes. It also has a direct Agent Skills provider, which makes skills part of a framework runtime rather than only a coding-client feature.

CrewAI emphasizes crews, flows, tasks/processes, tools, memory, knowledge, guardrails, callbacks, human-in-the-loop triggers, observability, and deployment. In this wiki, it is currently useful as evidence of the broader orchestration category, but needs a deeper source pass before making detailed claims.

OpenAI's Codex SDK and Codex App Server are narrower than general orchestration frameworks. They are automation and embedding surfaces for Codex specifically: the SDK controls local Codex agents programmatically, while App Server exposes the protocol used by rich Codex clients for conversation history, approvals, and streamed agent events.

Claude Agent SDK sits between a coding client and a general agent framework. It exposes Claude Code's harness, sessions, tool permissions, MCP integration, and filesystem configuration, including skills in `.claude/skills/*/SKILL.md`.

## Skill-Centered Design Guidance

Start with the least powerful layer that can reliably express the behavior:

1. Use a skill when repeatable judgment or procedure is the main missing piece.
2. Add scripts or function tools when the agent needs deterministic execution.
3. Add MCP when tools or resources should be reusable across agents, clients, or teams.
4. Add a specialist agent when one role needs a focused prompt, tool set, or output contract.
5. Add handoffs when user-facing control should move to the specialist.
6. Add graph/workflow orchestration when order, state, approvals, retries, auditing, or recovery must be explicit.

The practical test is ownership. If the behavior should be reviewed as knowledge, put it in a skill. If it should be tested like software, put it in code. If it must access an external system, expose it through a tool or MCP server. If it must coordinate multiple agents or steps reliably, put the control flow in a framework.

## Contradictions or Tensions

Frameworks make agent systems more controllable, but they can also hide whether a behavior is coming from a skill, a prompt, a tool schema, a workflow edge, middleware, or a subagent. For maintainability, skill repositories should document which runtime layer owns each repeated behavior.

There is also a portability tension. Agent Skills aim to travel across clients, while framework workflows are often code-specific. A skill can teach an agent how to build a LangGraph or Microsoft Agent Framework workflow, but the workflow itself is not portable in the same way as a `SKILL.md` package.

## Connections

- [[Agent Skills]] explains the reusable instruction-package layer.
- [[MCP and Tool-Integration Architecture]] explains the external action and context layer.
- [[Skill Authoring Workflow]] explains how repeated behavior becomes a skill.
- [[Validation and Evaluation]] explains why orchestration should be evaluated through traces, tool calls, outcomes, and repeated trials.
- [[Skill Governance and Metrics]] explains why ownership and runtime risk matter.
- [[Agent SDKs and Codex Automation]] compares OpenAI Agents SDK, Codex SDK, Codex App Server, and Claude Agent SDK as skill-adjacent runtime surfaces.
- [[concepts/Claude Code Architecture Deep Dive]] provides a concrete harness implementation reference — the 9-step queryLoop, subagent isolation, and extensibility injection points that frameworks abstract away.
- [[concepts/OpenAI Responses API]] explains how OpenAI's API itself now provides a built-in agentic loop, overlapping with what orchestration frameworks offer.
- [[concepts/Replacing Code with Skills]] — The best-of command uses subagents with worktree isolation and parent-level coordination as a lightweight orchestration pattern without a framework.
- [[concepts/Symphony Orchestration]] is a concrete issue-tracker-based orchestration pattern that extends beyond framework-level control to continuous always-on agent dispatch.
- [[concepts/Google Agent Development Kit (ADK)]] — Google's multi-language framework (Python, TypeScript, Go, Java) for production multi-agent systems with progressive complexity and structured context management.

## Open Questions

- Should the wiki maintain framework-specific pages for LangGraph, OpenAI Agents SDK, Microsoft Agent Framework, and CrewAI?
- What is the best portable way for a skill to declare expected tools, MCP servers, or subagents?
- When a framework has its own prompt, middleware, memory, and workflow graph, what should remain in `SKILL.md`?
