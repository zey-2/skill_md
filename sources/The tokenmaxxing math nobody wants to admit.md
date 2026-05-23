---
type: source-summary
created: 2026-05-23
updated: 2026-05-23
status: active
sources:
  - "raw/The tokenmaxxing math nobody wants to admit.md"
tags: [tokenmaxxing, agent-metrics, context-rot, ai-native-engineering, agentmail]
---

# The tokenmaxxing math nobody wants to admit

**Source**: Agentmail article text provided by user, `raw/The tokenmaxxing math nobody wants to admit.md`
**Created**: 2026-05-23

## Summary

This Agentmail article argues that tokenmaxxing is useful as an adoption and experimentation signal, but dangerous as a scoreboard. Its central distinction is that tokens are a cost and activity measure, while outputs are the value. The source's preferred metric is not raw token burn, but useful outputs per token spent.

## Key Points

- The source frames tokenmaxxing as a live competition among AI-heavy organizations to burn more tokens through internal agents and workflows.
- It gives the sympathetic case: early agent workflows require experimentation, and token usage can show who is actually trying the tools instead of merely talking about adoption.
- It warns that once token volume becomes a target, people will game the metric by creating busywork or optimizing for activity rather than useful outcomes.
- It introduces [[concepts/Context Rot]] as a technical reason that more tokens or longer context can produce worse agent behavior after a threshold.
- It argues that tokens measure what an agent reads or writes, not what the agent accomplishes.
- The proposed score is "outputs over tokens": more real work for fewer tokens, while still allowing heavy token spend when the output justifies it.

## Evidence

- The source states that Meta used an internal "Claudeonomics" leaderboard and that Google publicly named large-scale token processing as tokenmaxxing.
- The source states that Amazon's internal "MeshClaw" usage created incentives for employees to invent token-consuming busywork.
- The source attributes a "tasteful tokenmaxxing" version to Shopify's Mikhail Parakhin: deep serial reasoning rather than indiscriminate parallel-agent spam.
- The source claims that long-context models can lose substantial accuracy beyond roughly 100,000 tokens of context. Treat this as a source claim unless separately verified.
- The source uses the chandelier-by-weight analogy to explain Goodhart's law: when the measurement becomes the target, the system optimizes the measurement instead of the goal.

## Connections

- [[concepts/Tokenmaxxing]] - The durable concept page should now hold both the positive leverage case and this output-ratio critique.
- [[concepts/Context Rot]] - The article's term for degradation as context grows.
- [[concepts/Validation and Evaluation]] - The article strengthens the case for outcome metrics instead of activity metrics.
- [[concepts/Skill Governance and Metrics]] - Token footprint should be interpreted beside task success, quality, and downstream value.
- [[concepts/Harness Engineering Principles]] - High token spend needs harnesses that turn activity into verified output.

## Contradictions or Tensions

- This article challenges the more optimistic tokenmaxxing framing in [[sources/Tokenmaxxing How Top Builders Use AI To Do The Work Of 400 Engineers]] by arguing that token spend is only justified when tied to outputs.
- It does not reject heavy token use. The disagreement is about whether token spend is the goal, a dashboard signal, or a cost input in a value ratio.

## Open Questions

- What counts as a durable "output" for agent workflows: shipped code, meetings booked, payments collected, resolved tickets, validated research, or user satisfaction?
- How should teams detect when token use is experimentation versus metric gaming?
- What practical threshold signals context rot in different models, tools, and tasks?
