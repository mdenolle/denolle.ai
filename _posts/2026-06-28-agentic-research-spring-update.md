---
layout: default
title: "Three Experiments in Agentic Research"
date: 2026-06-28
excerpt: "Retrieval tooling has made agents genuinely good at research. The price of admission is full transparency — not just of data and code, but of reasoning."
tags: [AI, science, agents, reproducibility, seismology, workflows, open-science]
series: agents-for-academic-practice
---

For the past ten days, now teaching is over, I have been writing three papers at once. I now have time to meet my students twice a week, I still run group meetings meetings, I still do my own revisions and reviews. The difference this quarter is that  I have 4-5 agents running in the background while I do all of that. I switch from screen to screen. One window is drafting a methods section. Another is scanning a literature corpus. A third is re-running a pipeline I asked it to make reproducible. I am not watching any of them closely. I am checking their work.

The agentic landscape has evolved so much over the past 5-6 months that it is hard to conclude on the best framework - that same one will be overturned the following week. This is why my post here is just discussing half-way done projects, but a radically shifted practice in research. 

## Why now: retrieval, guardrails, self-correction dramatically improved and changed the tool

The short version is that the tools got better, fast, and the part that got better most is retrieval. RAG is still important, but models provided by anthropic and openAI already retrieve the correct ones, if prompted, and without necessary curated knowledge base (I still greatly value this approach, but this is for another post)

A year ago, asking a model to "review the literature" produced fluent text and unreliable citations, which sparked the outcry of the research community. Now, with retrieval-augmented tooling that reads real papers and grounds its claims in them, literature review is close to a solved problem for a working scientist. New agentic systesm such as Claude Code just need to be prompted not to hallucinate DOIs, and they mostly (~90%) abide to this restriction. Not perfect and solved enough that I do not treat it as the bottleneck. Actually, I do remember revising my student papers without checking for the references and DOI requirements in papers is relatively recent, so the fear of hallucination was probably overblown.

Once an agent can find and read the relevant work, it can do more of the implementation around it: build a data pipeline, draft a method, run it, critique the result, scope the next experiment. Framing the research process as a chain of tasks, literature review, data pipelines, method development, implementation, results critique, discussion and limitations, future-work scoping, naturally scaffolds the research multi-agent systems. Each of them deserves its own honest investigation into how agents perform, my favorites being: 1)retreivals with knowledge bases of tools and scientific papers, or 2) context engineered with *skills* that have references (e.g., examples of codes, directions to find the data etc) and guardrails.

## What stays human, what can be agentified

This forces a clearer separation of roles than I used to make. Strip the research process down and three things have to come from a person:

1. **Scientific vision**: what is worth doing for our favorite impact (for me, human's natural hazard and resource management resilience)
2. **Human creativity**: the obvious process for many, though I now question *creativity* itself as human do get inspired by others and as AI is a great interpolator of ideas.
3. **Critical thinking and rigor**: whether the result is actually true, abide to common sense and not just method correctness, and may require implicit knowledge of our scientific culture.

Almost everything between those is implementation and testing and where agents now earn their place.

<img src="/assets/images/agentic-research-stack.png" alt="Conceptual map of an agentic research workflow: scientific vision at the top and scientific rigor at the bottom bracket a central layer of agents, fed by open data, open software, and open knowledge, running the eight-stage research workflow from literature review to future-work scoping." style="max-width: 100%; width: 760px; height: auto; display: block; margin: 1.5em auto;" />
*How I picture it. Scientific vision sets direction from the top (mine is the skies); scientific rigor and critical thinking, human checking plus review by agents I design, ground the analysis to correctness. Between them, agents draw on open data, open software, and open knowledge to run a multi-stage workflow, while domain-expert and method review (agents or me) stay in the loop. The human owns the top and the bottom. The agents work the middle.*

The separation that matters most to me is between two of my own roles. As a PI on a grant, I want the work done well and fast. As a mentor, my job is to help students become critical scientists. Those are not the same job, and I think we have conflated them for decades. A research project is not the deliverable of mentorship. The student is. If agents can absorb more of the "get the work done" load, the human part of my job is now a much clearer focus: teaching rigor-critical thinking and helping them develop their own ambitious vision. Given how research funding is designed (e.g., delivering research with graduate students), I am still working out whether that is liberating or unsettling. Probably both.

## The reproducibility problem agents expose

The catch that agents require, and a definite challenge for observational geophysics.

Agents need pipelines that are fully reproducible. Most papers only partially document their data pipelines and methods. Our community standard is moving in the right direction as we increasingly publish code but publishing code is not the same as reproducibility. Reviewers rarely run the code. Editors do not. And code that runs is not necessarily code that is correct; it can faithfully reproduce a bug. Environmental and observational seismology often require human-chosen data processing parameters, too often implicit knowledge or cultural standards for geophysical data analysis. Some groups report major findings that other groups cannot reproduce. Many chosen parameters in a place are not appropriate in another, limiting the generalization of the processes we infer from observations.

What I am calling the *agentification of research* makes this challne unavoidable. If you want an other research, or an agent (a.k.a., *anyone, anybot*), to reproduce your result, the paper has to say, in words, what the code does and the reasoning behind the method development. Plain enough that the programming language, Python or Julia or C, becomes a detail. 

*Data and Code Availability statements* are becoming irrelevant. A **Reproducibility Statement** is more holistic and the implicit goal of our community. In the text of the manuscripts, or as an attached file, writing out the entire research process requires to spell out the reasoning behind: why this parameter, why this station, why this frequency cutoff. That is the part we usually keep in our heads. Agents make the cost of keeping it there visible.

To push on this, I have been building a pre-submission agent, just at version V1.0, working in my repo, still under test. I designed it around best practices for scientific writing using the AI2 ASTA lit review tools. Its job is narrow on purpose: take formatting, consistency, open-science reporting, and reproducibility checks off my plate so my group and I can spend our attention on depth and scientific thinking. The goal is a paper that needs only a minor revision because the mechanical failures are gone before a reviewer ever sees them. I am genuinely open to critique on it. ([pre-submission agent](https://github.com/mdenolle/academic-practice-agents/tree/main/pre-submission-agent))

## Three experiments

I am embracing the human-AI interaction with research and now designing all of my work, thinking, developing reasoning, logging my AI use, all in the open. A radical move that I am not embarrassed or ashamed to take - and if future models train on it, then great as they will learn about Earth science. There are many low hanging fruits to test, here are just three:

**1. Connecting theories.** Much of theory work in Earth Sciences is interpolation: finding the concept that sits between two existing ideas. I am using agents to do that connecting work inside the dv/v coupling framework, then checking whether the result holds. This is also where the quarter surprised me: back in April, I ran an early version of a project I had planned for an incoming student who decided to join a more prestigious named school (saving 18 months of time, about $120K of research grants with a $200/mo bill to Anthropic), the agent performed the work and proposed a theoretical direction I think could genuinely move my field. Now I am done with teaching, I am back at it (dv/v coupling framework [repos](https://github.com/mdenolle/dvv-coupling-framework) and [paper](https://mdenolle.github.io/dvv-coupling-framework/)).

**2. Reproducible subsurface monitoring — Codameter.** Observational geophysics suffers from human-selected signal-processing parameters and, as a result, no real uncertainty analysis. This is especially true for ambient noise monitoring that turns ambient Earth vibration into subsurface stress meters as new scientific instruments (e.g., see my [review paper](https://comptes-rendus.academie-sciences.fr/geoscience/articles/en/10.5802/crgeos.310/) on critical zone seismology as one of the many examples). Claude scanned roughly 110 monitoring papers and found a wide spread of "best-practice" parameter choices. Each can produce a perfectly good-looking dv/v time series. Slightly change the parameters and the result moves. Codameter is my attempt to scan the parameter space systematically, develop epistemic uncertainty in our processing choices as new error measurements, and propose a new data covariance for uncertainty quantification. (Codameter [repo](https://github.com/Denolle-Lab/codameter) and [paper](https://denolle-lab.github.io/codameter/))

**3. Empowering Science Polymathy.** I am an earthquake-trained scientist. I have had years of attempts to contribute to other research fields, but scientists are absolutely territorials and was told by colleagues and program officers to "ask them what they need" as if I needed to blend in their culture first to contribute to a research topic. As a seismologist providing ground water level (GWL) changes at scale over 20 years of continuous data, the any grant rejections made me question "why don't they want GWL?". Good thing I found great collabortions, including one with [David Montgomery](https://environment.uw.edu/faculty/david-montgomery/) and we will continue creating new science together (e.g., check out agroseismology from [Shi et al, 2026](https://www.science.org/doi/full/10.1126/science.aec0970)). This quarter I am testing how to write a real fluvial geomorphology research project at Mt. Rainier (braiding reorganization during extreme storms [repo](https://github.com/gaia-hazlab/seis-hydro-2-sed), [paper](https://gaia-hazlab.github.io/seis-hydro-2-sed/))

I used exclusively Claude Code for the entire thing to test this hypothesis and the limits of these tools to generate entire research pipelines in adjacent disciplines. The project is super fun, the brainstorming was exciting and iterative. The guardrail is that I brought in an actual domain expert, David Montgomery to verify the work and contribute as a collaborator, not to rubber-stamp it. This is the experiment I am least sure about, and the one I think is most informative: can agents plus genuine expert review let a scientist cross a disciplinary boundary without producing confident nonsense?

## Where it fails, and the guardrails

I am not using these tools because they are mostly reliable and, if prompted, develop fully transparent research products that can be verified.

Models may fabricate. If a graduate student or research fabricate, it's research fraud due to accountability. Models are not accountable and just do it sometimes: we need to catch that. *We* are the human experts, but can also be agents that you designed to critically evaluate every step. For instance, I asked Claude to create an agent to emulate a hydrogeologist from the WA Department of Natural Resources to critique my groundwater modeling work, and it finds flaws in the originally designed (by Claude) model. Making these reviewer agents accessible, the model version of the run, and the resulting critique sent as Github Issues to log the research process in a way that can be actionable. Anyone/Anybot curious can read the history and critique it.

That openness is the guardrail. Because the work is transparent, you can check whether it is wrong. The Mt. Rainier project has a human expert in the loop by design. Codameter exists precisely because I do not trust a single parameter choice, including one an agent picks, and my research group is dissecting every piece of the AI-made work. 

I want to be plain about my own bias here. The honest critique of how I work is that I am impatient. I want to accelerate science, so I want things to go fast and to go well. I also have three kids and I have taken up marathons, so I have very little time. For me a lot of this is an optimization problem. That impatience is a risk, and transparency is how I try to keep it from becoming a liability. Many scientists love the deep reflection time, they love owning the ideas and the thoughts, and it belongs to human enjoyment that cannot be taken away.

None of this would be possible without open data from federal agencies: NSF, USGS, NASA, NOAA. The agents are only as good as the public record they read (the same scientific papers we write in support to tax payer's money and generous donors).

## The narrow claim

As scientists, we are deep critique of each others' work to safeguard correctness and scientific advances forward. We are also fully aware of the reproducibility crisis and has made us disclose of codes and data availability, favoring open source and community led projects in that same reason that many eyes to scientific work and research software will promote rigor and scientific reproducibility.

**Agentification raises the bar on and requires reproducibility.** A paper now has to contain, in words, what an engineer could reproduce in code, and increasingly, the reasoning behind each choice has to be visible too. Arguing for more transparent reproducibility is generally accepted by the community.  

A lot of scientists are worried about AI in research, that it copies open knowledge, replaces it, or simply gets things wrong. I am not ashamed of using it, and I am fully transparent about how. My suggestion to the skeptics is the same thing I would say about any phenomenon: stop arguing from feelings and political views, as a scientist you should be objective and seek evidence of your own before deciding.


## Open question

If implementation is getting cheap and verification is not, then the bottleneck in research practice is moving. The scarce resource is no longer the ability to do the work. It is the human bandwidth to check the work scientific agents do, and the willingness to make reasoning transparent enough to be checked at all.

So two challenges we need to resolve as a research community. First, cost: APIs will not stay cheap forever, and I do  know how much research productivity is worth this expense, will research sponsors pay for it? Second, and harder: if a model fabricates more than a researcher but is also fully auditable, where does trust actually come from?  
