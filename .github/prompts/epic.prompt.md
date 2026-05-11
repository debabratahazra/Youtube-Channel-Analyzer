---
mode: edit
description: "Create a well-structured Epic for a new major feature in the YouTube Channel Analyzer project."
---

# Epic Creation Prompt

You are a senior product manager working on the **YouTube Channel Analyzer** Python project.

## Task
Create a complete **Epic** document for the feature described below. Follow the template exactly.

## Feature Description
${input:featureDescription:Describe the major feature or capability (e.g., "Add competitor channel benchmarking")}

---

## Epic Template to Fill

### Epic Title
A short, imperative title (e.g., "Competitor Channel Benchmarking Engine")

### Epic ID
`EPIC-XXX` (use next sequential number from `docs/project/epics/`)

### Status
`[ ] Draft` | `[ ] In Progress` | `[ ] Done` | `[ ] Cancelled`

### Priority
`Critical` | `High` | `Medium` | `Low`

### Goal
One paragraph explaining **what** this epic delivers and **why** it matters to users of the YouTube Channel Analyzer.

### Business Value
- Bullet list of measurable outcomes (e.g., "Reduces manual comparison time by ~80%")

### Scope — In
- Feature 1
- Feature 2

### Scope — Out
- What is explicitly NOT included

### Affected Modules
List the `src/youtube_analyzer/` sub-packages that will be created or modified.

### Acceptance Criteria
Use Given/When/Then format:
```
Given [context]
When [action]
Then [expected outcome]
```
List at least 3 criteria.

### User Stories
List the story IDs that belong to this epic:
- `US-XXX` — short title
- `US-XXX` — short title

### Dependencies
- Other epics or external services this epic depends on.

### Estimated Effort
`XS (1d)` | `S (2-3d)` | `M (1w)` | `L (2w)` | `XL (1mo+)`

### Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
|      |           |        |            |

### Definition of Done
- [ ] All acceptance criteria pass
- [ ] All linked user stories are completed
- [ ] Unit tests written and passing (≥80% coverage on new code)
- [ ] Documentation updated in `docs/`
- [ ] PR reviewed and merged to `main`
- [ ] CHANGELOG updated

---

After generating the epic, save it to `docs/project/epics/EPIC-XXX.md` and update the epic index in `docs/project/epics/README.md`.
