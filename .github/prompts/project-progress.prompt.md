---
mode: edit
description: "Generate or refresh the project progress report for YouTube Channel Analyzer."
---

# Project Progress Report Prompt

You are the project lead for the **YouTube Channel Analyzer** project.

## Task
Generate a **project progress report** that summarizes what has been done, what is in progress, what is blocked, and what comes next. This report is used in sprint reviews and stakeholder updates.

## Report Period
${input:reportPeriod:Report period, e.g. "Sprint 3 (May 6 – May 17, 2026)" or "Weekly update – May 11, 2026"}

---

## Instructions
1. Scan `docs/project/epics/`, `docs/project/stories/`, and `docs/project/bugs/` for current statuses.
2. Read `docs/project/ROADMAP.md` for milestone context.
3. Read the latest coverage report in `docs/project/coverage/`.
4. Generate the report below.
5. Save to `docs/project/progress/PROGRESS-<YYYY-MM-DD>.md`.

---

## Progress Report Template

```markdown
# Project Progress Report
**Period**: <report period>
**Date**: <YYYY-MM-DD>
**Prepared by**: GitHub Copilot (auto-generated)

---

## 🎯 Sprint / Period Goal
One sentence describing the primary objective for this period.

---

## ✅ Completed This Period

### Epics / Stories Closed
| ID | Title | Type | Notes |
|----|-------|------|-------|
| US-XXX | ... | Story | Merged in PR #XX |

### Bugs Fixed
| ID | Title | Severity | Fixed In |
|----|-------|---------|---------|
| BUG-XXX | ... | High | PR #XX |

---

## 🚧 In Progress

| ID | Title | Type | Owner | % Done | Blocker? |
|----|-------|------|-------|--------|---------|
| US-XXX | ... | Story | — | 60% | No |

---

## 🔴 Blocked

| ID | Title | Blocker Description | Action Needed |
|----|-------|-------------------|---------------|
| | | | |

---

## 📊 Metrics

### Code Coverage
| Module | Last Period | This Period | Target | Trend |
|--------|-----------|-------------|--------|-------|
| api/ | —% | —% | 90% | ↑/↓/→ |
| analysis/ | —% | —% | 90% | |
| Overall | —% | —% | 80% | |

### Open Issues
| Category | Count |
|---------|-------|
| Open bugs | X |
| Open stories | X |
| Unstarted stories in current milestone | X |

### Velocity (if tracked)
- Stories completed this period: X
- Story points delivered: X (if estimated)

---

## 🗓️ Next Period Plan

### Goals
1. Complete Milestone X acceptance criteria.
2. Reach ≥80% coverage on `analysis/` module.
3. Fix all P1 bugs.

### Stories Planned
| ID | Title | Priority | Estimate |
|----|-------|---------|---------|
| US-XXX | ... | High | M |

---

## ⚠️ Risks & Issues

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| YouTube API quota changes | Low | High | Monitor Google API announcements |

---

## 📎 References
- [Roadmap](../ROADMAP.md)
- [Latest Coverage Report](../coverage/)
- [Open Bugs](../bugs/README.md)
- [Open Stories](../stories/README.md)
```
