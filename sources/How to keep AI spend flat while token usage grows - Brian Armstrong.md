---
type: source-summary
created: 2026-06-27
updated: 2026-06-27
status: active
sources:
  - "raw/How to keep AI spend flat while token usage grows - Brian Armstrong.md"
tags: [ai-cost-management, token-spend, model-routing, caching, ai-native-engineering]
---

# How to Keep AI Spend Flat While Token Usage Grows

## Summary

Brian Armstrong (Coinbase CEO) describes how Coinbase cut AI spend nearly in half while token usage continued to grow — not through friction and spend alerts, but through better defaults, routing, caching, lean context, and visibility. The post frames cost management as an infrastructure problem, not a policy problem.

Source: `raw/How to keep AI spend flat while token usage grows - Brian Armstrong.md`.

## Key Points

- **Better Defaults, Not Usage Caps**: 91% of Coinbase employees never hit usage caps. Instead of lowering caps and driving alerts, they default to cheaper open-weight models (GLM 5.2, Kimi 2.7) through an LLM gateway. Engineers can still choose any model.
- **Model Diversity for Cross-Checking**: Code reviews use a diversity of models so they can check each other's work — a concrete cross-agent verification pattern.
- **Prompt Routing**: Custom harnesses preprocess prompts and route to the best model for the job, considering cache hits and model pricing. Frontier models for planning, cheaper models for execution.
- **Humans Shouldn't Choose Models**: Armstrong asserts that AI can automate model selection — humans choosing models is suboptimal.
- **Cache Awareness**: All requests are cache-aware. Cache hit rate went from 5% → 60% in LibreChat after proper implementation. Cache misses are the easiest way to drive cost up.
- **Context Hygiene**: Start fresh sessions when switching tasks, scope file context narrowly, disconnect unused tools. "Don't just compact." The goal is fewer tokens wasted, not fewer tokens used.
- **Visibility Over Friction**: Engineers can use as many tokens as they want from whatever model they want, but usage is visible. More spend implies more expected impact.

## Evidence

The post claims Coinbase cut AI spend nearly in half while token usage continued to grow. Specific metrics: 91% of employees never hitting caps, 5% → 60% cache hit rate improvement in LibreChat.

## Connections

- [[concepts/Tokenmaxxing]] — Armstrong's approach is the organizational counterweight to individual tokenmaxxing: enable high token usage while managing cost through infrastructure, not restriction.
- [[concepts/AI-Native Engineering Organizations]] — Concrete org-level AI cost management playbook: defaults, routing, caching, visibility as the operating model.
- [[concepts/Harness Engineering Principles]] — Routing, caching, and context hygiene are harness infrastructure that makes exponential token growth sustainable.
- [[concepts/Context Rot]] — "Keep context lean" directly addresses context rot: fresh sessions, narrow file scope, disconnected tools.
- [[concepts/LLM Provider Selection for AI Tools]] — Model routing and gateway defaults are a practical implementation of provider selection at scale.
- [[concepts/Tokenmaxxing#Contradictions or Tensions]] — Armstrong's cost-management approach resolves the tension between tokenmaxxing and cost control: spend tokens freely, but route them efficiently.

## Open Questions

- How does Coinbase's LLM gateway routing compare to third-party routers like OpenRouter in practice?
- What is the quality impact of defaulting to open-weight models vs. frontier models for typical engineering tasks?
- How does the "visibility drives impact" model hold up under scaling — does it create perverse incentives or self-regulate?
