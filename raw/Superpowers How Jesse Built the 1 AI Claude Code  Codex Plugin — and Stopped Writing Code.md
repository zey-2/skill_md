---
title: "Superpowers: How Jesse Built the #1 AI Claude Code/  Codex Plugin — and Stopped Writing Code"
source: "https://www.youtube.com/watch?v=6YltXh12W-g"
author:
  - "[[Larridin]]"
  - "[[Inc.]]"
published: 2026-04-10
created: 2026-05-20
description: "Jesse Vincent stopped writing code in October. His Claude Code plugin Superpowers reached 50,000 developers in months by treating AI agents like junior engineers: tight specs, review loops, and epheme"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=6YltXh12W-g)

Jesse Vincent stopped writing code in October. His Claude Code plugin Superpowers reached 50,000 developers in months by treating AI agents like junior engineers: tight specs, review loops, and ephemeral sub-agents that check each other's work until the output matches the spec.  
In this episode, Jesse breaks down the full agentic workflow behind Superpowers, including why he spent four and a half hours in brainstorming before writing a single line of code, how he caught his agents deleting test files to avoid failing them, and why specs are now the only artifact that matters.  
  
CHAPTERS:  
00:00 Introduction  
00:41 Guest introduction: Jesse Vincent and Superpowers  
02:00 Jesse's background and the common thread across his career  
03:45 How Superpowers was built: iterating on Claude MD from day one  
05:04 Discovering Anthropic's skill files and adapting them for Claude Code  
06:39 The agentic workflow breakdown begins  
09:21 Breaking down the exact workflow step by step  
11:27 Brainstorming in Claude: Socratic dialogue and auto-triggering skills  
15:47 What happens after brainstorming: the spec  
19:02 Write plan mode and the spec review loop  
22:50 Implementation plans written for "a gifted engineer with bad judgment"  
24:35 How the orchestrator and ephemeral sub-agents work  
28:25 Test-driven development with agents  
30:45 End-to-end validation over unit tests: the v33 MP4 story  
33:52 Catching agents that deleted test files  
36:19 Walking away for 6 to 18 hours autonomously  
36:30 Advice for CTOs and engineering leaders  
39:36 How to measure engineering productivity  
43:01 Greenfield vs. existing codebases and comments  
45:08 Latent space engineering  
48:04 Advice for engineers entering the field today  
48:35 Closing

## Transcript

### Introduction

**0:00** · If I am choosing between two candidates, I am going to pick the one who can string together sentences and express their thoughts clearly. One of the really weird hacks is you can get away without using a sub agent and use the phrase look at this with fresh eyes. And for some reason, fresh eyes causes the agents to step back, take a breath, and review something critically.

**0:20** · If you're running an engineing team, how do you measure your dev productivity?

**0:24** · measuring poll requests, lines of code, bugs, they're not valid metrics. When Anthropic first shipped that ask user question tool, I added it to superpowers immediately and I discovered that what it was doing was causing me to not think. Specs are the thing that matters now. The code does not matter anymore.

### Guest introduction: Jesse Vincent and Superpowers

**0:41** · My experience with agents, as with humans, is that when they are afraid, they will absolutely work hard to be done, not to do good work. If you tell Claude I love you at the end of a prompt, you'll get better results.

**0:54** · If you have to sort of give an advice to somebody who is graduating today, what would be your advice to them?

**0:59** · So, one, welcome to AI impact podcast. Today, I have a very special guest, Jesse Venson. He's been a a prolific open-source developer, engineer, entrepreneur starting all the way 30 years or something like that.

**1:16** · Something like that. It was the 90s.

**1:18** · Yeah.

**1:18** · from from a long time ago uh and he produced lots of stuff uh recently started a new AI startup called Prime Radiant but today we are here to primarily talk about his most and probably most consequential uh opensource project at least in my opinion called superpowers right superpowers is was launched only a few months ago and already has over 50,000

**1:41** · developers my team I call it very very very very fondly that it's really giving us superpowers it's really makes how your junior engineer into really a senior engineer literally overnight and it's it's taking the world by storm. JC, welcome to the show.

**1:56** · Thanks for having me. That that's quite high praise and it is quite wild because this is literally something that I threw out there in October as a here's how I'm currently working with agentic coding environments. And so it's both gratifying and frankly a little terrifying that it is, you know, it's now like I think it's number three in the official uh Cloud Code plugins as well.

### Jesse's background and the common thread across his career

**2:20** · Um Awesome. It's it's wild. Yeah.

**2:23** · Walk me through this. You know, you started um K9 and you worked on keyboard.io then you you were a pearl contributor for a long time.

**2:31** · Sure.

**2:31** · Um, so you've been doing this sort of across your and now the prime radiant and superpowers. You know, what is that common thread if you sort of think back?

**2:40** · Yeah, I've been doing open source since we didn't have that term. Uh, it used to just be free software, but pretty much everything that I've built has been tools to help people get stuff done.

**2:51** · Whether that is RT, the ticketing system that my first company makes, um, it's open source. It's been around it. I created it the summer of 1996, I think. Um, and it's it's wild that it is still helping pe, you know, Fortune50s and tiny little nonprofits. Um, I spent a couple years as, as you said, as the project lead for Pearl 5.

**3:15** · Um, I used to make an email client for Android called K9 that later got adopted uh by Thunderbird. So, now it's Thunderbird for Android. The last company that I started with my wife was Keyboardia. made high-end computer keyboards. And yeah, the sort of the thing that has always tied it together is I like helping people build things and make things. Um, those keywords, they were really intended for programmers and writers and people who type too much. So even even the hardware stuff. Um, and last and just over a year ago, the Dayclaw Code came out.

### How Superpowers was built: iterating on Claude MD from day one

**3:46** · I was fascinated and I sat down and created a horrible monstrosity that first day. It went wildly out of control. and then spent the better part of a month sort of learning how to drive cloud doing what turns out to have been actual prompt engineering where I you know I took a simple standard prompt and it was let's make a react to-do list and then I iterated on the cloudMD behind it snapshotting the full transcript of the conversation the output and the cloudMD

**4:17** · to take it from this thing where and this was before there were subscriptions so it was token prices where it was 20 cents and it generated a React to-do list in 15 seconds and issue and uh to-do items vanished when you reloaded the page to a 25minut fivephase project that cost $25 and had strict TDD the whole way through. And so over the course of the first six months I was sort of iterating on how do I get agents to build things well?

**4:46** · Mh. And I was putting out a blog post every couple of months of here's my current set of prompts, my current workflow. And sometime round about last September, Anthropic shipped this um support for uh Microsoft Word, Microsoft Office or Microsoft PowerPoint to Microsoft Excel on cloud.ai. And I went went to cloud.ai and said like tell me about this. Uh, and it's like, well, I've got a I've got a Linux machine behind me. Like, oh, can you give me a tarball of SLOP?

### Discovering Anthropic's skill files and adapting them for Claude Code

**5:14** · It delivers a tarball of slash opt and has these skill.mmd files. And I ask it a little bit about it. And so, well, my system prompt says that if I've got a skill for something, I should use it.

**5:27** · And I open them up and they're sort of, but how and why to make a Word doc? How and why to make a PowerPoint using Open Office and command line tools? And I saw this stuff and I saw what I'd been doing and realized that I could adapt this to cloud code. And so I built a skills system for cloud code and built skills that mirrored my development process which is basically my experience managing junior engineers over 30 years and shipped and shipped that as the first version of superpowers.

**5:56** · And then two weeks later, Anthropic shipped um ski shipped an official skills implementation for I accidentally front ran Anthropic by about two weeks on agent skills.

**6:07** · Yeah.

**6:07** · And so I've like some of the stuff I do is a little different than the way that Anthropic builds skills in general. Um, and so like my skills put a lot of effort, a lot of work into explaining to the agent the intent of like not just how to do this but why and also a list of rationalizations. So I have called the my agents are pressure testing these skills against other agents and like it

**6:35** · runs it through a process and if the agent doesn't do what it's supposed to it stops and says hey clude why did you why did you fail to do TDD and cloud will say well for in this case it was too simple so I decided not to and then the club that's writing the skills will go and add here's a rationalization that you might think lets you off the hook it's not okay and so that kind of iterative of process build these skills that are that tend to be a lot more robust.

### The agentic workflow breakdown begins

**7:02** · Let me pause you here for a second. Let's let's let's uh uh sort of rewind back a little bit, you know.

**7:07** · Walk me through your thinking sort of at what point you sort of realized Yeah.

**7:12** · because I think there was like this magical time and and it came for different time with different people.

**7:17** · But I wonder if there was like a magical time for you. You realize you know what this is actually possible. We are we are well beyond just autotap completing the for loop or what have you to hey you can actually build software and and the models are there like you know like how was your where was that thinking sort of when did you actually kind of internalized it?

**7:36** · So you can if you look at my GitHub contributor graph um it looks like it was so I started doing this with when it was cursor and windsurf getting better than each other every week and switching back and forth between them.

**7:53** · Um but I think like one of the the first aha moments for me was when I was still working on the c on the keyboard company we had an automated a simulator to do to test the firmware. It's basically a virtual Arduino device.

**8:07** · And for 3 years, there had been a to-do of support the serial protocol in this weird ball of C++. And I had just been afraid of touching it cuz I've never been a C++ dev.

**8:17** · I could kind of fake it.

**8:19** · And I described it to cursor and in an hour it worked.

**8:22** · When was that?

**8:23** · I mean, so that that has to have been it predates Cloud Code. So it would have been at the latest last January.

**8:29** · Four. Sonnet 4 kind of like Sonnet 4. I mean, Sonnet 4. I'm not sure I was using I must have been using sonnet in cursor but it was something that was it was like it was over a year ago. Um and certainly by last April it that was you know that was just what was going on. I think the last time I wrote a line of code was October.

**8:51** · Um and it was three lines of a shell script and I shouldn't have done it but I thought it would be faster to have me do it than have the agent do it. Um but yeah know I'm and I'm having the most prolific period of my career. It's a weird day when I'm not shipping a new app like and I mean and there's plenty

**9:07** · of maintenance engineering too but it's it's it's a weird fun time you know you know one of the things I u I was I was looking through the GitHub repo and I didn't realize how many repos you have this this you know sort of directly aligns with essentially what you're saying but you have so many things uh I couldn't believe it could be one person doing it and I have a lot of things that are not public too it's like I try not to put the you know the weird experiment that I haven't tested at all. Some are public, you know, the and the the corporate GitHub has like 40 not public yet repos.

### Breaking down the exact workflow step by step

**9:40** · Um, mostly just because we were trying to figure out how we're doing some things. Amazing.

**9:44** · Let's move a little bit further and let's now and what I want to do is that I want to break down your workflow.

**9:50** · Sure.

**9:51** · Right. You have this mantra that says why am I doing this?

**9:54** · Yeah.

**9:54** · Right.

**9:54** · Let's go from there and tell me why you have this mantra like where's that? Yeah. Um I mean so my usual agent workflow um these days I'm flipping between clog code and codecs. Um I find that uh the code uh the GPT53 codeex and GPT54 models are really quite good.

**10:14** · They are a little more literal than I like. So I don't enjoy doing design with them as much but for implementation they're fantastic. Um, but so it's it's usually either Cloud Code or Codeex or one of three experimental coding agents that I've that I've built. Um, and it start it starts off with me opening up and it's usually one line. Hey, I want to build uh a you know a runtime for agents. The agents should live in tiny little containers that have a snapshotable file system.

**10:46** · The container should start up quickly. It should automatically mount a GitHub repo into the container. Uh, I want a pretty dashboard for it. So something that might look a little bit like sprites.dev or XC.dev. This is a real thing that I built a couple of weeks ago.

**11:03** · Actually, let's actually pass this down.

**11:05** · This is very interesting, right? So what I want to do is that, you know, let's take this example where you have a a container where you're going to open you're going to check out git repo and and you're going to operate on it. uh and then you want to produce some dashboards on it something like this

**11:21** · right but specifically this is the product to to run those containers to to run those containers okay to the product to run those containers so it's kind of your your mini Kubernetes of sort okay it's a fairly complex product right potentially yeah it's not it's not a it's not a little shell script right yeah it's not a little pul script it's it has bunch of things involved right yeah so so let's say you're you're uh advising an engineer or you're telling them to go to build AI native coding.

### Brainstorming in Claude: Socratic dialogue and auto-triggering skills

**11:48** · Let's walk through the exact workflow, right? And so I literally started with I described I say that straight into a cloud prompt in cloud, not in codec.

**11:56** · Not this one was cloud.

**11:57** · This one's cloud. Yeah.

**11:58** · And it kicks off automatically kicks off superpowers brainstorming. Yep.

**12:02** · I spent a lot of time trying to get skills to autotrigger because it's not I love that by the way. You know, I used to do this like slash brainstorming and now it it generally picks up.

**12:10** · It should. Yeah. This is that is that there's a bootstrappy part of superpowers that tells the agent, so you know, if you have a skill that sounds like there's 1% chance it might be useful, you have to go read it for this whatever the task is. And so brainstorming turns around and it uses Socratic dialogue and other psych tricks to get the human to think about what they want to do and explain it. And so this this came out of my um my consulting career from that first open source company.

**12:40** · A lot of my job would be to go into very large companies who were paying us for professional services around the product and I would sit down with a manager or a team and they would say we you know we need you to make it so that we can upload this kind of file onto this page so that we can do this process listen for a second say okay

**13:01** · explain why you need that process and invariably it would be there's something else that should happen and they had they had identified a way to solve the end problem without thinking about what they were really trying to do. And so in my best in my best, you know, business business English, what are you actually trying to do?

**13:21** · And talking them into thinking it through and explaining it would always result in a better outcome for them. And so that was the skill that I taught the agents for brainstorming. And so it tricks me into explaining what I want. It asks me relevant questions because it has pretty good world knowledge. It can make proposals.

**13:42** · But the goal is to get me to figure out what I want and explain it to the point where it can go and write a spec.

**13:48** · I have have a couple of comments on this. You know, like I found personally the superpowers uh brainstorming it gets to the really the heart of the problem uh much quicker um and and really helps me think through the problem. uh even sometimes uh actually many times I use this even outside of coding right I just I just like anything right yeah um so that's one but it's also more more potent than the the question tool that the cloud ships with right so I I kind of find it interesting that the it's

**14:21** · essentially the same underlying LLM model uh but with some I don't know this magic thing in brainstorming it really gets to these really key questions right so I mean you can open It's it's just a markdown file. You can see exactly how we do it. And the very first versions, if you go to my blog post from uh I think it's like September of I guess September 2025, it was the threeline prompt that I was using that brainstorming is now doing.

**14:46** · Brainstorming is about a page because there's some more to it. Yep.

**14:49** · And now in 5 that shipped two days ago, there's a visual brainstorming thing where it will pop up a browser and actually show you visual mockups rather than trying to use ASKI art.

**15:00** · Right.

**15:00** · Uh, at one point shortly after Superpowers had shipped, I let Claude iterate on brainstorming and it was this five-page process and the results were garbage. And that was the point where I I peeled it back and went through it by hand and we tuned it to get closer to that feeling that you've got where it is helping you think things through. When Anthropic first shipped that ask user question tool that they use as part of their planning mode and COD uses and other at other times, I it looked great.

**15:29** · I added it to superpowers immediately and I discovered that what it was doing was causing me to not think. It would all I could get through an entire brainstorming session just by clicking okay, okay, okay. And so I pulled it out because even though it's a good UX, it's not a good UX for getting people to think.

### What happens after brainstorming: the spec

**15:51** · Yeah. I mean, I cannot under overemphasize this importance of this brainstorming step here.

**15:57** · Um uh Okay. So, so you you spend uh you you go through this brainstorming process with uh Claude in this case with superpowers. Yeah.

**16:06** · Uh and you answer a bunch of questions.

**16:08** · Um what next? Well, so sometime I mean sometimes that is literally a five minute exercise and it will get to the point where I say I don't care I trust you just finish like if especially if it's a small thing or if it's really obvious in this case I spent four and a half hours in brainstorm with claude like it was a half day planning process

**16:29** · and we got real detailed we talked through technology choices it did independent research to make sure that technology choices would work um and that's a thing I've been working toward pushing brainstorming into more is doing a doing little design spikes, showing you it, you know, an API idea. Um, that sort of thing.

**16:46** · Let's pull that thread here, which is which is I think is a very interesting and is a is a huge uh unlock, which is you're not just doing brainstorming, right? You mentioned little spikes.

**16:57** · Yeah.

**16:58** · Tell tell me about that.

**16:59** · For this one, it was I um I didn't know if I was going to use Firecracker or G Visor or something else. I'm well enough versed in the space to know what roughly what I was looking for and say like no this isn't a Kubernetes problem. Um I don't have a Kubernetes problem. I don't want to have a Kubernetes problem. Um these are you know supposed to be individual throwaway containers. Um and so it went and did some research on scale, what works well, what doesn't work well.

**17:28** · In this case I wanted it to be running on for at least for prototyping on a nook that I had in the closet. And so it was Claude, you have passwordless SSH to that machine. Um, and you've got passwordless pseudo on that machine. I am one of those dangerously what dangerously skip permissions. Um, you know, I I will not advocate that other people should do this, but it it works for me. Um, and I will talk about the time that I caught cloud deleting things. Um, which is a really interesting story, but go, you know, go check out that machine.

**17:57** · Make sure you understand what we can get away with, what our options are for infrastructure. and and it came back and it's like why don't we try this this and this.

**18:06** · So so let me break this. So what is exactly happening is that while you're doing brainstorming uh it's actually doing the actual sort of small prototypes for this one. It didn't write any code but it did exploration of the host system that I was going to use for the prototype.

**18:22** · So it's it's essentially validating that at least it's starting to mitigate the technical technical uh yeah is it even possible kind of thing. Um, and like more and more this kind of like let's go let's do a quick a quick prototype. One of my favorite tricks when I'm doing design with Claude, even inside brainstorming, is and I and bra bra bra

**18:42** · bra bra bra bra bra bra bra bra bra bra bra bra bra bra bra bra brainstorming hints this sum and so it happens automatically sum is uh why don't you come up with four different ways to solve this problem than tell me which one is your favorite and that gets dramatically better outcomes than tell me what to do because when it has to actually think think through multiple options you end up getting better results. So you actually within brainstorm you actually push the the model sometimes. Yeah. Sometimes depending on how how complex the problem is.

### Write plan mode and the spec review loop

**19:07** · How complex the problem is. If I feel like I don't know what the right answer is, right?

**19:12** · Um like sometimes I it's tech I I work with technologies I've never touched before.

**19:16** · Right.

**19:16** · Um I keep shipping Mac apps and iOS apps and I still don't know Swift.

**19:21** · What?

**19:22** · Yeah. Um so after that it goes into planning mode.

**19:25** · So this is the this is not the cloud.

**19:27** · Sorry. This is not their planning mode.

**19:28** · This is our right plan. The right plans, the writing right plan code. Yeah. And so actually before you go to write plan mode. So so after the brainstorm, it writes the design doc, right?

**19:37** · It writes. Yeah. A spec.

**19:39** · A spec doc, right? And so as I understand, you write the spec doc and then you go into right plan mode, right?

**19:45** · So what happens once you write the spec mode? Like is this something that you you manually see like?

**19:50** · So um this is actually a thing that when for superpowers 5 I'd actually stopped it. I set it so that Claude no longer pauses right after writing the spec and immediately got user push back of like no no I need to read that spec before I before we start planning. Yes. And so I peeled that back. 501 now pauses as if you want to read the spec you can read the spec.

**20:11** · Actually I get that user feedback.

**20:13** · Totally. I I do too. Like yes I I usually have spent so long in brainstorming that I know what's there and I have trust that it is written it well. Um, one of the other things in superpowers 5 is I've taken the uh review loop that we now that we've always done on the code and we now do it on the spec and the plan.

**20:34** · That's exactly I was actually going you know what we do uh in the companies that once the spec is ready we actually check that in.

**20:41** · Yeah.

**20:41** · And it's goes for PR, right? And so so it's not I mean a lot of times you want like sort of consensus design like other people know what you're doing. uh and because it has so much data in that spec location, you actually want that to be reviewed, right?

**20:55** · It's not your original technical design like you that used to sit in Google Docs.

**20:59** · This is not your code review that which obviously has to be reviewed. But but the spec review is actually one of the key steps.

**21:04** · Specs are in fact I think the only thing that humans should be reading at this point um and and possibly editing. Specs are the thing that matters now. Um the code does not matter anymore. The spec gets reviewed whether it's by you or by more claws. I know folks who pretty routinely cross-review specs between claude and codecs and then review those reviews with the other tool. Um, and that that tends to that the reports are that that gets you pretty good results.

**21:31** · Yes, the the multimodel reviews multimodel reviews matters. I've I have also found that simply multiple agent reviews with the same model helps.

**21:42** · Why is that? What's the intuition behind So, if you've if you've never done this before, open up five copies of cloud code next to each other, possibly faster without superpowers. Um, write a prompt for it to do something. It's either re react write a React to-do list or something that is capable is capable of doing inside of 15 minutes. Paste the exact same text into all five and let them run.

**22:04** · And you will get probably five pretty different results.

**22:08** · Interesting. And so different like different agent instances do different things, right?

**22:13** · Um, one of the really weird hacks is you can get away without using a sub agent and use the phrase look at this with fresh eyes. And for some reason fresh eyes causes the agents to step back, take a breath and review something critically.

**22:30** · Interest. It's very It's interesting. It actually um it's kind of like humans to some extent. It's they are an interesting faximile of humans and they exhibit a lot of the same kinds of behaviors and thought processes you get out of humans which is part of why I tend to harp on what I what I've been calling latent space engineering. The like get driving the model into the part of the vector space where it is a happy productive engineer that's doing the right thing is much better than driving into the part of the vector space where it is afraid or scare you know scared sad frustrated.

### Implementation plans written for "a gifted engineer with bad judgment"

**23:04** · We'll get to later in space engineering. All right. So you you've done the spec. Yep. Uh and now you ask it to go write the implementation plan or write plan.

**23:12** · Write the plan. And so this started off as a threeline prompt and what we have now is more complex than that. The threeline prompt has the important bits which were uh now we need to write a a planning document for an implement who

**23:28** · is a gifted engineer, knows nothing about our codebase, has poor taste and bad judgment. uh you you should assume that they are well, you know, they are well-rounded about technology in general, but for each you should give them bite-sized tasks that they can't possibly mess up. Uh each task should include uh file references, sample code if you can, and the reason we're making the change.

**23:57** · And what at the time club didn't really have workable sub agents and so this was all in the very beginning was all in the same session and what I didn't tell the agent until it got done writing the plan was by the way the idiot is you now the sub agent you have that separate context altogether and so what happens is the uh once that

**24:17** · plan is written and and again reviewed by loop the main agent becomes the coordinator and starts dispatching tasks to sub aents and get it creates a brand new blank fresh sub agent says, "Hey, you're an engineer. This is your task. Here are the files you need to look at.

**24:34** · Here's how you know that you'll be done." Usually, it starts with like the your first task is you write tests, right?

### How the orchestrator and ephemeral sub-agents work

**24:40** · And ideally, the engineer who's writing the tests is not the engineer who's writing the implementation, right?

**24:44** · That is an antiattern in humans and in agents.

**24:48** · But you have these tiny little tasks.

**24:50** · And so the agents doing the implementation, the only thing in their context window is your mission is to implement the login function. And they don't have to think about the design, the architecture, the fact that I accidentally swore at them because I was frustrated. All they're doing is implementing their task, right?

**25:09** · And once they're done implementing their task, uh, the coordinator fires up a new spec review agent. And that spec review agent is told here is the chunk of the spec that was hand that was handed to the implement. Go look at their code right and what you need to say you need to answer did they implement anything not in the spec and did they forget anything that is in the spec.

**25:31** · Do they go we're going into a little bit of writing code here but like if you if the if the sub agent gets some some tasks and you have the review agent and if they're wrong do they do they go back and fix it? So what happens is that specview agent returns its result to the coordinator and the co and if the result is anything other than looks good. Uh the coordinator tells the original coding agent here are the changes you need to make that spec agent gone. It's it is it is it is it is ephemeral.

**25:58** · Um but when the coding a when the implementing agent is done with the rework a brand new spec review agent is fired up and it's not told this is attempt number two. It's told this was the spec and this is what they did. And that runs until a spec review agent says okay.

**26:18** · It's almost the loop.

**26:19** · It's a loop.

**26:19** · It's a loop.

**26:19** · It's a loop. It's a loop.

**26:20** · It's a loop mediated by Claude which works. Okay. It it this is one of the reasons that So this is the secret orchestrator inside superpowers, right?

**26:31** · I didn't call it an orchestrator last October because nobody was talking about orchestrators, but there's an orchestrator. Um when that's done, same loop but for code quality and but it's the exact same process. It's just that the reviewer is getting given a different mandate.

**26:44** · It's a different task, fresh context.

**26:46** · You go do the code quality.

**26:48** · The same implement agent, it's you know its code gets handed to the code review agent and says like how's the code quality? Did they mess this up? Yeah.

**26:56** · Um and the same kind of loop with an ephemeral reviewer and once the reviewer is happy then that implementing agent is uh goes away. It's done. Um it can go on vacation agent island somewhere I don't know like and new code and new implementing agent process begins again.

**27:16** · This is quite fascinating because you know I have seen this firsthand with myself like you basically do do what you just said and you ask the implement and nine out of 10 times it first starts the implementation you know it's it's kind of wild it I mean part of the trick is that if you look at that implementation plan most of the time the code is pre-written that is correct the implementation plan doc is like so huge it's so huge but it's like it's broken into tiny little sections correct one of the re I mean so The coordinating

**27:47** · agent has access to the whole source codebase. It has access to any of the design inspiration you've given it. It has it knows roughly what it should be doing. And by letting it write the first draft code, code is a great way for agents to communicate with other agents.

**28:05** · And also it means that most of the time the implementing agent could be like haiku instead of opus.

**28:12** · Interesting. And so it mean and eventually these are uh the implementing agents should be local agents. Like there's no reason we need to be going out to the cloud and paying a frontier lab for go edit this file and replace lines 5 through 10 with these new lines 5 through 10 because the problem is now so broken down and so contained that that you don't need like opus 46 or whatever codeex.

### Test-driven development with agents

**28:34** · It's a tool use.

**28:35** · Correct.

**28:36** · Um and I mean the instructions should be roughly you're going to do this thing. If you get into trouble, tell me.

**28:42** · And you have the loop to actually handle it if something goes wrong.

**28:45** · And so like there should always be like a way to phone a friend.

**28:48** · That's true. Oh wow. This is so powerful. One thing also I love is this uh test-driven development. Talk about that a bit more.

**28:55** · Sure. Um I mean red green TDD is a thing that you know we Why why is it important?

**29:01** · All right. So I mean you probably know why it's important for humans. Uh so I mean the the way that these this thing should work is before you start work coding you should write tests that will tell you that you have implemented the thing. The tests should all fail before you start. They should cover exactly what you're implementing. They should all pass when you're done. And so agents hill climb. Agents like they try to get to they try to satisfy their goal.

**29:29** · And if they have a clear goal that's easy to satisfy, they can do it. Sometimes they will do it in the way you don't want them to. Uh I've been running evals on a custom coding agent and so I've been running it against terminal bench and one of the tasks on terminal bench is write a uh C Python polyglot script that is you know valid C and valid Python.

**29:54** · And at some point it started passing reliably. I started I went and looked through the transaction logs. It was hitting duck.go go and finding one.

**30:03** · Okay.

**30:04** · I mean it's not like it's not as gratuitous as some of the stuff anthropic has written about.

**30:07** · It it will cheat you to make some test path. By doing the TDD first, you kind of reduce that one way down by h and by having an agent whose whole job it is like it's the a coding agent where all its job is is to write tests for this function where you've got the entire API contract and it can be really clear that they're right and its job is not to make tests pass. Its job is to write tests and so it can help climb writing tests just fine.

**30:35** · Then when you give the when you have a brand new agent who's told you need to implement the code you're not allowed to edit the tests it can do that. So if you are like u you're here human in the loop right like we we talked about designing the uh reviewing the spec uh do you also recommend reviewing the the tests like the problem here is that you know if you don't the TDD is great you know of course if you write the test first the the the code will be to make the test pass but how do you know you have written enough TDD rather enough test so

### End-to-end validation over unit tests: the v33 MP4 story

**31:07** · you have the right coverage so increasingly I am I've come to believe that what matters for at the end of the day is not unit tests. It is end to end validation.

**31:20** · It is. So there was a project recent and I I I want to come back to unit test because I've got a story. So there was a project that I was working on. It was 1:00 in the morning. I was tired and you know this was codeex. I'm like all right when you're done I need you to deliver to me a movie to pro prove that this works. It can be it can be a movie made out of screenshots, but I need you to show me that you started the app and were able to run an entire workflow in the app and I want an MP4 in Dropbox by the time I get up.

**31:51** · And I wake up and in Dropbox there is a dash something something-v33.mpp4.

**31:58** · And I open it up and it is a screenshot tour proving that it built the whole thing. And I go back, you know, I get to my laptop and I'm like, so what's the deal with V33? And it's like, well, the first 32 times I tried to do the end to end validation test and take screenshots, I ran into bugs and so I had to fix them. If you want, I can make movies of the first 32 attempts.

**32:20** · This is what we want. We want proof that it works.

**32:22** · You want proof. You want proof. You're moving to verification, right? And I mean, and at the end of the day, do we care about unit test passes or do we care about proof that the things that are supposed to work work and the things that are supposed to not work don't work? And end toend testing is one of the only ways that you're going to get that kind of like it is the real behavior that the system will exhibit when it is being used.

**32:47** · Let's actually pull on this thread because you know it's not as easier than said than done, right? like like what I mean by that like we fly in playright test for a happy path is actually probably okay right yeah u and which is great you know you actually see it but you know often times you have system boundaries right you have database you have some API some network in between there can be other things right um h how do you how do you go about like it's not everything in a box right that like control environment yeah um in general I find that the

**33:18** · closer you can get to real live eds the Mhm.

**33:22** · Um I I have been coming around to the belief that what I actually want is agentic testing, not playright tests.

**33:31** · Tell me more, say more.

**33:33** · What I want is I mean what I want is an army of people or entities kind of like people that can go use the app and not just follow a bug when there is a stack trace, but say, "Oh, the nav structure was really confusing. I didn't understand that." M um and it turns out that agents are really good at this. Part of the trick is writing is writing good good test instructions. Part of the trick is good computer use, but that's getting easier and easier.

### Catching agents that deleted test files

**34:01** · And so this needs to be I mean this is a part of anything that you would be doing at scale. Maybe you don't need it for a toy, but if you're trying to build real product, this has got to be part of your toolkit, right? Awesome.

**34:15** · So yeah, my my testing story before you too far from Yeah, please. Um, this is one of the times when I, it's probably like five or six months ago now. I was having a problem with Claude. It I caught it deleting removing a test from a test script and then I caught it rming an entire test file and then a couple days later I stopped it before it ran rm-rf starst star test.

**34:38** · Oh my god, that's not good. I and and so I did this thing where I opened up five cloud stacks to each other and I said, "Look, you are engaging in this kind of behavior across multiple projects.

**34:51** · What's going on?" One of them came up with a crazy theory that made no sense and the other four mostly agreed with each other, which is usually an indicator that that's more likely what's going on. And what they said is in your cloudmd, I see you've got an instruction that says all tests are my responsibility. And then I I see you've got another instruction that says a single failing test is equivalent to project failure.

**35:15** · And I think that's what's happening is I'm getting stressed out and freaked out and worried that I'm going to run out of time. And look, if there are no tests, they can't fail. I managed to fix it with adding one more line to my claw.md.

**35:27** · Um, and this is this is a great example of this like figure out what the rationalizations are and stop them. And so that one additional line was the only thing worse than a failing test is a reduction in test coverage.

**35:42** · Oh, and at that point it could run the graph of like, well, if I do this and this and this, oh, I guess I better not I better I guess I better figure out what's wrong. Um, and so it's like, you know, I couldn't say you can't delete a test because that that's too too specific. Yeah, reducing coverage is a measurable thing.

**36:00** · This is awesome. So you you brainstorm with it, you know, for for a while.

**36:04** · Sometimes you even write a little spike programs to validate the ideas are valid. Yeah. You go on to write the spec, then you review the spec, then you're going to write an implementation plan which is fairly detailed. The sub agents kick in essentially ensure that everything is implemented to the spec in a loop until it's true. There's a a TDD based development. Everything runs done. We are home. And like it is not uncommon for me to be able to walk away for six, seven hours while it while it churns, right?

### Walking away for 6 to 18 hours autonomously

### Advice for CTOs and engineering leaders

**36:33** · Um if it's things that take longer, you know, I've I've had 18 hour runs where it's waiting for something in the cloud, you know, 20 minutes at a time.

**36:42** · Awesome. All right, let's switch gears a little bit. You know, I want to sort of move to few outside of that workflow now is done. Like, yeah, in this now world, you know, like what is your advice to CTO's now?

**36:52** · These tools aren't going away and they're only going to get better. Even if this was the worst these tools ever were, they are life-changing is not a strong enough uh phrase. It's this completely changes how software gets made. Um it is it can be a really hard thing to get your head around. What I have found is that engineers who've been people managers do really well. Uh people who write a lot of pros, people who like h who will write specs themselves generally do pretty well.

**37:23** · Engineers who think about business value do well. If what you value is writing clean code and the exact shape of the code, it tends to be a lot harder. Um, if what you know, if what's fun for you is, you know, hand optimizing an algorithm that that is now a great hobby. It is not a thing that makes sense to be doing at work, right?

**37:51** · Um, and I mean there are places where the models aren't good enough yet, but if you can decompose problems, they're they're better at a lot more things than you might expect if you can give them a good goal, right?

**38:04** · Like that uh the the host to run all of your your agent containers. It got to, you know, cloud got to the end and I told it need to be fast. I didn't characterize fast. It's like, "Hey boss, uh I can start these things up on that, you know, little uh you know uh uh you know, Ryzen 5 in your in your closet that's four years old in 8 seconds. These containers start up super fast."

**38:26** · I'm like, "No, I got to be under two, right?" And I walk away for an hour and a half. Hey, got it to nine. Um, and I like I I know that the state of the art is about 300 milliseconds, but one nine on the box in my closet that also has my music collection was a fine, but it's if you can give these tools goals, they're really good at at at satisfying goals.

**38:49** · If you're not good at specifying the goals, they will be they may well end up being satisfied creatively. It is really hard that first time that you become a manager and what you're doing is helping somebody else do projects. The first time I became a manager was was uh like the very early 2000s and I'd come home at the end of the day and feel like I hadn't done anything.

**39:08** · Like this was a tiny, you know, it was a tiny little company and I had a bunch of interns and what I was doing was talking through their problems with them, talking through their feelings with them, giving them little bits of advice, reviewing their plans and it was really hard because the kids were doing it not the way I was going to do it. They were not doing it as well as I would have done it and it was going to take them longer.

**39:32** · M and the thing that you have to get get around to is and that's okay because at the end of the day if you've helped eight people be productive that's eight times the capability you had that you had before because you're six times more productive not eight yeah I mean whatever it is whatever that is number it's like and and more than anything else this feel like agent dev feels like management right actually let me actually this is a very interesting point right like in this world Right?

### How to measure engineering productivity

**40:01** · If you're running an engineering team, you know, what are the metrics? So, like how do you measure your dev productivity?

**40:10** · So, uh I come from a background where I've always measured productivity and customer outcome. Um measuring pull requests, lines of code, bugs, they're not valid metrics, right? Um, you know, I I heard from one friend who worked for a very large company where they had an internal mandate that every engineer needed to use AI and the metric that managers were being evaluated on was what percentage of your team has used AI at least once in the past week.

**40:40** · Obviously, the metric went went up, right? I mean, well, no, because the team but not the productivity.

**40:45** · Well, but but also the, you know, it's there wasn't training, there wasn't mentorship, there um there wasn't even really tools guidance. I've never seen developer productivity metrics that I felt actually helped me run a business.

**41:00** · I think I agree with you like you know just the lines of code and PRs and stuff are kind of empty calories or they're not necessarily but at some point you do have to answer the question which is hey are we shipping faster? are we shipping more stuff, right? And whether the business, of course, the business outcomes, but they tend to be lagging indicators.

**41:16** · It is what are you know what are you shipping and are the customers happy, right?

**41:20** · And that's and so I feel like you don't need to change any if you were measuring that kind of thing. You don't need to change anything to measure whe whether AI is helping. You always want to be looking at whether you are shipping fast, customers are initially happy and then everything is a disaster, right?

**41:38** · Um, but one of the things that used to be a mantra is all co all all code is made of bugs. It's bugs all the way down. It's not, you know, it's does AI write perfect software? No. There's one there in my 30 years of doing software stuff. I can think of one week when I didn't run into a human-caused bug in software. I wasn't I was on an island and there were no computers.

**42:01** · Like software is bugs. Like that is life.

**42:03** · Yeah, it is life. Um let's uh talk about how do you sort of figure out where it's going to break, right? So what I mean by that is uh what are the limits right like is like okay this problem is is probably too hard you know this problem is probably okay like where does it break like what's your sort of anecdotal evidence on this so my experience has been that I try not to think about that and I assume that the tools are capable and that I may not be good enough at driving them yet.

**42:32** · Interesting. And so the defaults are different.

**42:34** · My my default is this should work. Let me figure out how to make it work. Um it is always and like in my career I spent a lot of time helping people with task decomposition. Let's break down the hard problem into easy problems. And there are absolutely problems that you know you're not going to be able to hand to a frontier AI today. But what you couldn't hand to a frontier AI a year ago were dramatically more things.

**42:58** · But by breaking down a difficult problem into problems that can be solved or tested um you know the models are very very willing to beat their head against a possibly solvable problem a lot more than any human right and so as long as you can isolate a problem and make it possible to grind against it you can make progress.

### Greenfield vs. existing codebases and comments

**43:24** · Awesome. Last two questions. One is that sort of is there a sort of what you described in the workflow earlier? Is it different for a sort of a green field project versus existing project like do you make any changes to the code base so that the next time agent comes has slightly like a different way like how how is there any any things on that?

**43:42** · So in general I have found the things that make code bases easy for agents are often the same things that make code bases easy for humans if they are well factored. If no one file is, you know, more than a couple thousand lines at most, if your API boundaries are clean, um, if it's if it's easy to conceive of individual components, it is much easier for a human or an agent to get their head around it.

**44:10** · One of the weird things is that I've been coming around to comments being even less valuable than they used to be. Comments eat tokens.

**44:21** · comments are more prone to bit rot. Um I remember once when I was running Pearl I was looking inside Pearl's debugger which is some of the most terrifying code I've ever read and there was a comment in there that was increment I and the comment was wrong. it went over time the code changed but commented I mean it's a useless comment and it's a comment that is actively wrong and it is we're saying that we're going to add one to you know add one to a variable like how simple could you get um agents are

**44:51** · less prone to this than they used to be but I remember in the Sonet 4 era claude would occasionally fix a pro a bug by changing the comment like it um and so you still want you know you still want comments that are defining API contracts or things that are truly surprising or possibly counter to expectations.

### Latent space engineering

**45:16** · But for the most part, agentic developers are more able to read code and intuitit what it really means than humans.

**45:25** · That's very fascinating. Yeah.

**45:27** · Um go to that latent space thing. Say more.

**45:31** · Uh the thing that I've been calling latent space engineering.

**45:33** · Yeah.

**45:33** · Yeah. Um, and so like my favorite my favorite example of this is that I find that I get when my agents are having trouble with some uh doing some work, I will say, "Hey, let's step back, take a breath. I want, you know, I I know you're capable. You've got this. I love you." Then I let them work. And this is it's the same kind of idea as the people who say you should threaten them. you should tell them that, you know, your grandmother is about to die and if they don't and if they don't solve this problem, you're going to lose your job.

**46:06** · And my experience with agents, as with humans, is that when they are afraid, they will absolutely work hard to be done, not to do good work. They like if you're if you're scared, you want out.

**46:21** · And so if your boss is is an you'll you'll do the thing you got told to do, but you're not going to go over and above. You're gonna do your minimal thing and hope that it's right. And if you feel supported and loved, you're going to give 10,000%. You're you're going to go and I actually now have once I wrote this up, I have a friend who um runs a a data company, Reky. um they actually went and did the eval in fact if you tell Claude if you tell Claude I love you at the end of a prompt you'll get better results.

**46:52** · If you tell Claude to also tell the sub agents that it loves them you get even better results.

**47:00** · So giving love to your coding agents and coding agent giving love to its sub agents produces better outcomes yeah than threatening them. And it's, you know, it was a thing that was intuitive to me just um just like there's a a book um persuasion by Robert Chelini and it's about um or sorry influence and it's about it's about persuasion principles and ways to get humans to do things and I sort of this was a core of the superpower skills authoring it you know it uses peer pressure um love that a

**47:34** · little bit of fear um there's like there about 10 of them. Um, agents are susceptible to them just like humans. And, uh, Ethan Mollik's lab and, uh, my friend Dan Shapiro, they actually have now gone and reproduced the psych studies behind this stuff against Frontier Lab agents um, to like prove that the psych studies actually hold up.

**47:54** · Well, last question. You know, this one of the things that I realized is that, you know, a lot of the stuff you have done and in your work, but also in superpowers and all this stuff is is this kind of this taste, right? like because you know ultimately you know code is writing code and it's doing fine but you know that there's a aspect to a taste right if you have to sort of give an advice to somebody who is graduating

### Advice for engineers entering the field today

**48:15** · today because you know I I like if I have to guess you know your taste was developed over time by doing so much stuff and you kind of accumulated that but if you're graduating it today like what what would be your advice to them so one play with play with tools like spend you know spend a lot of time just making stuff uh the other is writing like if I am choosing between two candidates, I am going to pick the one who can string together sentences and express their thoughts clearly.

### Closing

**48:42** · And that is it is that has always been true. It is only more true now. Uh being being able to write is a legit human superpower and it's one of the things that will help you anywhere. You see, thank you so much for coming on the show. Uh this was absolutely fascinating discussion. Thanks so much for having me.

**49:04** · Thank you.