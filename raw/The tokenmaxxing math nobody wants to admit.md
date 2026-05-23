---
title: "The tokenmaxxing math nobody wants to admit"
source: "Agentmail article text provided by user"
author:
  - "Agentmail"
published: unknown
created: 2026-05-23
description: "Agentmail article arguing that tokenmaxxing is useful only when measured against real outputs rather than raw token burn."
tags:
  - "clippings"
  - "tokenmaxxing"
  - "agent-metrics"
---

# The tokenmaxxing math nobody wants to admit

Do you believe less is more? Because right now, the people building the future of AI are betting hard that it isn't.

There's a competition happening at the forefront of AI building. The prize: who can burn the most tokens.

When Meta's internal leaderboard leaked, the internet finally had a name for the trend. Tokenmaxxing. Employees were ranked on a board called Claudeonomics, with titles like Token Legend and Session Immortal. The company burned through 60 trillion tokens in a single month, roughly 900 million dollars at Anthropic's API prices. Meta took it down once the press caught on. Amazon got caught running the same playbook with an internal agent called MeshClaw, where employees started inventing busywork to hit weekly targets. Google went the other direction and embraced it. At I/O, Sundar said Google now processes 3.2 quadrillion tokens a month and called the trend out by name.

So the real question is whether tokenmaxxing is a signal or a vanity metric.

The honest case for it: we're early. Nobody actually knows what a good agent workflow looks like yet. The only way to find one is to run a ton of experiments, and most of those experiments will look like waste from the outside. Reid Hoffman called token tracking "a good dashboard," meaning it tells you who is actually engaging with the tools versus who is pretending. Meta's CTO defended his top engineer for spending the equivalent of his salary in tokens, claiming a 10x productivity bump. Shopify's Mikhail Parakhin coined a softer version called tasteful tokenmaxxing, the idea that the good version is going deep with serial reasoning instead of spamming parallel agents at every problem.

That's the argument. Here's where it gets shaky.

Gaming. Amazon is the tell. Once a number becomes a target, people optimize for the number. Appian's Matt Calkins put the analogy on record: this is the Soviet practice of judging chandeliers by their weight. Factories ended up making chandeliers so heavy they pulled the ceilings down. The metric ate the goal.

Then there's the part most people miss. More tokens does not automatically mean a better agent. The opposite, often. Modern models with million-token context windows still lose more than half their accuracy once you cross roughly 100 thousand tokens of context. They forget. They contradict themselves. They drift. The agent world has a name for this now. Context rot. So past a certain point, you can spend more on your agent and get a worse result.

And the deepest one. A token is what an agent reads or writes. It is not what the agent did. An agent that burns billions of tokens with nothing to show for it has produced nothing. An agent that uses a few thousand to send the right message at the right time, and that message turns into a meeting or a payment or a reply, has produced something real. Tokens measure motion. They do not measure work.

So if tokens are the wrong scoreboard, what's the right one? The answer most people are arriving at is some version of outputs over tokens. The most work for the fewest tokens spent. This isn't an argument against burning tokens. If your agent torches a million tokens and produces something genuinely phenomenal, that's a win. Burn them. The problem isn't the spending. The problem is when the spending is the score. Tokens are the cost. Outputs are the value. The ratio is what matters.
