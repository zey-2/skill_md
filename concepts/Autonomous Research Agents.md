---
type: concept
created: 2026-05-11
updated: 2026-05-11
status: active
sources:
  - "raw/karpathyautoresearch AI agents running research on single-GPU nanochat training automatically.md"
tags: [autonomous-agents, research, experimentation, karpathy]
---

# Autonomous Research Agents

## Summary

Autonomous research agents are AI agents given a real experimental setup and a clear metric, left to iterate on their own code and methodology without human intervention. Karpathy's autoresearch project demonstrated this by giving an agent a single-GPU LLM training rig and letting it experiment overnight, producing ~100 experiments while the human sleeps.

Source: `github.com/karpathy/autoresearch`

## Key Ideas and Evidence

### Core Design

The project is intentionally minimal — only three files matter:

- **`prepare.py`** — Fixed. Downloads training data, trains a BPE tokenizer, provides dataloader and evaluation utilities. Never modified by the agent.
- **`train.py`** — Editable. Contains the full GPT model, optimizer (Muon + AdamW), and training loop. The agent modifies this freely: architecture, hyperparameters, optimizer, batch size, everything.
- **`program.md`** — Editable by humans. Baseline instructions for the agent. This is essentially a lightweight skill file — it sets up the research org and tells the agent what to do.

### Fixed Time Budget

Training runs for exactly 5 minutes (wall clock, excluding startup/compilation) regardless of compute platform. This has two advantages:

1. **Comparability.** Experiments are directly comparable regardless of what the agent changes — model size, batch size, architecture, etc.
2. **Platform optimization.** The agent finds the most optimal model for your specific hardware within that time budget.

The tradeoff is that results are not comparable across different compute platforms.

The metric is `val_bpb` (validation bits per byte) — lower is better, and vocab-size-independent so architectural changes are fairly compared.

### Autonomy Protocol

The agent is instructed to:
- Never stop once the experiment loop has begun.
- Not pause to ask the human if it should continue.
- Not ask about stopping points.
- Work indefinitely until manually stopped or no additional gains remain.

### Output Rate

Approximately 12 experiments per hour, ~100 experiments overnight. The human wakes up to a log of experiments and ideally a better model.

### Scope Control

The agent only touches `train.py`. This keeps the scope manageable and diffs reviewable. The human iterates on `program.md` over time to find the "research org code" that achieves the fastest research progress.

### Platform Requirements

Currently requires a single NVIDIA GPU (tested on H100). For smaller platforms, Karpathy recommends:
- Using a dataset with less entropy (e.g., TinyStories).
- Decreasing `vocab_size` (from 8192 down to 4096, 2048, or even 256 for byte-level).
- Lowering `MAX_SEQ_LEN` and compensating with `DEVICE_BATCH_SIZE`.
- Reducing model `DEPTH` (from 8 to 4).
- Using simpler attention patterns (`WINDOW_PATTERN` of "L" instead of "SSSL").
- Lowering `TOTAL_BATCH_SIZE` (down to ~16K).

## Connections

- [[Self-Improving Skills]] — applies the autoresearch loop to skill improvement instead of model training.
- [[Harness Engineering Principles]] — autoresearch is an example of a thin harness (the agent instructions) over a fat editable component (`train.py`).
- [[Spec-Driven Development]] — `program.md` is the specification the agent follows.

## Open Questions

- Can this pattern generalize beyond ML research to other domains (e.g., architecture optimization, algorithm design)?
- How do you prevent the agent from converging on local optima?
- What mechanisms exist for human-in-the-loop steering without breaking autonomy?
