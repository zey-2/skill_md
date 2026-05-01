---
type: raw-source
created: 2026-04-30
sources:
  - "https://openrouter.ai/docs/guides/coding-agents/claude-code-integration"
  - "https://code.claude.com/docs/en/llm-gateway"
  - "https://code.claude.com/docs/en/model-config"
  - "https://code.claude.com/docs/en/third-party-integrations"
tags: [claude-code, third-party-providers, openrouter, llm-gateway, vs-code]
---

# Claude Code Third-Party LLM Provider Configuration

## Core Mechanism

Claude Code supports third-party LLM providers through environment variable overrides that redirect its API calls. Any gateway or provider that exposes an Anthropic Messages-compatible API (`/v1/messages`, `/v1/messages/count_tokens`) can serve as a backend.

## Key Environment Variables

| Variable | Purpose |
|---|---|
| `ANTHROPIC_BASE_URL` | Override the API endpoint (default: `https://api.anthropic.com`) |
| `ANTHROPIC_AUTH_TOKEN` | API key or token for authentication |
| `ANTHROPIC_API_KEY` | Standard Anthropic API key; must be cleared (`""`) when using third-party providers |
| `ANTHROPIC_MODEL` | Force a specific model at startup |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Model for subagent workloads |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | What the `opus` alias resolves to |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | What the `sonnet` alias resolves to |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | What the `haiku` alias resolves to |

## OpenRouter Configuration

OpenRouter is the most popular third-party provider for Claude Code, offering 320+ models including free tiers.

```bash
# Redirect to OpenRouter
export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"
export ANTHROPIC_AUTH_TOKEN="sk-or-<your-openrouter-api-key>"
export ANTHROPIC_API_KEY=""
```

Model routing for specific task tiers:

```bash
export ANTHROPIC_DEFAULT_SONNET_MODEL="anthropic/claude-sonnet-4.6"
export ANTHROPIC_DEFAULT_OPUS_MODEL="anthropic/claude-opus-4.7"
export CLAUDE_CODE_SUBAGENT_MODEL="anthropic/claude-opus-4.7"
```

Fast mode shortcut: `export CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK=1`

Verification: launch Claude Code and run `/status` to confirm the base URL matches the configured provider.

## LiteLLM Gateway Configuration

LiteLLM Proxy Server can serve as an LLM gateway with load balancing and fallbacks.

### Anthropic Messages format (unified endpoint)

```bash
export ANTHROPIC_BASE_URL="https://litellm-server:4000"
export ANTHROPIC_AUTH_TOKEN="sk-litellm-static-key"
```

### Bedrock through LiteLLM

```bash
export ANTHROPIC_BEDROCK_BASE_URL="https://litellm-server:4000/bedrock"
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1
```

### Vertex AI through LiteLLM

```bash
export ANTHROPIC_VERTEX_BASE_URL="https://litellm-server:4000/vertex_ai/v1"
export ANTHROPIC_VERTEX_PROJECT_ID="your-gcp-project-id"
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION="us-east5"
```

## API Format Requirements

For a gateway to work with Claude Code, it must expose at least one of these API formats:

1. **Anthropic Messages**: `/v1/messages`, `/v1/messages/count_token` — must forward `anthropic-beta` and `anthropic-version` headers
2. **Bedrock InvokeModel**: `/invoke`, `/invoke-with-response-stream` — must preserve `anthropic_beta` and `anthropic_version` body fields
3. **Vertex rawPredict**: `:rawPredict`, `:streamRawPredict`, `/count-tokens:rawPredict` — must forward `anthropic-beta` and `anthropic-version` headers

When using Anthropic Messages format with Bedrock or Vertex, set `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` if needed.

## VS Code Integration

Claude Code in VS Code operates through the Claude Code extension. The same environment variables apply whether running from the integrated terminal or the extension's own agent surface. Configuration can also be set in `.claude/settings.local.json`:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://openrouter.ai/api/v1",
    "ANTHROPIC_AUTH_TOKEN": "sk-or-<your-key>",
    "ANTHROPIC_API_KEY": ""
  }
}
```

The VS Code extension also supports VS Code's Bring Your Own Key (BYOK) feature, which lets any model from a supported provider be used by bringing an API key.

## Cloud Provider Deployments

Claude Code supports direct deployment through these cloud providers:

| Provider | Enable Variable | Auth |
|---|---|---|
| Amazon Bedrock | `CLAUDE_CODE_USE_BEDROCK=1` | AWS credentials or API key |
| Google Vertex AI | `CLAUDE_CODE_USE_VERTEX=1` | GCP credentials |
| Microsoft Foundry | `CLAUDE_CODE_USE_FOUNDRY=1` | API key or Entra ID |

For corporate proxy routing, set `HTTPS_PROXY` or `HTTP_PROXY` environment variables.

## Custom Model Options

Add a custom entry to the `/model` picker:

```bash
export ANTHROPIC_CUSTOM_MODEL_OPTION="my-gateway/claude-opus-4-7"
export ANTHROPIC_CUSTOM_MODEL_OPTION_NAME="Opus via Gateway"
export ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION="Custom deployment routed through internal LLM gateway"
```

For third-party providers (Bedrock, Vertex, Foundry), pin model versions and declare capabilities:

```bash
export ANTHROPIC_DEFAULT_OPUS_MODEL="arn:aws:bedrock:us-east-1:123456789012:custom-model/abc"
export ANTHROPIC_DEFAULT_OPUS_MODEL_NAME="Opus via Bedrock"
export ANTHROPIC_DEFAULT_OPUS_MODEL_SUPPORTED_CAPABILITIES="effort,xhigh_effort,max_effort,thinking,adaptive_thinking,interleaved_thinking"
```

## Model Overrides

Route specific Anthropic model IDs to provider-specific endpoints via `modelOverrides` in settings:

```json
{
  "modelOverrides": {
    "claude-opus-4-7": "arn:aws:bedrock:us-east-2:123456789012:application-inference-profile/opus-prod",
    "claude-sonnet-4-6": "arn:aws:bedrock:us-east-2:123456789012:application-inference-profile/sonnet-prod"
  }
}
```

## Claude Code Router

The [claude-code-router](https://github.com/musistudio/claude-code-router) project provides infrastructure-level model routing, letting Claude Code act as the execution surface while a separate layer decides which model handles each task.
