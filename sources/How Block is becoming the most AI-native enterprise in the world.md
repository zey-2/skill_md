---
type: source-summary
created: 2026-05-18
updated: 2026-05-18
status: active
sources:
  - "raw/How Block is becoming the most AI-native enterprise in the world  Dhanji R. Prasanna.md"
tags: [ai-native-orgs, block, goose, mcp, org-design, ai-adoption]
---

# How Block Is Becoming the Most AI-Native Enterprise in the World

**Source**: Lenny's Podcast / YouTube, `https://www.youtube.com/watch?v=JMeXWVw0r3E`
**Speaker**: Dhanji R. Prasanna
**Published**: 2025-10-26
**Created**: 2026-05-18

## Summary

Dhanji R. Prasanna describes Block's AI-native transformation as a blend of identity, org design, open tooling, and executive dogfooding. The core argument is that large-company AI adoption requires more than handing out assistants: Block shifted back toward a technology-company identity, reorganized from business-unit silos into functional engineering and design orgs, built Goose as a deeply extensible agent platform, and used real work plus leadership usage to drive adoption.

## Key Points

- Block's AI push began with an internal "AI manifesto" arguing that the company should take AI seriously, centralize effort, and become AI-native.
- A major organizational move was from GM-style business-unit silos toward functional engineering and design structures, creating shared tools, policies, technical language, and mobility across teams.
- Block's top priority is described as "automate Block": applying AI automation across engineering, support, legal, risk, and other functions.
- Very AI-forward engineering teams self-report 8-10 hours saved per week; across the company, Block estimates a trend toward 20-25% manual hours saved, with caveats that this is measured through a mix of self-reporting and internal metrics.
- Non-technical teams are described as one of the most surprising beneficiaries because they can build small tools for their own workflows instead of waiting for internal app teams.
- Goose is a general-purpose, open-source desktop and command-line AI agent built around MCP. It gives models access to enterprise tools, local files, code, data systems, and desktop automation.
- Goose can orchestrate workflows such as marketing reports by using MCP connectors to query data, write code, generate charts, create documents, and distribute output.
- Block allows employees to use many AI tools, but Goose is the most integrated with Block's systems because MCP wrappers make internal systems orchestrable.
- The source emphasizes human taste, critical thinking, technical depth, and architecture as areas where humans remain important.
- AI has not simply reduced hiring needs; the bigger hiring and planning change comes from functional org design, shared platforms, modularization, and learning mindset.
- Leadership adoption matters: Jack Dorsey, Dhanji, and the executive team use Goose and related tools directly.
- The source favors starting small, experimentation, and controlled chaos backed by enough foundation to prevent reliability or financial harm.

## Evidence

- The transcript states that AI-forward engineering teams report 8-10 hours saved weekly and that Block is trending toward 20-25% manual hours saved across teams.
- Dhanji describes non-technical enterprise risk teams using Goose to compress work from weeks into hours by building self-service tools.
- Goose is described as a general-purpose agent using MCP wrappers around tools such as Salesforce, Snowflake, SQL, Tableau, Looker, code, and desktop automation.
- The transcript contrasts simple AI tooling with structural changes: moving engineering and design into functional organizations, sharing policies, and focusing on technical excellence.
- Hiring changes emphasize eagerness to learn AI tools and critical problem understanding rather than already being expert in a specific AI product.

## Connections

- [[concepts/Enterprise AI Adoption Flywheel]] - Block is the organizational-structure and open-agent case study.
- [[concepts/AI-Native Engineering Organizations]] - Adds Conway's Law, functional org design, and shared technical systems to the team-operating-model view.
- [[concepts/MCP and Tool-Integration Architecture]] - Goose illustrates MCP as the connective layer that turns enterprise systems into agent tools.
- [[concepts/Tool Assembly as a Skill]] - Non-technical teams use agentic tooling to assemble local workflow automations.
- [[concepts/Agentic Engineering vs Vibe Coding]] - Reinforces that AI-native work still needs human technical depth, judgment, and taste.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] - Hiring shifts toward learning mindset, AI fluency, and deeper problem understanding.

## Contradictions or Tensions

- Block is more cautious than Ramp about hiring filters: it values AI openness, but Dhanji says critical thinking and deep technical understanding still matter more than expertise in any specific tool.
- The source argues code quality is not the same as product success, but also stresses that controlled chaos needs foundations that prevent reliability or financial harm.
- Goose is open source and broadly useful, but the source also implies its internal value depends heavily on enterprise-specific integrations and leadership usage.

## Open Questions

- Which parts of Block's reported productivity gains come from AI tooling versus the functional reorganization?
- How does Block govern MCP permissions, data access, and auditability as Goose reaches more systems?
- Can Goose-style open platforms produce the same adoption in companies whose executives do not actively use the tools?
