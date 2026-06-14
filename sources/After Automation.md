---
type: source-summary
created: 2026-06-14
updated: 2026-06-14
status: active
sources:
  - "raw/After Automation.md"
tags: [ai-native-work, automation, agent-mode, interactive-essay, dan-shipper]
---

# After Automation

**Source**: Every, `https://every.to/p/after-automation`
**Author**: Dan Shipper / The Every Team
**Published**: (not specified)

## Summary

Dan Shipper's essay argues the same paradox as his Lenny's Podcast appearance — AI progress creates more work for humans, not less — but repackages it as an interactive "Agent Mode" article. The essay ships with a companion GitHub repo (`EveryInc/after-automation-agent-mode`) containing `claims.md`, `objections-and-responses.md`, starter prompts, and case studies. Readers paste a setup prompt into Codex, Claude Code, or OpenClaw, and the agent reads the repo to engage with the argument, inspect evidence, and apply it to the reader's own workflows.

## Key Points

### Agent Mode as Publishing Format

The article is structured as an agent-readable knowledge base rather than a traditional essay. The setup prompt instructs the agent to:
1. Read the companion repo first (not the essay itself).
2. Give the cleanest version of the core claim.
3. Identify the part most relevant to the reader's context.
4. Suggest one prompt to run next.

This is a concrete example of [[concepts/Spec-Driven Development]] applied to publishing: the essay is a spec, the repo is the implementation, and the agent is the runtime.

### Core Claim (Restated)

AI progress does not eliminate human work. It moves the human job up a level in expertise. At Every, Codex, Claude Code, OpenClaw, and frontier models are used across coding, writing, design, customer support, and operations — but the human role has shifted to higher-judgment work.

### Objections and Responses

The companion repo includes `objections-and-responses.md` for steelmanning counterarguments. This is notable as a pattern: shipping objections alongside claims makes the essay agent-navigable for adversarial engagement.

## Evidence

- The companion repo (`EveryInc/after-automation-agent-mode`) is a concrete artifact with `claims.md`, `objections-and-responses.md`, `starter-prompts.md`, and `case-studies/every-ai-native-workflows.md`.
- The setup prompt includes instructions for inspecting the reader's own workspace before interviewing them — a context-pull-before-ask pattern.

## Connections

- [[sources/The AI paradox More automation, more humans, more work  Dan Shipper]] — Same thesis, different format. The Lenny's Podcast transcript is the source of the detailed arguments; this article is the interactive publishing wrapper.
- [[concepts/AI-Native Work Archetypes]] — The frame-reset cycle and role evolution are the same as the podcast source.
- [[concepts/Spec-Driven Development]] — The Agent Mode format is spec-driven publishing: the essay is a spec, the repo is the code, the agent is the runtime.
- [[concepts/Skill Authoring Workflow]] — The setup prompt is a skill-like instruction set: connect your agent, read the repo, start with specific prompts.
- [[concepts/Understanding as the Human Bottleneck]] — The interactive format assumes the reader will use an agent to engage with the argument, but the reader still needs to understand the claims to evaluate the agent's output.

## Contradictions or Tensions

- The article format assumes readers have access to coding agents (Codex, Claude Code, OpenClaw). This limits the audience to agent-equipped readers, which may exclude the very people who most need to understand the argument about automation creating more work.
- The "inspect my workspace before interviewing me" instruction is powerful but raises privacy concerns — the agent reads project files, README, commits, issue lists, and calendars.
