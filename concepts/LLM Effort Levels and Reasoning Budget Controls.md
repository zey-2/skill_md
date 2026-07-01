---
type: concept
created: 2026-07-01
updated: 2026-07-01
status: active
sources:
  - "Anthropic Claude API docs (platform.claude.com)"
  - "OpenAI API docs (developers.openai.com)"
  - "Anthropic models overview"
  - "OpenAI API pricing"
tags: [llm, reasoning, cost-optimization, effort, api]
---

# LLM Effort Levels and Reasoning Budget Controls

## Summary

Both Anthropic and OpenAI offer effort/reasoning-budget parameters that let developers trade off between response quality and token cost. Anthropic uses an `effort` parameter (replacing the deprecated `budget_tokens`), while OpenAI uses `reasoning_effort`. Both follow the same pattern: lower effort = faster and cheaper, higher effort = deeper reasoning at higher cost. The key difference is that Anthropic's effort affects all tokens (including tool calls), while OpenAI's reasoning effort primarily controls internal reasoning chain depth.

## Anthropic: The `effort` Parameter

### How It Works

The `effort` parameter controls how eagerly Claude spends tokens when responding. It affects **all tokens** in the response: text, tool calls, and extended thinking. This is a behavioral signal, not a strict token budget -- at lower effort levels, Claude may still think deeply on hard problems, but will think less than it would at higher levels for the same problem.

- Default is `high` (equivalent to omitting the parameter entirely).
- Available on Claude Fable 5, Mythos 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, Sonnet 4.6, and Opus 4.5.
- No beta header required.
- Replaces the deprecated `budget_tokens` parameter (deprecated on Opus 4.6+, removed on Opus 4.7+).

### Effort Levels

| Level | Description | Typical Use Case |
|-------|-------------|-----------------|
| `low` | Most efficient. Significant token savings with some capability reduction. | Simple tasks, high-volume workloads, subagents, classification, quick lookups |
| `medium` | Balanced approach with moderate token savings. | Agentic tasks balancing speed, cost, and performance |
| `high` | High capability. Equivalent to not setting the parameter. | Complex reasoning, difficult coding, agentic tasks |
| `xhigh` | Extended capability for long-horizon work. | Long-running agentic/coding tasks (30+ min), token budgets in the millions |
| `max` | Absolute maximum capability with no constraints on token spending. | Frontier problems requiring deepest possible reasoning |

### Model-Specific Guidance

**Claude Sonnet 5** (default: `high`):
- `medium` is comparable to Sonnet 4.6 at `high` effort -- a cost-saving step-down.
- `low` for high-volume or latency-sensitive workloads.
- `xhigh` for the hardest coding/agentic tasks.
- `max` for absolute highest capability.

**Claude Sonnet 4.6** (default: `high`):
- `medium` is the recommended default for most applications.
- `low` for high-volume or latency-sensitive workloads.
- Explicitly set effort to avoid unexpected latency.

**Claude Opus 4.7/4.8** (default: `high`):
- Start with `xhigh` for coding and agentic use cases.
- `high` as the minimum for most intelligence-sensitive workloads.
- `medium` for cost-sensitive workloads.
- `max` only when evals show measurable headroom at `xhigh`.
- At `xhigh`/`max`, set `max_tokens` to 64k+ for room to think and act.

**Claude Fable 5** (default: `high`):
- Lower effort settings still perform well and often exceed `xhigh` on prior models.
- Reduce effort if a task takes longer than necessary.

### Effect on Tool Use

Lower effort levels tend to:
- Combine multiple operations into fewer tool calls
- Make fewer tool calls overall
- Proceed directly to action without preamble
- Use terse confirmation messages

Higher effort levels tend to:
- Make more tool calls
- Explain the plan before acting
- Provide detailed summaries
- Include more comprehensive code comments

### Effect on Extended Thinking / Adaptive Thinking

At `high`, `xhigh`, and `max` effort, Claude almost always thinks deeply. At lower levels, it may skip thinking for simpler problems. On models with adaptive thinking (Opus 4.7+, Sonnet 5, Fable 5), effort is the recommended control for thinking depth.

### Pricing

- You are charged for **full thinking tokens**, regardless of display mode.
- Summarized thinking billing counts original thinking tokens, not summary tokens.
- Thinking blocks count as input tokens when cached.
- There is no separate "thinking token" rate -- thinking tokens are billed as output tokens.

### API Usage

```python
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[{"role": "user", "content": "..."}],
    output_config={"effort": "medium"},
)
```

## OpenAI: The `reasoning_effort` Parameter

### How It Works

The `reasoning_effort` parameter controls how much computation the model uses for internal reasoning before responding. Lower effort favors speed and lower token usage; higher effort produces more thorough reasoning. Models adaptively allocate reasoning tokens regardless of the setting -- simpler tasks use fewer tokens even at `high`.

- Available on reasoning models: o1, o3, o4-mini, gpt-5.5, and related variants.
- Works via the Responses API and Chat Completions API.
- Defaults are model-dependent (e.g., `medium` for gpt-5.5).

### Effort Levels

| Level | Description | Typical Use Case |
|-------|-------------|-----------------|
| `none` | No reasoning. Latency-critical tasks that don't benefit from reasoning. | Voice, fast information retrieval, classification |
| `minimal` | Minimal reasoning overhead. | Ultra-low-latency applications |
| `low` | Efficient reasoning with modest latency increase. | Data analysis, drafting, execution-oriented coding, customer support |
| `medium` | Balanced. Default for most workloads. Pareto-optimal for latency/performance/cost. | Agentic coding, research, spreadsheets/slides, long-horizon delegation |
| `high` | Deep reasoning for complex problems. | Complex debugging, deep planning, high-value quality-critical tasks |
| `xhigh` | Deep research with very long rollouts. | Security/code review, enterprise productivity, challenging coding workflows |

Not all models support all effort values -- check the model page before choosing a setting.

### Pricing and Token Impact

- Reasoning tokens are billed as **output tokens** (even though they aren't visible via the API).
- Token counts visible in `usage.output_tokens_details.reasoning_tokens`.
- Costs managed via `max_output_tokens` (limits reasoning + visible output + formatting).
- A response may return `status: "incomplete"` if output limits are hit -- potentially consuming input and reasoning tokens with no visible output.
- OpenAI recommends reserving at least 25,000 tokens for reasoning and outputs when starting out.

### Reasoning Summaries

Raw reasoning tokens are not exposed, but summaries are available via `reasoning.summary: "auto"` for the most detailed summarizer. Summaries appear in the `summary` array within the reasoning output item.

### API Usage

```json
{
  "model": "gpt-5.5",
  "reasoning_effort": "high",
  "messages": [{"role": "user", "content": "..."}]
}
```

### Practical Guidance from OpenAI

- Treat effort as a tuning knob, not the primary way to recover quality.
- For latency-sensitive apps, ask the model to generate a short preamble before deeper reasoning to improve time-to-first-token.
- Use the `phase` parameter (`"commentary"` vs `"final_answer"`) in long-running tool-heavy flows with GPT-5.5/5.4 to prevent early stopping.
- Evaluate both `medium` and `high` depending on task complexity.

## Cost-Performance Tradeoffs

### Token Usage Scaling

The relationship between effort level and token usage is non-linear:

| Effort Level | Relative Token Usage (approximate) | Quality Impact |
|-------------|-----------------------------------|----------------|
| `none`/`low` | ~1/5th of `high` | Noticeable degradation on complex reasoning; near-ceiling on simple tasks |
| `medium` | ~1/3rd of `high` | Good quality for most tasks; may miss edge cases on hard problems |
| `high` | Baseline | Strong across the board |
| `xhigh` | 1.5-3x of `high` | Marginal gains on most tasks; meaningful on hard agentic/coding problems |
| `max` | 2-5x+ of `high` | Diminishing returns; significant cost for small quality gains on most tasks |

These are approximate ranges based on documented behavior, not fixed multipliers. Actual token usage varies by task complexity -- the model adaptively allocates reasoning regardless of effort setting.

### Where Effort Matters Most

| Task Type | Recommended Effort | Why |
|-----------|-------------------|-----|
| Simple classification, routing | `low` or `none` | Near-ceiling accuracy at minimal cost |
| Chat, quick lookups | `low` | Faster turnaround, cost-efficient |
| Data analysis, drafting | `low` to `medium` | Sufficient reasoning for structured tasks |
| Customer support | `low` | Latency matters more than deep reasoning |
| Code generation (routine) | `medium` | Balanced quality and cost |
| Agentic coding | `medium` to `xhigh` | Depends on complexity; start medium, step up |
| Complex debugging | `high` to `xhigh` | Deep reasoning needed for root cause analysis |
| Long-horizon research | `high` to `xhigh` | Extended exploration with many tool calls |
| Security review, deep research | `xhigh` to `max` | Quality-critical, async workflows tolerate latency |
| Frontiers problems (math, science) | `max` | When only the deepest reasoning suffices |

### Key Insight: On Easy Tasks, Effort Doesn't Matter Much

On benchmarks like MMLU that are within the capability range of frontier models, lower reasoning effort often performs comparably to high effort. The cost savings are real while quality impact is minimal. The effort knob matters most on tasks near the model's capability frontier -- SWE-bench-level coding, complex multi-step reasoning, and long-horizon agentic work.

## Cross-Provider Comparison

| Dimension | Anthropic (`effort`) | OpenAI (`reasoning_effort`) |
|-----------|---------------------|-----------------------------|
| Affects | All tokens (text, tools, thinking) | Primarily reasoning chain depth |
| Levels | `low`, `medium`, `high`, `xhigh`, `max` | `none`, `minimal`, `low`, `medium`, `high`, `xhigh` |
| Default | `high` | Model-dependent (`medium` for gpt-5.5) |
| Behavioral signal | Yes (not strict token budget) | Yes (adaptive allocation) |
| Tool call impact | Yes (fewer/combined calls at low effort) | Indirect (through reasoning quality) |
| Thinking control | Integrated (effort controls adaptive thinking) | Separate `reasoning_effort` parameter |
| Billing | Thinking tokens billed as output | Reasoning tokens billed as output |
| Cache interaction | Thinking blocks count as cached input | Reasoning items can be round-tripped |

## Best Practices

1. **Start at `medium`, tune from there.** It's the Pareto-optimal default for most workloads on both platforms.
2. **Don't use `max`/`xhigh` by default.** Reserve for tasks where evals show clear benefit. Most tasks get marginal gains at exponential cost increase.
3. **Use `low` for subagents and high-volume work.** When running many parallel agents, the cost savings compound significantly.
4. **Measure, don't guess.** Run your actual tasks at different effort levels and compare quality vs. cost. The right level depends on task difficulty relative to model capability.
5. **Consider dynamic effort.** Simple queries at `low`, complex reasoning at `high` -- adjust per-request based on task complexity.
6. **Watch for incomplete responses.** On OpenAI, `reasoning_effort: "high"` with low `max_output_tokens` can produce responses with no visible output (all tokens consumed by reasoning).

## Open Questions

- What are the precise token multipliers between effort levels? Neither provider publishes exact ratios.
- How does effort interact with prompt caching efficiency across both providers?
- Will effort levels converge to a standard across providers, or continue to diverge?
- How do effort levels interact with model fine-tuning and distillation?

## Connections

- [[concepts/LLM Prompt Caching|LLM Prompt Caching]] -- Effort level affects thinking token volume, which impacts cache behavior.
- [[concepts/Tokenmaxxing|Tokenmaxxing]] -- Effort controls are the primary mechanism for managing token spend quality.
- [[concepts/Parallel Agent Management|Parallel Agent Management]] -- Low effort for subagents is a key cost-management lever.
- [[concepts/The Compute Cost Tradeoff|The Compute Cost Tradeoff]] -- Effort levels formalize the intelligence-vs-cost tradeoff.
- [[concepts/LLM Provider Selection for AI Tools|LLM Provider Selection for AI Tools]] -- Effort parameter design is a factor in provider selection.
