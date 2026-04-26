---
type: raw-source-note
created: 2026-04-26
updated: 2026-04-26
status: active
tags: [openai, codex, sdk, app-server, agent-skills]
---

# OpenAI Codex SDK and App Server Source

## Source URLs

- https://developers.openai.com/codex/sdk
- https://developers.openai.com/codex/app-server
- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/subagents

## Key Source Claims

- The Codex SDK lets developers programmatically control local Codex agents. OpenAI recommends it when a developer needs to control Codex in CI/CD, create an agent that engages with Codex, build Codex into internal tools/workflows, or integrate Codex inside an application.
- The Codex SDK includes a TypeScript library, installable as `@openai/codex-sdk`, for controlling Codex from server-side applications. OpenAI says it requires Node.js 18 or later.
- The Codex Python SDK is described as experimental. It controls the local Codex app-server over JSON-RPC and requires Python 3.10 or later plus a local checkout of the open-source Codex repo.
- The Codex App Server is the protocol Codex uses to power rich clients such as the Codex VS Code extension. OpenAI says to use it for deep product integrations involving authentication, conversation history, approvals, and streamed agent events.
- Codex App Server uses bidirectional JSON-RPC 2.0-style messages. Supported transports include stdio, experimental/unsupported WebSocket, and off. The docs warn that non-loopback WebSocket listeners may allow unauthenticated connections by default during rollout and should be configured with WebSocket auth before remote exposure.
- App Server can generate TypeScript schemas or JSON Schema bundles from the CLI, and generated artifacts match the Codex version used to generate them.
- Codex Skills are the authoring format for reusable workflows, while plugins are the installable distribution unit for reusable skills and apps in Codex.
- Codex subagents let Codex spawn specialized agents in parallel and consolidate their results. Subagents inherit sandbox and approval policy from the parent workflow.

## Relevance to Agent Skills

The Codex SDK and App Server are automation and embedding surfaces around Codex. They matter for Agent Skills because they make skills operational inside custom products and workflows:

- a skill can define a reusable coding workflow;
- a plugin can distribute that workflow;
- Codex SDK can invoke Codex programmatically from internal tools or CI;
- Codex App Server can expose deeper client-like integration with history, approvals, and streaming;
- subagents can parallelize skill-guided exploration or implementation while preserving sandbox and approval boundaries.

## Follow-Ups

- Treat Codex App Server as a deep client protocol, not as a general MCP replacement.
- Track the maturity difference between the TypeScript Codex SDK and the experimental Python SDK.
- Compare Codex plugin distribution with Claude plugins and Agent Skills-compatible plugin marketplaces.
