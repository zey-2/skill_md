---
type: concept
created: 2026-05-01
updated: 2026-05-01
status: active
sources:
  - "raw/OpenAI’s 5 Levels Of ‘Super AI’ (AGI To Outperform Human Capability).md"
tags: [agi, openai, ai-capability-levels, ai-trends]
---

# OpenAI's 5 Levels of AGI Progression

## Key Points

OpenAI reportedly tracks its progress toward artificial general intelligence using a five-level framework. Each level represents a qualitatively different capability tier:

| Level | Name | Capability | Status |
|-------|------|------------|--------|
| 1 | Conversational AI | Natural language interaction (ChatGPT, Claude, customer service bots) | Current |
| 2 | Reasoners | Basic problem-solving at doctorate level without tool access | Approaching |
| 3 | Agents | Autonomous operation on user's behalf for multi-day tasks | Near future |
| 4 | Innovators | Independent development of innovations and process improvements | Future |
| 5 | Organizations | Full organizational work performed by collaborating AI agents | ~10-50 years |

## Context for This Wiki

This framework is useful context when evaluating:
- **Agent Skills maturity**: Current tools operate at Level 1-2, with some multi-day agent work approaching Level 3 behavior
- **Tool ecosystem trajectory**: The jump from Level 2 to 3 is described as "significant," involving a transition from limited capabilities to human-like proficiency — directly relevant to why Agent Skills standardization matters
- **Skill design implications**: Skills designed today should anticipate autonomous operation (Level 3) rather than assuming constant human supervision (Level 1-2)

## Connections

Skills designed for each AGI level have different requirements. [[concepts/Agent Skills]] should be written anticipating Level 3 autonomous operation — skills that assume constant human supervision (Level 1-2) will fail when agents run independently. At Level 5 (Organizations), multi-agent coordination becomes the norm, making [[concepts/Agent Frameworks and Orchestration]] essential for managing skill-guided agent teams. Safety and governance boundaries discussed in [[concepts/Skill Governance and Metrics]] grow in importance as agents move from supervised to autonomous operation.

## Source

- Forbes article by Jodie Cook, 2024-07-16, citing Bloomberg reporting on OpenAI's internal tracking
- [[raw/OpenAI’s 5 Levels Of ‘Super AI’ (AGI To Outperform Human Capability)]]
