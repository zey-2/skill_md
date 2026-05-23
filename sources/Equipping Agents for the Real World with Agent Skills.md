---
type: source-summary
created: 2026-05-10
updated: 2026-05-23
status: active
sources:
  - "raw/Equipping agents for the real world with Agent Skills.md"
tags: [agent-skills, anthropic, progressive-disclosure]
---

# Equipping Agents for the Real World with Agent Skills

**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
**Created**: 2026-05-10

## Summary

Anthropic's official engineering article introducing Agent Skills as composable, domain-specific capabilities for general-purpose agents. Uses the PDF skill as a walk-through example and explains progressive disclosure, code execution integration, skill development guidelines, and the future roadmap.

## Key Points

- Agent Skills are "organized folders of instructions, scripts, and resources" that agents discover and load dynamically, transforming general-purpose agents into specialized agents.
- The three-level progressive disclosure model: (1) SKILL.md frontmatter metadata pre-loaded at startup, (2) full SKILL.md body loaded when relevant, (3) bundled reference files loaded on demand.
- Skills can include executable scripts (e.g., Python) that Claude runs without loading the script or target file into context — deterministic operations are better suited to code than token generation.
- **Skill development guidelines**: start with evaluation to find gaps, split unwieldy SKILL.md files, think from Claude's perspective (especially name/description quality for triggering), iterate with Claude by asking it to capture successful approaches into skills.
- **Security**: skills can introduce vulnerabilities or direct data exfiltration. Install from trusted sources; audit file contents, code dependencies, bundled resources, and external network connections before use.
- **Current support**: Claude.ai, Claude Code, Claude Agent SDK, Claude Developer Platform.
- **Future**: agent self-creation/editing/evaluation of skills, and skills complementing MCP servers for complex external-tool workflows.

## Useful Quotes

- "Building a skill for an agent is like putting together an onboarding guide for a new hire."
- "Agents with a filesystem and code execution tools don't need to read the entirety of a skill into their context window when working on a particular task. This means that the amount of context that can be bundled into a skill is effectively unbounded."
- "Code can serve as both executable tools and as documentation. It should be clear whether Claude should run scripts directly or read them into context as reference."

## Evidence

The source-summary claims above are grounded in the local raw source file listed in frontmatter.

## Connections

- [[concepts/Agent Skills]] — Core concept page; this source is a primary Anthropic statement of the concept.
- [[concepts/Progressive Disclosure]] — This source provides the canonical three-level model with visual context window diagrams.
- [[concepts/Skill Authoring Workflow]] — Development guidelines section directly informs the authoring workflow.
- [[concepts/MCP and Tool-Integration Architecture]] — Future roadmap mentions skills complementing MCP servers.
- [[concepts/Plugin-Based Agent Extensions]] — Skills as the building block that plugins can bundle and distribute.
