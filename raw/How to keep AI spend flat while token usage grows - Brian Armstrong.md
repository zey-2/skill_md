Source: X post by @brian_armstrong (Coinbase CEO)
URL: https://x.com/brian_armstrong/status/2070670644577280109?s=20
Date: 2026-06-27
Followers/views: 3.8M views

---

How to keep AI spend flat while token usage grows exponentially: Not with friction and spend alerts. With better defaults, routing, and caching.

Better Defaults (not Usage Caps) – Engineers can choose any model they want, but defaults matter. We're experimenting with defaulting to open weight models like GLM 5.2 and Kimi 2.7 through our LLM gateway, while still encouraging engineers to choose the right model for the task. 91% of our employees were never hitting their usage caps, so instead of lowering caps and driving up alerts, we're moving to cheaper defaults. Note that code reviews use a diversity of models, so they can check each other's work.

Better Routing – In our custom harnesses, we preprocess prompts and route to the best model for the job, considering cache hits and model pricing. For instance, you may want a frontier model for planning, but not for execution where they can be overkill. Ultimately, humans shouldn't be choosing models - AI can automate this task.

Better Caching – Cache misses are the easiest way to drive your cost up. All of our requests are cache aware, so we're reusing a warm cache wherever possible. For example, our cache hit rate went from 5% → 60% in LibreChat once properly implemented.

Keep Context Lean – Start fresh sessions when switching tasks. Scope file context narrowly. Disconnect unused tools. Don't just compact. The goal isn't fewer tokens used, it's fewer tokens wasted.

Better Visibility – Our engineers can use as many tokens as they want, from whatever model they want, but we've made usage visible – and the more you spend on AI, the more impact we expect.

The goal isn't to suppress usage. It's to build the infrastructure that makes exponential growth sustainable.

Putting this into practice has cut our AI spend nearly in half, while our token usage continues to grow.
