---
type: concept
created: 2026-07-01
updated: 2026-07-01
status: active
sources:
  - "raw/How to keep AI spend flat while token usage grows - Brian Armstrong.md"
tags: [prompt-caching, cost-optimization, inference, kv-cache, llm-infrastructure]
---

# LLM Prompt Caching

## Summary

Prompt caching reuses the computed KV cache from previously processed prompt prefixes so that repeated requests with identical beginnings skip redundant computation. Both Anthropic and OpenAI offer provider-side caching with roughly 90% discounts on cached input tokens, but the mechanisms differ significantly: Anthropic requires explicit cache breakpoints while OpenAI caches automatically. Well-implemented caching can cut input token costs by up to 90% and latency by up to 85%.

## How Prompt Caching Works

When an LLM processes a prompt, it computes key-value (KV) representations for every token in the input. This is the most expensive part of inference for long prompts. Prompt caching stores these KV representations so that subsequent requests with the same prefix can skip recomputation.

The core requirement across all providers is **exact prefix matching**: the beginning of the prompt must be byte-identical to a previously cached version. Any change to the prefix -- even a single token -- invalidates the cache for everything after that point.

## Anthropic Prompt Caching

Anthropic uses an **explicit breakpoint** model. Developers place `cache_control` markers on content blocks to indicate what should be cached.

### Mechanism

- Cache prefix order: `tools` then `system` then `messages` (cumulative hierarchy).
- Two approaches: **automatic caching** (single top-level `cache_control` field; system auto-places the breakpoint on the last cacheable block) and **explicit breakpoints** (place `cache_control` on individual content blocks, up to 4 breakpoints).
- Lookback window: 20 blocks from each breakpoint. The system walks backward checking if a prior request wrote a cache entry at an earlier position.
- Cache refreshes for free each time cached content is reused.

### Pricing (per million tokens)

| Category | Multiplier | Example: Sonnet 5 ($3/MTok base) | Example: Opus 4.8 ($5/MTok base) |
|---|---|---|---|
| Base input | 1x | $3.00 | $5.00 |
| 5-minute cache write | 1.25x | $3.75 | $6.25 |
| 1-hour cache write | 2x | $6.00 | $10.00 |
| Cache read / hit | 0.1x | $0.30 | $0.50 |
| Output | -- | $15.00 | $25.00 |

Cache reads are 90% cheaper than base input. Cache writes cost 25% more (5-min) or 100% more (1-hour) than base input.

### TTL Options

- **Default (5 minutes)**: `{"cache_control": {"type": "ephemeral"}}`
- **1-hour TTL**: `{"cache_control": {"type": "ephemeral", "ttl": "1h"}}` -- costs 2x base input for writes
- Longer TTL entries must appear before shorter ones when mixing

### Minimum Cacheable Token Lengths

| Model | Minimum Tokens |
|---|---|
| Claude Fable 5, Mythos 5 | 512 |
| Claude Opus 4.8, Sonnet 5, Sonnet 4.6, Sonnet 4.5 | 1,024 |
| Claude Mythos Preview, Opus 4.7 | 2,048 |
| Claude Opus 4.6, Opus 4.5, Haiku 4.5 | 4,096 |

### What Gets Cached and What Invalidates

**Cached**: Tools, system messages, text messages (user + assistant), images/documents, tool use/results.

**Invalidation cascades**: Changing `tools` invalidates everything. Changing `system` invalidates system + messages. Changing thinking parameters invalidates message cache (but system/tools survive).

### Multi-Turn Behavior (Automatic Caching)

| Request | Cache behavior |
|---|---|
| Request 1: System + U1 + A1 + U2 | Everything written to cache |
| Request 2: ...+ A2 + U3 | System through U2 read from cache; A2+U3 written |
| Request 3: ...+ A3 + U4 | System through U3 read from cache; A3+U4 written |

### Pre-Warming

Set `max_tokens: 0` to load content into cache without generating output. Useful for startup latency reduction.

## OpenAI Prompt Caching

OpenAI uses **automatic prefix caching**. No code changes are required. The system routes requests to machines that recently processed the same prompt prefix.

### Mechanism

- Routing uses a hash of the first ~256 tokens (varies by model).
- A `prompt_cache_key` parameter can be provided to influence routing and improve hit rates.
- Minimum 1,024 tokens for caching to activate.
- No manual cache clearing available; evictions happen automatically after inactivity.
- Caches are isolated per organization.

### Pricing (per million tokens)

| Model | Input | Cached Input | Output | Cache Discount |
|---|---|---|---|---|
| gpt-5.5 | $5.00 | $0.50 | $30.00 | 90% |
| gpt-5.4 | $2.50 | $0.25 | $15.00 | 90% |
| gpt-5.4-mini | $0.75 | $0.075 | $4.50 | 90% |
| gpt-5.4-nano | $0.20 | $0.02 | $1.25 | 90% |

Cached input is consistently 10% of standard input pricing across all models (90% discount).

### Cache Retention Policies

| Policy | Duration | Models |
|---|---|---|
| In-memory | 5-10 min inactivity, max 1 hour | All caching-enabled models except gpt-5.5+ |
| Extended | Up to 24 hours | gpt-5.5, gpt-5.5-pro, gpt-5.4, gpt-5.2, gpt-5.1 variants, gpt-5, gpt-4.1 |

Extended retention offloads KV tensors to GPU-local storage. Original prompt text is never persisted to disk. Configuration via `prompt_cache_retention` parameter.

### Overflow Behavior

Requests with the same prefix and `prompt_cache_key` exceeding ~15 requests/minute may overflow to additional machines, reducing cache effectiveness.

## Amazon Bedrock Prompt Caching

Bedrock supports prompt caching for Claude models with explicit `cachePoint` markers in the Converse and InvokeModel APIs. Same pricing structure as Anthropic direct API. Supports both 5-minute and 1-hour TTL for compatible models. Also offers automatic prompt caching for Amazon Nova models.

## Prompt Structuring Guidelines for High Cache Hit Rates

1. **Static content first, dynamic content last**: Place system prompts, tool definitions, and shared context at the beginning. Put user-specific or per-request content at the end.

2. **Identical prefixes across requests**: Any change to the prefix -- timestamps, request IDs, per-user context injected early -- breaks the cache for everything downstream.

3. **Monitor cache performance**: Both providers expose `cache_creation_input_tokens` and `cache_read_input_tokens` (Anthropic) or `cached_tokens` (OpenAI) in response usage fields.

4. **Pre-warm caches at startup**: For latency-sensitive applications, send a warmup request with `max_tokens: 0` (Anthropic) or repeated identical prefixes (OpenAI) before serving traffic.

5. **Use 1-hour TTL for long-running sessions**: Agent workflows, multi-step tool use, and extended thinking sessions often exceed the default 5-minute window.

6. **Keep prompts under the lookback window**: Anthropic's automatic prefix checking looks back 20 blocks. If static content extends beyond this, use explicit breakpoints or restructure the prompt.

7. **Use `prompt_cache_key` (OpenAI)**: When many requests share long common prefixes, provide a consistent key to improve routing to machines with the cached version.

## Production Benchmarks

### Anthropic Published Benchmarks

| Use Case | Latency Without Cache | Latency With Cache | Cost Savings |
|---|---|---|---|
| Chat with a book (100K tokens cached) | 11.5s | 2.4s (-79%) | 90% |
| Many-shot prompting (10K tokens) | 1.6s | 1.1s (-31%) | 86% |
| Multi-turn conversation (10-turn, long system prompt) | ~10s | ~2.5s (-75%) | 53% |

Larger cached prompts yield proportionally greater savings. Cost savings scale more predictably than latency improvements.

### Coinbase Production Data

Brian Armstrong reported that Coinbase improved cache hit rates from 5% to 60% in LibreChat after proper implementation. Key enablers: cache-aware request routing, consistent prompt prefixes, and context hygiene (fresh sessions when switching tasks, narrow file scope).

### OpenAI Claims

OpenAI states caching can reduce latency by up to 80% and input token costs by up to 90%.

## Reasoning Tokens and Caching Interaction

### Anthropic Extended Thinking

- Thinking blocks from previous turns can be cached (Opus 4.5+ and Sonnet 4.6+ keep them by default; earlier models remove them from context).
- Changing thinking parameters (enabled/disabled, budget allocation) invalidates message cache breakpoints. System prompts and tools remain cached.
- When cached thinking blocks are read from cache, they count as input tokens.
- For long thinking sessions, use the 1-hour cache duration since extended thinking tasks often exceed 5 minutes.

### OpenAI Reasoning Models

- Reasoning tokens are billed as output tokens and do not benefit from prompt caching directly.
- The `reasoning.effort` parameter (`none`, `minimal`, `low`, `medium`, `high`, `xhigh`) controls internal reasoning depth. Lower settings reduce cost; higher settings improve quality.
- Cached input tokens still count toward TPM rate limits.
- For reasoning models, reserve at least 25,000 tokens for reasoning and outputs.

### Key Distinction

Prompt caching applies to **input tokens** (the prompt prefix). Reasoning tokens are **output tokens** generated during inference. Caching the prompt prefix reduces the input cost, but the reasoning token cost remains unchanged regardless of cache status. The two are orthogonal cost levers.

## Cross-Provider Comparison

| Feature | Anthropic | OpenAI | AWS Bedrock (Claude) |
|---|---|---|---|
| Caching model | Explicit breakpoints | Automatic prefix | Explicit cachePoint markers |
| Cache discount | 90% (0.1x base) | 90% (0.1x base) | Same as Anthropic |
| Write cost (5-min) | 1.25x base | No extra cost | Same as Anthropic |
| Write cost (1-hour) | 2x base | N/A | Same as Anthropic |
| Default TTL | 5 minutes | 5-10 min inactivity | 5 minutes |
| Extended TTL | 1 hour | Up to 24 hours | 1 hour |
| Min tokens | 512-4,096 (model-dependent) | 1,024 | Model-dependent |
| Max breakpoints | 4 | N/A (automatic) | 4 |
| Manual control | Yes (cache_control) | No (automatic only) | Yes (cachePoint) |
| Pre-warming | Yes (max_tokens: 0) | No | Yes |

## Connections

- [[concepts/Tokenmaxxing]] -- Prompt caching is the infrastructure that makes high token usage sustainable. Coinbase went from 5% to 60% cache hit rates, cutting spend nearly in half while usage grew.
- [[concepts/Harness Engineering Principles]] -- Cache-aware routing, prompt structuring, and context hygiene are harness infrastructure that determines whether exponential token growth is affordable.
- [[concepts/Context Rot]] -- Fresh sessions and narrow context scope improve cache hit rates by keeping prefixes consistent and avoiding cache-invalidating context pollution.
- [[concepts/LLM Provider Selection for AI Tools]] -- Caching differences (automatic vs explicit, TTL options, pricing) are a factor in provider selection for production systems.
- [[concepts/LLM Fundamentals]] -- Prompt caching operates on the KV cache from the transformer attention mechanism, reusing computed key-value representations for identical token prefixes.
- [[concepts/The Compute Cost Tradeoff]] -- Caching changes the cost equation: repeated use of the same context becomes 10x cheaper, shifting the tradeoff toward longer, richer prompts.

## Open Questions

- How do cache hit rates degrade in multi-tenant systems where prompt prefixes diverge across users?
- What is the quality impact of structuring prompts for cache friendliness vs. optimal model comprehension?
- How will caching interact with emerging model architectures (mixture-of-experts, sparse attention)?
- What monitoring and alerting should production systems implement for cache hit rate degradation?
