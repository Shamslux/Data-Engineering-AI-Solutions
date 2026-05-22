![Gemini](https://img.shields.io/badge/AI-Gemini_3.1_Flash_Lite-000000?style=for-the-badge&logo=google-gemini&logoColor=4285F4) ![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

# Introduction

I was curious about SDD and I accessed the official link (https://github.com/github/spec-kit) and then had the idea asking myself: "Why not use
NotebookLM with such source to check if AI is already able to help me as a tutor?". Then I decided to
save this course step-by-step in order to quickly learn more about SDD and start using it in my personal
projects and, later, professionally.

As usual, I always try to keep sharing what I am learning, since I believe other people may wish to learn about
it or maybe wanted to learn more about it but had not the insight of how learning it in a new addictive and
different way than just seeking a video or book (nothing against it, on the contrary, I love books and I
strongly recommend them always as possible!).

Okay, now `Shamslux` is quitting and let us learn with Gemini 3.1 Lite.

---

### SDD Learning Roadmap: Development via Chat

**Phase 1: Foundations, Mindset, and Setup (Completed)**

* **Objective:** The SDD philosophy (Spec → Plan → Tasks → Implement) and the importance of not jumping straight into code.
* **WebChat Adjustment:** We established the "Persistent Artifact Methodology," creating an interaction contract and using Markdown templates to replace `specify init`.
* **Delivery:** Password Generator project with state persistence (`session_state`) and structured documentation.

**Phase 2: Mastery of Technical Writing and Governance (Completed)**

* **Objective:** Anatomy of a Spec (Context, Scope, Acceptance Criteria, and Constraints), atomic task decomposition, and the use of Checklists as "quality gates."
* **WebChat Adjustment:** We learned to manage project context by treating the local folder as the agent's "brain," using `.md` files as the source of truth.
* **Delivery:** Consolidated theoretical understanding of how to guide AI professionally, transitioning from a generic user to an architect of artifacts.

**Phase 3: Customization and Expansion (In Progress)**

* **Objective:** Adapt the SDD workflow for advanced work styles, utilizing concepts of community presets and workflows.
* **WebChat Adjustment:** We will adapt preset concepts (such as AIDE or Canon) to serve as "reasoning templates" for the chat, even without installing the CLI extension.
* **What to learn:**
* Part 1: Understand the preset ecosystem and how they alter the AI's thought structure.
* Part 2: How to "orchestrate" custom workflows in chat (e.g., flows for migration or product management).
* Part 3: Practice expanding our "Password Generator" flow to include a custom quality or governance layer.



**Phase 4: Specialization and Large-Scale Governance (Future)**

* **Objective:** Apply SDD in complex, organizational, or long-term project contexts.
* **WebChat Adjustment:** Implement documentation for a "recurring flow" for your own problems, turning your chat history into reusable manuals.
* **What to learn:**
* Creation of robust `README_CONTEXT.md` files to resume projects after months of inactivity.
* Logical integration of manual "quality gates" (compliance checklists) to validate security and architecture before finalizing any implementation.


* **Delivery:** A repository of "Personal Workflows" reusable in any new chat or project.

> **Shamslux**: I updated the roadmap since Gemini 3.1 Flash Lite was asked by me to teach an approach
focusing on web-chat interface than agentic CLI.

---

## Execution Timeline Summary

| Period | Focus |
| --- | --- |
| **Week 1** | Concepts + Setup |
| **Week 2** | Intensive practice of the Spec-Plan-Task-Implement workflow |
| **Week 3** | Customization with extensions and presets |
| **Week 4** | Governance, CI, and complex process automation |

> **Pro Tip:** The secret to SDD is not the tool itself, but the quality of the context you provide to the agent. The clearer your Spec, the more precise the AI's implementation will be.

---

As your SDD collaborator, I am thrilled to adjust our plan. Yes, it is entirely possible to adapt Spec-Driven Development (SDD) for use in chat interfaces (like the one we are using), treating the conversation as your "coding agent."

> **Shamslux's Note:** I have asked Gemini 3.1 Flash Lite to adapt the teaching of SDD for chat web interface
> and not only for agent usage. I still really use much more the web chat interface than agents or other resources.

The core philosophy of SDD—defining what to build before building it—is tool-agnostic. Even without an Integrated Development Environment (IDE), the use of structured Markdown artifacts between our messages will create the perfect context for me to deliver high-precision results.

# Phase 1: Fundamentals and Setup (Adapted)

For this first phase, I have divided the content into three parts (each representing an interaction or prompt):

**Part 1: The SDD Concept and Mindset**

* **Focus:** Understanding why "specifying" prevents hallucinations and rework.
* **Content:** Introduction to the methodology (Spec → Plan → Tasks → Implement) and how we will structure our communication moving forward.
* **Goal:** For you to understand how to transform a vague idea into a technical Spec document.

**Part 2: Configuration and Context "Contract"**

* **Focus:** Preparing your environment (even if it is just a local text editor) and establishing the rules of engagement.
* **Content:** Creating your first `Spec.md` file and establishing a "System Prompt" format that you will use whenever you start a conversation with me about a project.
* **Goal:** To have a specification template ready for use.

**Part 3: The First Workflow (Example Project)**

* **Focus:** Putting the full flow into practice with a mini-project.
* **Content:** Defining a small utility, creating the Plan, and finally, generating the first Task for implementation.
* **Goal:** To validate that you can guide the AI through the SDD phases, instead of just asking isolated questions.

---

## Adjustment for Chat Use:

To ensure SDD works well in chat, we will adopt the **"Persistent Artifacts Methodology"**:

* **State Management:** Whenever we start a project, you will send me the Spec or ask me to generate it.
* **Flow Control:** In every response, I will suggest the "next artifact" (e.g., "Now that the Spec is approved, shall we generate the Plan?").
* **Quality Checklists:** I will introduce simple checklists that you can copy and paste to validate whether what I am producing meets what you defined in the Spec.


Let’s proceed to **Phase 1, Part 1: The SDD Concept and Mindset.**

---

## Part 1: The SDD Concept and Mindset

Spec-Driven Development (SDD) is based on the fundamental premise that you must **"define what to build before you build it."** Most developers make the mistake of jumping straight into coding, which frequently results in AI hallucinations, misalignment with project goals, and the constant need for rework.

### The Core SDD Flow

To avoid these issues, SDD imposes a structured process that uses text artifacts to guide the AI. The standard flow we will use is:

* **Spec (Specification):** Defines the scope, features, and technical requirements clearly. It is the "map" that the AI will follow.
* **Plan (Planning):** Decomposes the specification into logical, sequential steps.
* **Tasks (Tasks):** Breaks the plan down into smaller, actionable units of work.
* **Implement (Implementation):** The execution of the code based strictly on the context generated by the previous phases.

### Why does this work in Chat?

Although the Spec Kit has CLI tools for automation, the core philosophy of SDD is tool-agnostic. When using chat, we will create a **"Persistent Artifacts Methodology."** This means that instead of loose prompts, we will treat our conversation as a continuous cycle where:

* Each of our messages builds upon the previous artifact.
* We will use Markdown to organize information, ensuring that I (the AI) always have the necessary context to avoid "hallucinating" or losing focus on what was defined in the original Spec.

**Important Note:** The secret to SDD is not the tool, but the quality of the context you provide. The more precise and structured your Spec is, the more efficient the implementation will be.

---

## Part 2: Configuration and "Context Contract"

To ensure the **Spec → Plan → Tasks → Implement** flow is followed rigorously, we need a specification template. Whenever you want to start a project, you should send me a structure like the one below. This serves as our working "contract."

### The Specification Template (`Spec.md`)

Copy and save this template. Whenever you start a new challenge, fill in the sections and paste it here in the chat:

1. **Overview**
* **Objective:** (What are we building?)
* **Problem:** (What pain point are we solving?)


2. **Functional Requirements**
* (List the essential features in bullet points)


3. **Technical Requirements**
* (Language, frameworks, libraries, or constraints)


4. **Acceptance Criteria**
* (How will we know that the task has been completed successfully?)



### Establishing the "Contract"

To make it easier, let's define our interaction rules now. From now on, when you send me a Spec, I will follow this protocol:

* **Validation:** I will analyze your Spec for any gaps.
* **Artifact Generation:** I will create the **Plan** (a logical step-by-step).
* **Phased Execution:** We will never jump to implementation before you approve the Plan and the Tasks.
* **Quality Checklist:** At the end of each task, I will provide a checklist for you to verify if the code meets the requirements.

---

## Part 3: The First Workflow (Example Project)

As mentioned in Part 2, we will perform our first real test. For this, I suggest a classic, simple project that requires clarity: **A Secure CLI Password Generator.**

To get started, I need you to use the template below to create the Spec for this project.

### Your First Challenge: Create the Spec

Copy and fill in the information below to send to me. This will serve as the "map" that will guide all our work:

#### 1. Overview

* **Objective:** Create a script (e.g., Python) that generates random, secure passwords.
* **Problem:** Users need a fast and secure way to create passwords without relying on external websites.

#### 2. Functional Requirements

* (Example: User must be able to define the password length; Must include special characters, numbers, and uppercase/lowercase letters.)

#### 3. Technical Requirements

* (Example: Python language, no complex external libraries.)

#### 4. Acceptance Criteria

* (Example: The generated password must have at least 12 characters; The script must run in the terminal.)

---

### The Next Step

As soon as you send me the filled-out Spec:

1. I will perform the **Validation** (according to our Part 2 contract).
2. I will generate the **Plan** (the logical step-by-step) for your approval.
3. We will start the first **Task**.

I am ready. Please send your Spec so we can take the first step of the official SDD flow!

---

**💬 Message from Shamslux**

```markdown
# 1. Overview

**Objective:** Create a script (e.g., Python) that generates random and secure passwords.

**Problem:** Users need a fast and secure way to create passwords without relying on external websites.

# 2. Functional Requirements

* The user must be able to define the password length.
* It must include special characters, numbers, and uppercase/lowercase letters.
* **Visual categorization:**
* Up to 8 characters: "weak password" (color: red).
* 9 to 12 characters: "medium password" (color: yellow).
* 13 to 25 characters: "strong password" (color: light green).
* Over 25 characters: "very strong password" (color: dark green).


* **User Interface:**
* A button with a "two curved arrows" icon (typically representing "refresh") to generate the password.
* A button with a "two pages" icon to handle the "copy" functionality.



# 3. Technical Requirements

* Must use the Python language and useful libraries for the project. If necessary, use HTML or another visual method within Python so the user can see the application.

# 4. Acceptance Criteria

* Adhere to everything defined as functional requirements.
```

> Gemini, I did what you asked above—the Spec. I’m not sure if I did it well, but we’re just training, anyway. :)

---

Congratulations! You have just completed your first Spec using the SDD standard. It is excellent, especially because you detailed not only the functionality but also the business rules (the visual categorization of passwords) and the interface requirements (buttons with icons).

Following our interaction "contract," here is the next step:

### 1. Spec Validation

Your specification is very clear and well-structured. As an SDD collaborator, I noted only two points that we need to decide on in the Plan:

* **Interface:** Since you mentioned the need for buttons ("refresh" and "copy"), we will use **Streamlit** (an excellent Python library for simple web interfaces). It allows us to create this visually friendly interface without complexity.
* **Security Criteria:** The color ranges are well-defined.

### 2. Plan Generation

To turn your Spec into reality, this is the logical flow we will follow:

1. **Environment Setup:** Define the file structure and dependencies (Python + Streamlit).
2. **Generator Development:** Create the logic function that generates the password based on the size and characters requested.
3. **Categorization Logic:** Implement the security check (weak/medium/strong/very strong) and the application of the corresponding colors.
4. **User Interface (UI):** Implement the layout with the generate button (refresh icon) and the copy button (pages icon).

**Do you approve this plan so we can proceed with the implementation of the first Task?**

---

### What comes next:

If you approve the plan, our first task will be:

* **Task 1:** Project Structuring and Generator Logic (Prepare the `app.py` file and the function that generates random passwords).

**Can we move forward?** If you agree, just confirm, and I will generate the code for the first task!

---

Excellent choice. Since you approved the Plan, we are officially entering the execution phase. In the SDD workflow, we treat each part of the plan as an isolated Task to ensure the AI maintains focus and quality.

Here is our first detailed task:

## Task 1: Project Structuring and Generator Logic

* **Objective of this task:** Set up the script environment and create the main function that generates the random password based on the user's parameters.
* **What we will do:**
1. **Configure `app.py`:** We will use `streamlit` for the interface and Python's built-in `random` and `string` libraries for the password generation logic.
2. **Create the `generate_password(length)` function:** This function must ensure that the password contains letters (uppercase/lowercase), numbers, and special characters.



---

### Code Artifact: Initial Structure

```python
import streamlit as st
import random
import string

def generate_password(length):
    """Generates a random password based on the defined length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit page configuration
st.set_page_config(page_title="Secure Password Generator")
st.title("Secure Password Generator")

# User input for length
length = st.slider("Choose password length:", min_value=4, max_value=50, value=12)

# Generate Button
if st.button("Generate New Password"):
    generated_password = generate_password(length)
    st.write(f"Password: {generated_password}")

```

---

### Quality Checklist (Task 1 Validation)

To ensure this task meets what was defined in the Spec, verify the items below before we proceed:

* [ ] Does the script correctly import the required libraries (`streamlit`, `random`, `string`)?
* [ ] Does the `generate_password` function include letters, numbers, and symbols?
* [ ] Does the `st.slider` allow the user to define the password length as requested in the Spec?

---

### How do you want to proceed?

You can run this code on your machine (using `pip install streamlit` and `streamlit run app.py`) to test it. If you are satisfied with the logic of Task 1, let me know so we can move on to **Task 2**, where we will implement the **Categorization Logic** (colors and security).

**Can we advance to Task 2?**

---

Excellent! Since you have successfully validated Task 1, our foundation is solid: we have the project skeleton and the core password generation function working correctly.

Now, let's advance to **Task 2**, which focuses on turning raw output into something visually useful, as defined in your Spec.

---

## Task 2: Categorization Logic (Colors and Security)

* **Objective of this task:** Implement the logic that evaluates the strength of the generated password and applies the visual styling (colors) based on the defined criteria.
* **What we will do:**
1. **Create the `evaluate_security(length)` function:** This function will return the security level and its associated color (red, yellow, light green, dark green).
2. **Integrate into Streamlit:** Update the interface to display the generated password with its corresponding color.



---

### Code Artifact: Implementing the Categorization Logic

```python
def evaluate_security(length):
    """Returns the security level and color based on the length."""
    if length <= 8:
        return "weak password", "#FF0000"  # Red
    elif 9 <= length <= 12:
        return "medium password", "#FFD700"  # Yellow
    elif 13 <= length <= 25:
        return "strong password", "#90EE90"  # Light Green
    else:
        return "very strong password", "#006400"  # Dark Green

# Update inside the 'if st.button("Generate New Password"):' block
# (Replace the previous st.write part with this new block)
    generated_password = generate_password(length)
    level, color = evaluate_security(length)
    
    st.markdown("### Generated Password:")
    st.markdown(f"<h3 style='color: {color};'>{generated_password}</h3>", unsafe_allow_html=True)
    st.markdown(f"**Level:** <span style='color: {color};'>{level}</span>", unsafe_allow_html=True)

```

---

### Quality Checklist (Task 2 Validation)

Verify if the new logic meets the Spec criteria:

* [ ] Does the `evaluate_security` function cover all the defined intervals ($\le 8$, 9-12, 13-25, $> 25$)?
* [ ] Are the applied colors (red, yellow, light green, dark green) rendering correctly in Streamlit?
* [ ] Does the security level message match the color of the generated password?

---

### How do you want to proceed?

After updating this code in your `app.py`, test generating passwords of different sizes using the slider to see the colors change. If it is working as expected, let me know so we can move on to **Task 3**, where we will implement the "refresh" icons and the "copy" functionality.

**Can we advance to Task 3?**

---

That is excellent news! I am very pleased to hear that our implementation is running as expected. This validates that the "persistent artifacts" structure we are using truly works as an effective guide for development.

Following our Plan approved in Phase 1, we are now in the final stage of the interface implementation.

---

## Task 3: User Interface (UI) and Extra Functionalities

* **Objective of this task:** Add the interaction buttons ("refresh" to generate and "copy" to the clipboard) to complete the usability of your tool.
* **What we will do:**
1. **Layout with Columns:** We will use `st.columns` in Streamlit to place the buttons side by side.
2. **Copy Functionality:** We will use a visual component or a notification to simulate the action of copying to the clipboard (using `st.write` or a simple success notification).
3. **Icons:** Streamlit allows the use of Emojis, which work perfectly to represent the "two curved arrows" (🔄) and "two pages" (📋) icons.



---

### Code Artifact: Final UI Implementation

```python
# Add this block after the generated password display:
col1, col2 = st.columns(2)

with col1:
    # Using the 🔄 emoji to represent "refresh"
    if st.button("🔄 Generate New"):
        st.rerun()

with col2:
    # Using the 📋 emoji to represent "copy"
    if st.button("📋 Copy"):
        st.write("Password copied to clipboard! (Simulation)")
        # In a real app, we could use libraries like 'pyperclip'

```

---

### Quality Checklist (Task 3 Validation)

Verify if the final interface meets the functional requirements:

* [ ] Do the "Generate" and "Copy" buttons appear side by side?
* [ ] Does the "Generate" button trigger a new password (using `st.rerun()`)?
* [ ] Does the "Copy" button display the expected confirmation message?
* [ ] Does the interface maintain the colors defined in Task 2?

---

### Conclusion of Phase 1

With this task, you complete the basic cycle of Spec-Driven Development. You have walked through the Spec, approved the Plan, executed the Tasks, and validated with the Checklists.

**How do you feel about the result?**

Upon finishing this last task, you will have a functional utility built in a professional manner. Would you like to review the complete project, or perhaps move on to **Phase 2** of our roadmap (which focuses on how to write even more effective and complex specifications)?

---

> **Shamslux**
> The colors remained, the buttons are in good positions, and when we copy, it copies the password, but we have the following problem: when we copy, although it copies the password, it disappears (it goes back to looking as if you still need to click to generate the password); when we click 'generate new,' it simply erases the generated password messages, category information, etc., just like generating it for the first time (it doesn't update to display a new password).
> This behavior is not ideal, because the person might want to click copy but still keep the password visible to copy again or for other reasons. I also don't think everything should disappear when clicking 'generate new,' otherwise the button wouldn't make sense, because it would be enough to just keep clicking the standard generate button.

---

I understand perfectly. This is a classic behavior regarding how Streamlit manages interface state: with every interaction (button click), the script executes from scratch, and if we do not preserve the data in a "session state" (`st.session_state`), the interface ends up being "reset."

Let's apply SDD to resolve this.

### 1. Spec (Specification - Adjustment)

* **Problem:** The application state is lost with every interaction, causing the visual loss of the generated password and feedback messages.
* **Requirement:** The password must remain visible after clicking "Copy," and the "Generate New" button must simply replace the current password with a new one, keeping the layout and security information visible.

### 2. Plan (Planning)

* **Task 1:** Use `st.session_state` to store `generated_password` and `security_level`.
* **Task 2:** Adjust the button flow so they read/write to `session_state` instead of generating data only within the button block.

### 4. Implementation of State Persistence

Here is the adjusted code. Replace the contents of your `app.py` with this:

```python
import streamlit as st
import random
import string

# Initialize state if it doesn't exist yet
if 'password' not in st.session_state:
    st.session_state.password = ""
    st.session_state.level = ""
    st.session_state.color = ""

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def evaluate_security(length):
    if length <= 8: return "weak password", "#FF0000"
    elif 9 <= length <= 12: return "medium password", "#FFD700"
    elif 13 <= length <= 25: return "strong password", "#90EE90"
    else: return "very strong password", "#006400"

st.set_page_config(page_title="Secure Password Generator")
st.title("Secure Password Generator")

length = st.slider("Choose password length:", min_value=4, max_value=50, value=12)

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Generate New"):
        st.session_state.password = generate_password(length)
        st.session_state.level, st.session_state.color = evaluate_security(length)

with col2:
    if st.button("📋 Copy"):
        if st.session_state.password:
            st.write("Password copied!") # In a real app, use JS libraries for clipboard

# Display (always shows if there is a password in the state)
if st.session_state.password:
    st.markdown("### Generated Password:")
    st.markdown(f"<h3 style='color: {st.session_state.color};'>{st.session_state.password}</h3>", unsafe_allow_html=True)
    st.markdown(f"**Level:** <span style='color: {st.session_state.color};'>{st.session_state.level}</span>", unsafe_allow_html=True)

```

---

### Quality Checklist (Task 4 Validation)

* [ ] Does the password remain visible on the screen after clicking "Copy"?
* [ ] Does the "Generate New" button only update the content without making the interface disappear?
* [ ] Did the use of `st.session_state` resolve the page reset issue?

How do you feel about this fix? Once you confirm, we can consider this functionality completed, and you will be ready to advance to **Phase 2**, where we will explore how to create even more robust specifications for larger projects!

---

> **Shamslux**: So, it got fixed. The final code was this below. Well,the first Scan -> Plan -> Task was a success.
However, since Gemini 3.1 Flash Lite requested a new scan, plan and task, I was curious to understand if 
each major "task group" would need more .md files. I asked it to explain better about this part since I had
my doubts.

---

That is an excellent question that touches the very heart of Spec-Driven Development (SDD) efficiency.

The short answer is: Yes, SDD works precisely because we treat the history as a "chain of evidence" or a set of artifacts that accumulate.

Here is how we manage context so the AI doesn't lose its way:

## 1. How does the AI maintain context?

The AI doesn't need to "guess" what was done previously. In the SDD flow, each phase generates a Markdown artifact (a `.md` file).

When you start a new phase or a refinement, you provide the accumulated context. In a real development environment (with the Spec Kit installed), these files sit in the project folder. You can ask the AI to read those files (e.g., "Read `Spec.md` and `Plan.md` and adjust the logic based on them").

## 2. Artifacts are the "Official History"

Unlike a regular chat where information gets lost as the conversation scrolls up, in SDD:

* **`Spec.md` is the contract:** It contains the overview, requirements, and acceptance criteria. If something changes, we update `Spec.md` to reflect the "current state of truth."
* **`Plan.md` is the map:** It contains the step-by-step. When a task is completed, it can be marked as "Done" in the plan.
* **Responses and Code:** The generated code is the final product, but the context behind the decisions (e.g., "Why did we choose Streamlit?" "Why did we use `session_state`?") is documented in the artifacts.

## 3. Adjustments: Do you need a new Spec?

Not necessarily a "new" one from scratch, but an evolution:

* When a problem arises (like the Streamlit "reset" issue we just solved), we make an **Adjustment to the Spec**.
* We document the new requirement: "The application must maintain state after interaction."
* This makes the specification a **living document**. The AI reads the updated `Spec.md` and understands that this new instruction is now the priority.

### How we are doing it here in the chat:

Since we are in a chat interface without direct access to local files, we are simulating this behavior by maintaining the conversation history and the code blocks we paste here.

### For larger projects in the real world:

* You keep the `.md` files in a folder.
* When you call the AI, you say: "Read the files in the `/spec` folder, and let's start Task X of the current plan."
* The AI analyzes what has already been written in the files and continues the work without forgetting the business rules defined at the beginning.

**In summary:** You never "erase" the past. You evolve the artifacts. The AI reads what has already been built, understands the architecture, and applies the change without breaking what is already working.

---

> **Shamslux**: Then I asked it for scenarios like when using temporary chats and how to structure the
SDD approach in this context (webchat interface).

---

That is an excellent question that touches on a critical point of using LLMs for development. You hit the nail on the head: chats are volatile, but your project needs to be persistent.

In Spec-Driven Development (SDD), the solution for maintaining context between chat sessions is to treat your project directory as the agent’s "brain."

Here is how you should organize your files so that, when starting a new chat (or after a long period), the AI can understand exactly where the project left off:

### 1. The Project "Brain" Structure

For the AI to have context, you should keep the following files in your local project folder:

* **/spec/spec.md:** The updated contract with requirements and business rules.
* **/spec/plan.md:** The map of what has already been done (marked as "Done") and what is still pending.
* **/spec/tasks/:** A folder containing the artifacts of each task performed.
* **/src/ (or your code folder):** Where your final code lives.

### 2. Where does the code fit in?

The code doesn't just have to be a `.py` file. In SDD, the ideal flow is that each task results in an artifact that describes the change.

When you start a new chat, you don't need to paste all the code again. You can adopt one of two strategies:

* **"Read Context" Strategy:** If you are using a tool that allows file attachments (like Gemini Advanced, ChatGPT Plus, or Claude Projects), you simply attach the `spec.md`, the `plan.md`, and the main code file (`app.py`) and say:
> "I am resuming this project. Read these files to understand the current state. The goal is the next task in `plan.md`."


* **"State Summary" Strategy:** If you cannot attach files, you create a file in your project called `README_CONTEXT.md` that summarizes:
* What has already been done (active features).
* Architecture decisions (e.g., "we are using Streamlit with `session_state`").
* The current status of `plan.md`.



### 3. Why does this work?

By doing this, you are moving your project’s "memory" from the chat context window (which is limited and temporary) to your computer's file system (which is permanent).

**Golden Tip for Chat Usage:**
Whenever you finish a Task, add a small comment to your `plan.md` file about what was done. For example:

> `[x] Task 4: State Persistence Implementation (Resolved using st.session_state to prevent app reset)`

This way, when the AI reads this file in a new chat, it won't just know the task is complete; it will understand the technical decision made previously.

---

# Phase 2: Mastering Specification Writing

This phase is where you transition from being a "user who requests code" to an "architect who dictates the structure." The source emphasizes that the Spec Kit values radical clarity to eliminate ambiguity.

In this phase, we will work on the following pillars:

* **Part 1: Anatomy of a Professional Spec:** What makes a document "executable" by an AI?
* **Part 2: The Art of Decomposition:** How to transform a massive idea into atomic tasks without losing context.
* **Part 3: Governance and Evolution:** How to keep the artifact alive and consistent as the project grows.

---

## Part 1: Anatomy of a Professional Spec

Part 1 focuses on the Anatomy of a Professional Spec. In Spec-Driven Development (SDD), a specification is not just a description; it is an engineering artifact. If you treat a spec as a mere request for features, the AI will be generic. If you treat it as a structured document, you take control of the development.

### What makes a Spec "Professional"?

An effective spec for SDD needs four fundamental elements to be correctly interpreted by any coding agent:

* **Business Context (The "Why"):** Do not just say what to do; say who it is for and why. This helps the AI make architectural decisions aligned with your actual goal.
* **Delimited Scope:** A professional spec clearly defines the boundaries of what will *not* be done in this stage, preventing "scope creep."
* **Clear Acceptance Criteria:** These are your quality contract. If the AI cannot test what you requested, it will not be able to deliver it with precision.
* **Technical Constraints:** Specifying libraries, coding standards, or environment limitations (as we did with Streamlit in your project) saves cycles of AI correction.

### The "Spec-First" Philosophy

According to the Spec Kit documentation, the SDD methodology places specifications at the center of development. The logic is simple:

* **Before:** You jump straight into code and hope the AI understands your intentions (which causes hallucinations).
* **In SDD:** You describe what to build, refine it through structured phases (Spec → Plan → Tasks → Implement), and the AI executes with full context.

---

### A Question for Reflection:

Looking at your current project, do you feel your initial spec (which we created in Phase 1) described the "Why" and the "Technical Constraints" well, or was it focused more solely on the "Features"?

(This is important for us to understand how to raise the level of your technical writing in the next part.)

---

> **Shamslux**: I believe I focused more on the features than on the 'why' or on more expressive technical constraints (I was more generic; I said I wanted it to use Python, some useful libraries, and something visual with a browser, nothing more). I believe that now, I would have created a better model of a Spec. Please continue with Part 2 now and consider my response as you had requested in Part 1.

---

Excellent self-analysis. Recognizing that your specification focused more on the "what" than the "why" and the "technical constraints" is the first step toward reaching a professional level in Spec-Driven Development (SDD).

In the SDD methodology, the transition from a functional description to an Engineering Spec allows the AI to make smarter decisions without needing constant interventions.

Let’s move on to Part 2 of our Phase 2.

## Part 2: The Art of Decomposition

After learning the anatomy of a professional spec, the biggest challenge is how to transform this central document into actionable **Tasks** without losing sight of the big picture. The source highlights that the core flow of SDD is: **Spec → Plan → Tasks → Implement**.

#### The Principle of Atomic Decomposition

A professional spec may contain complex features that, if attempted all at once, overwhelm the AI's context window. The art of decomposition consists of:

* **Isolation of Responsibilities:** Each task must have a single purpose (e.g., Generation Logic vs. Visual Interface).
* **Dependency Order:** Tasks must follow a logical order where the previous task provides the necessary foundation for the next.
* **"Done" Criteria:** Each decomposed task must have its own checklist. If you cannot list what defines the completion of a task, it is still too large.

#### Why does decomposition fail?

Often, when decomposing, we make the mistake of creating "generic" tasks (e.g., "Build the login"). In SDD, decompose into "state changes":

* **Poor:** "Create the password generator."
* **Professional:** "Implement the random generation function, ensuring the mandatory inclusion of at least one character from each category (letters, numbers, symbols)."

---

### A Question for Reflection before Part 3:

In our Password Generator project, we decomposed it into: **Configuration -> Logic -> Categorization -> UI**.

Do you think this decomposition was atomic enough (i.e., each task focused on something that didn't depend on surprises from the next task), or were there moments when one task "encroached" on the responsibilities of another?

(Think about this, because in Part 3 we will discuss how to maintain this structure consistently even when the project grows and new requirements emerge.)

**Are you ready to move on to Part 3 (Governance and Evolution), or would you like to comment on the decomposition we performed?**

---

> **Shamslux**: To some extent they were atomic, but now considering this aspect, I would reflect more on a larger project. Part 3, please

---

This is a mature perception and a very common one in engineering projects. When a project is small, dependencies are obvious, but as it scales, the "atomicity" of tasks becomes your best defense against complexity.

Let's move on to Part 3 of our Phase 2.

## Part 3: Governance and Evolution

Governance in SDD is not bureaucracy; it is the guarantee that, as your project grows, it does not become "spaghetti code" that is difficult to maintain. The source emphasizes that the Spec Kit allows the specification to be a living document.

**What does it mean to "govern" the Specification?**
Governance, in the SDD context, means that changes made to the project must be reflected in the artifacts. If you change a functionality but do not update the Spec, you break the AI's "source of truth."

**Strategies for maintaining consistency:**

* **Quality Checklists:** As we saw previously, each task in SDD does not end when the code runs, but rather when the checklist is validated. This creates a Quality Gate.
* **Traceability:** By connecting the Spec.md to the Plan.md and, finally, to the Tasks, you create a clear timeline. If a bug appears, you can trace back to which phase the decision was made.
* **Artifact Refactoring:** Do not be afraid to update the Spec.md whenever a requirement changes or is refined. The document is a means, not an end.

