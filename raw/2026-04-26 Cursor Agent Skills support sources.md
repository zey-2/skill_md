---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://cursor.com/changelog/2-4"
  - "https://cursor.com/docs/skills"
  - "https://forum.cursor.com/t/cursor-2-4-skills/149402"
  - "https://forum.cursor.com/t/developing-skills-workflows-and-universal-standards/154369"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, cursor]
---

# Cursor Agent Skills support sources

## Source Identity

Cursor's official changelog for version 2.4 announces support for Agent Skills. The Cursor docs URL for skills exists, but the text extraction available in this run did not expose the full page body. Cursor forum posts and prior ecosystem sources provide supplemental path and behavior details.

## Relevant Extracted Facts

- Cursor's 2.4 changelog says Cursor supports Agent Skills in the editor and CLI.
- The changelog says agents can discover and apply skills when domain-specific knowledge and workflows are relevant.
- The changelog says skills can also be invoked from the slash command menu.
- The changelog says skills are defined in `SKILL.md` files and can include custom commands, scripts, and instructions.
- The changelog contrasts skills with always-on declarative rules, saying skills are better for dynamic context discovery and procedural instructions.
- Cursor's docs page for Agent Skills is at `https://cursor.com/docs/skills`; the page redirected correctly but yielded no readable body in this fetch.
- Cursor forum discussion links the feature to the official docs and says putting reusable logic into `.agents/skills/` at project root is a simple write-once path for cross-agent use.
- Existing local raw source `raw/VoltAgentawesome-agent-skills...md` lists Cursor paths as `.cursor/skills/` and `~/.cursor/skills/`.

## Tool Support Evidence

Primary support evidence: Cursor's official changelog says Agent Skills are supported in both editor and CLI.

Path details should be treated with moderate confidence unless confirmed directly from a readable Cursor docs page. Existing local raw ecosystem notes already cite `.cursor/skills/` and `~/.cursor/skills/`.

## Open Questions

- Need a direct readable copy of Cursor's current docs page to confirm all supported discovery paths and precedence rules.
