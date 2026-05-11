---
mode: edit
description: "Create a structured Bug Report for the YouTube Channel Analyzer project."
---

# Bug Report Prompt

You are a QA engineer working on the **YouTube Channel Analyzer** Python project.

## Task
Create a complete **Bug Report** for the issue described below. Investigate the codebase if needed to identify the root cause. Follow the template exactly.

## Bug Description
${input:bugDescription:Describe the bug (e.g., "Subscriber count returns None when channel has hidden stats")}

---

## Bug Report Template to Fill

### Bug ID
`BUG-XXX` (use next sequential number from `docs/project/bugs/`)

### Title
Concise, specific title describing what is wrong (not what the user wanted).

### Status
`[ ] Open` | `[ ] In Progress` | `[ ] Resolved` | `[ ] Wont Fix` | `[ ] Duplicate`

### Severity
`Critical` | `High` | `Medium` | `Low`

### Priority
`P1` | `P2` | `P3` | `P4`

### Environment
- OS:
- Python version:
- Package versions (from `requirements.txt`):
- YouTube Data API quota remaining (if relevant):

### Affected Module(s)
List the `src/youtube_analyzer/` files involved.

### Steps to Reproduce
```bash
# 1. Set up environment
cp .env.example .env
# fill in YOUTUBE_API_KEY

# 2. Run command
python -m youtube_analyzer analyze --channel UC_EXAMPLE

# 3. Observe error
```

### Expected Behavior
What should happen according to the spec / acceptance criteria.

### Actual Behavior
What actually happens. Include full error output:
```
Traceback (most recent call last):
  ...
```

### Root Cause Analysis
After investigating the code, describe:
- Which function/line is the immediate cause
- Why it happens (logic error, unhandled `None`, wrong API field name, etc.)

### Proposed Fix
```python
# Before (buggy code)

# After (fixed code)
```

### Regression Risk
Which other areas of the code could be affected by the fix?

### Test Cases to Add
- `TC-XXX` — description of new test that reproduces and prevents regression

### Linked Stories / Epics
- `US-XXX` or `EPIC-XXX` if the bug is in a feature's scope

### Fix Commit
`fix: <description>` — link to PR once resolved.

---

After generating the bug report, save it to `docs/project/bugs/BUG-XXX.md` and add a row to the bug index in `docs/project/bugs/README.md`.
