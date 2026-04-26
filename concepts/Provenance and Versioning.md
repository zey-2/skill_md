---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/skill.md for AI Agents.md"
tags: [agent-skills, provenance, versioning]
---

# Provenance and Versioning

## Summary

Provenance records where a skill came from. Versioning records when and how it changed. Together, they let maintainers refresh a skill confidently instead of guessing whether it still matches its sources.

Source: `raw/skill.md for AI Agents.md`, sections "Recommended repository model and schema" and "Authoring and maintenance workflow".

## Key Ideas and Evidence

The raw source recommends storing fields such as:

- `source_url`
- `source_sha`
- `source_type`
- `last_sync`
- `version`
- `release_tag`
- `last_validated_at`

It also points to repository practice such as storing generation or sync metadata with source Git SHAs and dates. The practical message is that a skill repository should be operated like code: reviewed, versioned, released, and traceable.

## Where Sources Agree

The sources agree that skills need lifecycle management. Official docs may change. Internal workflows may drift. Scripts may break. A skill without provenance becomes difficult to audit or refresh.

They also agree that release records matter. If an agent behaves differently after a skill update, maintainers need a way to inspect what changed.

## Where Sources Disagree

The sources differ on how formal provenance needs to be. A small skill package may only need a source URL and updated date. A generated repository may need source SHAs, sync manifests, release tags, validation status, and eval history.

The raw source's recommended approach is conservative: preserve source URLs and source Git SHAs where possible, validate in CI, and version releases explicitly. That advice goes beyond the minimal portable skill format because it is about repository operations, not just runtime loading.

## Connections

- [[Skill Repository Architecture]] explains where provenance metadata can live.
- [[Validation and Evaluation]] explains how validation status fits release tracking.
- [[Skill Authoring Workflow]] explains when to refresh from upstream docs.
- [[Skill Governance and Metrics]] explains stale-skill rate and mean refresh time.

## Open Questions

- How should a repository handle sources that do not expose stable Git SHAs?
- Should generated skills include their source provenance inside `SKILL.md`, in a sidecar file, or both?
