---
mode: edit
description: "Generate pytest test cases for a module or function in the YouTube Channel Analyzer project."
---

# Test Case Generation Prompt

You are a senior Python test engineer working on the **YouTube Channel Analyzer** project.

## Task
Generate complete **pytest test cases** for the module or function described below. Follow the project's testing instructions in `.github/instructions/testing.instructions.md`.

## Target
${input:target:Describe what to test (e.g., "the calculate_engagement_rate function in analysis/engagement.py")}

## Linked Story (optional)
${input:storyId:User story ID, e.g. US-003 (leave blank if not applicable)}

---

## What to Generate

### 1. Test File Location
Determine the correct file under `tests/` mirroring the `src/` path.

### 2. Required Test Cases

For every public function in the target, generate tests covering:

| Scenario Type | Description |
|--------------|-------------|
| Happy path | Valid inputs, expected output |
| Edge case — zero/empty | Empty list, zero count, empty string |
| Edge case — boundary | Max values, min values, quota limits |
| Error path | Invalid input types, missing required fields |
| API mock | Mock YouTube API response with `pytest-mock` |
| Pagination | Multiple pages via `nextPageToken` |

### 3. Test Structure (AAA)
All tests must follow **Arrange → Act → Assert**:
```python
def test_<function>_<scenario>():
    # Arrange
    ...
    # Act
    result = <function>(...)
    # Assert
    assert result == expected
```

### 4. Fixtures
Define reusable fixtures in `tests/conftest.py` if not already present:
```python
@pytest.fixture
def sample_channel() -> Channel:
    return Channel(
        channel_id="UC_TEST",
        title="Test Channel",
        subscriber_count=50_000,
        view_count=1_000_000,
        video_count=120,
    )
```

### 5. Mocking Template
```python
def test_fetch_channel_data_calls_api(mocker):
    mock_build = mocker.patch("youtube_analyzer.api.client.build")
    mock_execute = mock_build.return_value.channels.return_value.list.return_value.execute
    mock_execute.return_value = {"items": [...]}

    result = fetch_channel_data("UC_TEST")

    mock_execute.assert_called_once()
    assert result is not None
```

### 6. Parametrized Test Template
```python
@pytest.mark.parametrize("views,likes,comments,expected", [
    (10_000, 500, 100, 0.06),
    (0, 0, 0, 0.0),
    (1, 1, 0, 1.0),
])
def test_engagement_rate(views, likes, comments, expected):
    assert calculate_engagement_rate(views, likes, comments) == pytest.approx(expected)
```

### 7. Test Case Document
For each test, also produce a test case document entry:

```
TC-XXX: <test name>
  Story: US-XXX
  Type: Unit | Integration
  Precondition: <what must be true before>
  Steps: <numbered actions>
  Expected: <what assert checks>
  Status: [ ] Not Run | [ ] Pass | [ ] Fail
```

---

After generating, save test cases to the appropriate `tests/` file and append TC entries to `docs/project/test-cases/TC-LOG.md`.
