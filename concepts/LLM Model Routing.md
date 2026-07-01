---
type: concept
created: 2026-07-01
updated: 2026-07-01
status: active
sources:
  - "raw/How to keep AI spend flat while token usage grows - Brian Armstrong.md"
tags: [model-routing, cost-optimization, llm-gateway, provider-selection]
---

# LLM Model Routing

## Summary

Model routing sends each query to the most appropriate model based on task complexity, cost, latency, and cache availability. Research shows 50–98% cost reductions while maintaining 95%+ of frontier model quality. Routing ranges from simple provider-level fallback (OpenRouter, LiteLLM) to learned classifiers trained on query difficulty (RouteLLM, FrugalGPT). The key insight: most queries don't need the most expensive model.

## Routing Layers

### Provider Gateways

Provider gateways sit between applications and model providers, handling multi-provider access, fallback, and cost optimization:

| Gateway | Key features | Routing approach |
|---|---|---|
| **OpenRouter** | Unified `/api/v1/chat/completions` endpoint, hundreds of models, `~latest` alias | Provider preferences, model fallback lists, auto-routing (beta) |
| **LiteLLM** | Config-based model aliasing, four routing strategies | simple-shuffle, least-busy, usage-based, latency-based |
| **Portkey** | Conditional routing, semantic caching, budget limits, circuit breaker | Custom conditionals, load balancing across API keys |
| **Unify** | Task-based routing across all providers | Optimizes per task type for fastest/cheapest/most performant |

Coinbase implements a custom LLM gateway that preprocesses prompts and routes to the best model considering cache hits and model pricing. Armstrong reports this cut AI spend nearly in half.

### Learned Routers

Research systems that train classifiers to predict query difficulty and route accordingly:

| System | Method | Cost savings | Quality preserved |
|---|---|---|---|
| **RouteLLM** (LMSys) | Preference-trained routers from Chatbot Arena data (55K+ pairwise comparisons) | Up to 85% | 95% of GPT-4 performance |
| **FrugalGPT** (Stanford) | LLM cascade: cheap model first, escalate on uncertainty | Up to 98% | Matches best individual LLM |
| **AutoMix** | POMDP-based probabilistic routing, self-evaluation at temperature=1 | ~10× | Varies by cascade depth |
| **Semantic Router** | Embedding-based vector comparison (~10ms latency) | — | Depends on route definitions |

RouteLLM uses five router types (matrix factorization recommended, sw_ranking, BERT classifier, causal LLM classifier, random baseline). Routers generalize across model pairs without retraining.

FrugalGPT's cascade: start with cheapest model, self-evaluate ~40 times at temperature=1, build density curves for good vs. bad answers, decide whether to trust or escalate. Key weakness: small models cannot reliably detect their own errors.

### Classifier-Based Routing

Production routing uses two approaches:

- **Multi-label classifier**: predicts all suitable LLMs in one pass
- **Separate binary classifiers**: one per model, fine-tuned RoBERTa most effective

Training requires 9K–15K labeled queries with majority voting. Known pitfalls: overfitting from data sparsity, label skew concentrating on few models, diminishing returns when one model dominates.

## The Coinbase Model

Coinbase's approach is the most documented production implementation:

1. **Default to cheaper models** — open-weight models (GLM 5.2, Kimi 2.7) via LLM gateway
2. **Engineers override freely** — no caps, any model for any task
3. **Preprocess prompts** — route based on cache hits and model pricing
4. **Frontier for planning, cheaper for execution** — task-type routing
5. **Model diversity for cross-checking** — code reviews use multiple models

Result: AI spend cut nearly in half while token usage continued to grow.

Source: `raw/How to keep AI spend flat while token usage grows - Brian Armstrong.md`.

## Practical Routing Heuristics

Without a trained classifier, these heuristics guide model selection:

| Task characteristic | Suggested tier | Rationale |
|---|---|---|
| Simple code completion, formatting, extraction | Cheapest (Haiku, nano) | Pattern matching, not reasoning |
| Standard coding, summarization, Q&A | Mid-tier (Sonnet, mini) | General capability sufficient |
| Planning, architecture, complex reasoning | Frontier (Opus, large) | Quality matters more than cost |
| Agentic loops, tool orchestration | Mid-tier with high effort | Execution volume justifies cheaper model |
| Security-sensitive, high-stakes decisions | Frontier with review | Quality and safety paramount |

## Connections

- [[concepts/The Compute Cost Tradeoff]] — Routing is the operational mechanism for navigating the cost-performance frontier.
- [[concepts/AI-Native Engineering Organizations]] — Coinbase's routing playbook as org-level cost infrastructure.
- [[concepts/LLM Provider Selection for AI Tools]] — Provider selection is the static decision; routing is the dynamic per-query decision.
- [[concepts/Claude Code Third-Party Provider Configuration]] — Technical configuration for multi-provider setups.
- [[concepts/Harness Engineering Principles]] — Routing is harness infrastructure that makes exponential token growth sustainable.
- [[concepts/LLM Effort Levels and Reasoning Budget Controls]] — Effort levels add another dimension to routing: same model, different cost-performance tradeoff.

## Open Questions

- How do you preprocess prompts to determine the right model without adding latency?
- At what point does the routing overhead (latency, complexity) exceed the cost savings?
- How should routing interact with prompt caching? Route to where the warm cache lives, or route to the cheapest model?
- Is there a diminishing returns curve for routing accuracy as the model ecosystem homogenizes?
