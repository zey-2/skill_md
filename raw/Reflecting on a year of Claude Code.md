---
title: "Reflecting on a year of Claude Code"
source: "https://www.youtube.com/watch?v=Hth_tLaC2j8"
author:
  - "[[Claude]]"
published: 2026-06-09
created: 2026-06-14
description: "One year ago, we made Claude Code generally available. What started as an internal project—an agentic coding tool that runs in your terminal—is now used by developers and organizations worldwide.Bor"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Hth_tLaC2j8)

One year ago, we made Claude Code generally available. What started as an internal project—an agentic coding tool that runs in your terminal—is now used by developers and organizations worldwide.  
  
Boris Cherny (Head of Claude Code) and Cat Wu (Head of Product, Claude Code) look back on the Claude Code's first year, from a Slack demo that got two reactions to engineering teams deploying it across entire codebases. They cover best practices for verification, the thinking behind auto mode, their favorite routines and loops, Claude Code's adoption beyond engineering, the rise of context minimalism, and how to build for the AI exponential.  
  
0:00 - The origins and evolution of Claude Code  
1:10 - How to make Claude good at verification  
3:14 - Roles merging: Claude Code beyond engineers  
4:48 - Using routines for CI, code review, and more  
6:43 - Boris' go-to feature: auto mode  
8:10 - Securing auto mode: red teaming and evals  
10:24 - Why loop is the next leap  
11:06 - How engineering orgs and responsibilities are changing  
13:30 - Is the future product or engineering?  
14:20 - Working with hundreds of agents: using agent view, voice mode, and Remote Control  
16:05 - From context engineering to context minimalism  
17:17 - What's next for Claude Code  
  
Learn more about Claude Code: https://code.claude.com/docs/en/overview  
  
Follow ClaudeDevs on X for product updates and best practices from the Claude Code team: https://x.com/ClaudeDevs

## Transcript

### The origins and evolution of Claude Code

**0:00** · When we first released Claude Code, it was like a little video and I remember posting it to Slack, and there was like two people that gave like the reactions and like people were like excited.

**0:09** · I thought it was really cool, especially for my very easy engineering tasks.

**0:13** · It was quite good at it.

**0:14** · That's like a really nice way to say that it wasn't really good.

**0:31** · I can't believe it's only been a year since we first launched Claude Code.

**0:34** · It's hard to remember what what that was like.

**0:36** · Like, it’s so different than what we're doing today.

**0:40** · Like, now I just have, like, armies of agents that are doing stuff like I'm prompting one agent or I have like an agent that's like prompting agents, that's prompting agents.

**0:48** · And it's like a tree of like thousands of agents.

**0:50** · But I think it's just like the most important idea when working on this stuff is like, every single time Claude makes a mistake.

**0:57** · I don't tell Claude to do it differently, I tell it to write it to the CLAUDE.md, or to like make a skill or or something to do it differently.

**1:04** · And if you can do this, then Claude can just like run forever.

**1:07** · And I think the other thing that we kind of realize is the verification is really important.

### How to make Claude good at verification

**1:11** · Like we didn't realize that.

**1:12** · I hear this come up a lot with developers and enterprises that we meet with.

**1:17** · What are your tips for making a really good making Claude Code really good at verification?

**1:21** · I sort of feel like this is this thing that just like everyone misunderstands because whenever we talk about verification, people are thinking like unit tests or they're thinking like lint or like type check.

**1:31** · These are the things that are obviously really easy to automate.

**1:33** · And these are the things that were already automated.

**1:36** · But actually when we talk about verification for agents, it's something slightly different.

**1:40** · It's like can the agent run the thing?

**1:42** · It takes a little bit of mental work to figure out how exactly do you do this, because it's often not straightforward.

**1:47** · And I think that's like, that’s one of the challenges. I remember I remember with Opus 4 Claude tested itself.

**1:54** · And we just like hooked it up to Opus 4 And I was like, Claude build the feature and then test yourself in like bash.

**2:02** · And it opened a little Claude CLI and tested its own feature.

**2:07** · And I was just like, whoa.

**2:10** · It's crazy!

**2:10** · Like now, now we're so used to it.

**2:12** · Like now, you know, now we have these loops going for, you know, like the iOS simulator and the Android simulator and like computers for desktop, like it's not surprising.

**2:20** · But back then that was crazy.

**2:22** · How are, like, how are you doing it?

**2:24** · So I've been mainly hacking on the desktop app these days.

**2:27** · And one of the engineers on the team actually added this desktop development skill that teaches Claude how to run the local desktop app.

**2:35** · And I've been having it use it, and it still runs into issues or like bugs with the staging environment sometimes.

**2:42** · And so what I have it do is in those cases, I have it read Slack and understand, hey, is staging down right now?

**2:48** · Or has someone else already hit this?

**2:51** · And then when it debugs the whole issue, I tell it to update the desktop development skill.

**2:56** · What the skill does is Claude actually spins up a local desktop app, and it uses computer use to click around on it.

**3:03** · And so when I add a new UX, it clicks around to invoke the new UX.

**3:07** · It also tests edge cases, and when there's an issue it fixes it and re-checks.

**3:13** · This is like honestly, one of my favorite things about this team is everyone codes.

### Roles merging: Claude Code beyond engineers

**3:17** · I've never been on a team where, like, my PM would code and it's like crazy and like your code is like really good.

**3:26** · You’re too nice.

**3:28** · But I also just feel like it's it's also just becoming easier because it's like essentially Claude writes the code.

**3:34** · And so what matters a little more is like, what's the idea that you have?

**3:38** · And I feel like if you're a person that has like the product context and the business context and you're thinking about the design and the user, you're just going to come up with better ideas.

**3:46** · It's kind of like all the roles are merging.

**3:48** · I remember seeing Megan our designer’s PRs and I was just horrified at the beginning I was like, oh my God, why is Megan putting up PRs?

**3:54** · And then she was like, yeah, yeah.

**3:56** · I'm just like, I'm fixing the button.

**3:57** · And I was like, okay, all right, well, the code looks good, so maybe it's maybe it's fine.

**4:02** · And I feel like now it's just like it's totally normal.

**4:04** · Yeah, and we see this across all the enterprises we talk with.

**4:07** · Like, it's the engineers adopt Claude Code first and then the, the eng adjecent roles look over their shoulder and they're like, whoa, this thing is very powerful.

**4:16** · Let me try it out. And we found it's crazy.

**4:19** · We found that, like, our designers are more productive making prototypes and making changes directly in the app instead of pinging an engineer, PMs are making changes in the app.

**4:29** · Our finance team runs and in Claude Code, they do their projections there.

**4:34** · Data science.

**4:36** · Like if you talk with our data scientists, it's so cool.

**4:38** · It's just like everyone just has Claude Codes up on their screens.

**4:42** · I feel like it's remarkably versatile for different roles.

**4:47** · What do you feel like nowadays, are the use cases that are pushing the limit?

### Using routines for CI, code review, and more

**4:51** · One that I'm super excited about is routines.

**4:54** · There is one engineer on our team who launched voice mode across all of our products.

**4:59** · And, he has his routine set up that just listens for every ticket that comes, every GitHub issue, every bug report about voice mode.

**5:08** · And his Claude just picks it up, proactively puts up a fix, and then pings the PR to him.

**5:14** · And when he got that working for voice, he thought, okay, we're getting a lot of other feedback that isn't being responded to.

**5:21** · So, he also set up a routine to listen for that.

**5:24** · So I ship this, small feature.

**5:26** · And there was like an edge case in it that I didn't see.

**5:29** · And so someone filed a bug for it, and I was going to get to the bug that night.

**5:34** · And my Claude was working, it said, wait a second, another Claude has already fixed this.

**5:39** · And I was like, how is this possible?

**5:40** · Like, I've never talked to him about this feature before and so I pinged him, and I was like, how did you fix this so quickly?

**5:46** · And he said, he has another routine that just looks for bug reports that haven't been responded to in five hours and puts up a fix, and he merges the ones that are easy to verify.

**5:55** · Claude tells me this like all the time now.

**5:57** · That someone else has already fixed it?

**5:59** · There's always like another person’s Claude that's working on it.

**6:01** · It's like, yeah, that's been one of the changes.

**6:04** · I feel like we're, a while ago we were trying to figure out, like, how to use routines, and I feel like just like the agent SDK was this first idea that we could use Claude Code programmatically. But I feel like at the beginning, it just wasn't obvious.

**6:18** · How do we use it? What do we use it for?

**6:20** · And I think routines are the first really obvious application.

**6:24** · And I don't know, like it just does like all the code review, it babysits like every PR, you remember back in the day you used to actually have to like respond to code review comments.

**6:34** · You used to have to like fix CI. You used to have to rebase.

**6:38** · Yeah. Like I haven't done that in a long time.

**6:40** · Yeah.

**6:41** · When you're in the CLI and you're synchronously working with Claude, what are your go to features?

### Boris' go-to feature: auto mode

**6:47** · Okay.

**6:47** · What they used to be is plan mode.

**6:49** · I don't use that anymore.

**6:51** · What do you use instead?

**6:52** · Auto mode.

**6:53** · Auto mode?

**6:53** · It’s the best.

**6:54** · Instead of plan mode?

**6:55** · Instead of plan mode.

**6:56** · Yeah because the newer models they don't actually need like a planning step anymore.

**7:01** · I think this was really important for like Opus 4 through maybe 4.5.

**7:05** · Then I think starting with four six and definitely with four seven, it just doesn't need that planning step.

**7:09** · I think some people still use it.

**7:10** · They like to have that artifact.

**7:11** · I don't use it And I just do auto mode for everything because then I start my Claude, it starts to work and then I just like move on to the next Claude and I don't have to sit there and watch it.

**7:21** · But from the very early stage we had this like permission prompts model for Claude Code, right?

**7:25** · Like it runs a tool and then it asks you like, hey, are you okay running this tool?

**7:29** · And you had to say yes or no.

**7:31** · And at the time, that was kind of the best we had a year and a half ago because we didn't have, you know, classifiers.

**7:36** · The model was not as well aligned as it is today.

**7:38** · So auto mode was just such a it was such a big step up because actually you don't want to read most of these requests.

**7:44** · Just routing it to a different model and having it check for security works so much better.

**7:48** · Yeah.

**7:49** · And if a thing like is a little suss or, you know, this isn't the command that you think you want to run or it's not safe, the model will just deny it.

**7:57** · And then you can go back and you can allow it later.

**8:00** · I think this has been one of those, like, step changes.

**8:02** · We just, there's no way we could have done this a year and a half ago.

**8:04** · It's just human nature, when you accept 99% of requests, that your eyes just glaze over when you read it.

### Securing auto mode: red teaming and evals

**8:11** · And so actually, we feel that auto mode is more safe than reading every single permission prompt, because it means that your only paying attention to the most important thing and not like being spammed a bunch of things that are just 99% yes.

**8:24** · I think security is one of these things.

**8:26** · Like you can talk about it and then it's a totally different thing to actually do it correctly, because it just doesn't always look the way that you think it's going to look.

**8:33** · And it's just all about like always red teaming, always pentesting always looking, you know, always having a threat model and then using that to figure out, you know, how is this thing going to get attacked?

**8:43** · How are people going to get prompt injected?

**8:45** · And I just feel like like the team is just like obsessed with this.

**8:48** · And it's so important because as a result, I just trust the agent to run and I can move on and I can just have like a second agent.

**8:57** · And if I didn't trust it, then I just wouldn't have been able to do that.

**9:00** · And internally, to actually get auto mode out to our users, we needed to really trust it first.

**9:07** · And so what we did was we collected thousands of transcripts of like an entire agent trajectory and a permission prompt and had auto mode classify whether or not it was safe.

**9:18** · And it was extremely good at this.

**9:20** · So then we got red teamers, and we asked them to try to prompt inject, and try to hack the code base.

**9:27** · And we use this to create evals and make sure that all of these were denied.

**9:30** · And then we had our own internal teams try to prompt inject and hack Claude Code’s auto mode.

**9:37** · And then we improved auto mode to make sure that we caught all of these.

**9:40** · So it's not only just protecting you against the vulnerabilities that are out there in the wild today, but, the most intelligent attacks that we can construct.

**9:50** · Yeah. I mean, it's like, it’s honestly like a weird approach.

**9:52** · I feel like there's, like, all these features the last year where the first time someone pitched it, I was like, no way, that's not going to work.

**9:59** · And I feel like over time I just learned, like I'm actually wrong, like so often now.

**10:03** · Because, like, building on the model is so weird.

**10:06** · It's just like all this, like, engineering stuff that I've learned over the years.

**10:09** · So much of it I just have to, like, throw out.

**10:11** · And this is just like part of what the job is now.

**10:13** · We're building on a new thing and we just have to relearn it.

**10:16** · And auto mode was definitely one of these.

**10:18** · I was like, the first time I heard it, I was like, route the prompt for a model?

**10:21** · No way. That's not going to work.

**10:23** · And then it actually turns out empirically, it works really, really well.

### Why loop is the next leap

**10:26** · But I heard you also love loop.

**10:28** · Yeah, I love loop.

**10:30** · How do you use it?

**10:31** · I think for loop, there's this transition that we went through like a year and a half ago where we were like, all right there’s source code.

**10:39** · But actually the thing an engineer should interact with, maybe it's not the source code, maybe it's the agent.

**10:45** · And so we made this leap of I don't write the source code, I talked to an agent, and the agent writes the source code for me.

**10:51** · And I think right now what's happening is we're making the next leap.

**10:55** · I don't talk to an agent anymore.

**10:56** · I talk to loop or I talk to a routine and it prompts Claude for me.

**11:02** · And it's just it's crazy.

**11:04** · I mean, it's been like, it's a year and a half and this was like two big leaps.

### How engineering orgs and responsibilities are changing

**11:07** · If you take like, a step back, how are you seeing entire engineering orgs change?

**11:12** · I'm going to put on my business cat hat.

**11:14** · I have this, like, favorite case study.

**11:16** · This is like a Harvard Business Review from the 90s.

**11:18** · And they were talking about, like, computers are here.

**11:20** · Why are we not seeing the productivity benefits?

**11:23** · And it's just this, like amazing snapshot into like, what it actually felt like at the time because, like, you know, people used to use mainframes.

**11:29** · At some point companies switch to personal computers.

**11:32** · It was sort of a new thing, and the companies were trying to figure out how to use it.

**11:35** · The same way they're trying to figure out how to use AI right now.

**11:38** · And it turned out that to get the productivity benefits from computers, what you had to do isn't like you have your paper filing cabinet and your, like, paper and pen business process.

**11:48** · And then there's like a computer on the side that does something.

**11:51** · Actually, what you have to do is you throw out the filing cabinet, you have to throw out all your paper and all your pens, and then you put a computer in the center and everything has to run through the computer.

**11:59** · It has to be at the center of every business process.

**12:01** · And I feel like at Anthropic we do this thing where when you on board, you don't ask people questions like no one asks me questions when they on board.

**12:09** · You probably have the same thing, they ask Claude.

**12:12** · And this is kind of weird, like, this is the first company I've been at like that.

**12:17** · And I feel like for us, Claude is just at the center of everything.

**12:19** · Whenever I have a question, I ask Claude.

**12:21** · Whenever I write code, I use Claude.

**12:22** · Whenever I need a code review, Claude does it, whenever I need a security review, Claude does it, whenever I need to you know, fill out a form or something, Co-work does it.

**12:31** · So it's just like Claude is at the center of everything.

**12:33** · And I feel like the companies that are really figuring it out, and there's a bunch of them now, they're just putting Claude at the center of it.

**12:40** · And I think for computers, the transition took 10 to 15 years.

**12:43** · But actually for AI, because so much of our work is already digitized and Claude can use a computer and it can write code and run code.

**12:52** · This transition is happening a lot faster.

**12:54** · I think it's just like, really, it's just really exciting.

**12:56** · Like, I feel like now I don't have to bug people anymore and when I interact with people, it's because it's like fun and I get to collaborate with them on stuff and we get to create something together.

**13:06** · It's not that like, I need them.

**13:08** · I need something, you know, from them because, like, Claude can actually do a lot of that stuff now.

**13:13** · And I also feel like as an engineer, I've just never had this much fun doing engineering because the like the tedious part I don't have to do.

**13:19** · Like I'm just coming up with ideas.

**13:20** · I'm talking to customers and every idea, like, I don't have a to do list anymore.

**13:25** · Like Claude just builds everything.

**13:27** · And so my job is to come up with these ideas and it's just so fun.

### Is the future product or engineering?

**13:30** · Okay, so here's a question.

**13:31** · Is the future product or engineering?

**13:33** · Like, is everyone going to be a PM or is everyone going to be an engineer?

**13:36** · Everyone's going to be both.

**13:38** · I feel pretty strongly that these roles are merging.

**13:41** · Like when we look at our team, our product team all writes code.

**13:45** · Our Devrel team all writes code. Our design team all writes code.

**13:50** · And then we look at our engineers and a lot of them ship products end to end.

**13:54** · They have an idea for what to build.

**13:56** · They build it.

**13:57** · They work with legal and marketing to figure out how we communicate this to the world and make sure it's safe and with security, too.

**14:04** · And a lot of times they just see through this whole process end to end.

**14:08** · So I think right now AI really benefits people people who have a lot of curiosity, have a lot of product tastes who love to have this like end to end ownership.

**14:18** · And now a lot of people are running like hundreds of agents.

### Working with hundreds of agents: using agent view, voice mode, and Remote Control

**14:22** · What are the products that you think people should be adopting as they transition from single to multiple to hundreds?

**14:29** · Until recently, the way that I wrote code was I had like six terminal tabs with six git checkout on the same repo, and then I would just like tab between them.

**14:39** · Now it's pretty different.

**14:40** · I have like one tab, I use the new agent view that we just shipped.

**14:43** · It's like so good.

**14:44** · And I'm so glad that we took a while to iterate on it to make that really good.

**14:48** · And I also use the desktop app because I don't have to fiddle with checkouts that way.

**14:53** · It just like, you know, it does the work tree cloning or the like, it creates the work trees for me.

**14:58** · And the thing that I would not have expected six months ago is probably half my engineering now I do on my phone.

**15:05** · So I just have like I have so many agents running that I just start for my phone.

**15:09** · I use a remote control, which is like amazing now and like I will start something on my computer.

**15:14** · And then I’ll just remote control in from my phone and I’ll just like, walk around I’ll get coffee, and then I'll check in on my agents and maybe I'll start another agent.

**15:21** · And sometimes I'm like, talking to someone and we come up with a new idea.

**15:25** · I’ll just start an agent on the spot.

**15:26** · I like talk to it with voice mode and just have it build something, and I don't even have to go back to my computer anymore.

**15:32** · I remember when you started doing this because you would actually leave work, have your computer on your desk open, plugged in, screen locked, and I just thought you would, like, come back to the office at some point to get your computer, but then it would be like pretty late and I was like, maybe he just left it here by accident.

**15:48** · And then it happened again the next day.

**15:50** · And then it happened again the next day.

**15:52** · And I was like, wait, it's so weird because you're landing PRs but your computer is right next to me, and I remember you responding and you're like, yeah, I'm coding from my couch.

**16:01** · Yeah, that was the week the remote control got really good.

**16:04** · Yeah.

**16:04** · So another thing that users are asking about all the time is how do you do context engineering, especially in a large enterprise?

### From context engineering to context minimalism

**16:12** · This is a thing.

**16:12** · You know, people used to talk about prompt engineering.

**16:14** · They used to like work context engineering.

**16:16** · This is sort of matching where the model was at the time.

**16:20** · Back in the days of Sonnet 3.5, you had to prompt engineer back in the days of Opus 4, you had to context engineer.

**16:26** · But with the models of today, you don't do any of this.

**16:29** · You give it the minimal possible system prompt, the minimal possible tools, and then you let the model figure it out.

**16:36** · Like you just have to give the model some way to pull in the context.

**16:38** · I think that's the most important thing.

**16:40** · How do you think about it?

**16:41** · I see things very similarly.

**16:42** · I'm a context minimalist, so my general philosophy is tell the model only what it needs to know and let it figure out the rest of it.

**16:53** · I think when you give the model too much context, it's kind of like you're micromanaging it.

**16:58** · And sometimes the model knows a better way to get to the same outcome.

**17:02** · And I personally prefer to give the model that freedom to do that.

**17:07** · And then in general, we're also making our harness more lean so that you have more room for your own prompts.

**17:13** · And so that follows your prompts better.

**17:14** · There's all these different ways to Claude now, but I feel like in a year it's going to be a totally new set of things, and it's going to be so surprising if it's still these same things, because I think, like we're seeing these giant trends happening right now, agents are running for longer.

### What's next for Claude Code

**17:29** · They're more autonomous.

**17:31** · Very rarely am I running one agent at a time.

**17:33** · It's usually like a few agents or dozens or hundreds or thousands.

**17:37** · And so like the form factor for that, it's going to be really different than what came before.

**17:41** · And I don't know what it's going to be.

**17:42** · And I think in a large part, it's going to be up to the team to figure it out.

**17:46** · And this is, this is why I'm like, so happy we run the team that the way that we do, where everyone just comes up with ideas and everyone is able to think about the product.

**17:55** · Everyone talks to users all the time because I don't think these ideas are going to come from us.

**17:59** · It's going to come from the team.

**18:00** · Totally, and from everyone in our community building with us.