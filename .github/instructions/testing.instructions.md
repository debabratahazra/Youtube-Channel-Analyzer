---
applyTo: "tests/**/*.py"
---

# Testing Instructions — YouTube Channel Analyzer

## Framework & Tools
- Use **pytest** as the test runner.
- Use **pytest-mock** (`mocker` fixture) or `unittest.mock` for mocking.
- Use **pytest-cov** to measure coverage; enforce ≥80% on every PR.
- Use **pytest-parametrize** for data-driven tests.

## File Naming & Location
- Mirror the `src/` structure under `tests/`.
- Name test files: `test_<module_name>.py`.
- Name test functions: `test_<function_name>_<scenario>`.

```
tests/
    conftest.py                  # Shared fixtures
    unit/
        api/
            test_client.py
            test_channels.py
            test_videos.py
        models/
            test_channel.py
            test_video.py
        analysis/
            test_metrics.py
            test_trends.py
        cli/
            test_main.py
    integration/
        test_api_integration.py  # Skipped in CI unless INTEGRATION=1 env var set
```

## Mocking Rules
- **Always** mock external API calls — never make live YouTube API requests in unit tests.
- Mock at the boundary: patch `googleapiclient.discovery.build` or the wrapper functions in `src/youtube_analyzer/api/`.
- Use `pytest-mock`'s `mocker.patch` for simple patches; use `unittest.mock.MagicMock` for complex return values.
- Assert mock calls: verify both call count and arguments where relevant.

```python
# Example: mocking the YouTube API client
def test_get_channel_stats_returns_model(mocker):
    mock_response = {"items": [{"id": "UC123", "statistics": {"subscriberCount": "1000"}}]}
    mocker.patch(
        "youtube_analyzer.api.channels.build_client",
        return_value=mocker.MagicMock()
    )
    mocker.patch(
        "youtube_analyzer.api.channels.fetch_channel_data",
        return_value=mock_response
    )
    result = get_channel_stats("UC123")
    assert result.subscriber_count == 1000
```

## Test Structure (AAA Pattern)
Every test must follow **Arrange → Act → Assert**:
```python
def test_engagement_rate_calculation():
    # Arrange
    views = 10_000
    likes = 500
    comments = 100

    # Act
    rate = calculate_engagement_rate(views=views, likes=likes, comments=comments)

    # Assert
    assert rate == pytest.approx(0.06)
```

## Coverage Requirements
- Minimum overall coverage: **80%**.
- Critical modules (`api/`, `analysis/`) must reach **90%+**.
- Run with: `pytest --cov=src/youtube_analyzer --cov-report=term-missing --cov-fail-under=80`
- Add to `pyproject.toml`:
  ```toml
  [tool.pytest.ini_options]
  addopts = "--cov=src/youtube_analyzer --cov-report=term-missing --cov-fail-under=80"
  ```

## Fixtures
- Define reusable fixtures in `tests/conftest.py`.
- Scope fixtures appropriately: `function` (default), `module`, or `session`.
- Provide sample channel, video, and stats fixtures as Pydantic model instances.

## Edge Cases to Always Test
- Empty API response (`{"items": []}`)
- API quota exceeded (`HttpError 429`)
- Missing optional fields in API response
- Invalid channel ID formats
- Zero-value denominators in rate calculations
- Pagination (multiple pages of results)

## Integration Tests
- Gate with `@pytest.mark.integration` and an environment variable:
  ```python
  @pytest.mark.skipif(not os.getenv("INTEGRATION"), reason="Integration tests disabled")
  def test_live_channel_fetch():
      ...
  ```
- Integration tests must NOT run in default CI.
