---
type: source-summary
created: 2026-05-10
updated: 2026-05-23
status: active
sources:
  - "raw/Indirect Prompt Injection Attacks Hidden AI Risks.md"
tags: [prompt-injection, security, indirect-injection, shadow-ai]
---

# Indirect Prompt Injection Attacks (CrowdStrike)

**Source**: [CrowdStrike blog](https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/)
**Author**: John Gamble
**Published**: 2025-12-04
**Created**: 2026-05-10

## Summary

CrowdStrike analysis of indirect prompt injection attacks — where attackers embed malicious instructions in external content that AI systems access (documents, emails, webpages). OWASP 2025 ranks prompt injection as #1 risk. CrowdStrike has analyzed 300,000+ adversarial prompts and tracks 150+ prompt injection techniques.

## Key Points

- **Two types**: Direct (adversarial prompt to AI tool) vs Indirect (embedded in data sources AI accesses — email signatures, document metadata, webpage content, image files, database records).
- **Deployment patterns**: Targeted (webpages likely visited by specific company employees) or broad (hidden in industry research reports). Users likely never see the malicious prompt.
- **Shadow AI problem**: 45% of employees use AI tools (email clients, document processors, code assistants) without IT's knowledge. Approved and unknown AI tools crawl web and internal resources indiscriminately.
- **Real-world examples**: Job applicant manipulated AI hiring platform with 120+ lines of hidden code in a headshot photo file. Employee embedded prompt injection in LinkedIn bio instructing AI recruiting systems to share flan recipe (and one did).
- **Attack capabilities**: Data exfiltration, business process manipulation, reconnaissance, lateral movement within enterprise environments.
- **Defense layers**: (1) Prompt injection detection systems, (2) input validation/sanitization, (3) content security policies with allowlisting, (4) privilege separation for enterprise AI tools, (5) AI use monitoring and access control, (6) user education.

## Evidence

The source-summary claims above are grounded in the local raw source file listed in frontmatter.

## Connections

- [[concepts/Skill Governance and Metrics]] — Trust and audit concerns for third-party skills.
- [[concepts/Context Observability and Feedback]] — Context filters as WAF for prompt injections.
- [[Skill Security and Supply Chain Risk]] — Broader skill-specific security landscape including ToxicSkills research.
