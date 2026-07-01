---
type: concept
created: 2026-07-01
updated: 2026-07-01
status: active
sources:
  - "raw/Introducing Claude Sonnet 5.md"
tags: [tokenizer, cost-optimization, tokenization, migration]
---

# LLM Tokenizer Changes

## Summary

When LLM providers update their tokenizer, the same input text produces a different number of tokens — which directly affects cost and context window usage. Claude's new tokenizer (Opus 4.7+) produces ~30% more tokens for the same text. OpenAI's tokenizer evolved through four generations, each expanding vocabulary size. Users who compare only per-token prices without accounting for token count changes systematically underestimate migration costs.

## Claude's New Tokenizer

Claude Opus 4.7 introduced a new tokenizer that produces roughly 30% more tokens for the same text compared to earlier models. All subsequent models use this tokenizer: Opus 4.8, Fable 5, Mythos 5, and Sonnet 5.

Evidence from Anthropic's models page:
- Opus 4.7 context window: ~555K words / ~2.5M unicode characters per 1M tokens
- Opus 4.6 context window: ~750K words / ~3.4M unicode characters per 1M tokens
- Ratio: 555/750 = 0.74, confirming ~35% fewer words per token (or ~30% more tokens per word)

**Cost impact:** Sonnet 5 at $3/$15 per MTok with the new tokenizer means ~30% higher effective cost for identical content vs Sonnet 4.6 at the same per-token price. A $100/month workload becomes ~$130/month. Anthropic's introductory pricing ($2/$10 through August 2026) is set to offset this.

**Prompt caching minimums decreased** with the new tokenizer: Opus 4.8 lowered to 1,024 tokens; Fable 5 further lowered to 512 tokens.

## OpenAI's Tokenizer Evolution

OpenAI's tokenizer evolved through four generations:

| Generation | Vocabulary | Used by | Improvement |
|---|---|---|---|
| r50k_base | 50K | GPT-3 | Baseline |
| p50k_base | 50K | GPT-3.5 | Improved efficiency |
| cl100k_base | 100K | GPT-4 | 2× vocabulary |
| o200k_base | 200K | GPT-4o | 2× vocabulary, better multilingual |

Each vocabulary expansion improved efficiency, especially for non-English text.

## Content-Type Efficiency

Tokenizers treat different content types very differently:

| Content type | Approximate efficiency | Notes |
|---|---|---|
| English prose | ~4 chars/token | Most efficient |
| Code | Moderate | Varies by language (Python vs. JSON) |
| JSON/XML | High overhead | Punctuation and structure tokens are numerous |
| Non-English (Latin) | 1.5–2× more tokens | Romance languages, German |
| Non-English (non-Latin) | 2–4× more tokens | CJK, Arabic, Cyrillic on smaller vocabularies |

Llama 3 expanded from 32K to 128K vocabulary, showing 15–30% fewer tokens for English and up to 50% fewer for non-Latin scripts.

## Migration Guidance

Anthropic's official migration steps when switching to models with a new tokenizer:

1. **Recount prompts** — use `/v1/messages/count_tokens` with the target model parameter
2. **Re-benchmark cost and latency** — don't reuse counts from earlier models
3. **Re-tune max_tokens** — more tokens per input means less room for output before hitting limits
4. **Audit client-side token estimation** — if your app estimates tokens locally, update the tokenizer
5. **Update compaction triggers** — if using token thresholds for context management
6. **Re-run cost projections** — per-token price × new token count = actual cost

## Connections

- [[concepts/The Compute Cost Tradeoff]] — The 30% token increase partially offsets Sonnet 5's lower per-token price, narrowing the real cost advantage.
- [[concepts/LLM Fundamentals]] — Tokenization is the first stage of the LLM pipeline; tokenizer changes affect everything downstream.
- [[concepts/Progressive Disclosure]] — Token budgets in progressive disclosure must be recalibrated when the tokenizer changes.
- [[concepts/Context Rot]] — More tokens per input means context fills faster, potentially triggering rot sooner.
- [[concepts/AI Coding Plans]] — Tokenizer changes affect the cost calculus for coding tool subscriptions.
- [[sources/Introducing Claude Sonnet 5]] — Source for the Sonnet 5 tokenizer change.

## Open Questions

- How does the 30% token increase affect prompt caching hit rates? More tokens = more cacheable surface area, but also more cost per cache miss.
- Does the new tokenizer improve or degrade code tokenization efficiency specifically?
- How does tokenizer change interact with effort levels? Higher effort + more tokens per input = compounding cost increase.
- Should cost comparisons between providers normalize for tokenizer efficiency, not just per-token price?
