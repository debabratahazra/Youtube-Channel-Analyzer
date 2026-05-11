---
mode: edit
description: "Generate or refresh the README.md for the YouTube Channel Analyzer project."
---

# README Generation Prompt

You are a senior open-source developer. Generate a complete, polished **README.md** for the **YouTube Channel Analyzer** project based on the current state of the codebase.

## Instructions
1. Read the existing `README.md` (if any) and the project files under `src/`.
2. Read `.env.example` for environment variable names.
3. Generate a full replacement README following the template below.
4. Use real command examples that match the actual CLI interface.
5. Keep language clear and inviting for both technical and non-technical readers.

---

## README Template

```markdown
# YouTube Channel Analyzer 📊

> Analyze YouTube channel metrics, video performance, engagement rates, and growth trends from the command line.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/github/license/your-org/youtube-channel-analyzer)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-pytest-green)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-%E2%89%A580%25-brightgreen)](htmlcov/)
[![Code Style](https://img.shields.io/badge/style-ruff%20%7C%20black-black)](pyproject.toml)

## Features

- 📈 Subscriber and view growth trends over custom date ranges
- 🎬 Top video analysis by views, likes, and engagement rate
- 📊 Interactive Plotly charts and static matplotlib/seaborn exports
- 🔍 Multi-channel comparison and benchmarking
- 💾 Local JSON caching to minimize API quota usage
- 🖥️ Simple CLI interface powered by Typer

## Quick Start

### 1. Prerequisites
- Python 3.10+
- A [YouTube Data API v3 key](https://console.cloud.google.com/apis/library/youtube.googleapis.com)

### 2. Install

```bash
git clone https://github.com/your-org/youtube-channel-analyzer.git
cd youtube-channel-analyzer
pip install -e .
```

### 3. Configure

```bash
cp .env.example .env
# Edit .env and add your YouTube API key
```

`.env`:
```
YOUTUBE_API_KEY=your_api_key_here
```

### 4. Analyze a Channel

```bash
# Analyze by channel ID
python -m youtube_analyzer analyze --channel-id UCxxxxxx

# Analyze last 90 days, save HTML interactive charts
python -m youtube_analyzer analyze --channel-id UCxxxxxx --days 90 --format html
```

## CLI Reference

| Command | Description |
|---------|-------------|
| `analyze` | Fetch and analyze a single channel |
| `compare` | Compare two or more channels side by side |
| `top-videos` | List top N videos by a chosen metric |
| `export` | Export analysis results to CSV or JSON |

Run `python -m youtube_analyzer --help` for full option details.

## Output

Charts are saved to `./output/` by default:

| File | Description |
|------|-------------|
| `subscriber_growth.png` | Monthly subscriber growth line chart |
| `top_videos.png` | Bar chart of top 10 videos by views |
| `engagement.csv` | Per-video engagement metrics table |
| `summary.json` | Full channel summary in JSON format |

## Project Structure

```
src/youtube_analyzer/
├── api/            # YouTube Data API v3 wrappers
├── models/         # Pydantic data models
├── analysis/       # Metric computation
├── visualization/  # Chart generation
├── cli/            # Typer CLI entry point
└── utils/          # Shared helpers & caching
tests/              # pytest test suite (≥80% coverage)
docs/               # User and developer documentation
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests with coverage
pytest --cov=src/youtube_analyzer --cov-report=term-missing

# Lint and format
ruff check src/ tests/
black src/ tests/
```

## Contributing

1. Fork the repo and create a branch: `git checkout -b feat/your-feature`
2. Follow the coding standards in `.github/instructions/python.instructions.md`
3. Write tests for all new code (≥80% coverage required)
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/)
5. Open a Pull Request and fill in the PR template

## License

[MIT](LICENSE)
```

---

After generating, write the output directly to `README.md` in the project root.
