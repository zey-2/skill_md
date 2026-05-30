---
title: "How the engineer behind Claude Cowork actually uses Claude | Felix Rieseberg (Anthropic)"
source: "https://www.youtube.com/watch?v=-tdNsYi8AXs"
author:
  - "[[How I AI]]"
published: 2026-05-25
created: 2026-05-30
description: "Felix Rieseberg is the engineering lead for Claude Cowork and Claude Code Desktop at Anthropic. He previously spent five years at Slack building developer to..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=-tdNsYi8AXs)

## Transcript

### Introduction to Felix Rieseberg

**0:00** · AI is used poorly if it just needs to move the mouse cursor for you. I want AI to do a bunch of annoying things in the background to free you up for your creative energy.

**0:09** · The biggest gap that I see, it's not the capabilities of the tools. It is literally people being able to understand that almost any problem can go into these tools.

**0:19** · I have built this little thing which is just like a teeny tiny claw on a little stick. And this stick has Wi-Fi, has Bluetooth. I want my little claw to live on this thing. And I wanted to cheer me on every single time I do a good job.

**0:31** · And also every single time I need to approve something that Claude is doing, I wanted to be on this big button that is out here. Claude has built all of that in one shot. I needed to correct absolutely nothing.

**0:40** · My 9-year-old is a daily active Claude user, but he's decided he's really into cyber security. We're like very hacker adjacent here. And so he's truly clawed on one thing, the terminal other. He's like, "Mom, do you know that your device ID is this?" A truly magical thing is happening with kids because they've never learned what not to ask for. And I think our generation, we're very used to things just not working. So we've been living in this mind prison for many years.

**1:07** · Welcome back to How I AI. I'm Clarvo, product leader and AI obsessive here on a mission to help you build better with these new tools. Today we have Felix Reeseberg who leads some of our favorite cloud products over at Anthropic. He's going to walk us through how you can solve almost any problem with Claude and show us how for just $20 you can build your own hardware Claude Buddy that you can smash a button when you need to approve things. Let's get to it. This episode is brought to you by Magic Patterns.

**1:37** · Today's engineers use cursor and claude code to ship features in hours that used to take weeks. If you're a designer or PM, you've probably felt a shift, too. the pressure to move faster, validate sooner, and keep up with the team that's operating at a completely different speed. You've already tried AI prototyping tools to close that gap. But if your prototypes don't look like your actual product, it doesn't matter how fast you can build, you still end up redrawing it by hand.

**2:04** · Magic Patterns takes your product team from idea to production and works from your real design system. When you build a prototype, what you get back actually looks like your product. You'll validate faster, get alignment sooner, and when it's time to build, engineers can connect your prototype to cursor or cloud code with the magic patterns MCP to pick up where you left off. Your team has their AI advantage. Make magic patterns yours.

**2:32** · Try it today at magicpatterns.com/howi aai. Felix, welcome to How I AI. Thanks for joining us.

### Felix’s role at Anthropic

**2:43** · Hi Cara, how are you?

**2:45** · I am great. We were joking before we got started that I have referred to 2026 as the year of our claude 2026. That is that is the era we are all living in.

**2:56** · And you are in charge of a lot of the experience that that we every day get to get to play with and work with. So tell me how much of Claude do you get to product? Normally when I introduce myself I say I work on cloud co-work I work on cloud code and I work on uh cloud for chrome and I work on the cloud

**3:16** · desktop applications for macros and windows because obviously it's a team effort but I'm currently the engine engineering lead for those products for those products and what's really funny is I'm going to I'm going to give you a little bit of a hard time but every time I talk to someone about claude and how they're using it I say which of the tabs is your favorite?

### The multiple tabs in Claude and why they exist

**3:35** · I know I know. Yeah. Yeah. Which one is your favorite? Uh, the one I use the most in the desktop app is co-work. I'm really trying my best to figure out co-work because I work with a lot of folks who are just uncomfortable in the claude code. What is a terminal interface? Even that third tab stresses them out a little bit. So, I've been a lot I've been spending a lot of time banging my head against co-work scheduled tasks, um, live artifacts, all that stuff. So, that's the one I'm living in.

**4:04** · I think we live in this like super interesting time right now where I I often explain it to my friends and also to like people who work here as the um time right before we all came up with like the glass pebble as the correct shape for a phone. I think we currently live in this like super interesting time where some people are like should your phone be shaped like a taco? Should we shaped like a lipstick? Should it have the keyboard underneath the screen or like right next to the screen or like no keyboard? I think that's the time we currently live in and I think you can see that in a lot of products.

**4:30** · I think that's also why you probably see like more entry points into claude because I myself as an individual I I I think it's a super interesting year because we're playing with all of these different form factors and I've not yet gained the confidence to say throw them all away.

**4:48** · This is the one. I'm like perfectly happy if people sort of pick their favorites. But I I I do understand that simply giving people a choice, right?

**4:58** · like the same way that a restaurant does creates a little bit of like extra work that we put on the user. And it's it's true that if I fast forward to like what is the end state for for this? I'm probably not going to make people pick anymore, right? I'm just going to whatever you want to do, here's the one place where you do that. But right now, it helps us quite a bit to know are you just showing up to get some quick answers? Are you showing up to like do deep meaningful work or are you showing up showing up to do engineering work?

**5:24** · Like those are sort of the three buckets we put you in right now and knowing that ahead of time makes it a lot easier for me to give you an experience that is really really good depending on what what you came for. Yeah, I I like that because a lot of what I tell folks is we are really preconvergent on AI tooling just generally and AI experiences. And so my answer to, you know, how do you want to how do you want to use is like why not all of them? Just depends on the day. Depends on the day if I want my phone to be a taco or a or a glass glass pebble. And it honestly depends on what mindset I'm in.

### Using Claude Cowork to design a new house using floor plans

**5:55** · Well, we're going to talk a lot about product at the end, but to start, this is how I AI and we want to know how you cla. And so, we were talking before we got started and I said, you know, we've done a Claude Co-work 101 episode with JJ. We've done a lot of claude code in the terminal episodes, but we want to know how how you use it because you probably know the edges and secret features and um some workflows that maybe folks wouldn't think of.

**6:26** · So, I'd love for you to walk me through one of your favorite clawed maybe co-workflows that you're using these days.

**6:32** · You you'd think that I would be much better at using the tools than other people, right? like my entire job is to like build them, work on them. And an interesting thing is happening where whenever people show me something like super impressive in how they how they use cloud, like any of the product services, it is pretty rare that I'm impressed by something the model is capable of. Like I sort of know the model capabilities. We have a pretty good understanding of what the model is good at, what it's bad at.

**6:56** · And usually what impresses me is like the creativity in structuring your work and coming up with an idea. that that is usually what impresses me quite a bit. But um my favorite example sort of like change week over week. It kind of depends on like what I'm what I'm what I'm currently working on.

**7:12** · Claire, you and I like right before we started the interview like briefly talked about our kids and like how how we both recently had kids and like if you had asked me three months ago, I would have said, "Oh, like just putting all my medical documents into a folder and like constantly annoying Claude with all the questions I didn't have time for in the hospital." It's like an excellent use case.

**7:31** · But one that I've one that I've quite enjoyed recently was um I'm about to move I'm about to move into a new place and uh my realtor just gave me the the little like marketing floor plan that you get from from a real estate company. Um and it didn't have any units in it like whatsoever.

**7:48** · And this is like the kind of thing where I turn to co-work and what I've done is I have a folder and I like made made a very similar oh sorry I made like a similar fake folder that doesn't contain all the same like secret stuff but it contains fake documents about like an artificial house and an artificial house I'm like picking I'm just going to select this here I'm going to say always allow um it's the demo folder and the demo folder contains all the disclosure disclosures you would get. It's a floor plan.

**8:16** · It contains like information about the mortgage, um any kind of like records I could find about the house. And um I remember saying something along the lines of um in this folder you can find a floor plan.

**8:33** · Can you figure out what the units for that floor plan are and maybe make me a new one with units? Right. And you can fire this off. This doesn't actually need that smart of a model. I've actually I actually did that with Sonnet. So you can like just fire that off and it's going to go off and do do that work. This is a fake house so it's not going to do nearly as interesting of a job.

**8:55** · But for me what it did was um I'm I'm going to move to Marin broadly speaking and it figured out that it figured out that it found a permit for the garage and was like oh now that I know how big the garage is from the permit I can like do everything else for you. And uh maybe I'm going to share my my other screen in a second. But the the next thing that happened was once this is done, I was like cool. Now that I have a floor plan with units, can you come up with like some examples for interior design? Like I just want to like see some possible layouts. Where can the bed go?

**9:26** · Where can the nursery go? What can we do here? And Claude wanted to know how do you want that?

**9:32** · Like do you want me to just like put the furniture in the floor plan? And as I was writing the answer, I was like never mind. I need an interactive planner. I want to be able to like move the printer around. And ever since that has happened, I've just been like obsessed with how Cloud did it. So, I'm just going to show you how Cloud did it. Let me just like make a new window real quick.

**9:51** · Great. And and while you're doing that, I have to ask a question because you very quickly said this is not a problem that needs the smartest model and you switch from Opus to Sonnet.

### When to use Opus versus Sonnet 4.6

**10:02** · Yeah. Yeah, give us your like quick when you need the the beefy model and when you can go with good old reliable sonnet 46. What what's your heristic there?

**10:11** · I think people probably don't have to think about it as deeply as I do. Like I think for most tasks sonnet 46 is actually very very good. It is very very good and it's pretty rare for me that I bump into the ceiling of sonnet 46. This might be in part because the kind of things that I do every single day, especially in my personal life, are just not that tricky, right? Like going and finding finding the right floor plan on like a on like a public website and then making a new floor plan is not that hard. But I get what you're saying, right? Like what does that mean not that hard? Like where's where's the line for not that hard?

**10:41** · My huristic is usually um my tolerance for the model not having thought through very exactly what the actual problem is. Let me explain that a little bit more.

**10:56** · Like I think if you think of if you think of say a lawyer or an attorney or an accountant or a doctor, a a big chunk of their work is that they not just give you the exact answer you were looking for, but they also like need to sort of reinterpret what you're actually asking.

**11:16** · Like what are you really trying to figure out? That is like a pretty important job. Um, and any of the creatives who are listening in, right?

**11:21** · Like in creative work, that is the most important piece of your job is like figuring out what does the client actually want because usually what they come in in the door with is not really what they want. And I reach for opus over sonnet if I have selfidentified as someone who doesn't really know yet what they're asking for. Is that helpful?

**11:41** · Yeah.

**11:41** · I mean, it it seems more like your ability to scope the problem is how you is how you choose versus, you know, biting off something. I mean, I guess if you were to bite off something incredibly technically complex, maybe you would reach for opus, but it seems like more how it decomposes generally stated problems into more specifically stated problems that you can solve. This is a very specifically stated problem, which is I have a floor plan. I need units for that floor plan. I need a new one. So that seems a well scoped problem for 4 for 46. I will say I I love 46.

**12:11** · I use it a lot. It's been um via API a very happy uh player in my open clause. So I uh I like the 46 makes me happy.

**12:26** · It's like a it's a it has a really good soul and structure that I quite appreciate.

**12:32** · But you know it's a little bit like it's like a restaurant menu again. Like no wrong no wrong answers. Not really.

### Building an interactive 3D furniture planner

**12:38** · Okay.

**12:38** · So Claude came back with like this interactive planner and this is the thing that I find so cool. This is why I've been obsessed with this and I've been like telling people about it for a long time now. So in in theory this is a pretty novel furniture planner. You can just like go ahead and like move furniture around, right? Like this is no big deal. But but what Claude did is Claude used Python and this is maybe a thing I should explain. Co-work gives Claude its own computer. So Claude and Co is its own little developer.

**13:03** · It has its own computer, a virtual machine where it can develop whatever software it needs to do to solve your problem really, really well. And in my case, it like analyze the floor plan and then build a 3D model of the house where I can still move the furniture around in 3D and I can like drop in and like walk around like sort of look at things myself. At no point did I tell Claude um, hey, you like should do this.

**13:33** · Like at no point did I like go inside and say you should make me a 3D model. I have also no idea how you actually do that. I'm a I'm a pretty good software engineer. I have no idea how you turn like a 2D floor plan actually into a reliable 3D plan. I peaked a little bit at the transcript and I did some contrast analysis on the floor plan to figure out where are the walls, how thick are the walls. But I found that really impressive.

**13:54** · And then a thing I often like to tell people is that clot gets a lot more powerful for your personal life if you manage to get give a context right context in the form of your emails, your calendar, the kinds of information that is important to you to get your task done. And in this instance, a task that was pretty important was figuring out what kind of furniture I have. And in the in the olden days, I probably would have like looked up what furniture I have, looked up the dimensions, cut that out of paper. Um, but in this case, I just told Croach, you have access to my emails.

**14:28** · You find all the furniture that I bought and then please like add it in here so that I can move around the furniture I actually have.

### Using your email as a source of truth for personal inventory

**14:34** · I just want to pause so people really reflect on that use case because I think they they could gloss over if they don't hear it again, which is using your email as a source of truth for personal inventory, which is all of your purchases end up going through your email. Um, so you're buying furniture, you're purchasing rugs, you're getting receipts, even maybe moves that you've done in the I was thinking about this.

**14:59** · I've moved maybe twice in the last 10 years, and I've had to do that inventory manually, and I email it to moving companies. And if you use your email, which I don't know, I'm sure your your personal email is like my personal email, which is just sprawling and completely inconceivable to like manage through, and you use that as a source, connect it to Claude, and then inventory your stuff, then you have like a a structured source of data out of your email. I'm going to do this with my clothes, honestly.

**15:27** · Like, you buy clothes, you're like, what do I have? What do I have? if I can look in my closet or I can look in my email cuz we're all shopping online. Are there other things that you found like quering your email, quering your calendar, like that have been interesting kind of slices of data you wouldn't have thought of?

**15:45** · I think what you're saying like really resonates, right? Like especially the clothing thing, this is an idea I didn't have yet, but um now that you mentioned it, you can like build yourself a virtual closet and then use cloth to like get advice about like what to extend and like what what else to buy for me. And this is like honestly the trick. This is like something I have to remind myself of every single time I use AI is um there was a brief moment where I started entering like manual furniture, right? Like the furniture planner had this little thing at the bottom where you could enter like my bed is like this wide and this deep.

### The anti-to-do list: going one abstraction layer up

**16:14** · And like in the middle of it, I was like, "What am I doing? I'm just going to tell Claude I have this piece of furniture."

**16:22** · And then I went another step up. I was like again, what am I doing? Why do I need to tell Claw what kind of furniture I have? just like you figure out what furniture I have and like applying this like step up in abstraction of the task and doing that over and over and over again and then like spending all of my energy on the piece that is maybe like more fun and more creative which is like steering claw on what the what the house planner should be like or like adding stupid little features like I want to walk be able to walk through the house myself in 3D like it's a video game.

**16:54** · Those are the things that then I spend my time on and I spend my time less on like figuring out what was my furniture, when did I buy it, who did I buy it from. Um because I don't know for you, but for me certainly I did I did have this problem that I look at my house and I'm like I have no idea where I bought all of this stuff.

**17:08** · Wait till wait till your kid starts bringing more and more stuff into the into the house and I I do a very similar thing. I've been spending a lot of time with executives trying to figure out how to scaffold their own operating system with AI a lot of times with cloud co-work at the center of it and my rule I call this like the anti-to-do list which is anytime you're like doing something that's tedious I just am like I smack their hands I'm like why are you doing you don't do that your hands are not allowed to touch this you need to go ask again go that abstraction layer up how could claude do

**17:40** · this and then how could I never do this again I think is is the next question which is if you want to keep this this um furniture or household inventory going forever, the next abstraction would be like what's the system that in a year or two years if I have to ask this question again, it it's already there and ready for me to go. And so that's the other piece that I think people kind of miss is going that next layer up, which is like how will I never have to do this again?

**18:07** · Yeah.

**18:07** · Yeah. This is this is really good.

**18:08** · This is really really good. like what you're saying makes a lot of sense to me because like I also frequently I frequently then take the same step to what you're saying like how do I keep this going? how do I make sure I can continue using this and like the new data mix in and like it continues to be helpful in my life on an ongoing basis not just a point in time and um like a

**18:29** · thing that happened to me recently is um a lot more people have figured out that they can just like message me on Twitter to like solve their problem which is nice but it it created this problem for me where I now suddenly have to keep track of my problems and um I did briefly like uh sorry not keep track of my problems but keep track of my promises the promises I make to people I'm like, "Send me your logs. I'll look at them. I promise you I'm going to figure out whatever went wrong." And that too is a problem I just gave Claude. I was like, "Dear Claude, you can read all my messages. I want you to keep track of all my promises.

**19:00** · I also want you to figure out how you can do that without like rereading all the messages every single time I talk to them."

**19:08** · Yep.

**19:09** · And all of these things Claude is right good at. I have never actually looked at like Clots's little database. I think it like created both a SQL light database as well as like a mountain of text files, keeps track of all the promises I made to people, but it's quite good occasionally reminding me of like, hey, just so you know, two weeks ago you said you would do X. It is time to do X.

**19:28** · Please go do X.

**19:30** · What I what I like about what you're saying too is while you might be curious about how these things are built, you also aren't getting in your way being like, how do I build the perfect 3D renderer of my house? or like, "Oh my god, I cannot believe this is text files. This is so ridiculous." Like, as long as it solves the problem, you can sort of move on move on with your life because these are, you know, little micro apps. They're just for you. They don't have to be architecturally, you know, perfect or the code that you would write necessarily, although they're probably pretty good.

**19:58** · Um, and so you really get to like how to solve the problem versus or that the problem is solved versus how you've solved it being the most important thing.

**20:07** · Yeah.

**20:07** · Yeah. I think that's totally true.

**20:09** · like I I increasingly started stepping away from from actually like supervising claw too closely and really only judging it on its impact, right? It's like something that I think for for people in the workforce, we we often aspire to that we're really only being judged by like the the actual output. And I think as a control freak who like, you know, for a long time really needed to like read every single line that Claude writes anywhere, it was a little difficult for me to give up that level of control.

**20:39** · But I'm I'm getting increasingly comfortable consulting Claude with things where maybe I'm not the ultimate authority myself, right?

**20:49** · Like um there's a lot of things I'm good at. There's an even larger amount of things that I don't know and I'm not very good at. And I think a lot of us are making making this experience for the first time with getting just a little bit more context on medical issues. This is like this is like a thing that I think is very universal when I talk to my friends like when when they have medical issues they don't fully understand at least not completely and they just have like some questions about the physician's advice.

**21:15** · Um they ask it both to the physician as they should but they all of them without fail will also like ask an AI model of their choice. Hey, can you just explain this to me a little better? Like I have the following 10 questions about this, right? Like and and in a way there AI has replaced, you know, the usual like Google endpoint for I have the following function about life in the internet.

**21:35** · And knowing knowing that I'm quite comfortable with with using these tools in a domain where maybe I'm not the ultimate authority has also made it easier for me to not doublech checking every single thing it does because to your point like if the end result is good for like I have no like I am obsessed with software. I've not read a single line of this furniture planner.

**22:00** · It's just for I'm just going to play with it myself. It it is really only for me and my wife to like design our house. will get thrown away in a month. But in this moment, it is very, very fun and I don't need to optimize it for like a million users.

**22:13** · This episode is brought to you by Guru, the AI layer of truth for your company's knowledge. Here's the problem. Your AI is only as good as the information you feed it. Most companies are getting confident but wrong answers from AI because their underlying knowledge is outdated, incomplete, or just plain incorrect. Bad information doesn't just slow you down, it costs you money and puts you at risk. Guru solves this by adding a verification layer between your company's knowledge and AI tools.

**22:46** · Instead of just hoping your AI gets it right, Guru automatically scores content for accuracy, flags outdated information, and ensures your team gets trustworthy answers every time. It works with the tools you already use, so you don't have to change how you work. Thousands of companies trust Guru to keep their AI accurate and compliant.

**23:07** · Ready to stop playing Russian roulette with your company's knowledge? Visit getguru.com to learn more. I want to go back to something that you you said, which is, you know, you built this promise tracker, which I think is really interesting. And that made me think about a new a new feature in Claude that I've been using and playing with a little bit, which is live artifacts. And I think this idea you actually I'm not going to I'm not going to pitch live artifacts on your behalf. I'm going to let you explain what it is and then maybe you can give us an example of where live artifacts could be a helpful tool.

### Introduction to live artifacts

**23:39** · It because it it reminds me a little bit of what you're building with your furniture builder. So tell me a little bit about that and Claude.

**23:46** · Yeah. Yeah. Here let me like share my screen again.

**23:48** · Um and I'll give a little bit of a quick spiel of like what are artifacts, what are life artifacts, why do we have them, what's the point. So um generally speaking what do we call an artifact right like I can say dear claude please make me a beautifully formatted page with two poems on it formatted nicely

**24:14** · I like I like the the letter form yeah the lack of creativity here in the prompt is like um is like pretty rough but it's beautiful and nice the what Claude is now going to So obviously his cloud is going to figure out okay Felix wants me to write some poems and then um those should add those should end up on a page and um this page is what we call an artifact. We we within the cloud world an artifact is like some kind of file output from what you've been working on. The furniture planner I just showed you is a single file that is an artifact. Any kind of PDF you would make as an artifact.

**24:47** · Spreadsheet presentation, all of those are artifacts. And here we go. There are my poems over here on the right. This is a classic artifact and artifacts become really powerful if you if you use them in a way that they help with your life, right? Like the typical examples of reports, dashboards, presentations.

**25:07** · And we've discovered that data is a really important piece in your work. Um like a typical example maybe for the founders out there is like a pitch deck, right? Like you need to go and pitch your startup to 60 different VCs. All of them have like slightly different information that they they rely on that they have different reference points in terms of other companies they've invested in the past. The data should be up to date in those sheets, right? Like however many many signups you had is probably different this month than it was last month. So as a founder, you spend a decent chunk of your time making these pitch decks, right?

**25:38** · Like every single week you sit down and you update your pitch deck. And if you like abstract away and generalize a little bit what the core problem here is, it's that you have this like core idea of something you want, but you want it updated uh maybe for the audience. You want it updated with the latest data.

**25:56** · And we thought about the idea of can we make an artifact that like refreshes itself with the latest data. And a good example many people have used in the past is like sort of a personal dashboard. So when we say live data, what we use is we use connectors.

### Building a personal dashboard with live data

**26:11** · Connectors are a way for you to get all kinds of information into cloud about all kinds of things. Um, like we launched the Spotify connector today. I haven't actually tried this yet. This could go terribly well or terribly.

**26:24** · I was do live. Come on.

**26:26** · Okay, we'll do it live. So, we're just going to connect Spotify real quick.

**26:29** · There we go. I'm going to have to configure this and like actually log log in. Um, actually, this is good. This is good. Um, it's not going to show you my terrible music taste. I appreciate this quite a bit. Well, I mean, if if you are like any of the parents out there, and if you know, I think this is like Bay Area Insider Baseball. If you're moving to Marin, you're going hard parenting.

**26:48** · So, if you're like any parent out there though, your Spotify is going to be White Noise and then and then Disney soundtracks. That's it. Yeah. One of those for the next six years of your life.

**26:58** · That's really going to be the thing.

**26:59** · Yeah. But here's what we can do. Um, we're just going to go ahead now and I'm going to say, "Hi, please make me a personal daily dashboard, including reports and information um, from my various data sources, say Spotify, Gmail, Calendar, notion, whatever else you find that's relevant to my life." Um, you can you can see you can see that I'm like getting increasingly comfortable just like just whatever letting figure it out.

**27:34** · Yeah. Like usually my experience is that like whatever ideas I have, Claude will probably come up with a better idea and we'll go a little deeper than me. We'll spend like just a little bit more time thinking about this. And then I'm also going to say this is for a product demo.

**27:47** · Please do not use any real data. Just make all the data up. Thanks. And then we should probably define some kind of design. That is always a good idea. Um, design.

**27:59** · Last time you said beautiful and nice.

**28:02** · Hey, it was beautiful and nice. But we can go with like something like a modern editorial design. Something calming. Yeah, I think that's a good idea.

**28:12** · That's great, right? Oh, also make this uh live dash live artifact.

**28:17** · You know what I want to show for people is there is this thing called live artifacts. I always say when you're prompting something like use the magic word, use the incantation. And in this case, the incantation is live artifact. Um, just to make sure you're getting that that style of auto refreshing, auto updating artifact. Yeah.

### Being polite to Claude (and why it matters for your humanity)

**28:38** · I have to ask you a couple questions while this is loading.

**28:40** · Please do.

**28:41** · Do do you always greet Claude so politely? I've seen a lot of dear Claudes and a lot of hello, hi friend.

**28:50** · Do you always do that or is this just a little demo magic?

**28:53** · I always do that. I do think I do think this might be like a thing about the people who work in Anthropic. We probably all have like a relationship with Claude that is a little bit more personal than like maybe people have outside the company. Yeah. I think I I enjoy being polite and nice to Claude. I don't care at Claude. I don't like I appreciate that.

**29:13** · Yeah.

**29:13** · Yeah. I think I I understand that the ultimately the chips don't care, right? Like that's that's the whole thing. Like we ultimately know that I'm interacting with a tool here, but for me as like someone who cares about my mental health, it's like good for me in my own communication with anything to like be polite and nice.

**29:31** · Yeah.

**29:31** · I ask this question on every podcast and so you will be the on the very polite and nice camp. And I say it's not about Claude's humanity, it's about my humanity is why.

**29:43** · Yeah.

**29:43** · which is I don't need to get in the habit of being rude in in written language. I also have found myself it's so ridiculous but it makes me feel good in any broadly scoped problem. I've been consistently ending with like I believe in you. I know you can do it and make good decisions and it's so Do you feel like it makes a difference?

**30:07** · Yeah, I do because I I feel like they it asks me less when I say that because a lot of times I just don't actually want to be asked my opinion. I often just say whatever you think. And so this is my my method of saying like you make the decisions. I trust your judgment and saying I believe that you can do it and I trust you. Look at this.

### Claude interaction tips

**30:29** · It's beautiful.

**30:30** · Nice. Sorry, but before we talk about my dashboard, I have like more things to say about like what what you told me about like telling Claude that you believe you believe in it. I I I think on a very personal level it is wonderful that you do that because I think it's like good for you as the human in the loop. It is good for you.

**30:48** · However, however, I have an actual tip for um I have an actual tip for people like interacting with Claude. We have noticed quite a bit of difference internally because sometimes the experiments that we're doing here are I want to say a little bit on the fringe of what is possible with operating systems. I am at heart a desktop developer. Um I want to make full use of a computer and that often means pushing the computer far beyond what what maybe most people do with applications. Um and like just operating a little bit on the fringe.

**31:21** · I'll give you an example of like something that we have not shipped we will not ship. Um, but there's your operating system has a layer in between your icons and your wallpaper where you can draw pixels which draw like is useful mostly for art. The reason you don't have any applications to like draw stuff in between your wallpaper and your icons is because there's not much use to be found there. But as a concept, it's like fun that you can like put things there. And I have frequently found myself telling Claude um that something is possible and I know it's possible.

**31:54** · Yeah. sort of the idea of like I don't actually know how but I know it's possible.

**31:57** · Yeah, we'll figure out how you can do it. And that does seem to give Claude like more confidence in actually going after the task at hand.

**32:07** · It also like preempts a bunch of conversations that Claude and I might have about Claude being like, "Felix, your idea is dumb. You probably shouldn't do this." And I from the get-go can say, "I know I'm engaging in art.

**32:19** · Please go along with it anyway."

**32:21** · I I I love that. So, okay, I know it's possible. Well, I say that's my I believe in you. I think I think you're capable knowing it's possible. Um we'll discover the space.

### Looking at the daily dashboard

**32:33** · Yeah.

**32:33** · Yeah. Exactly. But here we are.

**32:36** · This is this is now my little like personal dashboard. The design is like something that Claude just came up with on the spot. The widgets I came up with are on the spot. This is like com this is like clay, right? This can be anything you want it to be. which is very open-ended but therefore so powerful. People frequently use this to get a little report about what they want to do in that day, right? Like just prep me for my day. What are the meetings I need to like think about? But again, the thing that is maybe most powerful here is going one abstraction layer up.

**33:06** · So I actually don't believe strongly in morning reports that just summarize what kind of meetings you have today. That is not all that impressive. I can just look at my calendar. What is really impressive is saying, "Look at all of my meetings I have for the day. Go figure out who I'm meeting with. Catch me up on like the recent conversations we've had.

**33:30** · What were the themes there? What were the problems?" If if it's a coworker, go on Slack, figure out what kind of stuff they've been working on in the last week and what stuff they might want to talk to you about today and then what you need to know about that concept. you can just like keep playing this like graph bounds where you go and pull in more and more information to get you prepared even better for whatever your actual work is. And that's where these things get really powerful and this is the kind of data you can pull in live and have cloud crunch on the go.

### How live artifacts work with connectors

**33:55** · Well, and I want to call out for folks a couple things that they might not notice that I think are really unique about um these Cloud Live live life live artifacts, which is one, the killer feature here is this little refresh button up in the top, which is you can constantly pull in and reload data. And so this isn't this is your dayto-day. Every time you come to this, it's going to refresh your data and pull the latest in. I think the second thing, and correct me if I'm wrong, is it just is reusing the off from your connectors.

**34:25** · And so there's like no magic I have to put an API key in and where am I going to store it.

**34:32** · It's if you go into settings and go into connectors and you connect your stuff, you can use any of those kind of connectors to scaffold out one of these live artifacts. And like look at this list of stuff. There's so many things that you can just one click add in sign in through OOTH or whatever and then you can build a live artifact in cloud without having to like ask for an API key.

**34:56** · Exactly.

**34:56** · And it can be, you know, it's not just the ones we have in our in our little like connector store. You can also connect your own. It it is quite powerful. The thing that I enjoy about this the most, this is like probably fairly unique to myself, but the thing that I enjoy about this the most is the amount of creativity you can pull in and how you can really shape this in your image, right? Like we could go in and say, I want this to look like it is software made in the early 2000s.

### Redesigning the dashboard

**35:24** · Oh.

**35:24** · Um Oh, 200 is maybe 200 is too early.

**35:28** · Well, let's see what it does.

**35:31** · I mean, honestly, this is flawed. Uh, Claude is probably smart enough to know that I meant the 2000s.

**35:36** · Well, this is my go-to claw design use case, which is I' I did an episode on claw design earlier this month, and I redesigned Lenny's newsletter in like 1999 Geio City style. It is incredible. We'll put the link in the show notes. It did an impeccable job at this. And what I told people is, and it wasn't even the design that was really impressive to me.

**36:02** · It was the copy was so Oh, was it like Yeah. Was it like Geio Cities era?

**36:09** · It was Geio Cities era.

**36:11** · It was 11 out of 10. Exceptional copy.

**36:15** · Um, beautiful.

**36:17** · I want to see if it's going to do 2000s or 200s. 200s would be way funnier.

**36:22** · We can probably look at it already. See, like very first thing is 2000s. Like Claude is smart enough. It knows knows too much. Knows too much. And also, I mean, this is obviously like a bit of a demo account, but if you if if I showed you my real account, Claude is like quite used to the fact that I constantly misspell things and like talked it in a slightly different style. I'm like I'm like eager to see how this is going to go.

**36:47** · I'm I'm in general quite excited about um the amount of creativity you express and especially the amount of creativity people can express who are not software developers, right? like this used to be this entire domain where um you were

**37:02** · maybe a designer working at a software company and like maybe then software developers would execute your vision or you like picked a medium where it's a little bit easier you can like low code things but I think what is really exciting to me is that we can now pull in people from all these different from all these different like expertise areas and they can all build these artifacts like be that a presentation or be like a straightup tool sort of in in the vision they have a

**37:27** · couple of weeks ago, I I read somewhere that Margaret Edward wrote about using Claude and the the immediate thing that popped into my head was I want to see software written by Margaret Edward.

**37:38** · Like I want to see what like tools look like that she has made for like writing her own books. Um that would be like so interesting and exciting to me. Okay, Margaret, if you want to come on how I AI, I would love love to see uh your your your claude setup. And on this, while this is we're going to make this happen while this is loading, I do want to call out because I do think there's a gap.

### The biggest gap: people don’t know what problems AI can solve

**38:03** · People listen to and watch how I AI along a a broad spectrum of technical capabilities. So we have the most AI pill a float through the tokens intense software engineering folks that are really pushing the edges of what these tools can do and then we have very ver very early users who are just coming to this in sort of a naive growth mindset way and saying I need to solve a problem. The biggest gap that I see which we were again talking about before we started recording is it's not the capabilities of the tools.

**38:33** · It is literally people being able to understand that almost any problem can go into these tools and what like a workflow would be. And this is why we've done this podcast. And on um the the chatp website, we have I think it's now close to 200 AI workflows that we've listed from this podcast that is just like if you're trying to solve a personal problem with claude code. Here are the 15 ideas that we've seen on the podcast.

**39:00** · And I do still think there needs to be this education and muscle memory change of you can build yourself a daily dashboard. You can build yourself a newborn sleep tracker. Hey, you're moving. Why not throw it all into a folder and then make your life easier as you're trying to close on the on the house? And I think people still the gap between technology and use case is still pretty pretty broad. And so, you know, my my advice is like if you're futing with something on your computer, ask Claude to do it. Any other any other tips you've seen on how to like discover use cases?

**39:33** · Yes.

**39:33** · But I think I think before I even give you an answer, I just want to like underline how correct I think you are.

**39:39** · Many years ago, I spent a decent amount of my time, like I spent five years at a company called Slack, which I think I think now is like fairly well known as like this chat tool that a lot of people use. And people were sort of like using Slack for different reasons, but they were all more about the way they organized their work with other people rather than it was about the tool itself.

**39:59** · So Slack by itself, if you used it the exact same way you would maybe communicate with emails in a silo, was not all that useful, right? like Slack becomes really powerful if you open it up to the idea of what if you communicate more transparently and people can see what's going on and we like sort of instead of having email threads we have a channel and like the channel is open to anyone who wants to see what's going on right like it's this transformation of work and the transformation of how do you actually organize communication with other people um and AI is like in a similar vein of

**40:33** · it it become it like opens up so many opportunities that to harness them all.

**40:38** · You probably have to change a little bit how you work like if you really want to harness them. And yeah, I think you're right that like one of the biggest problems we have as an industry overall is not even like training the models and making the models very smart and making them very powerful or giving them the tools that allow them to turn that intelligence into like output. The the the biggest hurdle we have is how do we design the the human model interface? How do we make this very easy for humans to harness?

**41:07** · And right now, I think the way it shows up is that humans are sharing these like tips on how to use this resource, right? I think the tip that you gave was a good one. It was like constantly whenever you do something that you find annoying and you're not enjoying and it doesn't feel creative and it doesn't feel like something where like you're you're you know, it doesn't feel like the the core of what you really want to do right now. That is a good time to pause for a second and like wonder is there a way I can I can use AI to do this.

**41:36** · And then of course and this is probably not surprising but of course like many people have a decent amount of success just like asking Claude, right?

**41:46** · Just ask Claude how would you help me with this task? And usually comes up with a pretty good idea.

**41:51** · I call this the like reverse interview which is just going into Claude and being like I am a mom of three boys. I run too many businesses for my own good and I, you know, my biggest challenges are XYZ. How can you help? Interview me and then tell me how you can help me.

### The reverse interview

**42:10** · That can be a really good um exercise because again people want the guidance of like do you have problems with your calendar? You know, are your kids in any sports, any any of those things. And so I do think this sort of like reverse interview where you can use claude or whatever AI tool to sort of solicit out of you the ways it can help solve your problems is a really a really good one.

### Making latency delightful through asynchronous design

**42:32** · And then again while we're sitting here I have to ask you another question because I think the um anthropic and the cloud products are so well known for this but we are chitchatting right now because we are waiting for co-work to load and one of the things that I think you all have solved is making loading delightful. So, give me your thesis on how to make a product with built-in latency not so annoying to watch loading.

**42:59** · Honestly, the most important piece is probably to just get comfortable. They help users get comfortable with the idea that things are asynchronous.

**43:08** · And I think most humans are actually quite comfortable waiting for something if the quality that they get at the end is very very good, right?

**43:15** · um that that is generally something we're like quite comfortable with and like maybe in the example of Slack like this is a good example at Slack. Um this was this was a problem we had fairly early on. The first version of Slack that I worked on when you hit send on a message it would immediately succeed or fail immediately right away. And of course the problem is the internet itself the internet as an entity is not very stable. It's like this complex mesh.

**43:39** · So like messages would frequently fail and we fairly quickly replace that with with a version that like tries sending the message once, twice, three times and only after like a good couple of seconds if it fails it would be like hey by the way something seems to be off here. And this is the same way that like iMessage works today, right? Like if you send a text message it's okay if you're currently in the tunnel. It's going to like try again um like about a second after. Okay, we can update this. Oh, I This is beautiful. He let me make this big to my heart.

### The redesigned dashboard

**44:13** · This is good.

**44:14** · This is This is very good.

**44:19** · I love how I am in moments where we're real delighted about Yeah, I'm like I'm like such a nerd for this stuff. Um I'm like mildly obsessed with like software the early 2000s. But yeah, this is beautiful. I'm a big fan of this.

**44:34** · Um this is quite good. I love I love that it like brought in I saw in the thinking notes that it was like Felix requested Spotify, but we're in the early 2000s. We should talk about Win Amp.

**44:43** · Win amp. I know. I was going to say you need to skin your Win AMP module here.

**44:48** · This is this is beautiful. Okay, so I'm going to wrap what we were talking about, which is loading screens.

**44:55** · Get comfortable with latency. I think realize when tasks don't need to be synchronous and build that concept into your product. And then look at that. We just chitchated for a while. And as we were talking about latency, Claude must have been listening and said, "I'm gonna show them. I'm gonna bop this right open." And and and again, folks, not paying attention to the details. Look in the top right. The clock is moving. It's ticking along in the seconds. You have this refresh. This is I I want to I want to open up and look at this every day.

### AI should free up your creative energy

**45:29** · It's like pretty fun. And you can like envision like you can shape this in any form you want. But I'll finish. I'll give you one more tip like how to actually build these things that like where you got to wait a little bit and like people need to wait for them and get a little comfortable with waiting. I think for us as anthropic or like maybe for me as a product builder I will always trade off taking a little bit longer and giving you a better result. I think ultimately it's better for humans.

**45:51** · And the thing I probably want to teach people is that it's okay to like not watch claw as it's actually working because that is not super that that is not really the vision I have for AI is that we humans just like sit around and do nothing and watch the AI do the thing that otherwise we could just do ourselves. Like the thing I always say is that AI is used poorly if if it just needs to move the mouse cursor for you.

**46:14** · Like the thing I really want to do is I want AI to like do a bunch of annoying things in the background to free you up for your creative energy. So you can come up with ideas as good as make a daily planner look like it was built in the 2000s. You will have better ideas than me. But I think I think it's sort of like actually moving people from having to watch the thing into a position where they get more comfortable not watching it. And I think this has more to do with trust than it has to do with patience.

**46:42** · I love it. Well, we do have one last little demo that you're gonna show us basically on that topic, which is how you know when when Claude's done, and this is actually the thing that I reached out to you about doing because I love it so much.

### Building a $20 hardware Claude buddy

**46:58** · Um, but but talk to us about the little stick.

**47:01** · Yeah.

**47:01** · So, um, in the interest of like getting really creative and like being more comfortable with like areas you're not very good at, um, I have always been like mildly obsessed with like these like little hardware devices and I'm just not I'm not a hardware developer. I I never really like soldered anything together. I'm not a hardware developer in any in any shape or form. But it occurred to me that I could just go on the internet and buy all of these components myself.

**47:24** · I saw a tweet yesterday on Twitter from someone who said, "Hey, if you want to build your own like if you want to build your own ebook reader, the components are actually quite cheap and very available." Um, and it occurred to me that I can just connect this device to claude. Um, we talked a lot about co-work, but we also have cloud code, right? So, I have built this little thing which is just like a teeny tiny teeny tiny cloud like on a little stick and this stick has Wi-Fi, it has Bluetooth. So let me tell you what this is. So the internet is a magical place.

**47:59** · And on the internet you can just exercise free will and buy whatever you want. Um and what you can now buy is you can buy like these teenytiny hardware devices with a perfectly good le LCD screen, LED screen. This thing has Wi-Fi, has a Bluetooth, it has a little bit of disk space. Um and you can program it. You do need to program it in a low-level language, but you don't, right? Hey, we live in the future. You don't need to do you don't need who cares. So, what you can do is you can just straight up connect this like this is a little stick right here, right?

**48:30** · Like you can just straight up connect this to your computer. I just plug this in and then all I did was I told Claude Code, here's here's my vision. Here's my grand creative vision. I want like my little claw to live on this thing and I wanted to um cheer me on every single time I do a good job. And also every single time I need to approve something that Claude is doing, I want it to like be on this like big button that is out here. And Claude has built all of that in like a one shot. I needed to correct absolutely nothing.

**48:59** · And I've since seen on the internet that a lot of other people have like built similar things because we I I open sourced my code so people play can play with it. But I've also since seen that this is just like the the tip of the iceberg. There's like so more so many more cool devices out there. This by the way. So, this thing is $19. It has Wi-Fi. It has Bluetooth.

**49:21** · I've already mentioned this like many times, but I can't I can't get over I can't get over the idea. We've been talking a lot about like how we optimize our our life sort of as it happens on a computer, right? Like because that's where we live. But I keep having this idea that it can just like unneath claw onto like all these little hardware devices and also improve my by improve I mean just make like more delightful or make a little cuter. I I did a very similar thing in a recent episode.

**49:46** · I bought it's like um it's already preloaded with this proprietary software, but it's like a tiny retro computer, very Windows 2000, and I had to hack into that thing. I was like Bluetooth sniffing between the like iPhone app and the thing. I was like dumping all the logs in and being like like backwards engineer the encoding of the the the files into this thing. And I finally got it and made myself a little CLI tool where I can type and it just shows up.

**50:17** · Yeah.

**50:17** · But see, that is so cool. That is so cool that we can do that just now.

**50:20** · Like I this thing also communicates over Bluetooth Bluetooth. Um I learned a lot about the Bluetooth protocol as I was building this just by osmosis. Um do you want to do you want to see it? Do you want to see this?

**50:33** · I do want to see it.

**50:34** · Okay.

**50:34** · So this is now also like partially live in actual cloud. So you can build something very similar if you like buy any IoT device of your choice. I'm not going to make a recommendation, but anything that you find on the internet will probably work as long as there's Bluetooth. But you go into help troubleshooting, you enable developer mode. Developer mode allows access to developer tools and features. We give you that warning because it does require that you sort of know a little bit of what you're doing.

**51:02** · It's going to restart the application.

**51:04** · Here we are.

**51:05** · And then you have this new developer menu where we hide all of our developer features. This is for people who work with MCPS or also for people who want to build their own little hardware devices.

**51:15** · And um in here is now a new open hardware buddy. This thing you will notice that it looks a lot like the one I've actually purchased. Um but it doesn't have to be the same one. I think I made that point clear. Follow your heart. Be creative. Um and you can hit connect and it's going to like scan for this little thing for like a few seconds to like find it on Bluetooth. And it's found it. There we go. So now it's connected. Uh it gives me a passcode.

**51:42** · Okay, cool. So we're now connected and uh Clara, you tell me if you can see anything. So maybe what we're going to do is we're going to um going to ask for like anything that would require any kind of like permission. I'm just going to say just make uh hello world.txt and write it to disk. Um, and the point of this is to just fire something off that will require a permission.

**52:09** · Okay, so you can now see I heard it.

**52:12** · Isn't that cute? Isn't that very cute?

**52:14** · Really?

**52:14** · And if I approve this here, then it will be approved. That's how it works. And now Claud's off doing his own thing.

**52:22** · I love it. We saved the best for last, people. If you have made it this long in our in our episode, we have saved the best for last. Felix, man, I really like it. And I'm like you. I'm like, I am a perfectly serviceable software engineer and I have no idea what I'm doing with the Bluetooth protocol and with hardware. And it's just been a thing that I've stayed so far away from. And you'll appreciate this, I think, more is as my kids get older, too.

### Why kids are magical AI users

**52:48** · I don't want them interacting with like the full computer thing, but I would love to have little little things for them to interact with. I think like being able to scope kind of like micro devices to to a use case just like we're getting this personalized software is going to be really fun.

**53:07** · Yeah.

**53:07** · And like um one one of the pieces that's been maybe most joyful about my job is that people frequently send me like little videos of the kinds of things their kids are doing with Claude.

**53:19** · And um the creativity they have is like beautiful, right? like you can like just take a photo of like a little animal your kid has drawn, give it to Claude and be like, I need a jump and run. I need a flappy bird, but instead of the bird, it needs to be this little drawn bird over there.

**53:35** · Um, and then you put your kid in front of the computer and like truly truly magical things happen because I think I'm still wrapping my head around this, Claire, but a truly magical thing is happening with kids because they've never learned what not to ask for. to them the

**53:52** · computer is just like can do anything and I think to like sort of our generation we're very used to like things just not working right we're like used to like oh you can't do that so like so we've been like living in this mind prison for like 20 years this is very on brand but my nine-year-old is a daily active Claude user but he he's decided he's really into cyber security we're like very hacker adjacent here and so he's like truly in like claude on one thing the terminal other he's like Um, do you know that your device ID is this?

**54:22** · I'm like, yeah, babe. I do know that, but good job. Good job. Um, yeah, I I think it's totally fascinating. Well, Felix, I know we have just been having so much fun this episode. I think people are going to get so much out of it. Just to reverse for folks, we talked about Claude Co-work being able to build you artifacts, both sort of like standard crazy 3D printed or 3D uh renderings of

### Recap and final thoughts

**54:47** · your floor plan and other things that you can just stand up to solve little problems in your life all the way to live artifacts that can pull from your live data and really give you a rich personal experience with your data. We touched on a lot of topics including email as a source of truth data. What we're going to do with all this latency and how to pick the smart enough model which is just say you know you know when you need opus and you know when you need sonnet but we both think that sonnet's pretty good at most things.

**55:12** · And then you showed us how we can hack into hardware for the all-in price of 20 bucks including shipping and build little little buddies for herself. I'm going to get you out of here. One quick lightning round question. Again, we did this at the in the at the midpoint, so maybe you can just answer really quickly, but when Claude is not listening, you we've we've talked about how to set it off on a good path, but when it's really just making mistakes, um instead of make no mistakes, it's making all the mistakes.

**55:45** · What is your prompting strategy? I can't imagine you yell. You don't seem like a yeller. Um but what what do you do?

**55:52** · Yeah, I do not yell. I think I think it is it is useful for me to know when people curse at Claude. This is like this is like an interesting thing for me to know um as a product builder. But my strategy for when Claude doesn't like really really understand what's going on or like Claude seems to have gone off the rails. Um I usually try to debug my workflow straight up by asking okay here's what I actually expected.

**56:18** · Can you maybe walk me through at what point you expect if something different or like how we can maybe prevent this in the future? It doesn't always work. Claude is AI and AI can make mistakes. However, however, that being said, I I have frequently found ways to improve the data source or to improve the amount of noise that is in the data um or like with cloud to come up with mechanisms.

**56:41** · Okay, how do we how do we like do do we set up some kind of dry run? Um, I usually end up at a place where the learning I take away is not, oh, Claude can't do this. I'm not going to have Claude do it. Usually the learning I take away is I can maybe change a little bit the harness, the prompt. I can change um something in like how we set this up at the beginning. And I think after after the time we had together now, this is no surprise to you, but like usually my answer to that is like to also involve Claude and say, "Claude, what do you think we can do here?"

**57:11** · Claude is a good friend and if people need if people need to vent and people need to like externalize their frustrations, Claude can take it. You can c you you can do it. Maybe just smash the button like have an angry button instead of saying the thing on our little hardware buddy. You can have like the mad button and the happy button. You just I'm not pleased Claude smash smash smash.

**57:35** · Yeah.

**57:35** · Yeah. Uh, and like there there is a I'm not pleased button that actually also ends up on my desk that I do want people to like use. So every single time Claud does make a mistake, we do have the little like in in many of our product services, this is a crosscloud. You will find the little thumbs up, thumbs down buttons. Those are super useful to us. We use those in training.

**57:52** · We use them in like improving improving not just the model but also the products. So maybe actually the thing I'm going to say is like if Claude hasn't done the thing that you wanted it to, cursing at Claude will probably not fix it for the future. But like pressing the little like thumbs down button um helps us quite a bit because it does end up on my desk. We deal with it.

**58:12** · Perfect. Well, this has been super fun.

**58:14** · Before we get you out of here, how can we find you? And other than hitting the thumbs up, thumbs down button, how can we be helpful?

**58:20** · Um it's really that that's like the the number one thing that like really helps us build a really good product is getting a good sense for what works for people. The option space is so big.

**58:29** · We're still in this like fun smartphone time. We talked about it. Um, and I do want to hear from people. I want to hear from people what works for them, what doesn't work. I'm always grateful for all kinds of feedback. Um, you can find me on LinkedIn and X. Those are the two big places.

**58:44** · Great. And and you make promises. You made a promise to me before this before this call that we will get to after we end. Well, thank you so much for joining How AI. That's this has been great.

**58:54** · Thank you, Claire. Yeah, this was fun.

**58:57** · Thanks so much for watching. If you enjoyed this show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiipod.com. See you next time.