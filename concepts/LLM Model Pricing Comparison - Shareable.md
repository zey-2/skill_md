# LLM Model Pricing Comparison

*July 2026 — Prices per million tokens (MTok), USD*

| Model | Provider | Input | Cached Input | Output |
|---|---|---|---|---|
| **Claude Fable 5** | Anthropic | $10.00 | $1.00 | $50.00 |
| **Claude Opus 4.8** | Anthropic | $5.00 | $0.50 | $25.00 |
| **Claude Sonnet 5** | Anthropic | $3.00 | $0.30 | $15.00 |
| **Claude Sonnet 5** *(intro, until Aug 31 2026)* | Anthropic | $2.00 | $0.20 | $10.00 |
| **GPT-5.5** | OpenAI | $5.50 | $0.55 | $33.00 |
| **GLM 5.2** | Zhipu AI | $1.54 | $0.154 | $4.84 |

---

## Key Takeaways

**Input volume usually drives the bill, but output is where you save.** In typical workloads, far more tokens are sent in (prompts, context, system messages, tool results) than generated out. Output is priced 5–6× higher per token, and unlike input, it is directly controllable — shorter responses, structured extraction, and tool use over prose can cut output cost significantly. Minimising output saves more per token than input optimisation.

**GLM 5.2 is dramatically cheaper.** At $4.84/MTok output, GLM 5.2 costs roughly one-third of Sonnet 5 and one-fifth of GPT-5.5 — while claiming Opus-level coding capability.

**Fable 5 is the frontier premium.** At $50/MTok output, Fable 5 is 2× Opus 4.8 and 10× Sonnet 5. Use it only when the quality gap justifies the cost.

**Sonnet 5 introductory pricing expires August 31, 2026.** Until then, Sonnet 5 at $2/$10 is roughly cost-neutral with Sonnet 4.6 despite the new tokenizer producing ~30% more tokens for the same text.

---

## Why Anthropic's New Tokenizer Matters

Starting with Opus 4.7, Anthropic introduced a new tokenizer used by all subsequent models (Opus 4.8, Fable 5, Sonnet 5). It produces **~30% more tokens for the same text** compared to earlier models like Sonnet 4.6 and Opus 4.6.

**How we know:** Opus 4.6 fits ~750K words per 1M tokens. Opus 4.7+ fits ~555K words per 1M tokens. That's 35% fewer words per token — or equivalently, ~30% more tokens for the same input.

**What it means in practice:**
- A workload that cost $100/month on Sonnet 4.6 becomes ~$130/month on Sonnet 5 at the same per-token rate — even though the per-token price didn't change.
- Anthropic's introductory pricing ($2/$10 vs standard $3/$15) is designed to offset this: the lower per-token price roughly cancels out the higher token count.
- The old Sonnet 4.6 and Opus 4.6 still use the previous tokenizer, so they remain cheaper per word for identical content.

**The same problem exists across providers.** OpenAI and Zhipu use their own tokenizers, which also differ from each other and from Anthropic. The same paragraph may produce different token counts on each platform. Per-token prices do **not** reflect actual cost for identical workloads — always benchmark on your own data.

**When comparing Anthropic models to each other**, compare by cost-per-word, not cost-per-token. **When comparing across providers**, the tokenizer gap makes price-per-token even less reliable.

---

## How to Choose

**Choose the model based on task complexity, not per-token price.** A cheap model that fails on a hard task wastes more tokens and time than an expensive model that succeeds in one pass. Some tasks — deep reasoning over long context, complex multi-step agentic coding, novel research synthesis — can only be accomplished by the most capable models. Using a cheaper model for these tasks doesn't save money; it produces nothing and costs you the time spent trying.

| Use case | Recommended model |
|---|---|
| Routine tasks, bulk extraction, simple Q&A | Sonnet 5 or GLM 5.2 |
| Hard reasoning, agentic coding, complex workflows | Opus 4.8 |
| Frontier quality at any cost | Fable 5 |

**The cheapest token is the one you never send.** Before calling the model, ask: can a script do this? Can a template replace this prompt? Can cached results be reused? Can the output be shorter? Every token saved is a token you don't pay for — at any price tier.

---

*Sources: Anthropic pricing page (July 2026), OpenAI API pricing (July 2026), Fireworks AI serverless pricing (July 2026). All prices shown include 10% Data Zone uplift where applicable.*
