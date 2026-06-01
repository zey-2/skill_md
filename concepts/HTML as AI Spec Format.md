---
type: concept
created: 2026-06-01
updated: 2026-06-01
status: active
sources:
  - "raw/Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic).md"
  - "raw/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md"
tags: [html, specs, prd, planning, design-systems, agent-communication]
---

# HTML as AI Spec Format

## Summary

HTML is emerging as a preferred format for AI-generated specifications, plans, and PRDs because it produces artifacts that humans actually read and engage with. Thariq Shihipar (Anthropic, Claude Code team) advocates "HTML is the new Markdown" — not because models read HTML better, but because visual, scrollable, interactive HTML keeps humans in the loop. The pattern includes brainstorming in HTML with visual mockups, planning in HTML with code excerpts and diagrams, building throwaway micro-UIs for editing specific plan sections, and maintaining living HTML design systems that travel with the codebase. Priscila Andre de Oliveira's "Catch Me Up" skill independently uses the same principle: visual tables and diagrams over prose for comprehension.

Sources: `raw/Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic).md` and `raw/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md`.

## The Compute Allocator Mindset

The shift to HTML specs is driven by a deeper change in the developer's role:

- When you say "Claude can run for 8 hours," you're really saying "Claude can spend $500."
- Developers are becoming **compute allocators** — deciding what work is worth delegating and how to frame it.
- Plans, PRDs, and specs matter *more* as models get more capable, because they determine where expensive compute is spent.
- **99% of AI tokens should go to planning, interfaces, and communication — not production code.**

The spec is where the human decides how to spend compute. A spec the human reads and edits is more valuable than one they ignore.

## Why HTML Beats Markdown for Specs

| Dimension | Markdown | HTML |
|---|---|---|
| Readability at scale | Thousand-line files become unreadable | Scrollable, structured, visually organized |
| Visual communication | ASCII diagrams, limited formatting | Real diagrams, mockups, tables, colors |
| Interactivity | None | Clickable sections, tabs, forms, comments |
| Human engagement | Low — eyes cross, skip to end | High — scroll, click, explore |
| Agent readability | Good | Good (models handle both well) |
| Editability | Easy — plain text | Requires tools or micro-UIs |

The key insight is that **HTML is not for the agent — it's for the human**. Agents read both formats well. The bottleneck is human engagement.

## The HTML Spec Workflow

Shihipar demonstrates a four-stage workflow:

1. **Brainstorm in HTML.** Ask Claude for ideas as visual HTML mockups with descriptions, risks, and rationale. The visual format makes it practical to evaluate eight ideas instead of skimming a text list.

2. **Plan in HTML.** After selecting an idea, ask Claude to create an HTML implementation plan with code excerpts, mockups, mood boards, component examples, and helper scripts. The "whatever is needed to give me maximum context" clause gives Claude flexibility.

3. **Edit with micro-UIs.** When a plan section needs refinement (e.g., data visualization rules), ask Claude to build a custom interactive HTML UI for that specific problem. Edit in the micro-UI, copy the output back into the plan.

4. **Maintain living design systems.** Create `designsystem.html` — a compressed visual reference of colors, typography, components, and spacing. Pass it to new projects so agents have design context.

## Supporting Patterns

### Visual Comprehension

Priscila's "Catch Me Up" skill independently arrived at the same principle: visual formats (tables, diagrams, flowcharts) are more effective for understanding than prose. She designed the skill to produce organograms, tables, and structured summaries because she is a visual person and finds them more scannable.

### Throwaway Software

When creation cost approaches zero, you can build disposable tools for specific problems:
- A micro-UI for editing one section of a plan
- A comment/annotation system built into a spec
- A component visualization page for marketers
- A living design system that gets updated per project

These are not permanent applications. They are just-in-time interfaces that serve a specific need and can be discarded.

### Abundance Mindset

Shihipar produces many more tokens in planning, dashboards, and custom interfaces than in production code. The Jevons paradox applies: as content creation gets cheaper, you don't use less — you use it differently and more. The artifacts are beautiful, and the hope is that this translates to output quality.

## Prompting Philosophy

The approach balances constraint and trust:

- Give enough information to get what you want, but don't over-constrain.
- Specific requests ("include excerpts, mockups, code") ensure key artifacts appear.
- Open-ended clauses ("whatever is needed") give the model flexibility to add useful context.
- "I trust you" endings produce better results than restrictive "make no mistakes" prompts.

## Relationship to Other Concepts

HTML specs extend [[concepts/Understanding as the Human Bottleneck]] by providing a concrete format for keeping humans engaged with agent work.

They are a form of [[concepts/Tokenmaxxing]] — spending tokens on visual planning artifacts rather than production code.

They connect to [[concepts/Comprehension-Driven Development]] as the format choice that makes comprehension practical at scale.

They relate to [[concepts/Progressive Disclosure]] because HTML's ability to show/hide sections and use tabs supports presenting complex information progressively.

They complement [[concepts/Skill Authoring Workflow]] — comprehension and planning skills can produce HTML artifacts as their output format.

## Contradictions or Tensions

- **Editability.** Markdown is easy to edit by hand. HTML requires tools or micro-UIs. The micro-UI pattern works but adds a step.
- **Discoverability.** HTML specs in repos may not be discovered by agents the way `SKILL.md` or `CLAUDE.md` files are. Discovery conventions need updating.
- **Just-in-time vs. durable.** HTML's throwaway nature trades off against institutional memory. When everything is disposable, what becomes the permanent record?
- **Git diffs.** HTML is harder to diff meaningfully than Markdown. Code review of spec changes is more complex.
- **Cost.** HTML specs use more tokens than Markdown. For teams with token budgets, this is a real tradeoff.

## Connections

- [[concepts/Comprehension-Driven Development]] — HTML is the format that makes comprehension practical at scale.
- [[concepts/Understanding as the Human Bottleneck]] — HTML specs exist to keep humans in the loop.
- [[concepts/Tokenmaxxing]] — The "99% of tokens on planning" pattern.
- [[concepts/Progressive Disclosure]] — HTML supports show/hide sections and tabs for complex information.
- [[concepts/Skill Authoring Workflow]] — Skills can produce HTML artifacts as output.
- [[concepts/Software Economics]] — Just-in-time documentation becomes viable when creation cost approaches zero.
- [[concepts/Ride the Models]] — HTML specs leverage longer-running, more capable models.
- [[concepts/Discovery Conventions]] — HTML specs need discoverability conventions.
- [[sources/Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic)]] — Primary source for HTML-as-spec format.
- [[sources/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry]] — Complementary source for visual comprehension pattern.

## Open Questions

- Will the ecosystem develop HTML spec conventions (standard sections, metadata, linking patterns)?
- How should HTML specs be versioned, diffed, and reviewed in git?
- Can HTML specs be combined with `SKILL.md` packages?
- What is the right balance between just-in-time documentation and durable institutional knowledge?
- Will agent runtimes develop native HTML spec discovery mechanisms?
