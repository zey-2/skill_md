---
type: concept
created: 2026-05-11
updated: 2026-05-11
status: active
sources:
  - "raw/Running an AI-native engineering org.md"
  - "raw/There will only be four jobs.md"
tags: [ai-native-orgs, engineering-management, verification, review, org-design]
---

# AI-Native Engineering Organizations

## Summary

An AI-native engineering organization is one that rewrites its operating model around the fact that coding throughput is no longer the main constraint. The new bottlenecks are verification, review, security, maintainability, alignment, product taste, and whether old processes still serve their purpose.

Source: `raw/Running an AI-native engineering org.md`.

## Shifted Bottlenecks

When agents make code generation cheap, the slow work moves elsewhere:

- Is the change correct?
- Who or what reviews it?
- Which parts need human judgment?
- How is it maintained?
- Can CI, QA, security, and cross-functional partners keep up?
- Which old planning or ownership rituals are now friction rather than safety?

This confirms the broader [[concepts/Harness Engineering Principles]] claim that code is no longer the scarce resource. It also adds a management layer: org processes have to be audited because processes rarely remove themselves.

## Rewritten Team Norms

| Area | Older Default | AI-Native Adjustment |
|---|---|---|
| Planning | Long up-front plans because coding is expensive | Just-in-time planning, prototypes, and PRs as concrete debate artifacts |
| Technical debate | Whiteboard and discuss hypothetical tradeoffs | Generate alternatives and compare real implementation plus caller impact |
| Review | Humans inspect most details | AI handles routine feedback; humans focus on risk, security, legal, expertise, and taste |
| Ownership | Ask who wrote the code | Ask the underlying question: regression source, domain expert, or context need |
| Hiring | Reward raw throughput | Prefer creative builders with product sense and deep systems experts |
| Management | Managers can be farther from code | Managers dogfood, start as ICs, and understand the workflow directly |
| Process | Add rituals as teams grow | Explicit permission to kill stale processes |

## Verification as the New Center

The source strongly reinforces [[concepts/Validation and Evaluation]]. Higher throughput increases the number of ways to break systems, so verification must move earlier and become more automated. Routine review, lint feedback, test additions, and PR babysitting are good AI-assisted review targets. Human expertise is still needed around trust boundaries, security-sensitive code, legal risk, product sense, and taste.

## Metrics

Useful directional metrics include:

- onboarding ramp-up time;
- PR cycle time;
- share of AI-assisted commits;
- quality, reliability, and product delight rather than raw commit count.

The source warns against treating AI-generated code percentage as the real goal. The product outcome still matters more than the throughput statistic.

## Work Archetypes

Yoni Rechtman's "There will only be four jobs" source complements Fiona Fung's org-operating view by naming the working styles that AI-native companies need. High-velocity product-minded builders accelerate output; stabilizers make the output robust; adults apply judgment and risk sense; interface people make the company and product legible and attractive. These are not literal job descriptions. They are a reminder that role boundaries blur when many people can generate code, designs, specs, and automations.

Source: `raw/There will only be four jobs.md`.

## Connections

- [[sources/Running an AI-native engineering org]] - Source summary.
- [[concepts/AI-Native Work Archetypes]] - Working-style taxonomy for AI-native teams.
- [[concepts/Harness Engineering Principles]] - The repo and workflow must preserve scarce human attention.
- [[concepts/Collaborative AI Engineering]] - Team alignment becomes more important when individual output accelerates.
- [[concepts/Validation and Evaluation]] - Verification shifts left and becomes central.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] - The team-level version of the individual rising-ceiling pattern.
- [[concepts/Agent Legibility]] - Code as source of truth works only if the repo is legible to agents and humans.

## Open Questions

- How much planning can be removed before alignment and product coherence suffer?
- Which human review categories should remain mandatory even as model capability improves?
- How should AI-native org structures differ across startups, platform teams, product teams, and regulated enterprises?
