---
title: "Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers"
source: "https://www.youtube.com/watch?v=57lDpTwiW6g"
author:
  - "[[Y Combinator]]"
published: 2026-05-08
created: 2026-05-11
description: "We're entering a new era of software where a single person, working with AI agents, can build products that previously required entire teams.In this episode ..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=57lDpTwiW6g)

## Transcript

### Will you control your AI?

**0:00** · I think that's like the defining question like will you have control over your own tools or will your tools have control over you? Using OpenClaw these days is like driving a Ferrari and it's like exhilarating. It's insane. Like you get to do things like it figures things out you would never think a machine could figure out and it does it so quickly.

**0:20** · But then it's also like a Ferrari and that you better be a mechanic. like it's a Ferrari that will break down on the side of the road, you know, when you most need it and you need to get out with your wrench and pop the hood and like f fix it, you know, you're gonna have to fix it yourself. And so this is a very exciting time in uh computer science and technology.

### Coding again after 13 years

**0:47** · Welcome back to a special episode of the light cone. In this episode, we're going to talk about how Gary Tan got back to building. If you follow us on Twitter, you'll know that after a multi-year hiatus to become an investor, Gary Tan is back to being a builder. And in the last couple months, he shipped hundreds of thousands of lines of code and built popular open- source projects that have gone from nothing to more than 100,000 stars on GitHub. And he did all of this while having a very demanding job running YC full-time.

**1:15** · A lot of people on the internet don't even think that this is possible and are somewhat like in disbelief, but it actually happened. We know because we were here to see the whole thing. And so today we're going to talk about how he did it.

**1:27** · Well, I'm relatively uh shocked myself.

**1:30** · So I'm amazed as well. It was 13 years of not coding and then suddenly boom, I'm doing about 400x the amount of work that I was that year. The last time I was even sort of like twothirds of the time writing code. Maybe to start things off, how about we go back to the project that started it all off, which was Gary's list. Oh, yeah. And just like talk about a few months ago how you powered up Cloud Code and like started to get back to coding.

**1:54** · It was right after one of the Lyon episodes, right?

### Rebuilding a startup with Claude Code

**1:56** · Oh yeah, definitely. I realized that I wanted to bring together all the people who believed what I believed um particularly for California. And so I started a uh 501c4 and now it's a C3 and a pack which is sort of what a lot of political groups do. Um it's a very common way to bring people together. You know, everyone focuses on the money but we're trying to bring together smart people.

**2:21** · Um you know what I learned in the years of working in San Francisco politics is that bringing together people is so powerful and uh that's what a mass social movement is. And I said, "Okay, well, why don't I just make a website where we start doing that?" And it would just start with um why don't I start writing about the issues that I'm worried about? It's like I want children in school. You know, people watching this from all around the world might find it very very strange.

**2:48** · Like I find it strange that uh it was not possible and still very very hard for a seventh grader or eighth grader in middle school in San Francisco public schools to be able to take algebra. And that was, you

**3:05** · know, a math education thing. like you know if I didn't get to do that when I was in public schools in the East Bay of the Bay Area there's no way I would have studied engineering at Stanford I never would have written code I never would have been able to do any of these things so it was close to my heart and I realized like hey it's time to write code and I ended up building Posterous my first YC startup from 2008 what what was Posterous for people who don't remember it yeah Posterous was dead simple blogs by email it grew to be a top 200 website on the internet and then Twitter ended up buying it for about $20 million.

**3:35** · So that was sort of like my first bag really. I actually built it again uh as Post Haven when Twitter um you know bought it for the amazing people that we had hired and uh they shut down the startup. It would have cost a couple million dollars to buy it back from Twitter and at the time I had no money in the world. So the next best thing was why don't I write it again? And then uh in January of this year I ended up writing it a third time.

**4:04** · um only, you know, the first time it took about, you know, $4 million and, you know, six or seven people and about a year and a half. And then the second time it, you know, took about, I don't know, a h 100red grand and two people, me and my co-founder Brett Gibson, who now runs initialized, um, and maybe like three months or so.

**4:26** · And then in this case it took about $200 which was my Claude Code Max account and probably five days fullfeatured blog platform does everything you want and then on top of that like full rag full um agentic retrieval like be able to you know sort of go out and read all of the internet like every tweet I've ever done recursive crawl deep research of any topic. The algebra thing is just one of a whole lot of different issues that we really really care about.

**4:56** · And to be able to go ingest the internet, you know, see all the arguments for and against and then to craft incredibly detailed um reports on the back end about um what are all the quotables like I think people who are big followers of the Lyone might remember one of our first episodes about agentic uh systems with Jake Heler actually.

**5:19** · So Jake created case text and he described exactly what I ended up building for basically journalistic uh long- form articles about any you know sort of issue or uh you know piece of news that was happening. And so you know anyone can go to gararys.org work today and you know we do about two or three relatively you know researched all fully sourced um articles about what's going on in California and San Francisco and LA and like how do we build a better government.

### Software that thinks like a journalist

**5:50** · This is the thing I feel like people missed about Gary's little don't fully get is that it's like the classic thing we've been talking about here which is like software was you build software to let people use it. So it's like you build a blogging platform and people like write blogs and maybe like they start their own substacks eventually or they write articles. But Gary's List is both blogging platform but it actually does the work of a highquality investigative journalist. It's not just something that a journalist uses to publish their articles.

**6:17** · Yeah.

**6:17** · I mean basically the for the equivalent of like5 or $10 of Opus calls. I mean, I would estimate that it does the work of like, you know, a real human being that would have to like go painstakingly through dozens of articles, read entire books about certain subjects, uh, annotate them. I mean, going back to the case text example, like the thing that Jake taught me was that you need to think about what a human would do with the context given.

**6:46** · Like, what would it retrieve? Like, does it go to the library? What kind of book would it look for? what does it search on for search you know on the web I mean the great thing now is like you don't have to just do that like you can get perplexities API and you can do deep research there you have X's API you can do deep research there you know Grock's API if you need to like do research on X using the Grock API is actually very very good and you can just grab all of the context this is sort of going back to the philosophy of uh boil the ocean

### The rise of “tokenmaxxing”

**7:15** · which is one of my essays it's like particularly when building agentic software now You don't have to settle for um what we did when we were humans writing the code like and that goes for research as well. What if you absolutely boiled the ocean like what is you know the total completionist like if you were a human this would take you about a month to do this research you can just you know zap the rocks harder. uh you know you pay more money and you might be

**7:44** · token maxing but you should token max like basically if there is incremental work that makes something more complete more awesome more you know in the case of um this type of writing like we want it to be more representative of reality

**8:00** · like you know we don't just settle for one source when we can get 20 sources and we can cross reference them we can figure out like well these 13 sources say this and the seven sources disagree with that and then you know you want to feed all of that context into like your core prompt and then you can basically

**8:18** · make a better decision than what you would like just you know a human being clicking on a link reading a headline and that's all you understand and I think if you token max like that's actually the coolest thing you can do now and it's not just in you know generating articles it's not you know it's clearly in uh writing code right I think now it's it's going to permeate every part of society like every thing that we would call knowledge work could be token maxed and um I don't think that it means that we're going to get rid of people.

**8:49** · I think it means that people need to still supply uh the agency like I need this like I'm the one who's sitting here caring about algebra like I want kids like me who couldn't afford private school you know San Francisco is the one city in the world that has the highest rate of private school attendance um probably in the entire country actually and that's not okay like you shouldn't have to be rich to have a good education and you know I don't know why that's controversial and so for me it's like this you know mass

**9:20** · sort of shift in technology was happening and then uh I had a need and a want and a desire and it was a burning desire like I it hurts me and pains me to think about 10 12 13year-old kids who don't know algebra and like could have but uh some bureaucrat or you know some virtue signaling person in power says like actually I don't want that kid who wants to learn algebra to learn it.

**9:45** · So I think in this process of basically solving your own pain and need from the young Gary and building Gary's list, you sort of discover a lot of patterns on token maxing and this new way of building that led you to the next project which was uh GStack.

### The accidental creation of GStack

**10:07** · Like I actually did not plan to make GStack. All I did was like I uh realized that I was doing the same things over and over again and then I got sick of typing the same thing. So I went into my Apple notes. I typed in all the things that I found myself writing over and over again into Cloud Code and it was pretty simple stuff. It's like here's the plan review. One of the things I started doing is I really love asking Claude to make asy art diagrams.

**10:34** · One of the things I discovered is um sometimes Claude would just get confused and like write bugs or not be complete. But once I started saying actually before you start your work make an asky diagram of all the data flows, all the inputs and outputs, what are the user flows, what are the error messages and you can see this it's like data flow, state machines, dependency graphs, processing pipelines, decision trees. Once it did that, it loaded all of the context in and then it just did the work more completely.

**11:06** · Like it boiled the ocean better and it broke down into a bunch of different sections. Like here's architecture review, code quality, test.

**11:14** · I mean, one of the things I learned building Gary's list was that when I was writing the code myself, I would always do the minimum amount of testing cuz it was just like not very fun. I knew I needed to have it, but I'm here to write, you know, fun new code. I, you know, did not like write to write tests.

**11:30** · And then honestly, like I hit all the things that everyone else hits when they start vibe coding, which is like this is slop. It's not working that well. Like it works fine for the 80% case, but if any users actually touch it, it starts falling over. And then that's when I realized, oh, I can get to 100% test coverage. I've since learned that 100% is probably too much. Like hitting 80 to 90% is usually the best practice at this point. Um, but yeah, this this is basically the first version of plan-ge- review.

**11:59** · I know, uh, everyone knows the office hour skill, uh, which is, you know, what people can use and I still use when I'm trying to make a brand new product or a brand new feature. It, uh, simulates what what we do when we're working with a company. It's like, how do you know that people want this? You know, who's it for? What does it do? And what's the impact, right? But this is like the proto skill. Like, this is I didn't even know skills existed. And I posted this and it went viral. Like, you know, 200,000 people saw that. And then I made another version of it that was a much more ex uh expansive version.

**12:31** · I called it the mega plan. And then I ended up um renaming it to the CEO plan.

**12:38** · We've probably talked about metaring before. I used metaprompting here. I took the other review plan that we had and then uh I said, "Okay, well, let's do a version of this, but like imagine Brian Chesy sitting with you, right?"

**12:52** · Like Brian Chesy has this great line about uh what is a 10-star experience.

**12:57** · So and you know the point of it is everyone thinks about hotels in terms of like three this is a two three star experience this is a fourstar experience and he like goes you know through the list like five stars. It's like everyone, you know, yeah, cool. Like, but he's like, "What's a six-star and what's a sevenstar and what's an eight star?" And like he goes all through that entire list. And um that's one of my favorite like product and design exercises to go through like as a mental exercise. And then the cool thing is like you can do that every single time now. And so that's what this is.

**13:25** · You know, this prompt basically tries to figure out what is the platonic ideal of uh what this is. These are sort of like the three the two things that are pretty awesome. one is uh what is the 10x check? What is more ambitious and delivers 10x more value uh for only 2x the effort, right?

**13:46** · And so for whatever reason coming out of latent spaces helps the model like really visualize like so I'm plan CEO skill I actually really enjoy because I'm an ADHD C CEO and I love um potential like pure potential and so this is like the one like I can't believe this is just literally two little sentences but like this unlocks an incredible amount and so that's how GStack started actually not as you know

**14:13** · I didn't want it to be anything other than like well I need to make some skills and I had heard that people were making like skill repos. But then the third thing I did was I started um using these two skills so much that um my conductor instance was getting very backed up. So this is how I use conductor. Uh this is actually my real setup like so this is your like daily workflow.

### The workflow behind 400x output

**14:36** · This is how you've been shipping hundreds of thousands of lines of code a month. It's all it's all in here.

**14:40** · Yeah, that's right. So, I dropped like 13 PRs in the last 48 hours and then, you know, I you just ceue them up. Like anytime I come up with a new idea, I come in and uh here it is. You know, I love using the CEO skill. I loved using the skill to like really make it super well tested. I did that all in plan mode. Uh and then I'd click approve here and then, you know, Claude would go and do all the stuff. And then I did that so much that I ended up having like 15 different features that were all queued up waiting for me to manually test it.

**15:14** · Like it passed it, you know, it passed end to end testing, it passed uh integration, it passed unit tests, but like at the end of the day, I still need to, you know, for Gary's list, it's like pop open the Rails server and like, you know, load that user and like make it into that configuration for that particular user and like manually just make sure it works. And I got sick of doing that and I was trying to use um clawed encode MCP and it was very very slow two to three seconds for every turn.

**15:44** · I was like this is not usable for QA but I had heard that Microsoft had released playright which is sort of um an alternative testing framework. In retrospect it's like actually there was like agent uh there like agent harness and like all these other like tools that I could have used. But the upside and downside of Claude Code is it's so easy to just start something that I just popped open like I literally went in here and this is probably what I did.

**16:08** · It's like I'm so sick of using Claude Claude in in Chrome MCP. It's too slow. Let's go ahead and wrap Microsoft's playright. Can we do that? And then I just pressed enter. And then, you know, one of the things that emerged with GStack is that like this is how I create new features. Now, of course, you know, what it's going to do now is like, "Hey, dude, you already did that." Which is hilarious.

**16:37** · You know, I have bug fixes right next to giant features. And then, um, the way GStack works, there's a CEO, there's a designer, there's actually a developer experience person in there. There's a number of design tools, uh, and then Plange is the last one. And then I actually usually run SLCEX. And um I recently added a slashclaw in codeex.

**16:58** · So one of the cool things that I actually learned from uh YC alums I came to an event and brain totally frazzled but you know went to one of our batch events and we were just you shooting the about what was going on with claude code versus codeex and at the time I was a total claude code only guy and uh I realized oh a lot of people actually prefer codecs. Why is that? And I discovered that claude code is ideal for the ADHD CEO, but once in a while there's a, you know, claude code will just BS a bunch of stuff.

**17:28** · Like claude models are very very good, but like they are not the smartest, it turns out. And so a lot of people, you know, explained to me that if you have a problem that's much crazier. You need the 200 IQ nearly nonverbal CTO. So you can just call in a friend and then that's what like /codex is.

**17:47** · It's a, you know, GStack skill that takes whatever plan your plan is or if you're out of plan mode and you already implement it, it'll take your repo and it'll run codeex in a command line prompt with the prompt that says find all the problems and all the bugs and it reports it back to cloud code and then you and cloud code can work through those feed that feedback. Uh, and then I have since added if you use codeex as your main coding agent, you can actually go and type slashclaude and have Claude come and be the CEO briefly if you want as well.

**18:19** · The cool thing about GStack is when I run it through this program like I always I do I start with office hours CEO review like I do design if there's UI if um I know a developer needs to use it which is like practically all of GStack and GBrain stuff I run the developer review and then I do review and then codecs once that plan is done I've worked through all of the issues the GStack relies very heavily on ask user question so because you know and that's that to me is like really important that's where the human, you

**18:51** · know, vibe coder, operator, agentic engineer needs to supply their understanding of what's going on, what are we building. There's not really a substitute to that. It would surprise me very much if someone really truly did manage to make a thing that could just make software without the human in the loop like that. You know, it's controversial take, I think, but um I never want to be entirely out of the loop. I just want the machine to do the stuff that I don't want to do. And so, you know, basically QA is a good examples.

**19:21** · And, you know, I mean, that's hilarious. Coming back to the demo, it's like I type something into the modern version of GStack and it's like, dude, what are you doing? Like, we already built that. We have browse. Browse is a longived HP demon with 70 commands as a CLI. And then QA is just browse. But, um, in the prompt for QA, it says look in your context. What did we do on this branch? if there's UI or any mutation of data, go and use the browser to test that thing, which is cool.

**19:51** · It's like having a blackbox browser. It blew my mind when it first worked. It's like mini AGI is already here. You know, I you know, I realize this is not true AGI. True true AGI would be like I'm not even here. Um, and actually that's fine in this respect. Like as a builder, you know, selfishly, uh, I hope that we never have to stop.

**20:14** · I hope that the machines never figure it out cuz that would be really cool. Like then, you know, humans are really important and like engineers who know how to do this, who have taste and design and product feedback and um you know, the real customer in mind, like we're going to be like we basically have wings for as long as we do. YC Startup School is back. We're hand selecting the most promising builders in the world and flying them out to San Francisco for July 25th and 26th to discuss the cutting edge of tech. Apply now for a spot. Okay, back to the video.

**20:45** · I think you crystallize a lot of these thinking in this post on X about thin hardness and fat skills.

**20:54** · Oh yes, which actually encompasses all of this philosophy on how to token max.

### Thin Harness, Fat Skills

**20:59** · Yeah.

**20:59** · I mean, some of it came out of uh being trolled on the internet relentlessly about markdown and like I you know, I'm just like peddling a markdown instead of markdown and it's like, you know, I guess my lived experience at this point is that markdown is actually code. It's just like this compiled in a different way, but like you can get the computer to do really astonishing things. Like I mean even this it's like could we have imagined that I would be talking to something that has replaced Visual Studio for like I I don't use Visual Studio at all.

**21:28** · Like there's no reason to like when I can talk to my agent and my agent can do this, right?

**21:33** · The article actually the name actually came from uh our partner Pete Kumin. We have had to build an internal agent and you know we call that the harness over and over again and then at some point using cloud code all day we realized like you know why should we rewrite a

**21:50** · version of that over and over again like you know we should just use the things that are really awesome as you know harnesses like a harness is the core loop that takes the user input gives it to the LLM runs what the LLM does like it can do tool calls and things like that I mean why would we build that like what we should spending all our time doing is thinking about what markdown should there be?

**22:11** · And the way to think about markdown is if you were an event planner and throwing a wedding and you were trying to write down a checklist of how to throw a wedding again, like what would you what would you write in plain English to teach the next person who had to do it what to do? All of that should be in the markdown.

**22:28** · Whereas um all the things that should you know be deterministic like um I mean or is is a real action like a a wedding planner might have to call like 20 venues right but you wouldn't use markdown for that like you would make a you know a call to Twilio for instance right there's like a you sort of all of the difficulty in enantic engineering today is when people try to do things that should be in markdown in code and it fails because code is brittle it doesn't understand special cases.

**22:59** · It actually you know code literally doesn't understand what you want or who you are. It is like you know executing deterministic zeros and ones in a touring complete loop right like it doesn't know but then now we have LLMs that have latent space and they know who you are and uh it knows what your motivations are and it can handle generic cases and then you know a lot of

**23:25** · the the magic right now as an engineer is like figuring out okay how much of it is over here in LLM land and how how much of it is over there in um code land. And then you know if you combine that with the other thing I learned which is like get to 80 to 90% tests like if it's not tested and you're just throwing users in there like it's slop you know 10x worse than like human written code cuz like you just have no idea what's going to happen. Um and so that's like one of the things that people have to do.

**23:57** · It's like all right, not only do you need to figure out what's going on in latent space and deterministic space, you also have to make sure that like it's, you know, unit individually tested and then the integration is tested. And then going back to uh boil the ocean, like the machine doesn't care, it'll just do it.

**24:13** · It's amazing. like just zap the rocks more and you can get to 90% test coverage and then you can have a system that you know is not quite perfect like you know openclaw right now um there are lots of like failure cases but it's 95% there you know it's uh I feel like using openclaw these days is like driving a Ferrari and it's like exhilarating it's

### AI agents are like Ferraris

**24:35** · insane like you get to do things like it figures things out you would never think a machine could figure out and it does it so quickly uh but then it's also like a Ferrari and that you better be a mechanic. Like it's a Ferrari that will break down on the side of the road, you know, when you most need it and you need to get out with your wrench and pop the hood and like fix it. You know, you're going to have to fix it yourself. And so this is a very exciting time in uh computer science and technology cuz it's like this is Homebrew Computer Club.

**25:02** · Uh, you know, the moment when the Apple 1 came out, like the Apple 1 created by Steve Jobs and Steve Waznjak was a breadboard inside like literally a wooden case hammered together with like nails and duct tape, you know, and uh if you wanted a personal computer, that's what you had to do.

**25:23** · And that's where we're at right now. like you have relatively, you know, smart technical and, you know, people who had to study computer science have to spend like two or three hours and like maybe like $500 or $1,000 in both tokens and cloud to actually get something like that running. But like once you get it, it's like we're sort of in the kit car Ferrari phase. It's like then you can drive and you can go anywhere and you know you want you want to shout to the hills like, "Hey, I got a Ferrari."

**25:49** · Even the part about fixing yourself, I feel people um it's just like one of those things until you've like pushed through, you just don't quite get if I really zoom out, it's almost like things have moved so quickly. Like if you think way back, just having Stack Overflow as a website that you could consult when you got stuck on a programming problem felt like amazing. And then it's like like chat GBT launches like oh now I've got this like interactive thing that's way better than Stack Overflow.

**26:13** · But you're still sort of doing the same thing. and you're like asking questions and you're copy and pasting code and you're running the code and seeing what happens and copy and pasting it back and then you sort of with clawed code you sort of push through and you realize you don't need to do the copy and pasting anymore.

**26:27** · It just like actually like executes and runs the code and even with open core I found out when I set it up yeah it's annoying because it can like effectively brick itself and it does a bunch of annoying things. But if you actually have like clawed code like it'll fix it.

**26:39** · Yeah.

**26:39** · I just have clawed code running it will just like fix it and it's clearly not the way things will be long term. But there's this like mentality shift of it doesn't actually matter if it's brittle and requires fixing because you can actually just have another agent like sat there like fixing it all the time.

**26:53** · Yeah, I feel like this evolution I was like completely clawed code pill uh and still am but like probably only like 50% or 60% of my time like building product um or agentic engineering is in cloud code now at some point basically almost half of it is through opencloud now.

### The future of personal AI

**27:12** · Yeah.

**27:12** · Which is very interesting. I mean then again I'm also spending a lot most of my time working on Gbrain itself. So GBrain came about because I met you obviously we had Peter on the show. Um and then I finally got around to it. It was like one weekend I said I got to check this out like what's going on with OpenClaw. Let's get it going. And um this was about the time Karpathy wrote his expost about knowledge LLM wikis.

**27:37** · And so I was like, okay, well, I have a repo full of markdown. All my, you know, I should put all of my context into that markdown. And then at some point I realized, oh shoot, it's just using GP.

**27:48** · And GP is not that good. Like it's, you know, wasting context. It's loading a lot more into context than it needs to.

**27:55** · And then I sort of fell into a rabbit hole. I just went into conductor, click quick start, and then I had GStack built into conductor already. And you know, basically this was how I started. I you know it was actually much more interesting than that. So uh I didn't start off from nothing. One of the things I've learned as you write like a larger and larger corpus of code is like you have it loaded in your brain.

**28:18** · You're like oh well in order to build an agentic newsroom for um Gary's list I actually had to learn about uh vector embedding and hybrid RRF and chunking. like when you're in there trying to make it work, you're just like very applied. It's like I have an output that I want.

**28:38** · I want the article to look like this. It needs to be of this quality. It needs to have these citations. Like you start building up uh your you know your tests and integration tests and like you end up with like a product that's like battle tested from like the output that you want. And so I sort of put two and two together. And I you know and this is something that you know anyone can do actually. It's like this. This is why I think we're entering the golden age of open source.

**29:01** · Uh I could just open you know this project in conductor and then the first thing I write is like you know go look at you know tilda/garry's list like look at how we do chunking embedding uh you know hybrid RF rag like all of this and then just like extract it and then I want to use Postgress with PG vector and like I want a a you know full rag system for my open claw and then sort of like one thing led to another.

**29:33** · It's like then I have, you know, 10 windows and Gbrain and I'm just like at it. What's cool about OpenClaw, I mean, maybe this is a good example. This is actually my open claw. I did go ahead and ask it's um how, you know, how did I actually get into it? January 23rd.

**29:48** · Also, all your emails.

**29:49** · I had a tweet that was like, Claude Code this week has awakened my 25-year-old self, the one that checked Red Bulls and stayed up till dawn coding. We're so back.

**29:58** · The builder identity resurfaces.

**30:00** · Yeah.

**30:00** · And you know, I'm basically back to, you know, sleeping 4 hours and, you know, coding 20 hours a day. You know, this is also when I started getting myself into trouble like talking about lines of code. I still believe this, by the way.

**30:12** · Yeah, this might be like a good quick aside to talk about like this this idea of like lines of code being important measure has been like controversial on the internet. There's obviously the counterargument like, oh, lines of code doesn't like measure developer productivity, but it doesn't, right? But it also does. So, It also kind of does, right?

**30:31** · Yeah.

**30:31** · Like it does. It's clearly And you know what's interesting is you can actually um there's wellpublished git repos out there that you can run to uh strip away and like standardize what is actual logical lines of code. And so I actually did go ahead and do that. Um you know, and I got into trouble for saying like, oh, I'm coding at like a 100x uh the rate that I was in 2013. And then after I did the logical lines of code strip down um it actually went up.

**30:59** · It actually went up. So it turns out that I was actually doing 400x the amount of code. But you know obviously I wasn't writing it. I was directing you know 15 agents at a time to do so. And then by the numbers like it was not that it did like knock down my lines of code from cloud code a little bit but uh the surprising thing to me was that it knocked down the amount of lines of code that I was writing in 2013 by like 70%.

**31:27** · And so I think that that's sort of the mismatch here. Like people get very upset because it's easy to like pad the lines of code if you're a human writing code. Whereas like unless you direct claude code to literally like pad the lines of code, it doesn't necessarily do that. Like it'll maybe build the wrong thing. Like you might not steer it very well. It might not do the right thing.

**31:53** · But like it's not trying to optimize for lines of code the way a human working a job would, right? which is you know that's just life and then I guess the really surprising thing is if you look at the literature about software engineering going back to like 2000 1990

**32:08** · I mean it's pretty clear that the average number of lines of code that a professional software engineer that's like tested and production ready it's not like a hundred lines of code it's like 50 it's like 30 like a day yeah a day right like for me it was like 14 but I was like part-time I don't know it's So that's where the 400x actually came from. You know, the other thing I know is like I should have said that instead of just trolling people more on the lines of code. So I, you know, if I trolled you on the internet, I'm very sorry for that.

**32:38** · Like there, you know, there is a deeper understanding of this.

**32:42** · And I did end up releasing a blog post about it that um explains this quite a bit more. I mean, and I think it's not a little bit significant. It's very significant for people who are technical because it actually raises the bar on like what you're capable of doing. Like all the people who are attacking me about lines of code, they particularly are the people who are most likely to get wings if you like let it rip and token max. This is sort of like the classic problem.

**33:09** · It's like if you have taste and you understand technology, you are particularly the people who should would benefit the most from getting this. all someone has to do is, you know, believe, right? So, stop fighting, just open cloud code and try it. You know, I think another thing that's potentially going on is just like the experiences vary dramatically depending on like the the models and the harnesses.

**33:32** · Um, like certainly something I've noticed is any sort of like semi complicated programming task I try and do through my openclaw agent just like kind of fails.

**33:47** · like it's exactly the same model and so like Opus 4.7 as clawed code but it just like like anything above like a simple script I just find like it's not like that great at so I'll go back into like clawed code and then it was sort of a moment for me where I realized oh like this is how it used to feel like this is how like even 6 months ago it used to feel like oh like you try and like these things yeah these things aren't quite there yet and then claude code with like opus 4.5 was like oh like it's actually like here it's about to recur.

**34:16** · Like right now, people sort of are feeling like OpenClaw or Hermes is like not quite there or it's like a lot of work. And then I guarantee you like this time next year like everyone's going to be saying what you heard here first, which is like every single person on the planet will have their own personal AI. We could either live in a world where we have our own AI, where we have our own data, our own integrations, like we see what's happening, we write our own prompts, and we have control over what we see.

**34:46** · Uh, or it's corporate controlled. It's something, you know, you go to a host, it's kind of like your Facebook feed, and like you don't know what that, you know, who wrote that algorithm and who does it benefit and like what business model is behind it. Like nobody knows.

**35:03** · the most powerful idea that like was a gift was the personal computer revolution and we're about to go through exactly that same shift with personal AI and it's going to be a choice like you know people are going to have to figure out am I willing to write my own prompts and you know I think I wish Pete Khan were here like that's one of the things we learned from him too it's like unless you have your own prompts and you can write it for yourself like you are you

**35:32** · know below the API guideline for some PM or developer that is not you who like will not understand you will not understand your needs will not understand what you uniquely care about and I think that's like the defining question like will you have control over your own tools or will your tool your tools have control over you and I think this is the one of the disconnects that the public has I think

**35:58** · is a lot of uh these capabilities you have to be on the latest and greatest models And it's actually quite expensive to use them and burn all the tokens for now.

**36:09** · It's coming down, but I think maybe people are just trying like set or the free model or having the basic claw pro subscription only.

**36:18** · Yeah.

**36:18** · And part of is maybe we have to address that this new way of really getting all this almost ASI AGI moment for for building is you have to be burning lots of tokens. the whole token maxing paradigm.

**36:32** · It actually reminds me of rent. San Francisco rents. Like one of the things that I feel like we always have to do um with YC founders is that it's like a general thing. I was like, "Oh, like I don't want to move to San Francisco because it's like so expensive to live there, but it's like it's so expensive to not live there."

**36:47** · Yeah, exactly. That's the whole point, right? Like early on in a YC batch, like I'm used to like a fan of being like like this like this apartment is like thousands of dollars a month in rent.

**36:56** · Like seems ridiculous. Like should I like pay it or not? And it's like, no, you should absolutely pay. And if anything, you should pay more to not just be in San Francisco, but be in like the dog patch and just like be in like neighborhoods where you create this serendipity. Like token maxing is going to be one of those things for founders that we sort of have to teach them where it's not immediately obvious that you shouldn't. This is actually like rent.

**37:16** · Like this is one of the things where you should like spend as much as you can to like get the like most utility out of it versus treating it like the office desk or something. Like sure you can economize on that or you don't need like a super expensive like couch, but like when it comes to like actually using the models and your token spend, you should probably be like pushing pretty hard on that.

**37:37** · Yeah.

**37:37** · One of the key maxims for YC is, you know, how do you find good startup ideas, live in the future, and build what's missing, right? And so this is a profound version of that where all you have to do is commit your brain to look at, you know, spending $500 in a single day on tokens and say actually like, you know, as long as I'm building something that's actually of great value to me, you know, and I'm building the right thing, uh, I'm going to do that.

**38:06** · Gary, I have a weird question. Do you think that in some ways the fact that you tried to build all of this while also being the CEO of Y Cominator actually helped you because like your time is so scarce you had to like try to figure out how to write hundreds of thousands of lines of code with just like spare minutes in between meetings unlike a a full-time software engineer that could you know just take the time to like open the website and like click around to like test it. like those minutes were like insanely scarce for you and so you were constantly pushing yourself to figure out how to like automate everything.

### Buying back time with tokens

**38:37** · Yeah, I I envy time billionaires, you know, sometimes look at I mean I'm look at my kids and it's like these kids are time billionaires right now, man. Like you know, you could just like do you know you we run across people at startup school all the time and it's like you're a time billionaire right now. Like this is incredible. Like you could just do any you like learn about anything. This is so great. So yeah, you know, personally like I think my philosophy is I am in a crazy rush in my brain. I'm like probably live 10 billion lifetimes to live in this body right now and I need every single moment to count.

**39:05** · Uh and then if you can token max it's like I mean you could buy millions of years of consciousness of machine consciousness. Now I can be a time billionaire. It's not you know my own time. It's the time of a machine like doing work for me and like the human entities that I care about working on the causes that I care about, right? I care about YC. I care about builders being able to build.

**39:32** · Even in a lot of our internal meetings last year, remember in our offsites, we would talk about like how do we teach the next generation how to use these tools? And so, you know, I'd like to I wish that I could say like that was all a part of the grand plan and that's how it started.

**39:48** · It's not like but you know subconsciously I actually think it was like I think subconsciously from doing Lite Cone and like talking about this stuff like sitting side by side with uh Boris Churnney right here was a very powerful moment for me because I realized like he's he started saying things that like I could do myself. It's like he said our team doesn't write a single line of code. I'm like oh actually like I can do that and like the people who are watching right now it's like you and I are not different right?

**40:18** · We're the same. Like we started in the same place. I don't think of myself as like, you know, in the sky yet. Even though people seem to talk like I am, you know, like I'm just a person trying to do a thing and if I sit next to Boris, I'm like, you know, this guy is one of the best engineers I've ever met.

**40:36** · But also like if I just open a prompt, we have the same prompt. We have the same MacBook Pro. And you know, there's nothing that stands between like me or you or any of us from like drawing on millions of years potentially of like tokens to like serve humanity.

**40:55** · Well, Gary, I think that was a beautiful quote that should be retweetable. It's just got to get it on X right away.

**41:03** · You could have infinite time by borrowing the time from the machines.

**41:06** · Yeah, what a time to be alive.

**41:08** · That's a beautiful thought to end on.

**41:10** · Thanks Gary for showing us the future.

**41:12** · Thanks guys.

**41:12** · Thanks Gary.

**41:13** · All right, thanks for watching and we'll see you on the next episode of Lyone.