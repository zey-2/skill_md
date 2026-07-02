---
type: concept
created: 2026-07-02
updated: 2026-07-02
status: active
sources:
  - "raw/Introducing Claude Sonnet 5.md"
tags: [pricing, cost-optimization, tokens, models]
---

# LLM Model Pricing Comparison

## Summary

Side-by-side comparison of per-token pricing for flagship models from Anthropic, OpenAI, and Zhipu AI (via Fireworks). Prices are per million tokens (MTok) in USD. Cached price shown is the discounted rate for repeated prompt prefixes.

## Pricing Table

| Model | Provider | Input | Cached Input | Output |
|---|---|---|---|---|
| **Claude Fable 5** | Anthropic | $10.00 | $1.00 | $50.00 |
| **Claude Opus 4.8** | Anthropic | $5.00 | $0.50 | $25.00 |
| **Claude Sonnet 5** | Anthropic | $3.00 | $0.30 | $15.00 |
| **Claude Sonnet 5** *(intro, until Aug 31 2026)* | Anthropic | $2.00 | $0.20 | $10.00 |
| **GPT-5.5** | OpenAI | $5.50 | $0.55 | $33.00 |
| **GLM 5.2** | Zhipu / Fireworks | $1.54 | $0.154 | $4.84 |

## Key Observations

**Output tokens dominate cost.** For all models, output is 5–6× the input price. Workflows that minimise output tokens (shorter responses, structured extraction, tool use over prose) save more than input optimisation alone.

**GLM 5.2 is dramatically cheaper.** At $4.84/MTok output, GLM 5.2 costs roughly one-third of Sonnet 5 and one-fifth of GPT-5.5. Even against Haiku 4.5 ($5/MTok output), GLM 5.2 is competitive — while claiming Opus-level coding capability.

**Fable 5 sits at the frontier premium.** At $50/MTok output, Fable 5 is 2× Opus 4.8 and 10× Sonnet 5. Use it only for tasks where the quality difference justifies the cost.

**Sonnet 5 introductory pricing expires August 31, 2026.** Until then, Sonnet 5 costs $2/$10 (input/output) — roughly cost-neutral with the old Sonnet 4.6 despite the new tokenizer producing ~30% more tokens.

## Notes

- **Tokenizer schemes differ across providers.** Anthropic (Opus 4.7+), OpenAI, and Zhipu each use different tokenizers that segment text differently. The same paragraph may produce 30% more tokens on one model than another. Per-token price comparisons do not reflect actual cost for identical workloads — always test on representative inputs.
- Cached input pricing for Anthropic is the cache hit rate (0.1× base input). GPT-5.5 and GLM 5.2 cached prices are from their respective provider pricing pages.
- GLM 5.2 pricing sourced from Fireworks AI serverless (Standard tier) with 10% Data Zone uplift applied. Direct Zhipu pricing may differ.

## Guidance

**Choose the model based on the complexity of the task, not the per-token price.** A cheap model that fails on a complex task wastes more tokens (and time) than an expensive model that succeeds in one pass. Use Sonnet 5 or GLM 5.2 for routine work; Opus 4.8 for hard reasoning and agentic coding; Fable 5 only when the frontier quality gap matters. The cheapest token is the one you never send.

## Connections

- [[Token-Efficient LLM Use]] — Strategies to reduce spend across all these models
- [[LLM Tokenizer Changes]] — How tokenizer redesigns affect real cost
- [[LLM Prompt Caching]] — Mechanism behind the cached input discount
- [[LLM Effort Levels and Reasoning Budget Controls]] — Trading quality vs. cost within a model
- [[The Compute Cost Tradeoff]] — Why frontier models cost more and when they're worth it

## Open Questions

- What is GLM 5.2's pricing directly from Zhipu (not via Fireworks)? The Fireworks price may include a margin.
- How does GLM 5.2's cached input compare to GPT-5.5's in real workloads? GLM 5.2's cache discount is 90% ($0.154 vs $1.54) while GPT-5.5's is also 90% ($0.55 vs $5.50) — same ratio, very different absolute cost.
- Will Anthropic introduce a model between Sonnet 5 and Opus 4.8 at a $4/MTok input price point to compete with GLM 5.2?
