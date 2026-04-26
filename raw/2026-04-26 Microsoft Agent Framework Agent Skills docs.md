---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://learn.microsoft.com/en-us/agent-framework/agents/skills"
  - "https://techcommunity.microsoft.com/blog/azuredevcommunityblog/giving-your-ai-agents-reliable-skills-with-the-agent-skills-sdk/4497074"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, microsoft, agent-framework, sdk]
---

# Microsoft Agent Framework Agent Skills docs

## Source Identity

Microsoft Learn documents Agent Skills for Microsoft Agent Framework. A Microsoft Community Hub post describes an Agent Skills SDK and ecosystem support.

## Relevant Extracted Facts

- Microsoft Learn defines Agent Skills as portable packages of instructions, scripts, and resources.
- Microsoft Learn says skills follow an open specification and use progressive disclosure.
- The documented skill structure is a directory containing `SKILL.md` with optional subdirectories for resources.
- Microsoft's progressive disclosure pattern has three stages: advertise, load, and read resources.
- Agent Framework includes a skills provider that discovers skills from filesystem directories and makes them available as a context provider.
- The provider searches configured paths recursively up to two levels deep for `SKILL.md` files.
- It validates skill format and resources.
- It exposes tools including `load_skill`, `read_skill_resource`, and, when scripts exist, `run_skill_script`.
- Multiple skill directories can be configured by passing a list of paths.
- Microsoft Community Hub says the format is supported by a growing list of products including Claude Code, VS Code, GitHub, OpenAI Codex, Cursor, and Gemini CLI.
- The Community Hub post describes SDK packages for core registry/validation, filesystem and HTTP providers, LangChain integration, Microsoft Agent Framework integration, and an MCP server.

## Tool Support Evidence

This is primary evidence that Microsoft Agent Framework can consume Agent Skills through a provider/tool pattern. The Community Hub post adds ecosystem context and SDK implementation details.

## Open Questions

- Microsoft Agent Framework is a framework for building agents rather than a standalone coding agent client, so it should be categorized separately from tools like Codex, Claude Code, and Gemini CLI.
