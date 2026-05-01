---
type: synthesis
created: 2026-04-30
updated: 2026-04-30
status: active
sources:
  - "raw/2026-04-30 Claude Code Third-Party LLM Provider Configuration.md"
  - "raw/2026-04-26 Claude Code Agent Skills docs.md"
tags: [claude-code, third-party-providers, llm-gateway, vs-code, model-routing]
---

# Claude Code Third-Party Provider Configuration

## Summary

Claude Code can be configured to use third-party LLM providers instead of the official Anthropic API. The mechanism works by overriding environment variables that control the API endpoint, authentication, and model resolution. Any provider or gateway that exposes an Anthropic Messages-compatible API format can serve as a backend, including OpenRouter, LiteLLM, AWS Bedrock, Google Vertex AI, and Microsoft Foundry.

## Key Points

- Set `ANTHROPIC_BASE_URL` to the provider endpoint, `ANTHROPIC_AUTH_TOKEN` to the credential, and clear `ANTHROPIC_API_KEY` to prevent conflicts
- The gateway must forward `anthropic-beta` and `anthropic-version` headers for full functionality
- Model aliases (`opus`, `sonnet`, `haiku`) may resolve to outdated versions on third-party providers — pin them with `ANTHROPIC_DEFAULT_*_MODEL` variables
- Configuration works in both the Claude Code VS Code extension and terminal CLI via environment variables or `.claude/settings.local.json`
- Run `/status` in a session to verify the active base URL and model match expectations

## How It Works

Claude Code uses the Anthropic SDK internally, which respects standard environment variable overrides for the API base URL and authentication token. By redirecting `ANTHROPIC_BASE_URL` to a third-party endpoint and providing credentials through `ANTHROPIC_AUTH_TOKEN`, all API requests flow through the alternate provider instead of `api.anthropic.com`. The `ANTHROPIC_API_KEY` must be explicitly cleared to prevent conflicts.

The gateway must forward two critical request headers (`anthropic-beta` and `anthropic-version`) and preserve provider-specific body fields (`anthropic_beta`, `anthropic_version`) for full functionality.

## VS Code Integration

The Claude Code VS Code extension inherits the same environment variable configuration. When running from the VS Code integrated terminal, shell environment variables apply directly. For persistent per-project or per-user configuration, set the `env` block in `.claude/settings.local.json`:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://openrouter.ai/api/v1",
    "ANTHROPIC_AUTH_TOKEN": "sk-or-<your-key>",
    "ANTHROPIC_API_KEY": ""
  }
}
```

VS Code also supports its Bring Your Own Key (BYOK) feature, which provides an additional path to using models from supported providers through the editor's AI surface.

## Common Provider Patterns

### OpenRouter

The most widely adopted third-party option, offering 320+ models including free tiers. Configuration requires three environment variables: `ANTHROPIC_BASE_URL` pointed at OpenRouter, `ANTHROPIC_AUTH_TOKEN` with the OpenRouter API key, and `ANTHROPIC_API_KEY` cleared. Model routing can be further refined by setting `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, and `CLAUDE_CODE_SUBAGENT_MODEL` to specific OpenRouter model IDs.

### LiteLLM Gateway

LiteLLM Proxy Server provides a self-hosted gateway with load balancing, fallback routing, and usage tracking. Two endpoint patterns exist: the unified Anthropic format endpoint (recommended for load balancing and fallbacks) and provider-specific pass-through endpoints for Bedrock, Vertex AI, or direct Claude API routing.

### Cloud Providers

Amazon Bedrock, Google Vertex AI, and Microsoft Foundry each have dedicated enable flags (`CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, `CLAUDE_CODE_USE_FOUNDRY`) along with region, project, and credential variables. These are the recommended paths for enterprise deployments that need IAM integration, data residency control, and procurement alignment.

## Model Configuration for Third Parties

When using third-party providers, model aliases (`opus`, `sonnet`, `haiku`) may resolve to outdated or unavailable versions. Pin models using `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, and `ANTHROPIC_DEFAULT_HAIKU_MODEL` with provider-specific IDs (Bedrock ARNs, Vertex version names, Foundry deployment names).

For custom model entries not recognized by Claude Code, use `ANTHROPIC_CUSTOM_MODEL_OPTION` to add them to the `/model` picker. Declare supported capabilities with companion `_NAME`, `_DESCRIPTION`, and `_SUPPORTED_CAPABILITIES` variables so Claude Code enables features like effort levels, extended thinking, and adaptive reasoning.

The `modelOverrides` setting in the configuration file maps specific Anthropic model IDs to provider-specific endpoint strings, enabling per-version routing for governance, cost allocation, or regional compliance.

## Verification

Run `/status` within a Claude Code session to confirm the active base URL, model, and account information match the expected third-party provider configuration.

## Connections

- [[LLM Provider Selection for AI Tools]] describes the provider landscape that Claude Code can route through.
- [[Tools Supporting Agent Skills]] describes how Claude Code discovers and uses skill packages, which operate independently of the LLM provider layer.
- [[Agent SDKs and Codex Automation]] compares Claude Agent SDK and OpenAI equivalents as runtime surfaces around skill-guided agents.
- [[MCP and Tool-Integration Architecture]] explains how MCP servers integrate with Claude Code regardless of the underlying LLM provider.

## Open Questions

- Which specific models beyond Claude perform reliably through Claude Code when routed via OpenRouter or LiteLLM?
- How does prompt caching behavior differ across third-party providers compared to the direct Anthropic API?
- What is the performance overhead of gateway-layer routing versus direct provider connections?
