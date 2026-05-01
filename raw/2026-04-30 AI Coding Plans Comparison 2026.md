---
type: raw-source
created: 2026-04-30
sources:
  - "https://zhuanlan.zhihu.com/p/2015468530938693485"
  - "https://www.cnblogs.com/wzxNote/p/19648084"
  - "https://www.kimi.com/code/zh"
  - "https://www.byteplus.com/en/activity/codingplan"
  - "https://post.smzdm.com/p/arz4o22g"
  - "https://gist.github.com/junbaor/06b01602889ea72d9159a6d6133c1522"
  - "https://kilo.ai/"
  - "https://vibecoding.app/blog/kilo-code-review"
  - "https://ijonis.com/en/ai-coding-tools-pricing"
  - "https://qoder.com/pricing"
  - "https://docs.qoder.com/events/pricing-adjustment-notice"
  - "https://www.augmentcode.com/pricing"
  - "https://devin.ai/pricing/"
  - "https://replit.com/pricing"
  - "https://github.com/features/copilot/plans"
  - "https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/"
  - "https://roocode.com/"
  - "https://roocode.com/blog/sunsetting-roo-code-extension-cloud-and-router"
  - "https://www.reddit.com/r/LocalLLaMA/comments/1ss1ls9/roo_code_hit_3_million_installs_were_shutting_it/"
  - "https://cline.bot/pricing"
tags: [coding-plan, ai-coding, subscription, comparison, kimi, byteplus, alibaba, kilo, cursor, copilot, claude-code]
---

# AI Coding Plans Comparison 2026

## Definition

"Coding Plan" refers to subscription packages specifically designed for AI-powered coding workflows. Two distinct categories exist:
1. **Model-provider coding plans** — fixed-quota API access to multiple AI models for use with coding agents (Chinese market origin: Alibaba 百炼, BytePlus ModelArk, Kimi Code, etc.)
2. **Coding-tool subscriptions** — direct subscriptions to AI coding products (Cursor, GitHub Copilot, Claude Code, Kilo Code)

## Chinese Model-Provider Coding Plans

These plans provide API access to frontier models at fixed monthly rates, designed to work with Cursor, Claude Code, Cline, OpenClaw, Qoder, and other agents.

### Alibaba Cloud Model Studio (百炼)
- **Pricing**: ¥40/month (~$5.50), intro ~¥7.90 first month
- **Quotas**: 1,200 calls/5h, 9,000/week, 18,000/month
- **Models**: Qwen3.5-Plus, Qwen3-Coder-Next, GLM-4.7, Kimi-K2.5
- **Compatible tools**: Claude Code, Cline, OpenClaw, and 4+ environments
- **Pros**: Reliable cloud infrastructure, diverse model selection
- **Cons**: Primary account only, no refunds, incomplete setup docs

### BytePlus ModelArk
- **Pricing**: ¥40/month (~$5.50), intro ~¥8.91 first month
- **Quotas**: Same as Alibaba (1,200/5h, 9,000/week, 18,000/month)
- **Models**: Doubao, DeepSeek, GLM, Kimi variants; Auto intelligent routing
- **Compatible tools**: Claude Code, Cursor, Cline, and 7+ editors
- **Pros**: Widest model catalog, simple two-step configuration
- **Cons**: Server overbooking causes 400/429 timeouts during peak hours, rigid refund terms

### Kimi Code (Moonshot AI)
- **Pricing**: ¥49/month (Andante tier)
- **Quotas**: Token-based billing, currently 3x temporary allowance
- **Models**: Kimi K2.5 / K2.6 (proprietary), 256K context, native multimodal
- **Compatible tools**: 3-4 official clients only
- **Pros**: Excels at visual programming (design-to-code), long-context analysis
- **Cons**: Personal use only, unauthorized clients risk account suspension

### Zhipu GLM
- **Pricing**: ¥49/month flat (intro discounts removed)
- **Quotas**: 80 prompts/5h, 400/week, no monthly ceiling
- **Models**: GLM-4.7 full lineup, GLM-5 (premium, 2-3x consumption during peak)
- **Compatible tools**: 20+ applications
- **Pros**: Strong open-source reputation, widest tool integration
- **Cons**: Weekly caps for new accounts, price increases reduced value

### MiniMax
- **Pricing**: ¥29/month standard, intro ~¥9.90
- **Quotas**: 40 prompts/5h refresh, no weekly/monthly ceiling
- **Models**: M2.5 frameworks (lightweight, high-speed variant)
- **Compatible tools**: 2 primary assistants
- **Pros**: Fast response (100+ TPS), good for lightweight scripting
- **Cons**: Smaller models unsuitable for heavy computational workloads

### Infini (无问芯穹)
- **Pricing**: ¥19.90/month flat
- **Quotas**: 1,000 calls/5h window
- **Models**: Aggregates DeepSeek, GLM, Kimi, MiniMax
- **Compatible tools**: 4 mainstream environments
- **Pros**: Lowest entry cost, solid budget efficiency
- **Cons**: Lower brand visibility, slower update cycles

## International Coding-Tool Subscriptions

These are direct subscriptions to AI coding products rather than API quotas.

### GitHub Copilot
- **Pricing**:
  - Copilot Free: $0 (2,000 code completions/month)
  - Copilot Pro: $10/month (unlimited completions, 300 premium requests/month)
  - Copilot Pro+: $39/month (unlimited completions, 1,500 premium requests/month)
  - Copilot Business: $19/user/month (org policies, centralized billing)
  - Copilot Enterprise: $39/user/month (knowledge base, custom models, advanced admin)
- **Type**: AI plugin (VS Code, JetBrains, Neovim, GitHub cloud agent)
- **SWE-bench**: 56%
- **2026 Changes**:
  - April 20, 2026: New sign-ups paused for Pro, Pro+, Student plans
  - June 1, 2026: Transition to usage-based billing announced
  - Student plan paused for new sign-ups
- **Best for**: Budget-conscious developers, multi-IDE use, GitHub-native workflow

### Cursor
- **Pricing**: $20/month (Pro), $40/month (Business)
- **Type**: AI-native IDE (fork of VS Code)
- **SWE-bench**: 52%
- **Best for**: Speed — completes tasks ~30% faster than competitors

### Claude Code
- **Pricing**: $20/month (Pro), usage-based API option also available
- **Type**: Terminal-native coding agent
- **Best for**: Agentic terminal workflow, complex reasoning with Opus

### Qoder
- **Pricing**:
  - Free: $0 (2-week Pro trial, 300 Credits)
  - Pro: $20/month ($17/mo annual) — 2,000 Credits
  - Pro+: $60/month — 6,000 Credits
  - Ultra: $200/month
  - Teams: $30/seat/month — 2,000 Credits/seat (changing to 3,000/seat after April 30, 2026)
- **Type**: Agentic coding platform (IDE + agent)
- **2026 Changes**:
  - April 30, 2026: All promotional discounts end (50% off Individual plans, 50% off Credits packs)
  - June 1, 2026: Monthly Pro/Pro+ users auto-migrate to usage-based billing
  - Teams plan: Credits per seat increasing to 3,000
- **Best for**: Teams wanting agentic coding with premium model access (includes Claude Code equivalent resources)

### Augment Code
- **Pricing**:
  - Indie: $20/month — 40,000 credits, 1 user
  - Standard: $60/month per dev — 130,000 pooled credits/seat (up to 20 users)
  - Max: $200/month per dev — 450,000 pooled credits (up to 20 users)
  - Enterprise: Custom pricing
- **Type**: AI coding assistant with Context Engine and MCP tools
- **Features**: SOC 2 Type II, Context Engine for codebase awareness, MCP tool integration
- **Best for**: Teams needing context-aware coding assistance with pooled credit sharing

### Devin (Cognition AI)
- **Pricing**:
  - Free: $0 (limited usage, Devin Review, DeepWiki)
  - Pro: $20/month (Devin usage quota, Windsurf IDE access)
  - Team/Enterprise: Custom pricing (originally $500/month, dramatically reduced)
- **Type**: Autonomous AI coding agent
- **Best for**: Developers wanting a fully autonomous agent that can handle end-to-end tasks

### Replit Agent
- **Pricing**:
  - Starter: Free (limited AI)
  - Core: $25/month ($20/month annual) — includes Replit Agent access, $20-25 monthly AI credits
  - Pro: $100/month — tiered AI credits for heavy usage
  - Teams: $40/month
- **Type**: Cloud-based IDE + autonomous agent
- **Best for**: Cloud-native development, quick prototyping, zero-setup environments

### Kilo Code
- **Pricing**: $49/month (KiloClaw cloud), free/open-source for self-hosted
- **Type**: Open-source AI coding agent for VS Code
- **Models**: 500+ model support
- **Best for**: Open-source advocates, self-hosted deployments

### Roo Code (sunsetting May 15, 2026)
- **Status**: Shutting down VS Code extension, cloud, and router services on May 15, 2026
- **Background**: Hit 3 million installs before announcing pivot to Roomote (autonomous agent for Slack/GitHub/Linear)
- **Team's rationale**: "IDE era is over" — shifting to cloud-based autonomous agent workflows
- **Community reaction**: Disappointment; developers seeking alternatives (Claude Code, Copilot, Cline)
- ~~**Pricing**: Free extension, Pro/Team up to $249/month for Roo Cloud~~
- ~~**Best for**: Full automation advocates, aggressive MCP users~~

### Cline
- **Pricing**:
  - Free: Free for individual developers
  - No subscriptions — purely pay-as-you-go for LLM API usage
- **Type**: VS Code extension
- **Model access**: Bring-your-own-API-key (BYOK)
- **Features**: File editing, terminal commands, headless browser, MCP tools
- **Best for**: Safety-first autonomy, developers who want full control over model choice and cost

## Selection Guidance

| Scenario | Recommended |
|---|---|
| Budget entry (Chinese plans) | Infini ($3/mo) or MiniMax ($4/mo) |
| Multi-model switching (Chinese plans) | BytePlus ModelArk ($6/mo, 7+ editors) or Alibaba ($6/mo, reliable infra) |
| Visual programming | Kimi Code (design-to-code, multimodal) |
| Tool compatibility breadth | Zhipu GLM (20+ apps) |
| Budget international tool | GitHub Copilot Free or Pro ($10/mo) |
| Speed / task completion | Cursor ($20/mo) |
| Agentic terminal workflow | Claude Code ($20/mo) |
| Full agent autonomy | Devin ($20/mo Pro) or Replit Agent ($25/mo Core) |
| Open-source / self-hosted | Kilo Code (free), Roo Code (free), or Cline (free) |
| BYOK with full control | Cline (Roo Code sunsetting May 15, 2026) |
| Cloud-native zero-setup | Replit ($25/mo Core) |
| Team pooled credits | Augment Code Standard ($60/dev/mo, 130K pooled) |
| Agentic platform with teams | Qoder Teams ($30/seat/mo) |
| Enterprise knowledge base | GitHub Copilot Enterprise ($39/user/mo) |

## Key Market Trends

- Shift from per-token billing to fixed monthly subscription quotas
- Chinese providers focus on model aggregation (multiple models in one plan)
- International tools compete on IDE experience and agent capability
- Cross-compatibility: Chinese coding plans can power international tools (Cursor, Claude Code, Cline) via OpenAI-compatible API endpoints
- Intro pricing heavily discounted (70-80% off first month) across Chinese providers
- **2026 billing shift**: GitHub Copilot and Qoder both moving to usage-based billing (June 1, 2026)
- **Pricing wars**: Devin slashed from $500/month to $20/month Pro plan
- **BYOK emergence**: Cline and Roo Code lead the "free extension + your own API key" model
- **Credit system standardization**: Augment Code, Qoder use pooled credits; Chinese plans use API-call quotas
- **Free tier competition**: Copilot Free, Devin Free, Roo Code free, Cline free — pressure on paid tiers to differentiate
- **Agent autonomy spectrum**: From inline suggestions (Copilot) to full autonomy (Devin, Replit Agent)
- **Roo Code sunset**: Announced April 2026, shutting down VS Code extension/cloud/router on May 15, 2026 — team pivoting to Roomote (Slack/GitHub/Linear autonomous agent), declaring "IDE era is over"
