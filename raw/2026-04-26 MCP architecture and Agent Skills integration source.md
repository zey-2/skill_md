---
type: raw-source-note
created: 2026-04-26
updated: 2026-04-26
status: active
tags: [mcp, agent-skills, tools]
---

# MCP Architecture and Agent Skills Integration Source

## Source URLs

- https://modelcontextprotocol.io/docs/learn/architecture
- https://modelcontextprotocol.io/docs/learn/server-concepts
- https://modelcontextprotocol.io/docs/develop/build-with-agent-skills
- https://modelcontextprotocol.io/docs/sdk

## Key Source Claims

- MCP defines a client-server architecture where an MCP host creates one MCP client per MCP server. The server provides context or capabilities to the host.
- The protocol has a data layer and a transport layer. The data layer is JSON-RPC based and includes lifecycle management, capability negotiation, tools, resources, prompts, notifications, sampling, elicitation, and logging.
- MCP servers expose three main building blocks:
  - Tools: model-controlled executable functions for actions such as API calls, file operations, database queries, and computations.
  - Resources: application-controlled data sources that provide context, such as files, API results, database schemas, or knowledge-base records.
  - Prompts: user-controlled templates that structure recurring interactions or workflows.
- Tool discovery and execution use `tools/list` and `tools/call`. Tool definitions include names, descriptions, and JSON Schema input definitions.
- Resources support direct URIs and resource templates; applications decide how to retrieve, filter, search, or pass resource content to the model.
- MCP supports both local and remote transport patterns, especially stdio for local process communication and Streamable HTTP for remote servers. The official SDK page says SDKs support creating servers, building clients, local and remote transports, and type-safe protocol compliance.
- The MCP "Build with Agent Skills" page directly connects Agent Skills to MCP development. It says MCP development skills encode decisions such as deployment model, tool patterns, authorization, and UI/widget needs so coding assistants can interrogate a use case and scaffold an appropriate server.
- The reference MCP development skills compose multiple skills: `build-mcp-server`, `build-mcp-app`, and `build-mcpb`. Each ships a `SKILL.md` plus references such as auth flows, tool-design patterns, widget templates, and manifest schemas.

## Relevance to Agent Skills

MCP and Agent Skills are complementary:

- An MCP server exposes live capabilities and context.
- A skill tells an agent when and how to use or build those capabilities.
- A skill can encode the design checklist for MCP server authoring: what system is being wrapped, who uses it, how large the action surface is, whether user interaction is needed, and which auth/deployment model fits.

## Follow-Ups

- Compare MCP prompts with Agent Skills: both are reusable instructions, but prompts are usually user-invoked templates while skills are agent-routed operating procedures.
- Add a separate security page for MCP authorization, approval, sandboxing, and third-party server risk.
