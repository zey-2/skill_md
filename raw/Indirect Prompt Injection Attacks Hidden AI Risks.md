---
title: "Indirect Prompt Injection Attacks: Hidden AI Risks"
source: "https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/"
author:
  - "[[John Gamble]]"
published: 2025-12-04
created: 2026-05-10
description: "Indirect prompt injection is a hidden threat to GenAI systems, allowing attackers to embed malicious instructions in content AI tools access. Learn how the risk works."
tags:
  - "clippings"
---
The rapid adoption of AI has introduced a new, semantic attack vector that many organizations are ill-prepared to defend against: prompt injection. While many security teams understand the threat of direct prompt injection attacks against AI agents developed by their organizations, another more subtle threat lurks in the shadows: indirect prompt injection attacks.

## Understanding Prompt Injection

Prompt injection is a new security challenge unique to large language models (LLMs) and AI agents. Recognized as the number one threat in the [OWASP 2025 Top 10 Risk & Mitigations for LLMs and Gen AI Apps](https://genai.owasp.org/llm-top-10/), prompt injection occurs when an attacker manipulates an AI tool's behavior by crafting malicious inputs to override the system's intended purpose or safety guardrails.

There are two basic types of prompt injection attacks:

1. **Direct prompt injection**: An attacker submits adversarial prompts directly to an AI tool.
2. **Indirect prompt injection**: An attacker embeds prompt injections in external content that a GenAI system may access, such as documents or emails.

CrowdStrike, via its acquisition of Pangea, has analyzed over 300,000 adversarial prompts and tracks over 150 prompt injection techniques, maintaining the industry’s most comprehensive taxonomy for this growing threat. In the AI era, the prompt layer must be monitored and defended like any other critical layer of the stack.

## Indirect Prompt Injection

Indirect prompt injection inserts malicious information into the data sources a GenAI system accesses. This may include text, code, emojis, images, and videos. An attacker might hide adversarial instructions in content such as:

- Email signatures or footers
- The metadata or hidden text of documents
- Webpage content
- Image files with embedded text instructions
- Database records

Indirect prompt injections can be deployed in targeted locations (e.g., on webpages likely to be visited by employees of a specific company, who may paste the malicious content into internal AI tools) or deployed broadly (e.g., hidden inside an industry research report) to reach multiple AI systems and targets simultaneously. End users of the AI tools targeted by indirect prompt injection will likely never see the malicious prompt, and the AI tool may even appear to function normally while subtly executing the attacker's hidden instructions in the background.

Prompt injection attacks can enable adversaries to exfiltrate sensitive data, manipulate business processes, and conduct reconnaissance. If they compromise agents that have access to sensitive tools and data, prompt injection attacks can even allow adversaries to execute specific attack techniques via agents such as lateral movement within enterprise environments.

## A Growing Blind Spot

Most security teams cannot imagine a world where IT tools roam the web, downloading every file they discover with little or no built-in malware detection capabilities. And yet, this is not unlike what happens on a daily basis at organizations where both approved and unknown AI tools continually and indiscriminately crawl the web and internal resources, ingesting text, files, and multimedia assets that could contain indirect prompt injections.

Employee BYO AI adoption trends expand this attack surface beyond internally developed AI tools. A recent study by Gusto shows that nearly half of employees surveyed ([45%](https://gusto.com/resources/articles/hr/team-management/ai-workplace-anxiety)) report using AI tools like email clients, document processors, and code assistants, without IT's knowledge. This has created a massive shadow AI visibility problem and an attack surface ripe for exploitation when these tools are reachable from the public internet and may have access to sensitive systems such as employee email inboxes.

Indirect prompt injection attacks are accessible to nation-states and individuals alike. A recent New York Times [article](https://www.nytimes.com/2025/10/07/business/ai-chatbot-prompts-resumes.html) reported on a job applicant who manipulated an AI hiring platform with an indirect prompt injection attack and who “wrote more than 120 lines of code to influence A.I. and hid it inside the file data for a headshot photo.”

In another example, an employee frustrated with recruitment spam [embedded an indirect prompt injection](https://www.fastcompany.com/91417981/how-one-worker-says-a-flan-recipe-exposed-an-ai-recruiter) in their LinkedIn bio instructing AI-enabled recruiting systems to share a recipe for flan in their outreach (and one did). While the latter example might elicit laughs, consider that these same AI-enabled HR tools may have the potential to leak employee contact information and calendar details and may also be able to autonomously send emails to internal employees.

## Defending Against Indirect Prompt Injection

Defending against indirect prompt injection attacks demands a multi-layered approach that addresses both technical controls and organizational processes to limit the size of the attack surface and detect and stop injection attacks. Organizations should implement:

1. **Prompt Injection Detection**: Deploy specialized prompt injection detection systems capable of identifying and blocking malicious prompts, both direct and indirect.
2. **Input Validation and Sanitization**: Implement robust filtering of AI system inputs and external data sources to limit the total addressable attack surface for indirect attack.
3. **Content Security Policies**: Establish clear policies about what types of content AI systems can process and from which sources. Implement allowlisting for trusted data sources and treat external content with appropriate suspicion.
4. **Privilege Separation**: AI tools that are enterprise-managed should have minimal access to sensitive data and limited capabilities to take actions. Separate the read and write permissions, and require explicit user confirmation for high-risk actions.
5. **AI Use Monitoring and Access Control**: Shadow AI exacerbates the attack surface for indirect prompt injection. Deploy solutions to illuminate employee AI tool use, and enforce governance policy and access controls to prevent unauthorized AI tool use.
6. **User Education**: Train employees to recognize risks associated with AI tool adoption, and establish clear policies about sanctioned versus unsanctioned AI applications.

The CrowdStrike Falcon® platform provides comprehensive protection against the threat of prompt injection, delivering [AI detection and response](https://www.crowdstrike.com/en-us/solutions/secure-your-ai/) (AIDR) that stops direct and indirect attacks with up to 99% efficacy at sub-30ms latency.<sup>1</sup>

#### Additional Resources

- *Learn to take control of the AI attack surface with AIDR [in a new CrowdCast](https://www.crowdstrike.com/en-us/resources/crowdcasts/securing-ai-era-with-pangea-crowdstrike-aidr/).*
- *Learn more about CrowdStrike innovations through the Falcon platform [Innovations Hub](https://www.crowdstrike.com/en-us/platform/quarterly-falcon-platform-release-highlights/).*

<sup>1</sup> Performance metrics are based on results from internal benchmark testing.

![](https://assets.crowdstrike.com/is/image/crowdstrikeinc/GTR26_Cover-Spread_Web?wid=2048&hei=1365&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0)

## CrowdStrike 2026 Global Threat Report

## CrowdStrike 2026 Global Threat Report

AI threats have reached a critical turning point. Access the definitive look at the cyber threat landscape.

[Download](https://www.crowdstrike.com/en-us/global-threat-report/)