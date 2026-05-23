---
type: concept
created: 2026-05-23
updated: 2026-05-23
status: active
sources:
  - "raw/The tokenmaxxing math nobody wants to admit.md"
tags: [context, agent-metrics, tokenmaxxing, evaluation]
---

# Context Rot

## Summary

Context rot is the degradation of model or agent performance as the context window grows too large or too noisy. The Agentmail tokenmaxxing article uses the term to explain why more tokens do not automatically mean better agent behavior: beyond a point, the model may forget, contradict itself, or drift.

Source: `raw/The tokenmaxxing math nobody wants to admit.md`.

## Key Points

- Context size is not the same as useful context quality.
- Long context can help when it contains relevant evidence, constraints, and examples.
- Long context can hurt when it buries the important material, introduces contradictions, or exceeds the model's reliable retrieval behavior.
- Context rot is one reason tokenmaxxing needs outcome metrics, not only token-volume metrics.

## Evidence

- The source claims that modern models with million-token context windows can lose more than half their accuracy after roughly 100,000 tokens of context. This should be treated as an Agentmail source claim unless a separate benchmark source is ingested.
- The source links context rot to observable agent failures: forgetting, contradiction, and drift.

## Connections

- [[concepts/Tokenmaxxing]] - Context rot marks the point where more token spend may reduce quality instead of improving it.
- [[concepts/Context Development Lifecycle]] - Context generation and distribution need evaluation and observability to prevent rot.
- [[concepts/Context Observability and Feedback]] - Monitoring context effectiveness can catch drift, failure modes, and noisy inputs.
- [[concepts/Validation and Evaluation]] - Outcome and trace evaluation can reveal when more context harms final results.

## Open Questions

- Which benchmarks best measure context rot across models and agent tasks?
- How should a harness decide when to summarize, retrieve, compact, or discard context?
- What signals show that a context window is large but no longer useful?
