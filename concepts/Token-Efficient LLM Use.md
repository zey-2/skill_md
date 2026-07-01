---
type: synthesis
created: 2026-07-01
updated: 2026-07-01
status: active
sources:
  - "[[How to keep AI spend flat while token usage grows - Brian Armstrong]]"
  - "[[Tokenmaxxing How Top Builders Use AI To Do The Work Of 400 Engineers]]"
  - "[[The tokenmaxxing math nobody wants to admit]]"
  - "[[How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code]]"
  - "[[LLM Model Routing]]"
  - "[[LLM Effort Levels and Reasoning Budget Controls]]"
  - "[[LLM Prompt Caching]]"
  - "[[LLM Context Compression]]"
  - "[[Context Rot]]"
  - "[[The Compute Cost Tradeoff]]"
  - "[[Tokenmaxxing]]"
  - "[[LLM Tokenizer Changes]]"
  - "[[Software Economics]]"
  - "[[Harness Engineering Principles]]"
tags:
  - token-efficiency
  - cost-optimization
  - llm-operations
  - synthesis
---

# Token-Efficient LLM Use

## Summary

Token usage is growing exponentially across every team adopting LLMs. The instinct — cap usage, add friction, ration access — kills adoption and punishes productive work. The better answer is a stack of seven independent strategies that, combined, can keep AI spend flat while usage continues to grow. Coinbase achieved this: spend cut nearly in half while engineers spent freely. The goal is fewer tokens *wasted*, not fewer tokens *used*.

This article lays out the seven strategies, the evidence behind each, and how they connect into a single cost-optimization framework.

---

## The Problem: Exponential Growth Meets Linear Budgets

Every team hitting the same wall. AI adoption accelerates, token consumption surges, and the bill follows. The dynamics are compounding:

- **Model pricing is dropping, but not fast enough.** Opus-tier pricing fell 67% in one generation — from $15/$75 per MTok (Opus 4.1) to $5/$25 (Opus 4.8). Claude Sonnet 5 approaches Opus quality at 40–60% of the price. But even with cheaper per-token costs, total spend grows when usage scales 10x. See [[LLM Tokenizer Changes]] for how tokenizer redesigns can silently increase costs by ~30% for the same text.

- **The "narrowing gap" pattern is real but not enough.** Mid-tier models absorb frontier capabilities within months at 40–60% of the price — this has played out across Claude Sonnet 3.5 through 5, GPT-4 through 4.1, and Gemini Pro through Flash. Relying on price drops alone is passive; the strategies below are active levers.

- **Autonomous development is already cheaper than human labour.** Geoffrey Huntley calculated frontier-model autonomous software development at approximately $10.42/hour (Sonnet 4.5 pricing) — less than minimum wage in most developed countries. The question is no longer "Can AI do this?" but "Is it worth the compute?" See [[The Compute Cost Tradeoff]] for the full argument, including the Waymo evidence: 90% fewer claims, rider cost at 1/3 of Uber/Lyft, yet the San Francisco taxi workforce *grew* because compute economics prevent full replacement.

The instinct to cap usage creates friction, and friction kills adoption. The Coinbase solution: let engineers spend freely, but build infrastructure that makes exponential growth cost-sustainable.

---

## The 7 Strategies

Each strategy is independent. Any one produces savings. Combined, they compound.

### Strategy 1: Model Routing

**The idea:** Most queries don't need the most expensive model. Route by task complexity, not habit.

**The evidence:**

| System | Cost Savings | Quality Preserved |
|---|---|---|
| RouteLLM (LMSys) | Up to 85% | 95% of GPT-4 performance |
| FrugalGPT (Stanford) | Up to 98% | Matches best individual LLM |
| AutoMix | ~10x | Varies by cascade depth |

RouteLLM uses matrix factorization trained on 55K+ pairwise comparisons from Chatbot Arena. FrugalGPT cascades: cheapest model first, self-evaluate ~40 times at temperature=1, build density curves, decide whether to trust or escalate.

**Practical routing heuristics (no trained classifier needed):**

- **Simple code completion / formatting** → cheapest tier (Haiku, nano)
- **Standard coding / summarization** → mid-tier (Sonnet, mini)
- **Planning / architecture / complex reasoning** → frontier (Opus, large)
- **Agentic loops / tool orchestration** → mid-tier with high effort
- **Security-sensitive / high-stakes** → frontier with review

**Provider gateways:** OpenRouter (unified endpoint, hundreds of models, auto-routing beta), LiteLLM (four routing strategies), Portkey (conditional routing, semantic caching, budget limits, circuit breaker), Unify (task-based routing across all providers).

**Coinbase model:** Default to cheaper open-weight models (GLM 5.2, Kimi 2.7). Engineers override freely. Custom LLM gateway preprocesses prompts and routes based on cache hits and pricing. Frontier for planning, cheaper for execution. Model diversity for cross-checking.

See [[LLM Model Routing]] for the full analysis.

---

### Strategy 2: Effort Tuning

**The idea:** The `effort` parameter controls how many tokens the model spends reasoning. Most tasks don't need maximum depth.

**Anthropic's `effort` parameter** affects all tokens (text, tool calls, extended thinking):

| Level | Relative Tokens | Use Case |
|---|---|---|
| `low` | ~1/5 of `high` | Subagents, bulk work, formatting |
| `medium` | ~1/3 of `high` | Most tasks — the Pareto-optimal default |
| `high` | 1x (baseline) | Standard agentic work |
| `xhigh` | 1.5–3x of `high` | Hard agentic/coding problems |
| `max` | 2–5x+ of `high` | Diminishing returns, reserve for evals |

**OpenAI's `reasoning_effort`** controls internal reasoning chain depth: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`. Reasoning tokens are billed as output tokens — invisible via API but they count toward costs.

**Key findings:**

- On easy tasks (MMLU-level), lower reasoning effort performs comparably to high effort. The knob matters most on tasks near the model's capability frontier.
- Use `low` for subagents and high-volume work — cost savings compound significantly across many parallel agents.
- Consider dynamic effort: simple queries at `low`, complex reasoning at `high`.

See [[LLM Effort Levels and Reasoning Budget Controls]] for the full parameter reference and provider comparison.

---

### Strategy 3: Prompt Caching

**The idea:** Store KV representations of processed prompt prefixes so subsequent requests with identical beginnings skip recomputation entirely.

**How it works:** Prompt caching stores the key-value attention state from previous requests. When a new request shares the same prefix, the cached KV state is loaded instead of recomputed. The core requirement is *exact prefix matching* — any change to the prefix invalidates everything downstream.

**Provider comparison:**

| Feature | Anthropic | OpenAI |
|---|---|---|
| Caching model | Explicit breakpoints (up to 4) | Automatic prefix matching |
| Cache discount | 90% on reads | 90% on reads |
| Write cost (5-min) | 1.25x base | No extra cost |
| Default TTL | 5 minutes | 5–10 min inactivity |
| Extended TTL | 1 hour | Up to 24 hours (gpt-5.5+) |
| Min cacheable tokens | 512–4,096 (model-dependent) | 1,024 |

**Production benchmarks:**

- Chat with a book (100K cached tokens): latency 11.5s → 2.4s (−79%), 90% cost savings.
- Multi-turn conversation (10-turn): latency ~10s → ~2.5s (−75%), 53% cost savings.
- Coinbase improved cache hit rates from 5% to 60% in LibreChat.

**Structuring for high hit rates:**

1. Static content first, dynamic content last.
2. Identical prefixes across requests.
3. Pre-warm caches at startup with `max_tokens: 0`.
4. Use 1-hour TTL for long-running agent sessions.
5. Use `prompt_cache_key` on OpenAI to improve routing to machines with warm caches.

**Important:** Reasoning tokens and caching are orthogonal. Prompt caching applies to input tokens. Reasoning tokens are output tokens. The two are independent cost levers.

See [[LLM Prompt Caching]] for the full provider comparison and implementation details.

---

### Strategy 4: Context Compression

**The idea:** Strip noise before tokens reach the model. Less input = fewer tokens = lower cost, and sometimes *better* output (compression removes noise that confused the model).

**Approaches:**

| Approach | Compression | Overhead | Key Result |
|---|---|---|---|
| LLMLingua-2 | 2–5x | 0.4–0.5s | 88.9% accuracy preserved at 5x on LongBench |
| Gist Tokens | 26x | Training required | 40% FLOPs reduction |
| AutoCompressor | Summary vectors | Training required | Compresses up to 30,720 tokens |
| Provider caching | N/A (cost reduction) | None | 90% read discount |

LLMLingua-2 at 14x compression on GSM8K: 77.79 vs 78.85 (98.7% preserved). On Mistral-7B, LLMLingua-2 sometimes outperforms uncompressed prompts — compression removes noise that confused the model.

**When compression works well:**

- Classification and sentiment analysis
- Few-shot pattern matching (0.9% relative loss at 5x)
- Code generation (can actually improve via noise removal)
- General summarization

**When compression hurts:**

- Fine-grained factual retrieval / needle-in-haystack
- Multi-hop reasoning chains
- Exact numbers, names, dates
- Synthetic/constructed tasks (44% relative loss at 5x)

**Headroom tool (practical):** Open-source wrapper achieving 47–92% token savings across real workflows: code search 92%, incident debugging 92%, GitHub issue tracking 73%, codebase exploration 47%. Includes `headroom learn` that mines failed sessions and writes corrections to CLAUDE.md/AGENTS.md — a self-improvement loop.

See [[LLM Context Compression]] for the full approach comparison and tooling details.

---

### Strategy 5: Context Rot

**The idea:** More context isn't always better. Quality degrades well before the window fills. Size tasks to finish before the cliff.

**The evidence:**

- Kilo Code engineers report quality drops at 60% context fill, well before the 95% compaction threshold. By compaction time, hallucinations have already started.
- RULER benchmark (46 models, 4K–128K tokens): top-tier models (Gemini-1.5-pro, Jamba-1.5-large) lose only 1–2% accuracy. Weaker models lose 60–95+ points.
- Effective context is typically 25–50% of claimed context for many models.
- "Lost in the Middle" effect: information in the middle of context is retrieved less reliably than at the beginning or end.
- Attention sink mechanism: models assign disproportionately high attention to initial tokens; evicting early tokens causes disproportionate quality collapse.

**Practical rule of thumb:** Size tasks so agents finish before 60% context fill. If the diff is too large to inspect, the task was too large.

This is not a cost-saving strategy per se — it's a quality-preservation strategy that prevents wasted tokens on degraded outputs. Sending more tokens and getting worse results is the worst of both worlds.

See [[Context Rot]] for the full benchmark data and the attention sink mechanism.

---

### Strategy 6: Code Over Inference

**The idea:** The most efficient token is the one never sent. Prefer deterministic code over AI inference for routine work. Cheaper, faster, repeatable.

**The evidence:**

- Claude Code itself is 98.4% deterministic infrastructure and only 1.6% AI (VILA-Lab analysis of ~512K lines of source code). Even the most advanced AI coding agent is overwhelmingly traditional code.
- Anthropic's "Building Effective Agents" guidance: "finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all."
- Cursor replaced ~15,000 lines of application code with a ~200-line skill, trading hard-coded guardrails for prompt-based instructions backed by evals and RL training.

**Where experts allocate tokens:**

- Priscila's 116-session analysis: 67% comprehension, 2% generation. The expensive work is understanding, not output.
- Thariq Shihipar allocates 99% of tokens to planning, not generation.

**Implications for skill design:**

1. Design skills to minimize thinking tokens through well-structured instructions, clear examples, and pre-computed reference data.
2. Reserve expensive model calls for high-value judgments; use cheaper models or code for routine steps.
3. Skills that embed deterministic logic (scripts, validation, formatting) avoid inference costs entirely.

See [[The Compute Cost Tradeoff]] and [[Harness Engineering Principles]] for the full argument.

---

### Strategy 7: Tokenmaxxing

**The idea:** The meta-strategy. Spend tokens *deliberately* when they buy real output. The goal isn't fewer tokens — it's better outputs per token.

**The positive case** (Garry Tan): Tokenmaxxing is leverage. GStack emerged from repeated prompts becoming reusable skills: planning review, CEO/product review, design review, test review, model cross-checking. The third rebuild of a full-featured blog platform took ~five days and a Claude Code Max subscription.

**The critique** (Agentmail): Tokens are activity and cost signals, not direct work signals. The useful ratio is *outputs over tokens*. When token volume becomes a target, people game the metric. Goodhart's law applies. Context rot means more tokens can produce *worse* behavior after a threshold.

**The organizational resolution** (Coinbase): Let engineers spend freely, but build infrastructure (cheaper defaults, prompt routing, cache awareness, context hygiene) that makes exponential token growth cost-sustainable.

**When to spend more tokens:**

| Bottleneck | Tokenmaxxing Move | Guardrail Needed |
|---|---|---|
| Thin research context | Retrieve more sources, compare disagreements | Citations, contradiction tracking |
| Weak plans | Run role-specific review skills before implementation | Clear acceptance criteria |
| Low test coverage | Generate unit, integration, browser tests | Human review of critical paths |
| Manual QA | Automate browser flows via Playwright | Visual/manual spot checks |
| Agent blind spots | Cross-check with another model or reviewer agent | Resolve disagreements explicitly |

See [[Tokenmaxxing]] for the full debate and practical patterns.

---

## How the Strategies Stack

These seven levers form a decision chain. In practice, a request flows through them:

```
[Query arrives]
    │
    ▼
01  Route to cheapest adequate model ──── 50–98% savings
    │
    ▼
02  Set effort level ──── up to 5x range
    │
    ▼
03  Check prompt cache ──── 90% on cache hits
    │
    ▼
04  Compress context ──── 2–5x token reduction
    │
    ▼
05  Stay under 60% context fill ──── quality preservation
    │
    ▼
06  Use code if deterministic ──── zero tokens
    │
    ▼
07  Measure outputs/tokens ──── iterate
```

Each step is independent — you can adopt any one without the others. But the compounding effect is where the real savings come from. Routing a query to a mid-tier model (step 1), at low effort (step 2), with a cache hit (step 3), after compression (step 4), while staying under 60% fill (step 5), produces a fraction of the cost of sending the same query to a frontier model at max effort with no caching.

---

## The Coinbase Case Study

Brian Armstrong's directive was simple: let engineers spend freely, but build infrastructure that makes exponential token growth cost-sustainable.

**The levers they pulled:**

1. **Cheaper defaults** — Open-weight models (GLM 5.2, Kimi 2.7) as default. Engineers override freely. This is model routing at the organizational level.
2. **Prompt routing** — Custom LLM gateway preprocesses prompts and routes based on cache hits and pricing. Frontier for planning, cheaper for execution.
3. **Cache awareness** — Cache hit rate improved from 5% to 60% in LibreChat. Structural changes to how prompts were organized.
4. **Context hygiene** — Compression and rot avoidance. Model diversity for cross-checking rather than sending everything to one expensive model.
5. **Visibility** — Measurement of what tokens produce, not just how many are consumed.

**Result:** Spend cut nearly in half while token usage continued to grow.

See [[How to keep AI spend flat while token usage grows - Brian Armstrong]] for the original source.

---

## The Hidden Cost: Tokenizer Changes

One often-overlooked factor: the tokenizer itself can silently increase costs.

- Claude Opus 4.7+ introduced a new tokenizer producing ~30% more tokens for the same text. A $100/month workload becomes ~$130/month at the same per-token price.
- OpenAI's tokenizer evolved through four generations: r50k (GPT-3), p50k (GPT-3.5), cl100k (GPT-4), o200k (GPT-4o). Each expanded vocabulary and improved efficiency.
- Content-type efficiency varies enormously: English prose is ~4 chars/token; non-Latin scripts can be 2–4x more tokens.

This means that even if your strategy stack is optimised, a provider-side tokenizer change can silently shift your costs. Monitor per-token pricing *and* token counts for representative workloads.

See [[LLM Tokenizer Changes]] for the full analysis.

---

## The Compute Cost Tradeoff

The deeper question behind all of this: intelligence costs energy, and AI lacks evolved heuristics.

The Waymo evidence is instructive: 90% fewer claims, rider cost at 1/3 of Uber/Lyft, yet San Francisco's taxi workforce *grew*. AGI for driving arrived, but compute economics prevent full replacement. The question shifts from "Can AI do this?" to "Is it worth the compute?"

Token efficiency is how you make the answer "yes" more often. Not by using less AI, but by using it *smarter* — routing, caching, compressing, coding what you can, and spending tokens only when they buy real output.

See [[The Compute Cost Tradeoff]] for the full argument and [[Software Economics]] for the broader economic context.

---

## Connections

- [[LLM Model Routing]] — Full provider gateway comparison, learned routers, routing heuristics
- [[LLM Effort Levels and Reasoning Budget Controls]] — Anthropic and OpenAI effort parameters, best practices
- [[LLM Prompt Caching]] — Provider comparison, TTL strategies, structuring for hit rates
- [[LLM Context Compression]] — LLMLingua-2, Gist Tokens, Headroom tool, when compression helps/hurts
- [[Context Rot]] — RULER benchmark, Lost in the Middle, attention sink mechanism, 60% rule
- [[Tokenmaxxing]] — The debate, practical patterns, outputs-over-tokens metric
- [[The Compute Cost Tradeoff]] — Waymo evidence, capability vs. adoption, energy costs
- [[LLM Tokenizer Changes]] — Silent cost shifts from tokenizer redesigns
- [[Software Economics]] — Broader economic context for AI cost structures
- [[Harness Engineering Principles]] — Code-over-inference in practice, skill design
- [[LLM Provider Selection for AI Tools]] — Choosing providers for cost efficiency
- [[Parallel Agent Management]] — Scaling agents while controlling costs
- [[How to keep AI spend flat while token usage grows - Brian Armstrong]] — Coinbase case study source
- [[Tokenmaxxing How Top Builders Use AI To Do The Work Of 400 Engineers]] — Garry Tan's tokenmaxxing argument
- [[The tokenmaxxing math nobody wants to admit]] — Agentmail's critique of tokenmaxxing
- [[How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code]] — Parallel agent cost management

---

## Open Questions

- How do these strategies interact with multi-modal inputs (images, audio, video)? Compression and caching behave differently for non-text tokens.
- What's the right default for `effort` as models improve? If `low` today matches `high` from six months ago, the Pareto-optimal default shifts over time.
- Can learned routers (RouteLLM, FrugalGPT) be deployed in production with acceptable latency, or are they only viable for offline/batch workloads?
- How do tokeniser changes interact with caching? If the tokenizer changes, cached KV states for the same text may no longer match.
