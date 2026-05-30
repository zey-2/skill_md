---
type: concept
created: 2026-05-11
updated: 2026-05-28
status: active
sources:
  - "raw/There will only be four jobs.md"
  - "raw/How to get your company AI pilled - geoffintech.md"
  - "raw/How Block is becoming the most AI-native enterprise in the world  Dhanji R. Prasanna.md"
  - "raw/The AI paradox More automation, more humans, more work  Dan Shipper.md"
tags: [ai-native-work, org-design, job-archetypes, product-engineering]
---

# AI-Native Work Archetypes

## Summary

AI-native work archetypes describe how people contribute when AI tools make many categories of output cheap. Instead of organizing purely around product, design, and engineering outputs, teams increasingly need to understand working styles: who accelerates, who stabilizes, who governs, and who makes the product and organization legible to others.

Source: `raw/There will only be four jobs.md`.

## The Four Archetypes

| Archetype | Function | Failure Mode |
|---|---|---|
| Product-minded builder | High-velocity generalist who uses tools, understands customers, and ships across role boundaries | Becomes a "slop cannon" when output outruns quality and judgment |
| Stabilizer | Makes the growing volume of output stable, secure, robust, and maintainable | Becomes a bottleneck if treated only as cleanup after the fact |
| Adult | Applies judgment, risk sense, earned intuition, and authority to keep acceleration pointed in the right direction | Gets ignored when speed is culturally rewarded over direction |
| Interface person | Makes the product, company, and customer relationship legible, pleasant, and trustworthy | Gets undervalued if the organization over-indexes on code generation |

The source uses more provocative labels, including "slop cannon" and "hot people." The durable interpretation is less about the labels and more about the functions: acceleration, stabilization, governance, and interface.

## Why Output-Based Roles Blur

The classic product/design/engineering triangle was organized around who produced what. AI tools weaken that boundary because many people can now produce code, designs, specs, automations, copy, internal tools, and analysis. The question shifts from "what title owns this output?" to "what working style does this problem need?"

This connects directly to [[concepts/AI-Native Engineering Organizations]]. Fiona Fung's Claude Code talk describes similar pressure: roles blur, non-engineering partners ship code, engineers lean into content/design/product work, and hiring weights product sense and deep systems expertise over raw throughput.

## Balance Is the Point

The archetypes are most useful as a balance model:

- Too many builders without stabilizers creates fragile systems.
- Too many builders without adults creates fast movement in the wrong direction.
- Too many builders without interface people creates products or organizations that others cannot understand or trust.
- Too many stabilizers, adults, or interface roles without builders can reduce speed and learning.

The source's strongest claim is not that there will literally be four jobs. It is that AI-native companies need to design for complementary modes of work after output becomes easier to produce.

## Enterprise Case Evidence

Ramp and Block both show the archetypes moving outside engineering. In Ramp's account, risk analysts, sales ops, L&D, finance, sellers, CX, legal, and marketing employees become product-minded builders by creating local tools and workflows. In Block's account, non-technical teams using Goose are among the highest-impact adopters because they can optimize their own workdays without waiting for internal app teams.

These cases also show why the other archetypes remain necessary. Central platform teams, MCP/tooling builders, and review/governance functions act as stabilizers. Executives and senior technical leaders provide the "adult" function by setting expectations, shaping org design, and preserving taste, critical thinking, security, and reliability. Interface work appears in demos, onboarding, office hours, skills marketplaces, and shared channels that make new workflows understandable to the rest of the organization.

## PMs, Full-Stack Designers, and Forward Deployed Engineers

Dan Shipper's Every case adds a more concrete role forecast. He is especially bullish on PMs because AI lets people with product sense, user understanding, and enough technical literacy implement directly instead of coordinating a large team for every change. He is similarly bullish on full-stack designers because taste and interaction quality become more valuable when default AI output makes many products look the same.

The source also identifies forward deployed engineer as a durable AI-native role. The reason is not that agents are weak; it is that stronger agents create more places where someone must understand the customer's workflow, manage the agent harness, debug the integration, and decide what good output looks like. This role blends builder, stabilizer, and interface functions.

## The Generalist Advantage

Shipper observes that when everyone can do everything — engineers design, PMs code, marketing people ship website changes — role confusion is a real side effect. People ask "what is my job anymore?" At Every, this settles because everyone is already a generalist who enjoys having fingers in multiple pots. The prediction is that this will feel more normal over time: marketing people still do marketing, but touching the website directly is just part of marketing now.

The generalist advantage is especially powerful in smaller companies. A PM with product sense, user understanding, and light technical literacy can implement directly without coordinating a large team. A designer with taste and interaction quality can build their own designs instead of handing off to engineers. Both become "dangerous" in the sense that they ship faster than specialists who wait for coordination.

## Two Agents Are Better Than One

The full transcript identifies a non-obvious pattern: when a user's work agent (Codex/Co-work) interacts with another agent (a SaaS product's agent or server), the agent-to-agent conversation carries much more context about the user than the user could type directly. Codex knows what the user has been working on, their preferences, their project history, and can share all of that during onboarding to a new tool. This creates a speed-up effect when the software experience assumes the user always has an agent in the loop.

It also changes debugging: when something goes wrong, the user tells their agent to go fix it, and the agent talks directly to the product's system to diagnose the issue. This is a fundamentally different interaction pattern from human-to-product.

## Connections

- [[sources/There will only be four jobs]] - Source summary.
- [[concepts/AI-Native Engineering Organizations]] - Team structures and norms after coding stops being the bottleneck.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] - Product-minded builders are one expression of the rising ceiling.
- [[concepts/Harness Engineering Principles]] - Stabilizers and adults are part of the organizational harness around agentic output.
- [[concepts/Collaborative AI Engineering]] - Alignment and interface work prevent decentralized execution from becoming coordination debt.
- [[concepts/Tokenmaxxing]] - High-token acceleration needs stabilizing and judgment layers.
- [[concepts/Enterprise AI Adoption Flywheel]] - Explains how these archetypes show up in company-wide adoption.
- [[sources/The AI paradox More automation, more humans, more work  Dan Shipper]] - Every case evidence for PMs, designers, and forward deployed engineers.
- [[concepts/Ride the Models]] - The career strategy that enables generalists to thrive.

## Open Questions

- Can one person sustainably hold multiple archetypes, or do teams need explicit archetype diversity?
- How should hiring loops test for stabilizer, adult, and interface strengths in AI-native companies?
- What rituals give adults and stabilizers real authority without recreating heavyweight process?
