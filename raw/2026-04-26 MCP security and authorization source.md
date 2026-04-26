---
type: raw-source-note
created: 2026-04-26
updated: 2026-04-26
status: active
tags: [mcp, security, authorization, tools]
---

# MCP Security and Authorization Source

## Source URLs

- https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices
- https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
- https://modelcontextprotocol.io/docs/tutorials/security/authorization
- https://modelcontextprotocol.io/docs/develop/clients/client-best-practices

## Key Source Claims

- MCP authorization is optional, but recommended when a server exposes user-specific data, administrative actions, enterprise controls, audit requirements, rate limits, or consent-sensitive APIs.
- HTTP-based MCP authorization is based on OAuth 2.1 patterns. Stdio-based local MCP servers should usually obtain credentials from the environment or embedded libraries rather than following the HTTP authorization flow.
- Important security requirements include HTTPS for authorization endpoints, redirect URI validation, PKCE, secure token storage, token expiration/rotation, token audience binding, and server-side token validation.
- MCP security best practices emphasize the confused deputy problem, per-client consent, exact redirect URI matching, CSRF protection, secure consent cookies/sessions, and least-privilege scopes.
- MCP clients that support one-click local server configuration should show the exact command that will be executed, require explicit consent, warn about dangerous command patterns, and prefer sandboxed execution with minimal privileges.
- MCP tools are model-controlled. The official server concepts page says implementations should preserve user control with visible tool exposure, approval dialogs, pre-approval settings, and activity logs.
- Programmatic tool calling adds a code execution surface. Client best practices recommend sandboxing model-generated code, routing external communication through a host broker, keeping credentials out of generated code, enforcing per-call authorization, and setting resource limits.

## Relevance to Agent Skills

Agent Skills can increase tool power, so they should also encode safe tool-use policy. A skill that teaches an agent to build or use MCP servers should include:

- how to choose least-privilege tools and scopes;
- when a tool should require approval;
- what secrets must never enter `SKILL.md`, logs, model-visible output, or generated code;
- when local stdio servers are acceptable versus when remote HTTP plus OAuth is needed;
- how to test that tool descriptions, schemas, and error handling do not invite unsafe calls.

## Follow-Ups

- Create an `Agent Security and Tool Permissions` page that connects MCP security, skill governance, sandboxing, and supply-chain trust.
