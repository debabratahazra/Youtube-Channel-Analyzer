---
mode: edit
description: "Generate or update the project roadmap for YouTube Channel Analyzer."
---

# Roadmap Generation Prompt

You are a senior product manager for the **YouTube Channel Analyzer** project.

## Task
Generate or update the **project roadmap** based on the current state of completed epics, open issues, and the project vision.

## Instructions
1. Read existing epics in `docs/project/epics/` to determine what is done vs. planned.
2. Read any open user stories in `docs/project/stories/`.
3. Synthesize a forward-looking roadmap with realistic phases.
4. Update `docs/project/ROADMAP.md`.

---

## Roadmap Template

```markdown
# YouTube Channel Analyzer — Project Roadmap

> Last updated: <YYYY-MM-DD>
> Status: Active development

## Vision
A fully-featured, open-source Python tool that empowers content creators and digital marketers to make data-driven decisions about their YouTube channels — accessible from the command line and exportable for use in any BI tool.

---

## Milestones

### ✅ Milestone 0 — Project Scaffold (Completed)
> Target: Week 1

- [x] Repository structure set up (`src/`, `tests/`, `docs/`)
- [x] CI/CD pipeline with GitHub Actions
- [x] Dev environment: `ruff`, `black`, `pytest-cov` configured
- [x] `.env.example` and secrets management

---

### 🚧 Milestone 1 — Core Data Fetching (In Progress)
> Target: <date range>

| ID | Feature | Status | Epic |
|----|---------|--------|------|
| US-001 | Fetch channel metadata | 🟡 In Progress | EPIC-001 |
| US-002 | Fetch video list with pagination | 🔴 Not Started | EPIC-001 |
| US-003 | Cache API responses locally | 🔴 Not Started | EPIC-001 |
| US-004 | CLI `analyze` command (basic) | 🔴 Not Started | EPIC-001 |

---

### 📋 Milestone 2 — Analytics Engine
> Target: <date range>

| ID | Feature | Status | Epic |
|----|---------|--------|------|
| US-005 | Engagement rate calculation | 🔴 Not Started | EPIC-002 |
| US-006 | Subscriber growth trend | 🔴 Not Started | EPIC-002 |
| US-007 | Top N videos by metric | 🔴 Not Started | EPIC-002 |
| US-008 | View velocity (rolling average) | 🔴 Not Started | EPIC-002 |

---

### 📋 Milestone 3 — Visualization
> Target: <date range>

| ID | Feature | Status | Epic |
|----|---------|--------|------|
| US-009 | Static charts (matplotlib/seaborn) | 🔴 Not Started | EPIC-003 |
| US-010 | Interactive charts (Plotly) | 🔴 Not Started | EPIC-003 |
| US-011 | HTML report export | 🔴 Not Started | EPIC-003 |

---

### 📋 Milestone 4 — Multi-Channel Comparison
> Target: <date range>

| ID | Feature | Status | Epic |
|----|---------|--------|------|
| US-012 | Compare 2+ channels side-by-side | 🔴 Not Started | EPIC-004 |
| US-013 | Benchmark against category average | 🔴 Not Started | EPIC-004 |

---

### 💡 Milestone 5 — Extended Features (Future)
> Planned / under consideration

- Scheduled analysis with email/Slack notifications
- Web dashboard (FastAPI + React)
- YouTube Shorts-specific analytics
- Keyword and SEO analysis using video descriptions/titles
- Integration with Google Sheets export

---

## Status Legend
| Symbol | Meaning |
|--------|---------|
| ✅ | Completed |
| 🚧 | In Progress |
| 📋 | Planned |
| 💡 | Future / Idea |
| ❌ | Cancelled |

## Contributing to the Roadmap
Open an issue or discussion to propose new features. All suggestions are evaluated against project priorities in the next planning cycle.
```

---

After generating, save to `docs/project/ROADMAP.md`.
