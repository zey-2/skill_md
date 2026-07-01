---
type: concept
created: 2026-07-01
updated: 2026-07-01
status: active
sources:
  - "raw/The tokenmaxxing math nobody wants to admit.md"
  - "raw/You NEED to try these open-source AI projects RIGHT NOW.md"
tags: [context-compression, token-efficiency, llm-optimization, prompt-compression]
---

# LLM Context Compression

## Summary

Context compression reduces the tokens an LLM reads per turn without changing the answer quality. Approaches range from token-level pruning (LLMLingua) to learned soft prompts (Gist Tokens, AutoCompressor) to provider-level caching (Anthropic, OpenAI, Google). The best tools achieve 2–5× compression with near-original accuracy on most tasks, but compression hurts on fine-grained retrieval, multi-hop reasoning, and exact factual recall.

## Compression Approaches

### Token-Level Pruning: LLMLingua / LLMLingua-2

LLMLingua-2 (ACL 2024) uses a token-classification approach (XLM-RoBERTa-large, 355M params) to decide which tokens to keep. Key results:

| Metric | LLMLingua-2 | LLMLingua v1 | Selective-Context |
|---|---|---|---|
| Compression overhead | 0.4–0.5s | 1.5–2.9s | 15.5–15.9s |
| GPU memory | 2.1 GB | 16.6 GB | — |
| Speedup vs v1 | 3–6× | baseline | — |

Benchmark results at 5× compression on LongBench:

| Task type | Original | LLMLingua-2 | Preserved |
|---|---|---|---|
| FewShot | 67.0 | 66.4 | 99.1% |
| Code | 54.2 | 58.9 | 108.7% (improved) |
| Synthetic | 37.8 | 21.3 | 56.3% |
| LongBench AVG | 44.0 | 39.1 | 88.9% |

At 14× compression on GSM8K: 77.79 vs 78.85 (98.7% preserved). On Mistral-7B, LLMLingua-2 sometimes outperforms uncompressed prompts.

LongLLMLingua improves RAG performance by up to 21.4% using only 1/4 of tokens.

### Learned Soft Prompts: Gist Tokens

Gist Tokens (NeurIPS 2023) compress prompts up to 26× by training LMs to compress into learned tokens via modified attention masks. Achieves 40% FLOPs reduction and 4.2% wall time speedups. Works on both decoder (LLaMA-7B) and encoder-decoder (FLAN-T5-XXL) architectures. Unlike finetuning/distillation, gist avoids retraining per task.

### Summary Vectors: AutoCompressor

AutoCompressor (EMNLP 2023) compresses long contexts into compact summary vectors that serve as soft prompts, trained with unsupervised objectives on sequences up to 30,720 tokens. Summary vectors are good substitutes for plain-text demonstrations in in-context learning.

### Provider-Level Caching

All three major providers offer 90% cache read discounts:

| Provider | Mechanism | Cache discount | Min tokens | TTL |
|---|---|---|---|---|
| Anthropic | Explicit breakpoints (up to 4) | 90% read / 1.25× write | 512–4,096 | 5 min / 1 hr |
| OpenAI | Automatic prefix matching | 90% read / no write cost | 1,024 | 5–10 min / 24 hr |
| Google Gemini | Implicit (2.5+) / explicit | 90% read / $1–4.50/hr storage | 2,048–4,096 | Configurable |

Provider caching is an alternative to content compression for repeated prefixes. It doesn't reduce tokens per se, but reduces their cost.

### Context Distillation

Anthropic uses context distillation to compress long system prompts into model weights via fine-tuning, eliminating the need to send verbose instructions in every API call. Reduces per-call token usage but requires fine-tuning investment.

## When Compression Hurts

Compression degrades accuracy most on:

- **Fine-grained factual retrieval** / needle-in-haystack tasks
- **Multi-hop reasoning chains** that require following connections across compressed context
- **Exact numbers, names, dates** — compression prunes these preferentially
- **Synthetic/constructed tasks** — 44% relative loss at 5× compression

Compression preserves accuracy well on:

- **Classification and sentiment** — minimal degradation
- **Few-shot pattern matching** — 0.9% relative loss at 5×
- **Code generation** — can actually improve (compression removes noise)
- **General summarization** — robust to moderate compression

Naive compression approaches achieve 27–123× ratios but with QA F1 dropping to 19.1–26.1 vs LLMLingua-2's 36.7 at 2.6×. Instruction design matters enormously.

## Practical Guidelines

1. **Start with provider caching** — it's free to implement and gives 90% savings on repeated prefixes.
2. **Use LLMLingua-2 for RAG and long-context workflows** — 2–5× compression with near-original accuracy, 0.4s overhead.
3. **Avoid compression for retrieval-heavy tasks** where exact recall matters.
4. **Test compression on your specific workload** — aggregate benchmarks mask task-specific variation.
5. **Combine with progressive disclosure** — compress the context that reaches the model, not the source material itself.

## Connections

- [[concepts/Context Rot]] — Compression mitigates context rot by keeping effective context below the quality-drop threshold.
- [[concepts/Tokenmaxxing]] — Compression multiplies the effective token budget: same quota covers more work.
- [[concepts/Progressive Disclosure]] — Progressive disclosure reduces what enters context; compression reduces what context costs.
- [[concepts/The Compute Cost Tradeoff]] — Compression is one mechanism for reducing the cost side of the compute tradeoff.
- [[concepts/LLM Prompt Caching]] — Provider caching as a complementary approach to content compression.
- [[sources/You NEED to try these open-source AI projects RIGHT NOW]] — Earlier wiki source on Headroom (now found to be unverifiable; LLMLingua-2 is the evidence-backed alternative).

## Contradictions or Tensions

- The earlier wiki cited "Headroom" as a context compression tool with 47–92% savings. Research found no active, independently reviewed product by that name. LLMLingua-2 is the evidence-backed alternative with published benchmarks.
- Provider caching (90% discount) may be more practical than content compression for many workloads, since it requires no additional tooling. The two approaches are complementary, not competing.
- Compression that improves code generation results (LLMLingua-2 on Mistral-7B) suggests some prompts contain noise that compression removes — the model benefits from signal extraction, not just cost reduction.

## Open Questions

- How does compression interact with prompt caching? Do compressed prompts hit cache differently?
- What's the optimal compression ratio for agentic workflows (tool outputs, conversation history, code context)?
- Does compression interact with effort levels? Lower effort + compression might be redundant or compounding.
- How does compression perform on multimodal contexts (images + text)?
