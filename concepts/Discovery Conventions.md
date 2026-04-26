---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
  - "raw/2026-04-26 OpenAI Codex Agent Skills docs.md"
  - "raw/2026-04-26 Claude Code Agent Skills docs.md"
  - "raw/2026-04-26 Gemini CLI Agent Skills docs.md"
  - "raw/2026-04-26 GitHub Copilot and VS Code Agent Skills docs.md"
  - "raw/2026-04-26 OpenCode Agent Skills docs.md"
  - "raw/2026-04-26 OpenClaw Skills docs.md"
  - "raw/2026-04-26 Windsurf Cascade Skills docs.md"
  - "raw/2026-04-26 Cursor Agent Skills support sources.md"
tags: [agent-skills, discovery, skill-md]
---

# Discovery Conventions

## Summary

Discovery conventions are the ways agents or tools find skills and skill-like guidance. The earlier synthesis distinguishes between package-level uppercase `SKILL.md` and site-level lowercase `skill.md`. The newer ecosystem source adds a second axis: even when the file format is similar, local install paths differ by tool.

In plain language: `SKILL.md` is usually the file inside an installable skill package. A website's `/skill.md` is more like a public signpost. And once a skill is installed locally, different tools may look in different folders for it.

Sources include `raw/skill.md for AI Agents.md`, the VoltAgent ecosystem source, and the 2026-04-26 web-source notes for Codex, Claude Code, Gemini CLI, GitHub Copilot/VS Code, Cursor, OpenCode, OpenClaw, and Windsurf.

## Key Ideas and Evidence

The earlier source says package-level `SKILL.md` is the clearest common pattern for installed skills. It also says site-level lowercase `/skill.md` and `/.well-known/skills/default/skill.md` are emerging discovery surfaces, especially in docs-site contexts.

The curated ecosystem source adds local path variation across tools, with examples such as:

- Codex: `.agents/skills/` or `~/.agents/skills/`
- Claude Code: `.claude/skills/` or `~/.claude/skills/`
- Cursor: `.cursor/skills/` or `~/.cursor/skills/`
- Gemini CLI: `.gemini/skills/` or `~/.gemini/skills/`

This distinction prevents confusion. One question is "What file tells the agent what this skill is?" Another is "Where does this tool look for installed skills?"

The 2026-04-26 ingest expands the local discovery picture:

| Tool or client | Discovery paths or scopes named in sources |
| --- | --- |
| OpenAI Codex | Repository `.agents/skills` from CWD to repo root, `$HOME/.agents/skills`, `/etc/codex/skills`, and OpenAI-bundled system skills. |
| Claude Code | `~/.claude/skills/`, `.claude/skills/`, plugin skills, and enterprise skills. |
| GitHub Copilot and VS Code | Project `.github/skills/`, `.claude/skills/`, `.agents/skills/`; personal `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/`; configurable extra locations in VS Code. |
| Gemini CLI | Workspace `.gemini/skills/` or `.agents/skills/`; user `~/.gemini/skills/` or `~/.agents/skills/`; extension skills. |
| Cursor | Official changelog confirms Agent Skills in editor and CLI; path details still need a direct readable Cursor docs capture. Existing ecosystem source lists `.cursor/skills/` and `~/.cursor/skills/`. |
| OpenCode | `.opencode/skills/`, `~/.config/opencode/skills/`, `.claude/skills/`, `~/.claude/skills/`, `.agents/skills/`, and `~/.agents/skills/`. |
| OpenClaw | `<workspace>/skills`, `<workspace>/.agents/skills`, `~/.agents/skills`, `~/.openclaw/skills`, bundled skills, and configured extra dirs. |
| Windsurf Cascade | `.windsurf/skills/`, `~/.codeium/windsurf/skills/`, enterprise system paths, `.agents/skills/`, `~/.agents/skills/`, and conditional Claude-compatible paths. |

## Where Sources Agree

The sources agree that agents need discoverable instructions. They also agree that metadata and file location matter because they shape how tools find and load guidance.

There is also agreement that the convention is becoming concrete enough to design around, even if not every detail is universal.

## Where Sources Disagree

The sources disagree on casing, path, and scope. Uppercase `SKILL.md` is associated with package-level skill files. Lowercase `/skill.md` is associated with web discovery. Local install directories vary by platform and are clearly not standardized across the current ecosystem.

The likely reason is that local agent packages and public documentation sites solve different discovery problems. One is about installed capabilities. The other is about letting an agent discover instructions from a website.

## Connections

- [[Agent Skills]] explains the difference between package skills and general agent-readable guidance.
- [[SKILL.md Package Anatomy]] explains the installable package file.
- [[Portable Skill Core]] explains the metadata an agent may use after discovery.
- [[Skill Distribution and Installation]] explains how discovery paths connect to installation methods.
- [[Skill Repository Tooling]] explains search and documentation layers.

## Open Questions

- Will lowercase `/skill.md` become common outside documentation platforms?
- Will agents converge on a smaller set of local skill directories, or keep tool-specific paths?
- Will `.agents/skills/` become a de facto shared compatibility path across most coding agents?
