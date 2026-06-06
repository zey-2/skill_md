---
title: "How Anthropic Engineers ACTUALLY Prompt Claude Code"
source: "https://www.youtube.com/watch?v=qOvc9IUKEIc"
author:
  - "[[Austin Marchese]]"
published: 2026-05-16
created: 2026-06-06
description: "Get my free 5-day AI playbook (what I used to build a $25M+ startup): https://the-ai-playbook.com/4rulesIn this video, I break down 4 rules I uncovered from studying how Anthropic's own engineers AC"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=qOvc9IUKEIc)

Get my free 5-day AI playbook (what I used to build a $25M+ startup): https://the-ai-playbook.com/4rules  
  
In this video, I break down 4 rules I uncovered from studying how Anthropic's own engineers ACTUALLY prompt Claude Code. Almost everyone is doing it wrong, and once you see these rules, you can't unsee them. No technical experience required, and they apply to any project you're working on.  
  
Timestamps:  
(0:00) - How Anthropic Engineers ACTUALLY Prompt Claude Code  
(0:18) - Rule #1: Prompt Skills, Not Claude  
(2:05) - Rule #2: Skills Are More Than Prompts  
(4:36) - Rule #3: Build Composable Skills, Not Custom Skills  
(6:30) - Pattern #1: Save Scripts Inside Skills  
(7:35) - Pattern #2: Control Who Invokes What  
(8:51) - Rule #4: Skills Get Smarter Every Session  
  
\--------  
FOR INDIVIDUALS:  
\- Free 5-day AI playbook (what I used to build a $25M+ startup): https://the-ai-playbook.com/4rules  
\- Use BuildPartner to build 10x faster with Claude Code (try free): https://buildpartner.ai/4rules  
  
FOR BUSINESSES, Ways to work with me:  
\- Want AI systems built into your operations? https://theincubator.xyz/ops/4rules  
\- Want to build a SaaS product without hiring a CTO? https://www.theincubator.xyz/eng/4rules  
\--------  
  
If you're new here, I'm Austin Marchese. How I got here...  
16: First business (SAT Math Tutor)  
22: Graduated Stevens Tech, 4.0, College Basketball, software engineering job at JPM  
23: Bitcoin ATM company + building algorithms for a professional gambler (fun story)  
24: Started creating content, grew 100k+ followers, built first agency, The Incubator  
25: Scaled agency to 15+ team members, $75K/M while working full time  
26: Quit my job, joined a startup called IYK  
27: Became COO of a $25M+ tech startup, worked with Ed Sheeran, Chance the Rapper and more  
28: Built a $20M+ real estate portfolio in the background  
29: Transitioned from IYK, re-launched The Incubator, grew it to a 6-figure biz in 30 days. Now building BuildPartner.ai  
  
To everyone who's spending time learning and putting the work in, cheers. Anyone can make comments from the sidelines but not everyone can build...  
  
\- Austin  
  
Follow/Subscribe  
  
\- Instagram: https://www.instagram.com/austin.marchese/  
\- Youtube: https://www.youtube.com/@austin.marchese

## Transcript

### How Anthropic Engineers ACTUALLY Prompt Claude Code

**0:00** · I listened to Anthropic's engineers at the AI Code Summit and I learned something I wasn't expecting. Almost everyone is prompting Claude code wrong.

**0:07** · So, I decided to dig deeper and after studying everything Anthropic engineers have published, I uncovered four rules for how they actually prompt Claude code. And it turns out you don't need any technical experience to implement these rules. So, rule number one is they prompt skills, not Claude. Before we get to the rules that will transform how you work, we need to understand the foundation of how they use Claude.

### Rule #1: Prompt Skills, Not Claude

**0:26** · Generally, when people first start using AI, they start writing new prompts for everything they do. But, the reality is most of what people do is repetitive tasks. So, Anthropic engineers created Claude skills to help tackle these repetitive tasks. Here's them describing what they are and don't get worried about the technical terms.

**0:42** · Skills are organized collections of files that package composable procedural knowledge for agents. In other words, they're folders. Barry describes it as procedural knowledge for agents, which is a fancy way to say a way to get a task done. And there's an art to actually creating these skills, which we'll cover in rules two, three, and four. But, first you need to have the mental shift. Stop thinking in traditional prompts, start thinking in prompting Claude skills. This may sound complicated, but it really it's quite simple. Here's what it could look like if you wanted to draft a response to an email.

**1:09** · Instead of you having a crazy prompt to help you respond to an email with your voice, your tone, and your writing style, you would just type {slash} draft email and then bring in the email you want to respond to. So, that's how you do it in practice, but conceptually, how should you think about this? I pulled this graph from the Anthropic engineering presentation and added a slight tweak to it. Layer one, you have the AI model. This is the AI that you're using. Layer two is you have the AI agents and the prompts. This is likely how you've been interacting with AI to date, but you want to move up a layer to layer three, which is skills.

**1:38** · This is the application layer of the AI world. If you were to compare this to your cell phone, Anthropic is building the phone itself. You have to create the apps. That's the layer to control. And before we get to how to best create these skills, here's a prompt you can run to help you identify the skills that are worth creating. So, you're no longer writing custom prompts, you're writing more specific prompts that clearly reference skills. And this leads to the next topic, which most people get wrong, which is how do you actually build a skill that works? Rule number two is skills are more than prompts. So, you're convinced you need to change how you prompt to prompt skills.

### Rule #2: Skills Are More Than Prompts

**2:08** · So, the next question is how do you actually create skills that work? There's an art to this, a lot like when prompt engineering went viral when ChatGPT first came out, and it's important that you get this right. The act of actually creating the skill is super easy. You can just write in Claude, build me a skill for X, and it'll just create a skill for you. But to use these skills well, you need to understand what's actually inside them.

**2:28** · Because it's not just a prompt that lives in a folder. A skill is more than a prompt. Inside a skill, there are three layers. Layer one is the description. This is what Claude checks every time you ask a specific question, and it determines if it should use the skill or not. Think of it like a title on a folder. If the label's vague, Claude's going to have tough time identifying when to use it. If it's specific, it'll know exactly when it needs to use it. And yes, when you're prompting Claude, you don't need to explicitly call a skill if it's properly described. Claude will automatically know when to use it, which is awesome.

**2:58** · Layer two is the instructions. Once Claude grabs the skill, this is the playbook it follows. This is a step-by-step process on how to actually complete the task. And layer three are the tools it has access to. This is code scripts, API calls, reference files. This is where a skill becomes a lot more than prompts, and this layer three is where most of the leverage lives, but most people stop at that layer two.

**3:20** · Here's Eric from the Anthropic team talking about exactly this. And I think maybe the funniest things I see is that people will put a lot of effort into creating these really beautiful, detailed prompts.

**3:31** · Um, and then the tools that they make to give the model are sort of these incredibly bare-bones, uh, like, you know, no documentation, func- like the parameters are named A and B, and it's kind of like, oh, like an engineer wouldn't be able to like, you know, work with this as a, um, you know, work with this as if this was a function they I to use. People obsess over the prompt and skip the tools, the third layer of a skill. Anthropic engineers do the opposite. They focus on these tools.

**3:57** · So, instead of this whole back and forth, I created my own custom skill that could check these domains programmatically, so that whatever domains it was telling me, it is already verified that I could go and buy it. So, I gave this skill access to the right tool and it leveled up the entire process. And like I mentioned in rule one, instead of manually thinking about domains, I could have 10 different sub agents using this skill to look through 10,000 plus domains to find the right one. Now, I can do something that I literally would have never been able to do before.

**4:24** · Here's a prompt you can use to think deeper about the skills you create, so when you actually go ahead and prompt them, they'll be that much more effective. So, rule number two covers how anthropic engineers make skills, but what skills do they actually create? Rule number three is they build composable skills, not custom skills.

### Rule #3: Build Composable Skills, Not Custom Skills

**4:40** · Pulling directly from Anthropic's engineering blog about what skills are and how to position them, they are composable, portable, efficient, and powerful. Composability means multiple skills can work together with Claude automatically coordinating which to use.

**4:53** · What this means is you should have small, focused, and reusable skills that can work together, versus having a single massive skill that does everything. A concrete example that I experienced when I first started building skills for my content engine, I built a single {slash} content creation skill that did everything. Generated ideas, wrote scripts, drafted social posts, all of it, one skill, a million possibilities, and it just became unmanageable. Every time I wanted to change how scripts were written, I had to rewrite the whole skill and I didn't know what it actually impacted.

**5:21** · And so, instead I split it up to more specific skills, right? YouTube idea research, YouTube script writer, LinkedIn post. Each skill had a specific goal in mind.

**5:33** · And the benefit is that each can call the other skills, so that they start chaining them together. This may seem a bit overkill, but it really isn't for three specific reasons. The first is that issues are easy to spot. When When focused skill breaks, you know exactly where to look, whereas if it's a giant skill, you don't know what exactly the issue was. The second is that improvements compound. If you update, let's call it YouTube idea research, every workflow that uses the same skill automatically gets upgraded.

**5:59** · Whereas if you're using a giant skill, you're going to have overlapping functionality, which means you'll fix it in one skill and it will still be broken in the other. The third is that you can reuse instead of rebuilding. If you build something like the check domain skill I mentioned earlier, you can plug that into any workflow you want. You're not rebuilding the wheel every time with a new workflow. So you know you should break them up, but what's some more technical patterns that you should consider to make these even more powerful. So both of these come from directly how Anthropic engineers actually use them.

**6:29** · So pattern one is save scripts inside of skills. This is part of the tools layer of a skill and it's how you actually make them sharper. Here's Barry at the AI Engineering Code Summit talking about how he does exactly this. We kept seeing Claude write the same Python script over and over again to apply styling to slides. So we just asked Claude it inside of the skill as a tool for his version for his future self. Now we can just run the script and that makes everything a lot more consistent, a lot more efficient. Let me break down what he said. Claude kept rewriting the same Python script every session and instead of him letting it rewrite it, they saved the script inside of a skill folder.

### Pattern #1: Save Scripts Inside Skills

**7:00** · So now the next session Claude doesn't have to rewrite the script, it just reruns it. And this is so powerful because code is deterministic, which essentially means if you give it the same input, it will give you the same output every single time. Whereas in the AI world, that's not necessarily the case. It interprets it, it guesses, it uses tokens that cost money. And when you have a script inside a skill, you're trading AI tokens for code compute, which is cheaper, faster and repeatable.

**7:26** · A general rule of thumb is if you can use code instead of AI, you should. And you don't have to write the code, you can just have AI write it for you once and then you can reuse it as much as you want. The second pattern is you can control who invokes what. Most people don't know this exists, but Anthropic built two flags into Claude's skills that are important to understand. The first is user invocable. If you set this to false, it hides the skill from your slash menu. It means that the user, you or me or whoever, can't directly invoke this skill. It's only a skill for agents.

### Pattern #2: Control Who Invokes What

**7:54** · This is perfect for any AI agent specific tools that you don't even want to think about. And then disable model invocation. This does the opposite. Only you can run it and the model can't. This is great for higher risk things like a skill that sends a message or deploys a new version of your code to production.

**8:10** · Most of you watching this have likely never heard of either of those things, but now you have it in your bag when you're designing these skills. Here's a prompt you can run to audit your setup to make sure that you're properly applying these things into your skills.

**8:21** · Screenshot this and just send the photo into Claude and I highly recommend you do this. So you know how to build skills and what to build, but how do you make these improve over time? And before I get to that, if this is your first video of mine, welcome to channel. But if it's your second or more, here is our anti-slop agreement. The visuals, the testing, the time I put into this video, that's entirely built for humans, not for AI robots or data scrapers. So all I ask is you subscribe as part of this agreement to help this content reach more people so I can keep making videos like this. Rule number four is their prompts get smarter every session.

### Rule #4: Skills Get Smarter Every Session

**8:53** · Here's where Anthropic engineers really pull ahead. Their skills and in turn their prompting doesn't just work. They get better every session. When you prompt Claude with a sentence, that prompt disadvantages the moment you close the chat. When you prompt with a skill, the skill stays. And every time you use it, you have a chance to sharpen it. Listen their engineering team talk about exactly this. When you first start using Claude, this standardized format gives a very important guarantee.

**9:18** · Anything that Claude writes down can be used efficiently in by the future version of itself. Our goal is that Claude on day 30 of working with you is going to be a lot better on Claude on day one. Every time Claude learns something about how you work, your voice, your process, your edge cases, you write it down in the skill. Next session starts smarter than the last. So how do you actually do this? Every time you run a skill and the output isn't exactly what you want, ask yourself one question. Is this a one-time fix or should this be in the skill forever? If it's forever, update the skill. Add the rule, the example, the edge case.

**9:48** · And a lot of people skip this entirely.

**9:51** · They're just like, "Okay, run the skill, get an output." Like, continue with their day. But Anthropic engineers use a skill, get the output, then update the skill so that there's a compounding loop that improves over time. And it's really quite simple. Like, it's literally you can just use your chat history as a reference point to improve the skill itself. Just say, "Review the back and forth I just had after using this skill.

**10:14** · Can we enhance the skill so this is handled automatically or we don't make the same mistake again?" So, zooming out, these four rules are clear. Use skills, not prompts. Build tools, not just skills with prompts. Build skills that are composable, not custom. And update your skills every time you use them. Using Claude like an engineer doesn't have to be complicated. And if you like this, you'll love this video where I break down how Boris Cherny, the creator of Claude Code, uses Claude skills. It's pretty wild and builds on a lot of what we covered here. I'll see you over there. Peace.