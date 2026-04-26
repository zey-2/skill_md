---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
tags: [agent-skills, authoring, workflow]
---

# Skill Authoring Workflow

## Summary

A skill authoring workflow is the repeatable process for turning a recurring task into an agent skill. The earlier synthesis recommends starting from concrete use cases, drafting a concise core, moving bulky detail into references, adding scripts where determinism matters, validating the package, reviewing it, releasing it, and improving it from real usage.

The newer raw sources make the target clearer. In practice, many successful skills encode working habits such as planning, TDD, issue triage, interface design, debugging, code review, or safety guardrails. A good authoring workflow therefore starts by asking not only "What information does the agent need?" but also "What operating procedure keeps repeating?"

Sources: `raw/skill.md for AI Agents.md`, `raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md`, `raw/obrasuperpowers An agentic skills framework & software development methodology that works.md`, and `raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md`.

## Key Ideas and Evidence

The earlier synthesis says strong public guidance converges on the same operational pattern:

1. Collect concrete agent use cases.
2. Draft the `SKILL.md` core.
3. Split bulky detail into references.
4. Add deterministic scripts where needed.
5. Generate repository indexes and vendor adapters.
6. Run validation and evals.
7. Peer review.
8. Release with version and source SHA.
9. Monitor trigger quality and task success.
10. Refresh from upstream docs and changelogs.

The new repository examples show what those use cases look like in the wild. One personal catalog packages skills for PRD writing, issue slicing, TDD, architecture review, and git guardrails. A larger framework packages brainstorming, plan writing, execution, code review, and subagent coordination as named skills. A single-file behavior guide shows that some teams also codify principles such as "think before coding," "simplicity first," and "surgical changes."

A reasonable inference is that strong skill authors often begin with recurring failure modes. If agents keep overcomplicating, skipping tests, or making unsafe edits, those patterns are good candidates for skills or adjacent behavior guides.

## Where Sources Agree

The sources agree that examples matter. The earlier synthesis says OpenAI recommends understanding skills through concrete examples before designing reusable resources. The newer repositories show exactly that pattern by publishing concrete workflow skills instead of only abstract templates.

They also agree that skills should improve through validation and iteration rather than being treated as one-time documents.

## Where Sources Disagree

The sources disagree mainly in packaging and granularity. Some publish many small skills for narrow jobs. Others publish one broader methodology that coordinates multiple stages of work. The `CLAUDE.md` source is adjacent again: it is clearly reusable guidance, but it is merged into project instructions instead of being packaged as a portable skill directory.

These differences reflect different maintenance contexts. A solo author may favor simple project overlays. A skill marketplace may favor installable units. A framework author may favor an integrated workflow system.

## Connections

- [[Progressive Disclosure]] explains why authoring should split content into layers.
- [[Validation and Evaluation]] explains the testing stage.
- [[Provenance and Versioning]] explains release and source tracking.
- [[Vendor Adapters]] explains generated platform-specific outputs.
- [[Agent Skills]] explains why workflow skills still count as skills.
- [[MCP and Tool-Integration Architecture]] helps decide when a workflow needs tools, scripts, resources, or an MCP server.
- [[Agent Frameworks and Orchestration]] helps decide when a repeated behavior should become a skill versus framework-level control flow.

## Open Questions

- How much peer review is enough for an internal skill?
- When should a repeated behavior live in a portable skill package versus a project-level instruction file?
