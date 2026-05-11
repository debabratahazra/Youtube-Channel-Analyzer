---
applyTo: "**/*.py"
---

# Python Coding Instructions — YouTube Channel Analyzer

## General Python Standards

- Target Python **3.10+**; use `match/case`, `|` union types, and `X | None` over `Optional[X]`.
- All functions and methods must include **Google-style docstrings**.
- Use **type hints** on every function signature (parameters and return type).
- Maximum function length: **~40 lines**. Split into helpers if longer.
- No bare `except:` — always catch specific exceptions.
- Never use mutable default arguments (e.g., `def f(x=[]):`).

## Imports
- Group imports: stdlib → third-party → local, separated by blank lines.
- Use absolute imports inside the `src/` package.
- Never use wildcard imports (`from module import *`).

## Naming Conventions
- `snake_case` for functions, variables, modules.
- `PascalCase` for classes.
- `UPPER_SNAKE_CASE` for constants.
- Prefix private members with a single underscore `_`.

## Data Models
- Prefer **Pydantic v2 BaseModel** for API response models.
- Use **dataclasses** for lightweight internal data transfer objects.
- Always validate data at system boundaries (API response ingestion).

## Environment & Secrets
- Read all secrets and config from environment variables using `python-dotenv`.
- Reference `.env.example` for all required keys — never commit a real `.env`.
- Raise `EnvironmentError` with a descriptive message if a required variable is missing.

## Logging
- Use the stdlib `logging` module. Never use bare `print()` for application output.
- `DEBUG` — detailed internal state.
- `INFO` — normal operational events.
- `WARNING` — unexpected but recoverable situations.
- `ERROR` — failures that need attention.
- Configure the root logger in `__main__` or CLI entry point only.

## Error Handling
- Define project-specific exceptions in `src/youtube_analyzer/utils/exceptions.py`.
- Re-raise external library exceptions with context: `raise YouTubeAPIError("...") from e`.
- Handle `googleapiclient.errors.HttpError` 429 with exponential backoff.

## API Interaction
- All YouTube Data API v3 calls must go through wrapper functions in `src/youtube_analyzer/api/`.
- Always check quota-sensitive endpoints and log quota usage at DEBUG level.
- Cache API responses to `data/` using JSON files; check cache before making a live call.

## File & Module Layout
```
src/youtube_analyzer/
    __init__.py
    api/
        __init__.py
        client.py          # YouTube API client setup
        channels.py        # Channel resource calls
        videos.py          # Video resource calls
        search.py          # Search resource calls
    models/
        __init__.py
        channel.py         # Channel Pydantic model
        video.py           # Video Pydantic model
        stats.py           # Stats/metrics models
    analysis/
        __init__.py
        metrics.py         # Metric computation functions
        trends.py          # Trend analysis functions
        engagement.py      # Engagement rate calculations
    visualization/
        __init__.py
        charts.py          # matplotlib/seaborn chart helpers
        interactive.py     # Plotly interactive charts
    cli/
        __init__.py
        main.py            # Entry point (typer app)
    utils/
        __init__.py
        exceptions.py      # Custom exceptions
        helpers.py         # Shared utility functions
        cache.py           # File-based caching utilities
```

## Performance
- Use `pandas` vectorized operations; avoid row-by-row loops on DataFrames.
- Paginate YouTube API list results using `nextPageToken`; never assume a single page.
- Use `concurrent.futures.ThreadPoolExecutor` for parallel independent API calls.
