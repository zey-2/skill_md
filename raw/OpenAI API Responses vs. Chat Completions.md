---
title: "OpenAI API: Responses vs. Chat Completions"
source: "https://simonwillison.net/2025/Mar/11/responses-vs-chat-completions/"
author:
  - "[[Simon Willison]]"
published:
created: 2026-05-01
description: "OpenAI released a bunch of new API platform features this morning under the headline \"New tools for building agents\" (their somewhat mushy interpretation of \"agents\" here is \"systems that independently …"
tags:
  - "clippings"
---
**[OpenAI API: Responses vs. Chat Completions](https://platform.openai.com/docs/guides/responses-vs-chat-completions)**. OpenAI released a bunch of new API platform features this morning under the headline " [New tools for building agents](https://openai.com/index/new-tools-for-building-agents/) " (their somewhat mushy interpretation of "agents" here is "systems that independently accomplish tasks on behalf of users").

A particularly significant change is the introduction of a new **Responses API**, which is a slightly different shape from the Chat Completions API that they've offered for the past couple of years and which others in the industry have widely cloned as an ad-hoc standard.

In [this guide](https://platform.openai.com/docs/guides/responses-vs-chat-completions) they illustrate the differences, with a reassuring note that:

> The Chat Completions API is an industry standard for building AI applications, and we intend to continue supporting this API indefinitely. We're introducing the Responses API to simplify workflows involving tool use, code execution, and state management. We believe this new API primitive will allow us to more effectively enhance the OpenAI platform into the future.

An API that *is* going away is the [Assistants API](https://platform.openai.com/docs/api-reference/assistants), a perpetual beta first launched at OpenAI DevDay in 2023. The new responses API solves effectively the same problems but better, and assistants will be sunset "in the first half of 2026".

The best illustration I've seen of the differences between the two is this [giant commit](https://github.com/openai/openai-python/commit/2954945ecc185259cfd7cd33c8cbc818a88e4e1b) to the `openai-python` GitHub repository updating ALL of the example code in one go.

The most important feature of the Responses API (a feature it shares with the old Assistants API) is that it can manage conversation state on the server for you. An oddity of the Chat Completions API is that you need to maintain your own records of the current conversation, sending back full copies of it with each new prompt. You end up making API calls that look like this (from [their examples](https://platform.openai.com/docs/guides/conversation-state?api-mode=chat&lang=javascript#manually-manage-conversation-state)):

```
{
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": "knock knock.",
        },
        {
            "role": "assistant",
            "content": "Who's there?",
        },
        {
            "role": "user",
            "content": "Orange."
        }
    ]
}
```

These can get long and unwieldy - especially when attachments such as images are involved - but the real challenge is when you start integrating tools: in a conversation with tool use you'll need to maintain that full state *and* drop messages in that show the output of the tools the model requested. It's not a trivial thing to work with.

The new Responses API continues to support this list of messages format, but you also get the option to outsource that to OpenAI entirely: you can add a new `"store": true` property and then in subsequent messages include a `"previous_response_id: response_id` key to continue that conversation.

This feels a whole lot more natural than the Assistants API, which required you to think in terms of [threads, messages and runs](https://platform.openai.com/docs/assistants/overview#objects) to achieve the same effect.

Also fun: the Response API [supports HTML form encoding](https://twitter.com/athyuttamre/status/1899541484308971822) now in addition to JSON:

```
curl https://api.openai.com/v1/responses \
  -u :$OPENAI_API_KEY \
  -d model="gpt-4o" \
  -d input="What is the capital of France?"
```

I found that in an excellent [Twitter thread](https://twitter.com/athyuttamre/status/1899541471532867821) providing background on the design decisions in the new API from OpenAI's Atty Eleti. Here's [a nitter link](https://nitter.net/athyuttamre/status/1899541471532867821) for people who don't have a Twitter account.

#### New built-in tools

A potentially more exciting change today is the introduction of default tools that you can request while using the new Responses API. There are three of these, all of which can be specified in the `"tools": [...]` array.

- `{"type": "web_search_preview"}` - the same search feature available through ChatGPT. The documentation doesn't clarify which underlying search engine is used - I initially assumed Bing, but the tool documentation links to this [Overview of OpenAI Crawlers](https://platform.openai.com/docs/bots) page so maybe it's entirely in-house now? Web search [is priced](https://platform.openai.com/docs/pricing#web-search) at between $25 and $50 per thousand queries depending on if you're using GPT-4o or GPT-4o mini and the configurable size of your "search context".
- `{"type": "file_search", "vector_store_ids": [...]}` provides integration with the latest version of their [file search](https://platform.openai.com/docs/guides/tools-file-search) vector store, mainly used for RAG. "Usage is priced⁠ at $2.50 per thousand queries and file storage at $0.10/GB/day, with the first GB free".
- `{"type": "computer_use_preview", "display_width": 1024, "display_height": 768, "environment": "browser"}` is the most surprising to me: it's tool access to the [Computer-Using Agent](https://openai.com/index/computer-using-agent/) system they built for their Operator product. This one is going to be *a lot* of fun to explore. The tool's documentation includes a warning [about prompt injection risks](https://platform.openai.com/docs/guides/tools-computer-use#beware-of-prompt-injections). Though on closer inspection I think this may work more like [Claude Computer Use](https://simonwillison.net/2024/Oct/22/computer-use/), where you have to [run the sandboxed environment yourself](https://platform.openai.com/docs/guides/tools-computer-use#setting-up-your-environment) rather than outsource that difficult part to them.

I'm still thinking through how to expose these new features in my [LLM](https://llm.datasette.io/) tool, which is made harder by the fact that a number of plugins now rely on the default OpenAI implementation from core, which is currently built on top of Chat Completions. I've been worrying for a while about the impact of our entire industry building clones of one proprietary API that might change in the future, I guess now we get to see how that shakes out!