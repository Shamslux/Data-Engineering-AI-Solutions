![Gemini](https://img.shields.io/badge/AI-Gemini_3.1_Flash_Lite-000000?style=for-the-badge&logo=google-gemini&logoColor=4285F4) ![YouTube](https://img.shields.io/badge/YouTube-212121?style=for-the-badge&logo=youtube&logoColor=FF0000)
> **IMPORTANT**: Credits to Waldemar Neto. Original video link: https://www.youtube.com/watch?v=YFDp-smGYqQ

> **Shamslux**: I found this video interesting. Since I was only relying on Gemini 3.1 Flash Lite using the
GitHub SDD kit as truth-source, I wished to check a human video for observe if I was learning well together
with AI. (It seems AI is doing a good job too).

## Spec-Driven Development: The #1 Skill for Devs in 2026

I have been using AI agents daily for a long time—such as Cloud Code, Cursor, and Copilot—and I’ve reached a conclusion that most people ignore: the model, even though current ones are very good, is not enough. What separates a "so-so" result from a complete, functional system is the context you provide to the agent.

This is where **Spec-Driven Development (SDD)** comes in: a pattern for developing by optimizing context to achieve the best results. In this guide, you will learn how to apply this to any coding agent to develop at scale, with security, while saving tokens and avoiding rework.

---

### 1. The Problem: Why do we get frustrated with AI?

Most developers fail when dealing with large demands. For example, imagine implementing a recommendation system in a streaming service (like a "Fake Flix"). This is a feature that impacts the entire system and touches many modules.

When receiving this demand, people usually do one of two things:

* **Break it into random parts:** They lose context between one task and another.
* **Try to run it all at once:** They generate a plan from a very large PRD (Product Requirements Document).

The plans that AI tools generate today are not built to be long; they are built to execute well-defined tasks. In a complex project, we need to parallelize, understand dependencies between tasks, and know the correct order. Spec-Driven Development solves this.

### 2. The Premise: Optimizing the Context Window

We have 1 million-token windows today, but I don't suggest using them. The larger the window, the higher the chance of hallucination. Try to keep your usage within 200,000 tokens.

When you start using AI, the agent has a clean window. As you work, it gets filled by:

* Your original prompt;
* Required files retrieved by the agent;
* Project rules and guidelines;
* MCPs (Model Context Protocols);
* Loaded skills.

To change 90 files and keep the window under 50,000 tokens, we use **RPI (Research, Plan, Implement)**.

### 3. The RPI Methodology (Research, Plan, Implement)

#### Research Phase

Open an agent focused solely on research. It will go through the codebase, hit relevant files, use skills, and fetch external data (via MCPs) or websites.
**The Secret:** Upon completion, save everything learned into Markdown files. This way, you don't waste tokens researching the same things in the future.

#### Plan Phase

With the learned information saved, we enter the planning phase. Here, we create the **Spec** and, if necessary, the **Design**.
The logic is: first, you expand the scope (research), then you save it in Markdown to be reused during implementation. This saves tokens, as the AI doesn't need to re-research; it consults the spec and the design.

#### Implement Phase

With the spec and design defined, the work is broken down into deliverable tasks. Each task contains:

* What will be done;
* Where it will be done;
* What will be reused;
* Prerequisites from other tasks;
* **Definition of Done (DoD):** This acts as a plan that contains all the necessary context for the AI to write the code without hallucinating.

### 4. Structure of Spec-Driven Development

The structure I recommend (available in the "TLC Spec Driven" skill) follows these steps:

* **Spec:** Explains the problem, goals (e.g., reduce play time), what is out of scope, and the user stories. It is the mandatory reference for the AI.
* **Design (Optional):** For large projects (40+ tasks), the design concentrates important decisions, architecture diagrams, and components, avoiding repetition within each task.
* **Tasks:** Assertive breakdown defining what can be run in parallel, sequentially, etc.
* **State:** Stores important decisions the agent made during implementation. This ensures continuity: you can stop, commit the specs, and continue the rest of the project later, or split it into several Pull Requests.

### 5. Execution at Scale

Currently, we use generic sub-agents. Instead of doing everything in the main window, the agent opens sub-agents for specific research or implementations.

In practice: You can run four sub-agents in parallel, each performing a group of tasks. This optimizes the context, reduces errors (since each agent does something specific), and allows you to implement large changes without blowing up your context window.

---

### How to get started?

If you have a PRD, you can tell the agent: *"This is the new project; I have the PRD and a POC. Use Spec-Driven Development to plan the project."*

* **Golden Tip:** Open one window for research/planning and a fresh, clean context window just for implementation.
* **Flexibility:** You don't need everything all the time. Small projects? Just spec and tasks. Large projects? Use all phases.

Using this methodology allows you to develop at scale, following an assertive process that eliminates the chance of unexpected errors and ensures the AI makes decisions based on clear, defined context.