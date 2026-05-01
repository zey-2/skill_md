---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/2026-04-26 MCP architecture and Agent Skills integration source.md"
  - "raw/2026-04-26 MCP security and authorization source.md"
  - "raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md"
  - "raw/2026-04-26 OpenAI Codex SDK and App Server source.md"
  - "raw/2026-04-26 Claude Agent SDK source.md"
  - "raw/2026-04-26 OpenAI Codex Plugins docs.md"
  - "raw/2026-04-26 Claude Code Plugins docs.md"
tags: [mcp, tools, agent-skills, architecture]
---

# MCP and Tool-Integration Architecture

## Summary

MCP and tool-integration architecture is the layer that lets an agent act on external systems and read external context. Around Agent Skills, the clean mental split is:

- a skill tells the agent what procedure to follow and when;
- a tool lets the agent perform an action;
- a resource gives the agent context;
- an MCP server exposes tools, resources, and prompts through a standard protocol;
- a plugin can package skills together with app integrations, MCP server configuration, metadata, and install policy;
- an agent framework decides how agents, tools, skills, state, and humans are coordinated at runtime.

Sources: `raw/2026-04-26 MCP architecture and Agent Skills integration source.md`, `raw/2026-04-26 MCP security and authorization source.md`, and `raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md`.

## Key Ideas and Evidence

MCP uses a host-client-server model. The host is the AI application, the client maintains a connection to a server, and the server exposes capabilities or context. The protocol has a JSON-RPC data layer and a transport layer. Current documentation emphasizes stdio for local process communication and Streamable HTTP for remote servers.

The core MCP server primitives are:

| Primitive | Main control pattern | Use around skills |
| --- | --- | --- |
| Tools | Model-controlled | Actions the agent can call, such as API calls, file edits, ticket creation, database queries, or computations. |
| Resources | Application-controlled | Context the host can fetch, filter, search, or pass to the model, such as files, records, schemas, and knowledge-base entries. |
| Prompts | User-controlled | Parameterized templates for recurring interactions or workflows. |

Tool discovery and invocation are explicit. Servers list tools with names, descriptions, and JSON Schema inputs; clients then call a tool by name with validated arguments. This resembles Agent Skills routing: both depend heavily on precise names and descriptions, but tools are executable interfaces while skills are procedural guidance.

The official MCP docs now directly connect Agent Skills to MCP development. The MCP development skill set uses composing skills such as `build-mcp-server`, `build-mcp-app`, and `build-mcpb` to guide design choices around deployment model, tool patterns, authorization, widgets, and packaging. This is strong evidence that skills can be used not only to call tools, but to help design good tool surfaces.

## Design Rules for Skill-Centered Tooling

Use a skill when the hard part is judgment, procedure, domain context, or recurring workflow.

Use a function tool or script when the hard part is deterministic execution inside the current runtime.

Use an MCP server when the agent needs reusable access to an external system, a large action surface, a remote service, shared organization tools, or cross-client portability.

Use a plugin when the tool surface and the operating procedure should be distributed together. For example, a plugin may ship the skill that explains the workflow, the MCP server configuration that exposes actions, and the install-surface metadata that tells users what capability they are enabling.

Use resources when the agent needs context but should not freely execute actions.

Use prompts when the user should explicitly start a structured workflow.

Use approval policies, tool filtering, strict schemas, clear error formatting, and tracing when a tool can cause side effects or expose sensitive data.

Do not collapse every agent protocol into MCP. Codex App Server also uses JSON-RPC-style bidirectional messages, but it is a Codex client integration protocol for authentication, conversation history, approvals, and streamed events. MCP is the more general tool/context protocol for external capabilities.

## Security and Control

MCP tools are model-controlled, so tool integration must preserve user and application control. Current MCP guidance emphasizes visible tool exposure, approval dialogs, permission settings, activity logs, least-privilege scopes, exact redirect URI validation, PKCE, short-lived tokens, secure token storage, and careful treatment of one-click local server configuration.

For Agent Skills, that means tool-using skills should say not only "call this tool" but also:

- which actions are safe to pre-approve;
- which actions need human approval;
- what credentials, tokens, files, and logs must stay out of model-visible context;
- whether local stdio, local sandboxing, remote Streamable HTTP, or hosted MCP is the right deployment shape;
- how to handle tool failures without leaking sensitive details.

## Connections

- [[Agent Skills]] explains why procedural guidance belongs in skills.
- [[Portable Skill Core]] explains why routing descriptions matter.
- [[Progressive Disclosure]] explains why skills and tool surfaces should load only what is needed.
- [[Plugin-Based Agent Extensions]] explains how plugins bundle skills with app integrations and MCP configuration.
- [[Validation and Evaluation]] explains how to test tool-call behavior and outcomes.
- [[Agent Frameworks and Orchestration]] explains the runtime layer that coordinates tools, agents, and skills.
- [[Agent SDKs and Codex Automation]] explains how SDKs and app protocols embed skill-guided agents into products and workflows.
- [[concepts/Claude Code Architecture Deep Dive]] shows at source level how MCP fits into Claude Code's 5-step tool pool assembly, the execute() injection point, and the pre-trust execution window where MCP servers run before the trust dialog.

## Open Questions

- When should a tool bundle be published as an MCP server versus kept as local function tools or scripts inside one skill?
- Should Agent Skills define a standard way to declare required MCP servers, tool permissions, and approval policies?
- How should skill evals measure whether an agent chose the right tool, used the right arguments, and respected approval boundaries?
