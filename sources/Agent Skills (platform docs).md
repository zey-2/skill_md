---
type: source-summary
created: 2026-05-10
updated: 2026-05-23
status: active
sources:
  - "raw/Agent Skills.md"
tags: [agent-skills, claude-platform, progressive-disclosure]
---

# Agent Skills (platform.claude.com docs)

**Source**: [platform.claude.com/docs/en/agents-and-tools/agent-skills/overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
**Created**: 2026-05-10

## Summary

Official Claude Agent Skills documentation covering the VM-based architecture, progressive disclosure model, product surface availability (API, Claude Code, claude.ai), skill structure with field requirements, security considerations, and runtime environment constraints.

## Key Points

- **ZDR notice**: Agent Skills is **not** eligible for Zero Data Retention. Skill definitions and execution data are retained per Anthropic's standard policy.
- **VM architecture**: Skills leverage Claude's VM environment with filesystem access. Skills exist as directories; Claude interacts with them via bash commands. Script code never enters context — only output does.
- **Three-level progressive disclosure** with concrete token budgets:
  - Level 1 (Metadata): ~100 tokens per skill, always loaded at startup
  - Level 2 (Instructions): under 5k tokens, loaded when triggered
  - Level 3+ (Resources): effectively unlimited, executed via bash without loading into context
- **Product surface availability**:
  - **Claude API**: Both pre-built and custom skills. Requires 3 beta headers: `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14`. Custom skills shared org-wide.
  - **Claude Code**: Custom skills only. Filesystem-based, no API upload needed.
  - **Claude.ai**: Both pre-built and custom skills. Custom skills via zip upload in Settings. Individual user only — not shared org-wide, no admin management.
- **Field requirements**: `name` max 64 chars (lowercase, numbers, hyphens, no "anthropic"/"claude" reserved words); `description` max 1024 chars, must be non-empty, no XML tags.
- **Runtime constraints per surface**:
  - Claude.ai: varying network access (user/admin configurable)
  - Claude API: no network access, no runtime package installation, pre-configured dependencies only
  - Claude Code: full network access, but skills should only install packages locally
- **Cross-surface sync**: Custom skills do NOT sync across surfaces. Each surface requires separate management and uploads.
- **Security**: "Treat like installing software." Audit all files. External URL fetching is the highest-risk pattern.

## Evidence

The source-summary claims above are grounded in the local raw source file listed in frontmatter.

## Connections

- [[concepts/Agent Skills]] — Official platform docs for the core concept.
- [[concepts/Progressive Disclosure]] — Concrete token budgets per level (~100 / <5k / unlimited).
- [[concepts/Skill Distribution and Installation]] — Product surface availability and sharing scope details.
- [[concepts/Plugin-Based Agent Extensions]] — Claude Code plugins as an additional sharing mechanism.
