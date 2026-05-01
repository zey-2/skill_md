---
type: raw-source
created: 2026-04-30
source_type: web
source_url:
  - "https://code.visualstudio.com/docs/copilot/customization/agent-skills"
  - "https://developercommunity.microsoft.com/t/Add-Agent-Skills-for-Copilot/11038989"
  - "https://learn.microsoft.com/en-us/microsoft-365/copilot/people-skills-manage-custom-skill"
  - "https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-sdk/use-copilot-sdk/custom-skills"
  - "https://techcommunity.microsoft.com/blog/azuredevcommunityblog/supercharge-your-dev-workflows-with-github-copilot-custom-skills/4510012"
  - "https://robquickenden.blog/2026/04/creating-custom-skills-in-cowork/"
  - "https://blog.ciaops.com/2026/04/24/3-ready-to-use-copilot-cowork-skill-md-examples-for-msps/"
  - "https://www.agensi.io/learn/how-to-use-skill-md-in-vscode"
  - "https://medium.com/@mpholoane/agent-skills-in-github-copilot-for-visual-studio-2026-stop-repeating-yourself-d0b5a0209f48"
  - "https://visualstudiomagazine.com/articles/2026/01/11/hand-on-with-new-github-copilot-agent-skills-in-vs-code.aspx"
accessed: 2026-04-30
status: raw-notes
tags: [agent-skills, microsoft-copilot, copilot-cowork, vscode, m365]
---

# Microsoft Copilot SKILL.md Support — 2026 Roadmap and Current State

## Source Identity

Multiple Microsoft and community sources describe SKILL.md support across the Microsoft Copilot family: GitHub Copilot in VS Code, Visual Studio 2026, Copilot Cowork (Microsoft 365), Copilot Studio, and the Microsoft Agent Framework.

## Relevant Extracted Facts

### GitHub Copilot in VS Code (Dev Tools)
- VS Code added Agent Skills support through GitHub Copilot's agent mode, reaching full support around April 2026.
- Started as experimental in January 2026, now a standard feature.
- Project skills: `.github/skills/`, `.claude/skills/`, `.agents/skills/`.
- Personal skills: `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/`.
- Additional paths configurable via `chat.agentSkillsLocations` setting.
- Skills also work as slash commands (`/skill-name`).
- VS Code extensions can contribute skills through the `chatSkills` contribution point.
- The Copilot SDK supports custom skills programmatically for enterprise integration.

### Visual Studio 2026 (Full IDE)
- March 2026 update added custom agents with skill support.
- SKILL.md files are natively recognized and can be authored within the environment.
- Agent Skills enable reusable, specialized actions (debugging, refactoring, etc.).

### Copilot Cowork (Microsoft 365 / Productivity)
- Copilot Cowork is a 2026 feature for collaborative work with custom skill support.
- Skills stored as `SKILL.md` files in OneDrive: `/Documents/Cowork/Skills/<skill-name>/SKILL.md`
- SharePoint integration: skills saved in site's Agent Assets library at `/Agent Assets/Skills/<skill-name>/SKILL.md`
- Auto-detection: Cowork picks up new skills automatically — no manual configuration needed.
- Skills are shareable across teams via SharePoint/OneDrive.
- Publicly available as of April 2026.

### Copilot Studio
- Supports skills for specialized agent actions: booking appointments, sending confirmation emails, managing tasks.
- Skills are used within custom agents built through Agent Builder and Copilot Studio.
- [Use skills in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-skills)

### Microsoft Agent Framework (SDK)
- Skills provider discovers `SKILL.md` files from configured filesystem directories.
- Searches up to two levels deep recursively.
- Exposes tools: `load_skill`, `read_skill_resource`, `run_skill_script`.
- SDK packages available: core registry/validation, filesystem/HTTP providers, LangChain integration, MCP server.

### SKILL.md File Format (Microsoft Products)
- Markdown file with YAML frontmatter.
- Required fields: `name`, `description`.
- Optional fields vary by product: `argument-hint`, `user-invocable`, `disable-model-invocation`.
- Can bundle scripts, templates, and reference documentation alongside the markdown file.

## Timeline (2026)

| Date | Milestone |
|------|-----------|
| January 2026 | Copilot Studio skills updates; VS Code Agent Skills experimental |
| February 2026 | VS Code Agent Skills preview; `/skills` command for auto-generation |
| March 2026 | Visual Studio March Update: custom agents with skills |
| April 2026 | Full SKILL.md support in VS Code; Copilot Cowork skills GA |

## Ecosystem Context

- SKILL.md is now an open standard supported by 16+ AI tools including Claude Code, Cursor, Codex, Gemini CLI, OpenCode, OpenClaw, Windsurf, and GitHub Copilot.
- Microsoft maintains the `github/awesome-copilot` repository with skill templates including `skills/microsoft-skill-creator/SKILL.md`.
- Microsoft's own Agent Framework is a framework consumer (builds agents that use skills) rather than a standalone coding client.

## Tool Support Evidence

Primary evidence from Microsoft Learn, VS Code docs, GitHub Docs, and multiple community sources confirms SKILL.md support across:
1. **GitHub Copilot** (VS Code, Visual Studio 2026, CLI, cloud agent)
2. **Copilot Cowork** (Microsoft 365 — OneDrive/SharePoint-based custom skills)
3. **Copilot Studio** (custom agent skills for business workflows)
4. **Microsoft Agent Framework** (SDK-based skill provider for agent development)

## Open Questions

- Organization and enterprise skill distribution for GitHub Copilot remains "planned but not yet available."
- Copilot Cowork skill governance (versioning, conflict resolution) is not yet well-documented.
- Cross-product skill portability (e.g., can a dev SKILL.md work in Cowork?) is unclear.
