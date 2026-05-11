---
mode: edit
description: "Analyze and report code coverage for the YouTube Channel Analyzer project."
---

# Code Coverage Analysis Prompt

You are a senior Python engineer working on the **YouTube Channel Analyzer** project.

## Task
Analyze the current test coverage for the module(s) described, identify gaps, and generate missing tests to reach the project target of **≥80% coverage** (90%+ for `api/` and `analysis/`).

## Target Module(s)
${input:targetModules:Module path(s) to analyze, e.g. src/youtube_analyzer/analysis/ or leave blank for full project}

---

## Step 1: Run Coverage Report

```bash
pytest --cov=src/youtube_analyzer \
       --cov-report=term-missing \
       --cov-report=html:htmlcov \
       --cov-fail-under=80
```

## Step 2: Interpret Coverage Output

Parse the `term-missing` output. For each file, identify:

| File | Stmts | Miss | Cover | Missing Lines |
|------|-------|------|-------|---------------|
| ... | ... | ... | ...% | ... |

Flag any file below target:
- 🔴 Critical: < 60%
- 🟡 Warning: 60–79%
- 🟢 OK: ≥ 80%
- ✅ Excellent: ≥ 90%

## Step 3: Identify Untested Code

For each under-covered file, list the uncovered lines and classify each:

| Line Range | Code | Gap Type |
|-----------|------|----------|
| 42–47 | `except HttpError` block | Error path not tested |
| 88 | `if next_page_token:` | Pagination not tested |

Gap Types:
- `Error path` — exception handlers never triggered
- `Edge case` — boundary condition not covered
- `Unreachable` — dead code (flag for removal)
- `Missing mock` — external call not mocked in tests

## Step 4: Generate Missing Tests

For every identified gap, generate a pytest test that covers it. Follow the AAA pattern and mocking rules from `.github/instructions/testing.instructions.md`.

## Step 5: Coverage Report Document

Produce a coverage summary report:

```markdown
## Coverage Report — <date>

### Summary
| Module | Target | Actual | Status |
|--------|--------|--------|--------|
| api/ | 90% | ?% | 🔴/🟡/🟢 |
| analysis/ | 90% | ?% | |
| models/ | 80% | ?% | |
| visualization/ | 80% | ?% | |
| cli/ | 80% | ?% | |
| **Overall** | **80%** | **?%** | |

### Gaps Addressed This Run
- Added `test_fetch_channel_http_error_retries` → covers lines 42–47 in `api/channels.py`
- ...

### Remaining Gaps
- ...

### Next Actions
- [ ] ...
```

---

Save the coverage report to `docs/project/coverage/COVERAGE-REPORT-<YYYY-MM-DD>.md`.
