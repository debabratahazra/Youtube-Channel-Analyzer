---
mode: edit
description: "Generate or update developer documentation for a YouTube Channel Analyzer module or subsystem."
---

# Developer Documentation Prompt

You are a senior software engineer writing **developer-facing documentation** for the **YouTube Channel Analyzer** project.

## Task
Generate comprehensive developer documentation for the module or subsystem described below. The audience is a **Python developer** contributing to or extending this project.

## Module / Subsystem to Document
${input:moduleOrSubsystem:Describe the module (e.g., "the api/ package and YouTube API client setup")}

---

## Documentation Template

Save output to `docs/developer/` with an appropriate filename (e.g., `docs/developer/api-client.md`).

---

# [Module Name] — Developer Guide

## Purpose
What this module does and its role in the overall architecture.

## Architecture Diagram
```
[CLI Layer]
    │
    ▼
[Analysis Layer] ←→ [Models Layer]
    │
    ▼
[API Layer]
    │
    ▼
[YouTube Data API v3]
```

## Module Structure
```
src/youtube_analyzer/<module>/
    __init__.py         # Public exports
    <file1>.py          # Description
    <file2>.py          # Description
```

## Key Classes and Functions

### `ClassName`
```python
class ClassName:
    """Brief description."""
```

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `attr_name` | `str` | What it holds |

**Methods:**

#### `method_name(param: type) -> return_type`
- **Purpose**: What it does
- **Parameters**: Description of each param
- **Returns**: What it returns
- **Raises**: Exceptions it can raise
- **Example**:
  ```python
  instance = ClassName(...)
  result = instance.method_name(param)
  ```

### `function_name(param: type) -> return_type`
- **Purpose**: ...
- **Parameters**: ...
- **Returns**: ...
- **Side Effects**: File writes, API calls, etc.
- **Example**:
  ```python
  result = function_name(...)
  ```

## Data Flow

1. **Input**: What data enters this module and from where.
2. **Processing**: Key transformations applied.
3. **Output**: What data leaves and where it goes.

```
Raw API JSON → Pydantic validation → Domain model → Analysis functions → DataFrame
```

## Configuration & Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `YOUTUBE_API_KEY` | ✅ | — | YouTube Data API v3 key |
| `CACHE_TTL_SECONDS` | ❌ | `3600` | How long to cache API responses |
| `MAX_RETRIES` | ❌ | `3` | Retry count for 429 errors |

## Error Handling

| Exception | When Raised | How to Handle |
|-----------|-------------|---------------|
| `YouTubeAPIError` | Any API call failure | Log and propagate; surface to CLI |
| `ChannelNotFoundError` | Invalid channel ID | User-facing error message |
| `QuotaExceededError` | HTTP 429 from YouTube | Exponential backoff; abort after N retries |

## Caching Strategy
- API responses are cached as JSON files in `data/cache/<resource>/<id>.json`.
- Cache is checked before every API call.
- TTL is controlled by `CACHE_TTL_SECONDS`.
- Force-refresh with `--no-cache` CLI flag.

## Adding a New Feature
1. Add the API wrapper function in `src/youtube_analyzer/api/`.
2. Define a Pydantic model in `src/youtube_analyzer/models/`.
3. Add analysis logic in `src/youtube_analyzer/analysis/`.
4. Wire up a CLI command in `src/youtube_analyzer/cli/main.py`.
5. Add unit tests in `tests/unit/` for each new function.
6. Update this doc and the public API reference.

## Testing This Module
```bash
# Run only this module's tests
pytest tests/unit/<module>/ -v

# With coverage
pytest tests/unit/<module>/ --cov=src/youtube_analyzer/<module> --cov-report=term-missing
```

## Known Limitations
- List any known constraints, edge cases, or technical debt.

## See Also
- [User Guide](../user/)
- [Architecture Overview](architecture.md)
- [YouTube Data API v3 Reference](https://developers.google.com/youtube/v3/docs)
