---
type: source-summary
created: 2026-06-01
updated: 2026-06-01
status: active
sources:
  - "raw/Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic).md"
tags: [html-specs, planning, prd, design-systems, compute-allocation, agent-communication]
---

# Why this Claude Code engineer uses HTML files as AI specs — Thariq Shihipar

**Source**: How I AI podcast / YouTube, `https://www.youtube.com/watch?v=Qrpm7E80wQ0`  
**Speaker**: Thariq Shihipar (Anthropic, Claude Code team)  
**Published**: 2026-05-18  
**Created**: 2026-05-31 (updated 2026-06-01)

## Summary

Thariq Shihipar, an engineer on the Claude Code team at Anthropic, advocates replacing Markdown with HTML as the primary format for AI agent planning and specification documents. The argument is not that HTML is easier for models to read — they handle both well — but that HTML produces **more engaging artifacts for humans**, which leads to better human engagement with specs and ultimately better products. He demonstrates a workflow of brainstorming in HTML, planning in HTML, building throwaway micro-UIs for editing specific plan sections, and maintaining living HTML design systems that travel with the codebase.

## Key Points

- **Plans matter more as models get more capable.** When you say "Claude can run for 8 hours," you're really saying "Claude can spend $500." Humans must decide what compute is worth spending on.
- **Everyone is becoming a "compute allocator."** The job is deciding what work to delegate and how to frame it.
- **Markdown plans are too long to read.** With Opus 4.5/4.7 running for hours, plans become thousand-line files that Shihipar admits he stopped reading and started asking Claude to edit instead.
- **HTML is more scrollable, visual, and engaging.** Models can produce HTML diagrams, mockups, tables, and interactive elements that a human will actually read.
- **99% of AI-generated tokens should go to planning, interfaces, and communication — not production code.**
- **HTML brainstorming produces visual demos, not text lists.** Shihipar asked Claude to brainstorm podcast demo ideas in HTML and got eight visual mockups with descriptions, risks, and rationale.
- **Throwaway micro-UIs for editing plan sections.** When a plan section (e.g., data visualization rules) needs refinement, he asks Claude to build a custom interactive HTML UI for that specific editing problem, then copies the output back.
- **Living HTML design systems.** Instead of `design.md`, he uses `designsystem.html` — a compressed, visual representation of colors, typography, components, spacing that agents can reference across projects.
- **Prompting philosophy: trust Claude but give constraints.** "Create an HTML file with a plan... include excerpts, mockups, code, whatever is needed to give me maximum context." The "whatever is needed" clause gives Claude flexibility while the specific requests ensure key artifacts are included.
- **HTML specs enable just-in-time documentation.** When creation cost approaches zero, you can produce very high quality, format-specific artifacts without worrying about central repository compliance.
- **Comments and annotations can be built into HTML plans.** Teams can build lightweight review interfaces directly into plan HTML, shaped to their team's review process.
- **"Complexity has to earn its keep."** HTML should not over-constrain Claude; the goal is richer communication, not rigid templates.
- **Collaboration benefit:** colleagues are 100× more likely to read an engaging HTML plan than a thousand-line Markdown file.
- **The abundance mindset:** Shihipar produces many more tokens in planning, dashboards, and custom interfaces than in production code. The artifacts are beautiful and he hopes that translates to output quality.

## Evidence

- Shihipar works on the Claude Code team at Anthropic and speaks from direct experience with the tool's development.
- The demo showed a real Claude Code session: brainstorming → interview → HTML plan → micro-UI for editing section.
- His weekly status updates to his manager (Cat) are generated as HTML — and she actually reads them.
- He references the Jevons paradox: as software gets cheaper, you don't use less — you use it differently and more.

## Connections

- [[concepts/HTML as AI Spec Format]] — Primary source for the HTML-as-spec format and the compute allocator mindset.
- [[concepts/Ride the Models]] — Shihipar's workflow exemplifies riding the models: using longer-running, more capable models for richer spec formats.
- [[concepts/Understanding as the Human Bottleneck]] — HTML specs exist to keep humans engaged and in the loop, not to replace human review.
- [[concepts/Tokenmaxxing]] — The "99% of tokens on planning" claim is a concrete tokenmaxxing pattern.
- [[concepts/Skill Authoring Workflow]] — HTML specs can be packaged as skills that produce visual planning artifacts.
- [[concepts/Progressive Disclosure]] — HTML's ability to show/hide sections supports progressive disclosure in spec documents.
- [[concepts/Software Economics]] — Just-in-time documentation becomes viable when content creation cost approaches zero.

## Contradictions or Tensions

- HTML is less editable by humans than Markdown. Shihipar acknowledges this and shows the micro-UI workaround, but the workflow depends on Claude being available.
- HTML specs living in repos may not be discoverable by agents as easily as `SKILL.md` or `CLAUDE.md` files. The wiki's [[Discovery Conventions]] concept needs updating.
- The "99% of tokens on planning" claim conflicts with cost-minimization instincts and raises governance questions about token budgets.
- Just-in-time documentation trades off against the need for institutional memory and centralized truth.

## Open Questions

- Will the ecosystem develop HTML spec conventions (e.g., standard sections, metadata, linking patterns) the way Markdown has conventions for README and docs?
- How should HTML specs be versioned and diffed in git?
- Can HTML specs be combined with `SKILL.md` packages — e.g., a skill that always produces HTML artifacts?
- What is the right balance between just-in-time documentation and durable institutional knowledge?
