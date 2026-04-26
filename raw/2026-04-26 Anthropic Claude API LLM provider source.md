# Anthropic Claude API LLM provider source

Captured: 2026-04-26

Primary source:

- Claude models overview: https://platform.claude.com/docs/en/about-claude/models/overview

## Source Summary

Anthropic is a direct frontier-model API provider centered on the Claude model family. The current models overview recommends Claude Opus 4.7 for the most complex tasks and describes it as the most capable generally available model, with a major improvement in agentic coding over Opus 4.6. The source also says current Claude models support text and image input, text output, multilingual capability, and vision.

For powering AI tools, Anthropic is especially relevant for agentic coding, long-context reasoning, careful writing, and enterprise-friendly model access through multiple platforms.

## Provider Notes

- Current models in the comparison include Claude Opus 4.7, Claude Sonnet 4.6, and Claude Haiku 4.5.
- The model overview lists Claude availability through the Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry.
- Claude Opus 4.7 and Sonnet 4.6 are presented with 1M-token context windows; Haiku 4.5 is listed with a 200k-token context window.
- The docs distinguish snapshot model IDs and aliases, which matters for reproducibility.
- Anthropic notes endpoint differences across third-party platforms such as AWS Bedrock and Google Vertex AI.

## AI Tool Fit

- Strong candidate for AI tools involving software engineering, complex reasoning, long documents, and high-quality natural language.
- Useful when the same Claude model family must be accessed directly or through Bedrock, Vertex AI, or Microsoft Foundry.
- Worth benchmarking against OpenAI and Gemini for tool calling, structured outputs, latency, and cost.

## Open Questions

- Check account access, regional availability, and output-token limits for the chosen platform before implementation.
- Use pinned model IDs for reproducibility; aliases are convenient but may shift behavior over time.
