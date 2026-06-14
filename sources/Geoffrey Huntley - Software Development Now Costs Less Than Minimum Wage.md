---
type: source-summary
created: 2026-06-07
updated: 2026-06-07
status: active
sources:
  - "raw/Geoffrey Huntley - Software Development Now Costs Less Than Minimum Wage.md"
tags: [software-economics, model-first-companies, ai-adoption, identity-erasure, tokenmaxxing, pycon]
---

# Geoffrey Huntley — Software Development Now Costs Less Than Minimum Wage

**Source**: PyCon Lithuania 2026, `https://www.youtube.com/watch?v=6zQTQ4iVaKg`
**Author**: Geoffrey Huntley
**Published**: 2026-04-24

## Summary

Geoffrey Huntley's PyCon Lithuania talk argues that the unit economics of software development have permanently changed: running frontier models in a loop costs ~$10.42/hour, and cheaper models bring it to cents per hour. This creates a K-shaped economy where "model-first companies" (5–20 people doing the work of 100) outcompete traditional corporates. The talk covers identity function erasure for developers, the collapse of middle management, the shift from knowledge scarcity to knowledge abundance, and the imperative to build your own agent as the fundamental skill.

## Key Points

- **$10.42/hour for software development.** Running Claude or frontier models in a loop autonomously builds software. With cheaper models (e.g., ZAI), it's cents per hour. This was calculated on Sonnet 4.5 pricing 8 months prior.
- **Knowledge scarcity → knowledge abundance.** Society was structured on scarce knowledge commanding premium prices. AI ("amplified intelligence") shifts all knowledge work to abundance. This applies to legal, medical, and all white-collar professions — not just software.
- **The Ralph Wiggum loop.** A memory management technique for autonomous coding agents. Huntley sat on it for 6 months, showed it in Silicon Valley, and it went viral in January 2026 through YC startups. Built into Claude Code, Cursor, and Copilot.
- **Skill floor has dropped.** Models used to be "wild horses" requiring skill to tame. Now they "come factory defaults and just work." The expertise advantage is eroding.
- **Identity function erasure.** Professional identity (.NET developer, Python developer, Vim/Emacs user) is being erased. "You're a Python developer. I don't care." Engineers should be fungible across languages — AI is the ultimate learning tool.
- **Model-first companies.** A new class of company that works "with the grain of the wood" — using Rust and Python because frontier labs dogfood them. Traditional corporates fight the grain with Java/.NET, where models are weaker. Model-first companies: 5–20 people, 30x output, parabolic revenue.
- **Middle management is "utterly screwed."** If your value is coordination, summarization, or information dissemination, AI does that well. Ratios moving to 50:1 engineer-to-manager. "Get back on the tools."
- **Software as clay on a pottery wheel.** No longer front-loading engineering perfection. Get it done, get it right, make it better. Bugs are cheap to fix with OTEL + Sentry + agents.
- **Agile is waste.** Daily stand-ups, estimations, planning poker — all waste now. Remove them. Any management layer between engineers and customer is suspect.
- **Ideas are now execution.** "Ideas are worthless, execution is everything" has flipped. Anyone can build; taste decides what should be built.
- **The cascading displacement.** Displaced Block engineers go to next employer → implement AI → displace more people → recursively feral.
- **$800K in tokens burned.** Huntley's personal spend over 12 months. Hyper-engineer community requires $20K/month minimum token spend to join.
- **Build your damn agent.** The fundamental skill. Use the agent to self-improve itself recursively. ghuntley.com/agent — free workshop, 300 lines of code.

## Evidence

- Atlassian cursor meetup: speakers were designers, PMs, everyone — not software developers.
- NZ Hobbiton tour guide using Cursor to build things. "He's not a software developer. He's a tour guide for Lord of the Rings."
- NZ startup: reduced from 60 to 20 people, getting 30x the output. "It was the best decision — I got rid of all the people who are sick of hearing about AI."
- Block layoffs: "Jack is right. But I don't think AI is factored in yet. What we're seeing is classic over-hiring corrections."
- VCs in NZ, Australia, San Francisco, Korea: "Is software still investable?"
- Vercel website: majority of visitors are agents, not humans. "SEO for agents."
- Geoffrey's AI adoption stages: "It's not good enough" → experimentation → "oh crap" → deliberate practice → mastery. "I don't hire on the left side of the line anymore."

## Connections

- [[concepts/Software Economics]] — $10.42/hour as the concrete unit economics of code generation; knowledge scarcity → abundance.
- [[concepts/The Compute Cost Tradeoff]] — Counterpoint: Huntley says compute is already cheap enough to disrupt; MT says it's the ceiling.
- [[concepts/Software 3.0]] — Skill floor drop, identity erasure, and "software as clay" as evidence of the paradigm shift.
- [[concepts/AI-Native Engineering Organizations]] — Model-first companies as the organizational template; middle management collapse.
- [[concepts/AI-Native Work Archetypes]] — Identity erasure and the consumer-vs-builder distinction.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] — Consumer (cursor user) vs. builder (built an agent) as the new hiring line.
- [[concepts/Tokenmaxxing]] — $800K token spend, $20K/month hyper-engineer community.
- [[concepts/Harness Engineering Principles]] — "Software as clay" and the shift from engineering perfection to business value.
- [[concepts/Self-Improving Skills]] — "Use the agent to self-improve itself recursively."
- [[concepts/Enterprise AI Adoption Flywheel]] — The guitar analogy: forcing AI on employees vs. deliberate practice.

## Contradictions or Tensions

- Huntley says software costs $10.42/hour and model-first companies will destroy corporates. The [[concepts/The Compute Cost Tradeoff|compute cost tradeoff]] source (same week's Every newsletter) argues compute costs keep humans employed. Direct disagreement on whether cheap compute enables or constrains AI displacement.
- "Ideas are now execution" tensions with [[concepts/Understanding as the Human Bottleneck]] — Huntley says anyone can build; the understanding-bottleneck thesis says judgment is the scarce resource.
- "Agile is waste" is a strong claim. Some agile practices (iterative delivery, feedback loops) align with agentic workflows. The waste may be in the ceremony, not the philosophy.
- The NZ startup cutting 2/3 of staff and getting 30x output is a single anecdote from a known contact. The multiplier claim is extraordinary and needs more evidence.
