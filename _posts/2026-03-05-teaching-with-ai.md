---
layout: default
title: "Translating a Textbook: How I Use AI to Build a Living Seismology Course"
series: agents-for-academic-practice
repo_url: "https://github.com/mdenolle/academic-practice-agents"
skills_url: ""
discussion:
  url: ""
---

## One Prompt, Two Deliverables, and a Sign Error

I was preparing Lecture 7 of my seismology course at the University of Washington. The topic: moment tensors. The source material: Peter Shearer's *Introduction to Seismology*, the standard reference that most of us learned from and still teach from.

The textbook treatment is rigorous. The decomposition of the moment tensor into its isotropic, deviatoric, double-couple, and CLVD components follows a mathematically precise sequence that is correct but not optimized for how students actually build intuition.

I opened openAI ChatGPT - 5.3, pasted the relevant textbook Chapter 9.2 as a PDF, and wrote a single structured prompt[^moment-tensor-prompt] asking for a whiteboard lecture and a companion Jupyter notebook covering moment tensor decomposition, source types, the Moon/Lune representation, modern inversion methods, and USGS catalog examples.

What came back surprised me.

The decomposition flow — isotropic to deviatoric to double-couple to CLVD — was reformulated into a sequence that was dramatically easier to explain. The mathematical content was intact. The pedagogical scaffolding was better than what I had built manually over several years of teaching the same material. The Jupyter notebook included well-structured exercises that bridged the textbook formalism to modern observational examples.

One prompt. Two deliverables. Minimal iteration needed.

Except for one problem. The polarities in the four quadrants of the focal sphere, separated by the nodal planes, were not physically correct. A compressional quadrant and a dilatational quadrant were swapped. The AI had produced a confident, cleanly formatted, and wrong radiation pattern.

I caught it in class, comfortable showing my own imperfections in using GenAI tools for classroom exercise and pointing this to the students so that they also learn from it. I know what a focal mechanism looks like. I fixed it in thirty seconds.

A student would have been confused but trusting of the instructor.

This is the story of how I build my seismology course now, and it is entirely about the process.

## The Role: Translator, Not Author

I am not rewriting Peter Shearer's textbook. The physics of elastic wave propagation, source mechanics, and Earth structure has not changed.  Textbooks do not need to change much for what they cover.

What has changed is everything around the fundamentals.

The data volumes are orders of magnitude larger. The computational tools are different. The research questions that students will encounter after this course are built upon textbook concepts but approached with methods and datasets that did not exist when the textbook was written. Induced seismicity monitoring, machine-learning phase pickers, distributed acoustic sensing, wavefield simulation, real-time moment tensor inversion at scale — these are not future topics. They are present-day research.

The gap between textbook and research frontier grows every year because the frontier moves and the textbook, appropriately, stays anchored.

My role is to bridge that gap. Not as a textbook author, but as a researcher-teacher. I am a *translator*. I take stable, well-established physics and tailor its presentation to my specific students, connecting it to the tools and questions they will encounter in their research lives.

The result is a [Jupyter Book](https://uw-geophysics-edu.github.io/ess-412-512-intro2seismology) companion to Shearer that ChatGPT 5.3, Claude Sonnet 4.6 and Opus 4.6, and I are writing together. It is not a reproduction of Shearer — students still need the textbook for full derivations and in-depth discussions. The Jupyter Book translates the main points that support my syllabus into a different delivery mode: interactive notebooks with code, visualizations, and exercises connecting the formalism to modern data and tools. A companion, not a replacement.

Traditional course development cannot keep pace with how fast tools and data evolve. Building a new lecture from scratch takes days; a fifteen-week course has thirty or more lectures. AI-assisted course design compresses the initial drafting phase from days to hours, freeing time for the parts of teaching that remain irreducibly human: reading the room, mentoring individual students, judging when an explanation has actually connected. Jose Antonio Bowen and C. Edward Watson's *Teaching with AI* has been shaping how I think about this space — particularly around tutorbots and the deliberate structuring of AI-student interactions. I plan to experiment with their ideas in future posts.

I define the scientific anchor, AI drafts the instructional translation, and I validate every research-to-fundamentals link.

## The Process: Iterate to Converge

This is a post about process, so let me describe the workflow precisely.

**Step 1: The unchanging layer.** I start with a relevant chapter or section that provides the physics foundation that does not move. The textbook remains the required reference; students must read it and work through the derivations. I do not ask the AI to reproduce that content. I ask it to help me build the companion layer that sits alongside it.

**Step 2: The bridge layer.** I attach recent papers — typically two or three — that use or extend the textbook concepts with modern data or methods. For every lecture, I explicitly map each paper to the specific textbook concept it extends. These are the bridge between settled science and current research. For the moment tensor lecture, this meant papers on full-waveform moment tensor inversion and non-double-couple source characterization in geothermal systems.

**Step 3: The prompt.** Each ChatGPT project carries a standing instruction file — what I call a *skill* — that encodes the persistent constraints for that role: target audience, tone, pedagogical philosophy, what the model should and should not do with source material.[^skill-file] On top of that skill, I write a specific prompt for each lecture that layers in the particular content and deliverables I need. For the moment tensor lecture, the skill already specifies:
- Translate content for advanced undergraduates with introductory physics and linear algebra.
- Preserve the physics exactly. Do not simplify the math; simplify the *explanation*.
- Restructure derivation sequences if a more intuitive ordering exists.
- Connect concepts to observational examples from attached papers.

The lecture-specific prompt then adds: generate a whiteboard lecture and a Jupyter notebook for chapter 9.2, covering these particular learning outcomes, these source types, these catalog examples. For each research finding, the agent must return four elements: the anchor principle, the new evidence, the instructional relevance, and the verification check. This task is a *translation task*: it takes correct content and reshapes it for a specific audience with specific goals.

[^skill-file]: The skill file for seismology course development is publicly available in the [academic-practice-agents](https://github.com/mdenolle/academic-practice-agents) repository, alongside other agent specifications I use across academic roles. These skills are to be iterated on, AI and my vision for education are moving fast.

**Step 4: Review, deploy, iterate.** I review the output (physics first, pedagogy, relevance) and restructure it until it becomes *my best version of the class yet*. Then I give the lecture, observe what works and what confuses, and return to the AI with adjusted instructions. This cycle should repeat until convergence (if I allocate the time for it). The moment tensor lecture converged fast. Other lectures have taken three or four passes.

The key insight: **the physics does not change between iterations. The translation does.**

## Where It Breaks: The Polarity Error and What It Means

The focal sphere polarity error in Lecture 7 was not catastrophic — compression and dilatation swapped in two quadrants, the figure rendered cleanly, the labels were correct, the surrounding text was consistent with the (wrong) figure. This is exactly the failure mode that matters most: not the obvious errors, but the ones that are *almost* right, formatted with the confidence that makes AI-generated content feel authoritative.

I caught it in thirty seconds because I have spent decades studying earthquake source mechanics. That knowledge is not something I can prompt-engineer into the model. The AI accelerates translation, synthesis, and formatting. But the verification — the moment where an expert says *this quadrant is wrong* — cannot be removed. Domain expertise is not diminished by this workflow. It is the error-correction mechanism that makes it safe.

## The Deeper Pattern

Three recurring observations from this work:

**Domain expertise becomes more valuable, not less.** The AI can synthesize and translate at speed. But the quality of the output is bounded by the quality of the verification. An expert who can catch a polarity error in seconds is more valuable in this workflow than an expert who builds everything from scratch but takes weeks. Expertise shifts from production to judgment.

**Academic timelines are misaligned with AI innovation speed.** Course development, textbook revision, curriculum committee review — these operate on multi-year cycles. The tools and data that students need to understand operate on monthly cycles. AI-assisted course design is one mechanism for closing that gap, not by abandoning rigor but by accelerating the iteration between stable science and evolving application.

**Context engineering is becoming a core teaching skill.** The quality of the AI output depends almost entirely on how I structure the prompt: what textbook content I include, what papers I attach, what constraints I specify, what I explicitly exclude. This is not casual prompting. It is a form of pedagogical design — deciding what the model should and should not do with the source material. The prompt is a teaching decision.

## An Open Question

Here is what I have not resolved.

My students also have access to AI models. They can paste Shearer's textbook into ChatGPT and ask for an explanation of moment tensor decomposition. They may get output similar to what I generated — perhaps even the same pedagogical reformulation, perhaps with the same polarity error. Developing guardrails for hallucination for teaching bots seems critical.

Does the carefully designed lecture still matter if students can generate their own version? Is the value of the instructor's curation visible to a student who has not yet developed the expertise to distinguish good translation from subtly wrong translation?

I have not resolved how visible expert curation is to students when AI output is fluent. In my current workflow, fundamentals remain the anchor, and each AI-generated draft is only accepted after I trace every claim back to textbook mechanics and current evidence. The unresolved question is pedagogical: how do we teach students to perform that same verification, rather than outsource judgment to the interface? In the next post, I will test this same anchor-bridge-verification framework in proposal development, where rigor and relevance are judged under tighter constraints.

[^moment-tensor-prompt]: Full prompt: "Come up with a whiteboard lecture about this chapter 9.2 on moment tensor for a 20 min live lecture, then come up with a notebook to add to our collection of synthetic tests and exercise that will help build intuition around the various elements of chapter 9.2, based on the learning outcomes of moment tensor symmetry, double couple component, isotropic component, and CLVD in the context of seismic sources: earthquake shear faults, hydrofracture, volcanic caldera collapse, landslides / single force mechanism (search for scientific context in the research geophysical scientific peer reviewed literature for best use cases), also research on the Moon/Lune representation of moment tensors in general from Carl Tape's work, and provide an example on how to read the moment tensors provided by USGS and other earthquake catalogs. Add to the lecture a section on how researchers calculate moment tensors nowadays (e.g., polarity or full waveform inversion etc)."
