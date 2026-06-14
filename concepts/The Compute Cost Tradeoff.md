---
type: concept
created: 2026-06-07
updated: 2026-06-07
status: active
sources:
  - "raw/Why We’ll Still Be Employed When AI Can Do Everything.md"
tags: [compute-costs, software-economics, ai-adoption, energy, tradeoffs]
---

# The Compute Cost Tradeoff

## Summary

As AI models become more capable, the binding constraint shifts from "Can AI do this?" to "Is it worth the compute?" Intelligence costs energy. Evolution optimized human cognition for constrained resources over millions of years; AI doesn't inherit that optimization and must brute-force its way to comparable judgment through expensive inference. For many tasks — especially subjective, creative, or socially embedded ones — the compute cost of achieving human-level quality exceeds the cost of hiring a human. This creates a ceiling on AI adoption that is economic, not technical.

Source: MT's counterpoint in `raw/Why We’ll Still Be Employed When AI Can Do Everything.md`.

## The Core Argument

The argument has three parts:

1. **AI capability will outpace human ability.** In a year or two, well-run companies will have AI that executes every knowledge-worker task better than humans — including setting the frames, defining evals, and choosing goals. Framing isn't magic; it derives from layered experience of being a person in the world, and a system that learns from its environment can eventually run the same loop.

2. **But capability doesn't imply adoption.** Intelligence costs energy. Humans run on heuristics — thinking shortcuts evolved over millions of years for survival. AI lacks this evolutionary inheritance and must brute-force equivalent judgment through expensive simulations or "thinking" tokens. There are no free lunches in economics, and AI can't reach superhuman general intelligence without superhuman energy consumption.

3. **The question becomes economic.** It makes sense to delegate tasks to a $20/month model or a $200/month model. But as the "jagged free lunch" ends, is it worth $2,000/month to make slide decks, check email, and vibe code prototypes? If a $20,000/month Ph.D.-level model existed, wouldn't it be better deployed finding cures for cancer than doing routine knowledge work?

## The Waymo Case Study

Waymo is the clearest empirical evidence for the compute cost tradeoff:

| Metric | Waymo | Human Drivers |
|---|---|---|
| Safety (Swiss Re claims data) | 90% fewer claims | Baseline |
| Rider cost | 1/3+ of Uber/Lyft prices | Market rate |
| Workforce impact | San Francisco taxi workforce **grew** | — |

AGI for driving has arrived. The technology is objectively superior. Yet the human workforce grew because the economics of scaling compute-intensive driving to every trip don't outweigh the marginal cost of human drivers for many use cases.

## The Jagged Free Lunch

The "jagged free lunch" is the period when AI capability dramatically exceeds its cost — when a $20/month model can do work that would cost a human $50/hour. This period creates the impression that AI will replace all human work.

The tradeoff argument says this period is temporary. As AI absorbs more tasks, the remaining tasks require more compute (deeper reasoning, more context, more verification). The cost curve bends upward while the capability curve flattens. Eventually, the marginal cost of AI competence on subjective tasks exceeds the marginal cost of human labor.

## Implications for Skill Design

The compute cost tradeoff has direct implications for how skills should be designed:

- **Prefer deterministic code over AI inference when possible.** This is the "save scripts inside skills" pattern from [[concepts/Prompting Skills Not Prompts]]. Trading AI tokens for code compute is cheaper, faster, and repeatable.
- **Design skills to minimize thinking tokens.** Well-structured instructions, clear examples, and pre-computed reference data reduce the inference cost of each skill invocation.
- **Reserve expensive model calls for high-value judgments.** Use cheaper models or code for routine steps; escalate to frontier models only when the task requires genuine reasoning.
- **Measure value as outputs over tokens.** The [[concepts/Tokenmaxxing|tokenmaxxing]] philosophy of spending more model time applies only when the extra tokens produce proportionally better outcomes.

## Connections

- [[concepts/Software Economics]] — The compute cost tradeoff is the next constraint after software scarcity collapses. When code is free, the new scarce resource is judgment — and judgment costs compute.
- [[concepts/Tokenmaxxing]] — Tokenmaxxing assumes more tokens = better output. The compute cost tradeoff says there's a ceiling where additional tokens aren't worth the marginal quality gain.
- [[concepts/Harness Engineering Principles]] — Harness engineering optimizes the human-agent boundary. The compute cost tradeoff defines where that boundary should be drawn for economic reasons.
- [[concepts/Prompting Skills Not Prompts]] — "If you can use code instead of AI, you should" is the skill-design expression of the compute cost tradeoff.
- [[concepts/Understanding as the Human Bottleneck]] — Human understanding may be cheaper than AI understanding for tasks that require embodied experience, social context, or domain intuition.
- [[concepts/Ride the Models]] — The career strategy for humans who remain competitive by leveraging the compute cost tradeoff: focus on tasks where human judgment is cheaper than AI inference.
- [[concepts/AI-Native Work Archetypes]] — The frame-reset cycle creates new human roles precisely because the compute cost of automating the previous frame exceeds hiring a human.
- [[sources/Why We'll Still Be Employed When AI Can Do Everything]] — Source summary.

## Contradictions or Tensions

- The argument assumes energy costs stay high. Historical trends show inference costs dropping rapidly (100x per year in some estimates). If this continues, the compute barrier weakens significantly.
- Dan Shipper's position in the same newsletter directly contradicts this: he argues the frame resets forever, meaning humans always have new work. MT argues AI will eventually outpace framing too, but compute costs keep humans employed anyway. These are different mechanisms for the same conclusion.
- The Waymo case could be read differently: Waymo is already cheaper than Uber for riders, and the taxi workforce grew because of induced demand, not because compute costs are too high. The argument may prove less durable than it appears.

## Open Questions

- How fast are inference costs actually declining for frontier models on complex reasoning tasks? The historical cost decline may not continue at the same rate for the most capable models.
- At what price point does the compute cost tradeoff flip for common knowledge work tasks (email, slide decks, code review)?
- Does the Waymo analogy generalize, or is driving a special case where induced demand and regulatory barriers create unique dynamics?
- How should organizations budget for AI compute when the cost of frontier model inference is unpredictable and vendor-dependent?
