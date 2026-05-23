---
type: concept
created: 2026-04-26
updated: 2026-05-23
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/openaiskills Skills Catalog for Codex.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
  - "raw/The tokenmaxxing math nobody wants to admit.md"
tags: [agent-skills, governance, metrics]
---

# Skill Governance and Metrics

## Summary

Skill governance is the set of practices that keep agent skills trustworthy over time. It covers ownership, review, validation, licensing, provenance, release control, and now, increasingly, trust in third-party skills. Metrics show whether the repository is healthy and whether the skills actually help agents.

Sources: `raw/skill.md for AI Agents.md`, `raw/openaiskills Skills Catalog for Codex.md`, `raw/obrasuperpowers An agentic skills framework & software development methodology that works.md`, and `raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md`.

## Key Ideas and Evidence

The earlier synthesis says governance matters because skills can directly change agent behavior. It names four important layers:

- ownership
- source control
- validation
- licensing

It also recommends operational KPIs:

- trigger precision
- trigger recall
- task success rate
- validation pass rate
- eval pass rate
- stale-skill rate
- mean refresh time
- token footprint
- duplicate-skill rate
- reference hit rate

The newer ecosystem sources add concrete trust and quality concerns:

- One curated list warns that listed skills are curated, not audited, and may change after listing.
- That same source warns about risks such as prompt injection, tool poisoning, malware payloads, or unsafe data handling patterns, and recommends reviewing the source before use.
- The curated quality criteria emphasize specific descriptions, progressive disclosure, no absolute machine-specific paths, and scoped tool access.
- OpenAI's catalog notes that licensing can live at the individual skill-directory level.

These details sharpen the meaning of governance. It is not only about "Is this our skill?" It is also about "Can we trust this skill enough to let it shape agent behavior?"

The Agentmail tokenmaxxing source adds a metric-governance caution: token footprint is useful only beside outcome measures. If token count becomes the target, teams may optimize for activity rather than work. For skill repositories and agent programs, token metrics should be interpreted as cost, adoption, or diagnostic signals, then paired with task success, output quality, downstream value, and [[concepts/Context Rot]] checks.

## Where Sources Agree

The sources agree that skills are operational artifacts, not decorative documentation. That makes ownership and quality checks necessary.

They also agree that routing quality matters. If an agent selects the wrong skill, misses the right one, or loads too much irrelevant material, the skill repository is failing even if every Markdown file looks polished.

Finally, they agree that reuse introduces risk. A skill imported from a public catalog may be helpful, but it should not be treated as automatically safe or current.

## Where Sources Disagree

The sources do not report a single shared governance standard across vendors. Instead, they offer overlapping pieces: package design, repository practice, validation guidance, licensing advice, and curation warnings.

There is also a tension between curation and audit. A curated list can improve discovery and quality signals, but curation does not guarantee security review. The raw sources make that uncertainty explicit.

## Connections

- [[Validation and Evaluation]] explains quality checks.
- [[Provenance and Versioning]] explains source tracking and releases.
- [[Portable Skill Core]] explains why routing metadata affects metrics.
- [[Vendor Adapters]] explains how governance can preserve portability.
- [[Progressive Disclosure]] explains token footprint and reference hit rate.
- [[Skill Distribution and Installation]] explains why public distribution increases trust requirements.
- [[Context Development Lifecycle]] frames governance as the organizational loop that scales individual skill authoring to team-level context management.
- [[Context Observability and Feedback]] covers the security scanning, AI SBOM, and context filter patterns that governance must enforce for third-party skills.
- [[concepts/Tokenmaxxing]] and [[sources/The tokenmaxxing math nobody wants to admit]] explain why token spend should not become the scoreboard.

## Open Questions

- Which KPIs should be mandatory for a small personal skill repository?
- Will public skill ecosystems converge on signing, trust metadata, or stronger audit signals?
