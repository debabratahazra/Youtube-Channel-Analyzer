# GitHub Copilot Instructions — YouTube Channel Analyzer

## Project Overview
YouTube Channel Analyzer is a Python application that fetches, processes, and visualizes YouTube channel data including subscriber counts, view metrics, video performance, engagement rates, and growth trends using the YouTube Data API v3.

## Tech Stack
- **Language**: Python 3.10+
- **API**: YouTube Data API v3 (via `google-api-python-client`)
- **Data**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`, `plotly`
- **CLI**: `argparse` or `typer`
- **Testing**: `pytest`, `pytest-cov`
- **Linting**: `ruff`, `black`
- **Environment**: `python-dotenv` for API key management

## Code Style Rules
- Follow PEP 8 strictly.
- Use type hints on all function signatures.
- Keep functions small and single-purpose (max ~40 lines).
- Use dataclasses or Pydantic models for structured data.
- Never hardcode API keys — always read from environment variables via `python-dotenv`.
- All public functions must have a docstring (Google style).
- Prefer f-strings over `.format()` or `%`.

## Architecture Conventions
- `src/youtube_analyzer/` — main package
  - `api/` — YouTube API client wrappers
  - `models/` — data models (Channel, Video, Stats)
  - `analysis/` — analytics and metric computation
  - `visualization/` — chart and graph generation
  - `cli/` — command-line interface
  - `utils/` — shared helpers
- `tests/` — mirrors the `src/` structure
- `docs/` — user and developer documentation
- `data/` — cached API responses (gitignored)
- `.env.example` — template for required environment variables

## Security Rules
- NEVER suggest hardcoding API keys, tokens, or secrets in code.
- Always validate and sanitize external API responses before processing.
- Rate-limit API calls; handle `HttpError 429` with exponential backoff.
- Do not log sensitive data (API keys, user tokens).

## Testing Rules
- Every new function must have at least one unit test.
- Mock all external API calls in tests using `unittest.mock` or `pytest-mock`.
- Target ≥80% code coverage; enforce with `pytest-cov`.
- Test file naming: `test_<module>.py`.

## Git Commit Convention
Use Conventional Commits:
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation only
- `test:` adding or fixing tests
- `refactor:` code change without feature/fix
- `chore:` build, CI, tooling

## When Generating Code
1. Always check for an existing utility before creating a new one.
2. Prefer composition over inheritance.
3. Raise specific exceptions (not bare `Exception`).
4. Log at appropriate levels: `DEBUG` for internals, `INFO` for user-facing steps, `ERROR` for failures.
5. Include a `__main__` guard in all CLI entry scripts.
