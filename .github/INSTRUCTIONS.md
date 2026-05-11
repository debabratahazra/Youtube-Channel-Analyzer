# How to Use GitHub Copilot Prompts & Instructions
## YouTube Channel Analyzer — Complete Workflow Guide

This document explains **every file in `.github/`**, what it does, and **exactly how to invoke it** in VS Code with GitHub Copilot to automate each project management and development task.

---

## Table of Contents

1. [File Map](#file-map)
2. [How Instruction Files Work](#how-instruction-files-work)
3. [How Prompt Files Work](#how-prompt-files-work)
4. [Task Workflows](#task-workflows)
   - [Starting a New Feature (Epic → Stories → Code)](#1-starting-a-new-feature)
   - [Writing Code](#2-writing-code)
   - [Writing Tests](#3-writing-tests)
   - [Reporting a Bug](#4-reporting-a-bug)
   - [Checking Code Coverage](#5-checking-code-coverage)
   - [Writing User Documentation](#6-writing-user-documentation)
   - [Writing Developer Documentation](#7-writing-developer-documentation)
   - [Refreshing the README](#8-refreshing-the-readme)
   - [Updating the Roadmap](#9-updating-the-roadmap)
   - [Generating a Progress Report](#10-generating-a-progress-report)
5. [Recommended Project Folder Structure](#recommended-project-folder-structure)
6. [Quick Reference Card](#quick-reference-card)

---

## File Map

```
.github/
├── copilot-instructions.md             ← Global rules applied to ALL Copilot responses
│
├── instructions/
│   ├── python.instructions.md          ← Auto-applied to *.py files (coding standards)
│   └── testing.instructions.md        ← Auto-applied to tests/**/*.py
│
└── prompts/
    ├── epic.prompt.md                  ← Slash command: create an Epic document
    ├── user-story.prompt.md            ← Slash command: create a User Story
    ├── bug-report.prompt.md            ← Slash command: create a Bug Report
    ├── test-case.prompt.md             ← Slash command: generate test cases
    ├── code-coverage.prompt.md         ← Slash command: analyze & improve coverage
    ├── user-docs.prompt.md             ← Slash command: write user documentation
    ├── dev-docs.prompt.md              ← Slash command: write developer documentation
    ├── readme.prompt.md                ← Slash command: generate/refresh README.md
    ├── roadmap.prompt.md               ← Slash command: generate/update roadmap
    └── project-progress.prompt.md     ← Slash command: generate progress report
```

---

## How Instruction Files Work

Instruction files (`.instructions.md`) are **automatically applied** by GitHub Copilot based on the `applyTo` pattern in their frontmatter. You do **not** need to reference them manually.

| File                                   | Applies To      | What It Enforces                                       |
| -------------------------------------- | --------------- | ------------------------------------------------------ |
| `copilot-instructions.md`              | All files       | Project-wide rules: tech stack, commit style, security |
| `instructions/python.instructions.md`  | `**/*.py`       | PEP 8, type hints, docstrings, logging, error handling |
| `instructions/testing.instructions.md` | `tests/**/*.py` | pytest patterns, mocking, AAA structure, coverage      |

**No action needed** — just write or edit Python files and Copilot will follow these rules automatically.

---

## How Prompt Files Work

Prompt files (`.prompt.md`) are **slash commands** you invoke manually in the Copilot Chat panel.

### To Run a Prompt in VS Code:

1. Open **GitHub Copilot Chat** (press `Ctrl+Shift+I` or click the Copilot icon).
2. Make sure you are in **Agent mode** (select "Agent" from the mode dropdown).
3. Type `/` followed by the prompt file name (without path or extension):

   ```
   /epic
   /user-story
   /bug-report
   /test-case
   /code-coverage
   /user-docs
   /dev-docs
   /readme
   /roadmap
   /project-progress
   ```

4. Copilot will prompt you to fill in any `${input:...}` variables defined in the prompt.
5. Review the generated output and confirm to apply.

> **Tip**: You can also run a prompt with context by selecting code in the editor first, then invoking the slash command.

---

## Task Workflows

### 1. Starting a New Feature

**Goal**: Define the scope of a large feature from epic down to implementable stories.

#### Step A — Create the Epic
```
/epic
```
- Input: A one-paragraph description of the major capability.
- Output: `docs/project/epics/EPIC-XXX.md` with full scope, acceptance criteria, and story list.

#### Step B — Break Down into User Stories
```
/user-story
```
- Input: One specific user-facing behaviour from the epic's scope. Reference the epic ID.
- Repeat for each story in the epic.
- Output: `docs/project/stories/US-XXX.md` per story.

#### Step C — Implement the Code
Open a Python file in `src/youtube_analyzer/` and start coding. The `python.instructions.md` rules apply automatically:
- Copilot will enforce type hints, docstrings, PEP 8, and logging conventions.
- Reference the story ID in your commit: `feat(analysis): add engagement rate calculation [US-003]`

#### Step D — Write Tests
```
/test-case
```
- Input: The function or module you just implemented.
- Output: pytest test file + TC entries in `docs/project/test-cases/TC-LOG.md`.

---

### 2. Writing Code

Just open any `.py` file and use Copilot as normal. The instructions are applied automatically.

**For a specific coding task**, you can be explicit in chat:
```
Add a function to src/youtube_analyzer/analysis/engagement.py that calculates
the engagement rate for a video given view count, like count, and comment count.
Follow the project coding standards.
```

Copilot will automatically apply `python.instructions.md` and `copilot-instructions.md`.

---

### 3. Writing Tests

Open a test file under `tests/` — `testing.instructions.md` is applied automatically.

**Or generate full test suites with:**
```
/test-case
```
- Input: `the calculate_engagement_rate function in analysis/engagement.py`
- Output: Complete pytest file with happy path, edge cases, mocked API calls, and parametrized tests.

**Run tests:**
```bash
pytest --cov=src/youtube_analyzer --cov-report=term-missing -v
```

---

### 4. Reporting a Bug

```
/bug-report
```
- Input: A description of the unexpected behaviour.
- Copilot will investigate the codebase, identify the root cause, propose a fix, and generate a regression test.
- Output: `docs/project/bugs/BUG-XXX.md`.

**After fixing**, commit with:
```
fix(api): handle None subscriber_count when channel hides stats [BUG-XXX]
```

---

### 5. Checking Code Coverage

```
/code-coverage
```
- Input: A module path (e.g., `src/youtube_analyzer/analysis/`) or leave blank for the full project.
- Copilot will:
  1. Show you how to run the coverage command.
  2. Interpret the output to identify gaps.
  3. Generate missing tests to fill those gaps.
  4. Produce a coverage report document.
- Output: Missing tests + `docs/project/coverage/COVERAGE-REPORT-<date>.md`.

**Run manually anytime:**
```bash
pytest --cov=src/youtube_analyzer --cov-report=html:htmlcov --cov-fail-under=80
# Open htmlcov/index.html in a browser for the visual report
```

---

### 6. Writing User Documentation

```
/user-docs
```
- Input: A feature name or CLI command (e.g., `the analyze channel command and its output charts`).
- Output: `docs/user/<feature-name>.md` in plain English for non-developer users.

**When to use**: After completing a user story that introduces a new CLI command, chart type, or output format.

---

### 7. Writing Developer Documentation

```
/dev-docs
```
- Input: A module or subsystem name (e.g., `the api/ package and YouTube API client setup`).
- Output: `docs/developer/<module>.md` covering architecture, classes, data flow, error handling, and testing.

**When to use**: After completing an epic or when onboarding new contributors to a subsystem.

---

### 8. Refreshing the README

```
/readme
```
- No input required — Copilot reads the current codebase state.
- Output: A complete `README.md` replacement with badges, feature list, install instructions, CLI reference, and contributing guide.

**When to use**: After each milestone completion or before a release.

---

### 9. Updating the Roadmap

```
/roadmap
```
- No input required — Copilot reads all epic and story statuses.
- Output: Updated `docs/project/ROADMAP.md` with current milestone progress.

**When to use**: At the start of each sprint or after closing multiple stories.

---

### 10. Generating a Progress Report

```
/project-progress
```
- Input: Report period (e.g., `Sprint 3 (May 6–17, 2026)`).
- Copilot reads all docs under `docs/project/` for current status.
- Output: `docs/project/progress/PROGRESS-<date>.md` for sprint review or stakeholder update.

**When to use**: End of each sprint or weekly.

---

## Recommended Project Folder Structure

Run this once to set up the documentation directories:

```bash
mkdir -p docs/user
mkdir -p docs/developer
mkdir -p docs/project/epics
mkdir -p docs/project/stories
mkdir -p docs/project/bugs
mkdir -p docs/project/test-cases
mkdir -p docs/project/coverage
mkdir -p docs/project/progress
```

Each prompt will save its output to the correct location automatically.

---

## Quick Reference Card

| Task                        | Slash Command       | Output Location                                   |
| --------------------------- | ------------------- | ------------------------------------------------- |
| Define a major feature      | `/epic`             | `docs/project/epics/EPIC-XXX.md`                  |
| Break feature into tasks    | `/user-story`       | `docs/project/stories/US-XXX.md`                  |
| Report a bug                | `/bug-report`       | `docs/project/bugs/BUG-XXX.md`                    |
| Generate tests for code     | `/test-case`        | `tests/unit/.../test_<module>.py`                 |
| Analyze & fix test coverage | `/code-coverage`    | `docs/project/coverage/COVERAGE-REPORT-<date>.md` |
| Write user-facing docs      | `/user-docs`        | `docs/user/<feature>.md`                          |
| Write developer docs        | `/dev-docs`         | `docs/developer/<module>.md`                      |
| Refresh README              | `/readme`           | `README.md`                                       |
| Update the roadmap          | `/roadmap`          | `docs/project/ROADMAP.md`                         |
| Generate progress report    | `/project-progress` | `docs/project/progress/PROGRESS-<date>.md`        |

---

## Enforced Automatically (No Action Needed)

| Rule Set               | File                                           | Trigger                  |
| ---------------------- | ---------------------------------------------- | ------------------------ |
| Project-wide standards | `.github/copilot-instructions.md`              | All Copilot interactions |
| Python coding rules    | `.github/instructions/python.instructions.md`  | Any `*.py` file          |
| Testing rules          | `.github/instructions/testing.instructions.md` | Any `tests/**/*.py` file |
