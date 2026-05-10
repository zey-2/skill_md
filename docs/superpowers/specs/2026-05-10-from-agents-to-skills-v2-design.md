---
name: from-agents-to-skills-v2-presentation
description: Design spec for the SKILL.md-focused version of the "From Agents to Skills" presentation
type: presentation-design
---

# Design Spec: From Agents to Skills v2 — SKILL.md at the Center

## Context

This is a rewrite of the existing 60-minute presentation ([presentation.html](courses/from-agents-to-skills/presentation.html)). The new version keeps the same audience and neobrutalist visual style but shifts the center of gravity to SKILL.md. The agent recap is compressed to 1 slide. New sections cover: why generative AI / why skills, how skills are built in practice, a creation framework, AI risks, and a demo intro slide leading into a separate 30-minute live demo session.

## Slide Count & Timing

~18-20 slides, ~60 minutes total + 30-min demo session (separate).

---

## Section 1: Software 3.0 & the Skills Unlock (8 min, 3 slides)

### Slide 1 — Title
"From Agents to Skills" — subtitle, presenter info. Reuse existing title slide style with reveal-word animation.

### Slide 2 — Software 3.0
Software 1.0 = deterministic code. 2.0 = web/mobile access and scale. 3.0 = probabilistic AI that can reason, synthesize, and execute autonomously. Gen AI unlocks capabilities that were impossible to program.

### Slide 3 — The Expertise Problem
Agents are powerful but inconsistent. Domain expertise lives in people's heads. Skills capture that expertise and make it repeatable and reusable across any agent instance. Thesis: "Skills is to capture the domain expertise and make it repeatable and reusable."

**Visual:** 3-stage evolution diagram (1.0 → 2.0 → 3.0) leading into the skills thesis. CSS-only boxes with arrows, matching existing neobrutalist style.

---

## Section 2: Why Agent Skills (7 min, 2 slides)

### Slide 4 — Section Divider
"02 — Why Agent Skills" with section number background.

### Slide 5 — The Problem: Agents Without Skills
Same task, different output every time. No packaged knowledge of how your team wants it done. Agents hallucinate patterns, skip steps, invent conventions.

### Slide 6 — The Solution: What Skills Give You
Consistency, repeatability, reusability. Skills as reusable operating procedures. "MCP gives agents hands, skills give them a brain for a specific job." Domain vs workflow skills.

**Visual:** Reuse the existing "Problem vs Solution" split layout with neobrutalist badges. Two-column comparison cards.

---

## Section 3: SKILL.md Deep Dive (12 min, 3 slides)

### Slide 7 — Section Divider
"03 — SKILL.md Deep Dive"

### Slide 8 — The Skill Package
Directory structure: SKILL.md (required), references/, scripts/, assets/. What each folder does. Front matter (name + description) is the routing mechanism.

**Visual:** Reuse the existing CSS folder illustration (package-illustration with folder tab, file icons, SKILL.md highlighted).

### Slide 9 — Frontmatter is Everything
`name` and `description` are the routing mechanism. Description = triggering conditions ONLY, not workflow summary. The critical insight from superpowers: when descriptions summarize process, Claude skips the full skill content. Keep under 500 characters. Third person. Start with "Use when..."

### Slide 10 — Progressive Disclosure
3-tier loading: metadata (~100 tokens) → body (~500 lines) → references (on-demand). Key rule: if too long for main file, put in references/ and link.

**Visual:** Reuse the existing CSS layered illustration (layers-illustration with 3 nested colored layers).

### Slide 11 — The SKILL.md Template
Full template with color-coded sections: frontmatter, When to use, Steps, Constraints, Examples.

**Visual:** Reuse the existing template-block with YAML/section/placeholder color coding.

---

## Section 4: How Skills Are Built in Practice (8 min, 2 slides)

### Slide 12 — Section Divider
"04 — How Skills Are Built"

### Slide 13 — The Creation Spectrum
5 approaches on a spectrum from lightweight to rigorous:

1. **gbrain** — "If you ask twice, it's a skill." Simple discovery trigger.
2. **write-a-skill (mattpocock)** — Gather, draft, review. 3-step process.
3. **skill-creator** — Iterate with eval viewer. Quantitative benchmarking.
4. **writing-skills (superpowers)** — TDD for process docs. RED-GREEN-REFACTOR.
5. **gstack** — Virtual team specialist. Preamble, decision gates, routing.

**Visual:** Horizontal spectrum bar with 5 labeled positions. CSS-only cards showing approach name, core idea, and when to use.

### Slide 14 — What They All Agree On
Common patterns across all 5: description = routing, progressive disclosure, examples > abstractions, test before deploy, keep SKILL.md concise, references one level deep.

**Visual:** Grid of 6 agreement points in neobrutalist cards.

---

## Section 5: Creation Framework (8 min, 2 slides)

### Slide 15 — Section Divider
"05 — Creation Framework"

### Slide 16 — The Core Loop
5-step practical framework synthesized from all 5 approaches:

1. **Discover** — Identify the repeating task
2. **Draft** — Write SKILL.md with structure and progressive disclosure
3. **Test** — Run with and without the skill, compare outputs
4. **Refine** — Fix triggers, tighten constraints, add examples
5. **Deploy** — Version, share, install

**Visual:** Circular flow diagram using CSS-only numbered nodes with arrows.

### Slide 17 — Choosing Your Rigor Level
Decision guide matching use case to approach:
- Simple personal skills → gbrain / write-a-skill
- Team-critical with measurable quality → skill-creator with evals
- Discipline-enforcing → superpowers TDD methodology

**Visual:** 3-column decision matrix. Each column has a use case, recommended approach, and why.

---

## Section 6: AI Risks (5 min, 1 slide)

### Slide 18 — Section Divider
"06 — AI Risks"

### Slide 19 — Risks of Agent Skills
Prompt injection via malicious SKILL.md. Supply chain risks from unknown sources. Data exfiltration through injected scripts. Over-reliance on unverified skills. What to watch for: skills that run arbitrary code on install, modify agent config, contain hidden instructions. Basic defense: read before installing, sandbox execution, trust verified sources.

**Visual:** Warning-style neobrutalist cards. Red-accented danger cards for each risk type, green-accented defense cards for each mitigation.

---

## Section 7: Demo Intro (2 min, 1 slide)

### Slide 20 — Demo Time
"Let's See It in Action" — Introduce the 3 demo skills for the 30-minute session:

1. **presentation-slides** — Creating interactive HTML presentations
2. **reviewing-technical-documents** — Reviewing and improving technical docs
3. **claim-review-entry** — Processing claim review entries

Each demo shows a different skill type: creative output, analytical review, structured data processing.

**Visual:** 3 large numbered cards, each with skill name and what it demonstrates.

---

## Visual Design Decisions

- **Reuse existing neobrutalist CSS** — Same variables, same card/badge/button styles, same color palette
- **Reuse existing illustrations** — Package anatomy folder, progressive disclosure layers, agent loop (compressed to 1 slide)
- **New illustrations needed** — Software 3.0 evolution diagram, creation spectrum horizontal bar, circular framework flow, AI risk warning cards
- **All CSS-only** — No images, no SVGs, no external assets beyond existing Google Fonts

## Slide Count Summary

| Section | Slides | Time |
|---------|--------|------|
| Title | 1 | 0 |
| Software 3.0 | 3 | 8 min |
| Why Agent Skills | 2 | 7 min |
| SKILL.md Deep Dive | 5 | 12 min |
| How Skills Are Built | 2 | 8 min |
| Creation Framework | 3 | 8 min |
| AI Risks | 2 | 5 min |
| Demo Intro | 1 | 2 min |
| **Total** | **~19** | **~50 min** |

The 10 min slack absorbs into natural pacing, questions during delivery, and deeper emphasis on SKILL.md sections.
