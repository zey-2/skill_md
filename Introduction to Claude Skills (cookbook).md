---
type: source-summary
created: 2026-05-10
updated: 2026-05-10
status: active
sources:
  - "raw/Introduction to Claude Skills.md"
tags: [agent-skills, claude-cookbook, token-optimization]
---

# Introduction to Claude Skills (cookbook)

**Source**: [platform.claude.com/cookbook/skills-notebooks-01-skills-introduction](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
**Created**: 2026-05-10

## Summary

Anthropic's official Jupyter notebook cookbook demonstrating Claude Skills with Excel, PowerPoint, and PDF examples. Covers API setup, progressive disclosure, token usage optimization, versioning strategy, and troubleshooting.

## Key Points

- **Token optimization**: Skills reduce initial context cost by ~98%. Manual instructions cost 5,000-10,000 tokens/request vs minimal metadata overhead with skills. Full skill instructions only load when invoked (~5,000 tokens).
- **Versioning strategy**: Use "latest" for Anthropic skills (recommended). Pin specific versions for production stability. Custom skills use epoch timestamps for versions.
- **Generation times**: Excel ~2 min (with charts/formatting), PowerPoint ~1-2 min (simple 2-slide), PDF ~40-60 seconds (simple documents).
- **API requirements**: Must use `client.beta.messages.create()` (not `client.messages.create()`). Must include `code_execution` tool. Requires 3 beta headers in `betas` parameter.
- **Skills vs MCPs**: "Skills are higher-level than individual tools — they combine instructions, code, and resources." Skills are composable and use progressive disclosure for efficiency.
- **Token reuse tip**: Reuse containers via `container.id` from previous responses to avoid reloading skills.
- **Anthropic-managed skills**: `xlsx`, `pptx`, `pdf`, `docx` — pre-built, maintained by Anthropic.

## Connections

- [[concepts/Agent Skills]] — Practical cookbook examples of the core concept.
- [[concepts/Progressive Disclosure]] — Token optimization numbers (98% savings on initial context).
- [[concepts/Skill Authoring Workflow]] — Versioning strategy and token optimization tips for authors.
