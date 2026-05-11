---
mode: edit
description: "Create a well-structured User Story for a YouTube Channel Analyzer feature."
---

# User Story Creation Prompt

You are a senior product owner working on the **YouTube Channel Analyzer** Python project.

## Task
Create a complete **User Story** document for the feature described below. Follow the template exactly.

## Story Description
${input:storyDescription:Describe what the user needs (e.g., "As a content creator, I want to see my top 10 videos by engagement rate")}

## Parent Epic (optional)
${input:epicId:Parent epic ID, e.g. EPIC-001 (leave blank if standalone)}

---

## User Story Template to Fill

### Story ID
`US-XXX` (use next sequential number from `docs/project/stories/`)

### Story Title
Short imperative phrase.

### Parent Epic
`EPIC-XXX` or `None`

### Status
`[ ] Backlog` | `[ ] Ready` | `[ ] In Progress` | `[ ] In Review` | `[ ] Done`

### Priority
`Critical` | `High` | `Medium` | `Low`

### Story Statement
```
As a [type of user],
I want to [perform an action],
So that [I achieve a goal / get a benefit].
```

### Persona
Describe the target user:
- **Who**: (e.g., YouTube content creator, digital marketer, data analyst)
- **Goal**: What they're trying to accomplish
- **Pain Point**: What problem this solves

### Acceptance Criteria
Use Given/When/Then format for each criterion:
```
Scenario 1: [name]
  Given [initial context]
  When [user action]
  Then [expected result]
```
Provide at least 3 scenarios including happy path and at least one edge case.

### Technical Notes
- Which modules in `src/youtube_analyzer/` are involved?
- Any API endpoints from YouTube Data API v3 required?
- Any new Pydantic models needed?
- Performance considerations (quota usage, caching)?

### Test Cases
List the test case IDs that cover this story:
- `TC-XXX` — description
- `TC-XXX` — description

### UI / Output Description
Describe the expected CLI output, chart, or data format the user will see.

```
# Example CLI output or data schema
```

### Estimated Effort
`XS (< 2h)` | `S (half day)` | `M (1d)` | `L (2-3d)` | `XL (1w+)`

### Definition of Done
- [ ] Acceptance criteria verified
- [ ] Unit tests pass with ≥80% coverage on changed code
- [ ] Code reviewed and approved
- [ ] Docstrings and type hints complete
- [ ] Story linked to parent epic (if applicable)

---

After generating the story, save it to `docs/project/stories/US-XXX.md` and add a row to the story index in `docs/project/stories/README.md`.
