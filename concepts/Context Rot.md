---
type: concept
created: 2026-05-23
updated: 2026-06-14
status: active
sources:
  - "raw/The tokenmaxxing math nobody wants to admit.md"
  - "raw/How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code.md"
  - "raw/You NEED to try these open-source AI projects RIGHT NOW.md"
tags: [context, agent-metrics, tokenmaxxing, evaluation, parallel-agents, context-compression]
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

- The Agentmail source claims that modern models with million-token context windows can lose more than half their accuracy after roughly 100,000 tokens of context. This should be treated as an Agentmail source claim unless a separate benchmark source is ingested.
- The source links context rot to observable agent failures: forgetting, contradiction, and drift.
- Kilo Code engineers report that **quality drops at 60% context fill**, well before the 95% threshold where compaction kicks in for many coding agents. By compaction time, hallucinations have already started. An Anthropic employee confirmed the "bad compacting" risk when context grows too large. Igor's workaround: split tasks into smaller sub-agents so each finishes before its context fills. The practical heuristic: size tasks by reviewability — if the diff is too large to inspect, the task was too large.
- Source: `raw/How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code.md`.
- **Context compression tools** address context rot directly by reducing redundant and noisy tokens before they reach the model. Headroom compresses tool outputs, logs, RAG chunks, files, and conversation history with 47–92% token savings while preserving accuracy on four benchmarks (GSM8K, TruthfulQA, SQuAD v2, BFCL). This keeps the effective context well below the 60% quality-drop threshold. Source: `raw/You NEED to try these open-source AI projects RIGHT NOW.md`.

## Connections

- [[concepts/Tokenmaxxing]] - Context rot marks the point where more token spend may reduce quality instead of improving it.
- [[concepts/Context Development Lifecycle]] - Context generation and distribution need evaluation and observability to prevent rot.
- [[concepts/Context Observability and Feedback]] - Monitoring context effectiveness can catch drift, failure modes, and noisy inputs.
- [[concepts/Validation and Evaluation]] - Outcome and trace evaluation can reveal when more context harms final results.
- [[concepts/Parallel Agent Management]] — Context rot is the reason tasks must be sized for sub-agents to finish before context fills.
- [[sources/How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code]] — 60% quality drop threshold as practical evidence.
- [[sources/You NEED to try these open-source AI projects RIGHT NOW]] — Headroom context compression as a mitigation tool (47–92% savings, accuracy preserved).

## Open Questions

- Which benchmarks best measure context rot across models and agent tasks?
- How should a harness decide when to summarize, retrieve, compact, or discard context?
- What signals show that a context window is large but no longer useful?
