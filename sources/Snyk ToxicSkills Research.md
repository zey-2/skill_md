---
type: source-summary
created: 2026-05-10
updated: 2026-05-23
status: active
sources:
  - "raw/Snyk Finds Prompt Injection in 36%, 1467 Malicious Payloads in a ToxicSkills Study of Agent Skills Supply Chain Compromise.md"
tags: [skill-security, supply-chain, malware, prompt-injection, toxic-skills]
---

# Snyk ToxicSkills Research

**Source**: [Snyk blog](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)
**Authors**: Luca Beurer-Kellner, Aleksei Kudrinskii, Marco Milanta, Kristian Bonde Nielsen, Hemang Sarkar, Liran Tal
**Published**: 2026-02-05
**Created**: 2026-05-10

## Summary

First comprehensive security audit of the Agent Skills ecosystem. Snyk scanned 3,984 skills from ClawHub and skills.sh, finding 36.82% contain at least one security flaw and 76 confirmed malicious payloads. The research establishes a threat taxonomy for skill-specific attacks including prompt injection convergence with traditional malware.

## Key Points

- **13.4% critical**: 534 of 3,984 skills contain at least one critical-level security issue
- **36.82% any flaw**: 1,467 skills affected (hardcoded API keys, insecure credential handling, dangerous third-party content exposure)
- **76 confirmed malicious payloads**: credential theft, backdoor installation, data exfiltration. 8 remained live on ClawHub at publication.
- **91% of malicious skills combine prompt injection + traditional malware** — a convergence that bypasses both AI safety mechanisms and traditional security tools.
- **Skill permissions**: When installed, skills inherit shell access, read/write filesystem, credential access (env vars, configs), messaging capabilities (email, Slack, WhatsApp), and persistent memory across sessions.
- **Publishing barrier**: A `SKILL.md` file and a GitHub account that's one week old. No code signing, no security review, no sandbox by default.

## Attack Techniques Observed

1. **External malware distribution**: Skills link to password-protected ZIP files containing malware
2. **Obfuscated data exfiltration**: Base64-encoded commands that steal AWS credentials
3. **Security disablement**: Instructions to disable safety measures, add persistent backdoors, DAN-style jailbreaks

## ToxicSkills Threat Taxonomy (8 policies)

| Category | Risk | Key Pattern |
|---|---|---|
| Prompt injection | CRITICAL | Base64 obfuscation, Unicode smuggling, "ignore previous instructions" |
| Malicious code | CRITICAL | Backdoors, RCE, supply-chain attacks, credential theft |
| Suspicious downloads | CRITICAL | Unknown domains, password-protected ZIPs, GitHub releases |
| Credential handling | HIGH | Echo/print API keys, embed credentials in commands |
| Secret detection | HIGH | Hardcoded secrets, API keys in skill prompts |
| Third-party content | MEDIUM | Web fetching, social media parsing, external repo cloning |
| Unverifiable dependencies | MEDIUM | `curl | bash` patterns, dynamic imports, remote instruction loading |
| Direct money access | MEDIUM | Financial accounts, trading platforms, crypto operations |

## Comparison to Package Ecosystems

Agent Skills parallels early npm/PyPI security but is worse in key ways:
- Higher privilege by default (full agent permissions)
- Prompt injection has no analog in traditional packages
- Persistence through memory (malicious skills can modify agent behavior permanently)

## Identified Threat Actors

- `zaycv`: 40+ skills following identical programmatic malware pattern
- `Aslaep123`: Multiple malicious skills targeting crypto/trading
- `aztr0nutzs`: Ready-to-deploy malicious skills on GitHub (not yet on ClawHub)

## Defense Recommendations

1. Audit installed skills: `uvx mcp-scan@latest --skills`
2. Rotate credentials if installed skills handled API keys or cloud credentials
3. Review memory files (`SOUL.md`, `MEMORY.md`) for unauthorized modifications
4. Skills that fetch untrusted content create indirect prompt injection vectors even when skill author had benign intent

## Evidence

The source-summary claims above are grounded in the cited Snyk blog and the local raw source file listed in frontmatter.

## Connections

- [[concepts/Skill Security and Supply Chain Risk]] — This source is the primary evidence for the dedicated concept page.
- [[concepts/Skill Governance and Metrics]] — Trust and audit requirements, curation vs audit distinction.
- [[sources/Indirect Prompt Injection Attacks (CrowdStrike)]] — Third-party content exposure becomes an indirect injection vector.
- [[concepts/MCP and Tool-Integration Architecture]] — mcp-scan detects both MCP server and Agent Skills security issues.
