---
type: concept
created: 2026-05-01
updated: 2026-05-01
status: active
sources:
  - "raw/Deep Dive into LLMs like ChatGPT.md"
tags: [llm-fundamentals, transformer, training, inference, tokenization]
---

# LLM Fundamentals

## Key Points

Andrej Karpathy's "Deep Dive into LLMs like ChatGPT" (Feb 2025) is a comprehensive visual walkthrough of how modern language models are built — from raw internet text to trained inference. It is the single best introductory resource in this wiki for understanding the mechanics behind the models that Agent Skills guide.

## The Pipeline

The full pipeline has three stages: **pretraining** → **fine-tuning** → **inference**.

### Pretraining: Learning Statistical Patterns

1. **Data collection**: Crawl the web (Common Crawl), filter aggressively (URL blocklists, language detection, PII removal, deduplication). Result: ~44TB of clean text = ~15 trillion tokens.
2. **Tokenization**: Convert text to symbols using Byte Pair Encoding (BPE). GPT-4 uses ~100K tokens. This trades vocabulary size for shorter sequences — context window is a precious resource.
3. **Neural network training**: A Transformer model learns to predict the next token in a sequence. Input: variable-length token windows (up to context limit). Output: probability distribution over all tokens. Training iteratively adjusts billions of parameters to match the statistical patterns of the training data.

### Fine-Tuning: Shaping Behavior

After pretraining, the model is a powerful next-token predictor but not necessarily a helpful conversational partner. Fine-tuning (especially RLHF — Reinforcement Learning from Human Feedback) shapes the model's behavior to be helpful, harmless, and honest — or at least aligned with human preferences.

### Inference: Generating New Text

At inference time, the model generates autoregressively: feed prefix → predict next token → sample from distribution → append → repeat. The sampling process (temperature, top_p) controls creativity vs. determinism. Generated text is a "remix" of training patterns, not a retrieval of memorized documents.

## Key Mental Models

- **LLMs are not databases** — they are statistical pattern matchers. They don't "know" things; they predict what tokens likely follow given their training.
- **Context window is finite and precious** — every token in the prompt (including skills, instructions, tool results) consumes part of a fixed budget. This is why progressive disclosure matters.
- **Stochastic by nature** — same prompt can produce different outputs due to sampling. This is why evaluation and guardrails matter.
- **No persistent memory** — each inference call is stateless. Conversation history must be passed explicitly (or managed server-side, as in the Responses API).
- **Pretraining is expensive; inference is cheap** — training costs millions; serving a single request costs fractions of a cent. This asymmetry makes reusable skills valuable — they improve behavior without retraining.

## Numbers That Matter

| Metric | GPT-2 (2019) | Modern (2025+) |
|---|---|---|
| Parameters | 1.6B | 100B–1T+ |
| Context length | 1,024 tokens | 128K–1M tokens |
| Training tokens | ~100B | 10T–15T+ |
| Training cost (approx.) | ~$40K | $10M–$100M+ |

The GPT-2 reproduction in `llm.c` showed that training costs have dropped dramatically: ~$600 for a day of training (down from $40K in 2019), with potential to reach ~$100.

## Relationship to Agent Skills

Understanding these fundamentals clarifies why Agent Skills are structured the way they are:

- **Why skills need precise descriptions**: The model routes to skills by matching the skill's `name` and `description` against the user's request. This is token-level pattern matching, not semantic search. Wording matters because the model predicts which skill's token patterns best match the task.

- **Why progressive disclosure is necessary**: The context window is finite. Loading all skill resources upfront wastes tokens that could be used for the actual task. Skills should load incrementally — metadata first, then details on demand.

- **Why evaluation matters**: Because LLMs are stochastic, a skill that works once may not work consistently. Systematic evals (pass@k, trajectory grading) are needed to measure reliability.

- **Why tools extend LLM capability**: LLMs can't execute code, read files, or search the web by default. Tool calling gives them external capabilities while keeping the model's role as "reasoner and router."

## Connections

- [[concepts/LLM Provider Selection for AI Tools]] — compares the model providers that produce these LLMs.
- [[concepts/AI Coding Plans]] — compares pricing plans for accessing these models.
- [[concepts/Progressive Disclosure]] — directly motivated by context window constraints explained here.
- [[concepts/Validation and Evaluation]] — addresses the stochastic behavior that makes systematic evaluation necessary.
- [[concepts/MCP and Tool-Integration Architecture]] — tools are the mechanism that extends LLMs beyond pure text generation.
- [[concepts/OpenAI Responses API]] — shows how the Responses API manages the statelessness of LLM inference via server-side conversation state.
- [[concepts/Neuro-Symbolic AI Architecture]] — LLM fundamentals explain what LLMs can do; neuro-symbolic architecture addresses what they cannot (deterministic reasoning, verifiable logic).
- [[concepts/Graph-Based Memory for AI Agents]] — LLMs have no persistent memory; graph memory solves this architectural gap.
- [[courses/ai-fundamentals-to-agent-skills/lesson-plan]] — Modules 1–4 cover these foundations as prerequisites for the full curriculum.
