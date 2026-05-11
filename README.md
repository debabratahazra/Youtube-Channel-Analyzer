# YouTube Niche Channel Analyzer 📊

> Find YouTube niche opportunities by identifying channels with **high views but low subscribers** — your gap in the market — across 8 profitable niches.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/github/license/your-org/youtube-channel-analyzer)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-informational)](https://www.microsoft.com/windows)

---

## What It Does

This tool connects to the YouTube Data API v3, searches across **8 profitable niches**, collects channel statistics, scores each channel on a **0–100 opportunity scale**, and exports the results to colour-coded Excel workbooks and CSV files — so you can instantly see where the content gaps are.

---

## 8 Analysed Niches

| #   | Niche                       | CPM Range |
| --- | --------------------------- | --------- |
| 1   | Finance & Investing         | $15 – $50 |
| 2   | Business & Entrepreneurship | $12 – $40 |
| 3   | Technology & Software       | —         |
| 4   | Health & Wellness           | $8 – $25  |
| 5   | True Crime                  | $5 – $15  |
| 6   | Motivational & Self Help    | —         |
| 7   | AI & Future Technology      | —         |
| 8   | History & Education         | —         |

---

## Features

- 🔍 Keyword-based YouTube search across all 8 niches (15 keywords each)
- 📊 Channel scoring 0–100 based on views-to-subscribers ratio
- 💰 Revenue potential estimates using niche CPM ranges
- 📁 Professional Excel reports with colour coding, per-niche sheets, and charts
- 📄 CSV export for use in external tools
- 🖥️ Colour-coded interactive CLI menu (`colorama`)
- ⏳ Progress indicators and rate-limit-safe pacing (`tqdm`)
- 🔒 API key loaded securely from `.env` (`python-dotenv`)
- 📝 Automatic logging to `results/logs/analyzer.log`

---

## Prerequisites

- **Python 3.10+** — [Download](https://www.python.org/downloads/)
- A **YouTube Data API v3 key** — [Get one here](https://console.cloud.google.com/apis/library/youtube.googleapis.com)

---

## Setup (Windows)

### 1. Clone the Repository

```bat
git clone https://github.com/your-org/youtube-channel-analyzer.git
cd "youtube-channel-analyzer"
```

### 2. Create & Activate the Virtual Environment

```bat
:: Create (only needed once)
python -m venv .venv_win

:: Activate
.venv_win\Scripts\activate
```

Your prompt changes to `(.venv_win)` when the environment is active.

### 3. Install Dependencies

```bat
pip install -r requirements.txt
```

| Package                    | Version | Purpose                             |
| -------------------------- | ------- | ----------------------------------- |
| `google-api-python-client` | ≥2.100  | YouTube Data API v3 client          |
| `pandas`                   | ≥2.1    | Data processing & report generation |
| `openpyxl`                 | ≥3.1.2  | Excel workbook creation             |
| `requests`                 | ≥2.31   | HTTP calls                          |
| `python-dotenv`            | ≥1.0    | `.env` file management              |
| `colorama`                 | ≥0.4.6  | Coloured terminal output (Windows)  |
| `tqdm`                     | ≥4.66   | Progress bars                       |

### 4. Configure Your API Key

```bat
copy .env.example .env
```

Edit `.env` and add your key:

```
YOUTUBE_API_KEY=your_youtube_api_key_here
```

> **Security**: Never commit your `.env` file — it is already in `.gitignore`.

---

## Running the Tool

```bat
:: Activate the environment first
.venv_win\Scripts\activate

:: Launch the interactive menu
python main.py
```

### Main Menu Options

```
  1. 🔍 Analyze ALL 8 Niches (Complete Analysis)   ~15–25 min
  2. 💰 Analyze Specific Niche                      ~3–5 min
  3. 🏆 Quick Top Opportunity Scan                  ~5–8 min
  4. 📊 View Previous Results
  5. ❌ Exit
```

---

## Output

All results are saved to `results/reports/`:

| File                                      | Description                                                       |
| ----------------------------------------- | ----------------------------------------------------------------- |
| `YouTube_Niche_Analysis_<timestamp>.xlsx` | Full colour-coded Excel workbook with per-niche sheets and charts |
| `YouTube_Niche_Analysis_<timestamp>.csv`  | Flat CSV of all channels for external analysis                    |
| `results/logs/analyzer.log`               | Timestamped debug and error log                                   |

### Excel Workbook Sheets

- **📊 SUMMARY** — executive overview across all niches
- **🔍 ALL CHANNELS** — every qualifying channel in one sheet
- **Per-niche sheets** — one tab per niche with colour-coded opportunity scores

### Opportunity Score Guide

| Score  | Grade       | Meaning                                       |
| ------ | ----------- | --------------------------------------------- |
| 80–100 | 🏆 Excellent | Prime opportunity — high views, very low subs |
| 65–79  | ✅ Good      | Strong opportunity worth investigating        |
| 50–64  | 📊 Fair      | Moderate opportunity                          |
| < 50   | 📌 Low       | Competitive or saturated                      |

---

## Project Structure

```
youtube-channel-analyzer/
├── .venv_win/               ← Windows virtual environment (not committed)
├── main.py                  ← Entry point — run this file
├── youtube_analyzer.py      ← Core analysis engine (YouTubeAnalyzer class)
├── report_generator.py      ← Excel & CSV report builder (ReportGenerator class)
├── display_results.py       ← CLI colour output (DisplayManager class)
├── niche_keywords.py        ← 8 niches × 15 keywords + CPM data
├── config.py                ← Settings loaded from .env
├── requirements.txt         ← Python dependencies
├── .env.example             ← Template — copy to .env and fill in your key
├── results/
│   ├── reports/             ← Generated Excel and CSV files
│   └── logs/                ← analyzer.log
└── .github/
    ├── copilot-instructions.md
    ├── INSTRUCTIONS.md      ← How to use all Copilot prompts
    ├── instructions/        ← Auto-applied coding & testing rules
    └── prompts/             ← Slash-command prompt templates
```

---

## Deactivating the Environment

```bat
deactivate
```

---

## Contributing

1. Fork the repo and create a branch: `git checkout -b feat/your-feature`
2. Follow the coding standards in [.github/instructions/python.instructions.md](.github/instructions/python.instructions.md)
3. Write tests for all new code (≥80% coverage required)
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`, `test:`
5. Open a Pull Request

See [.github/INSTRUCTIONS.md](.github/INSTRUCTIONS.md) for the full workflow guide including how to use Copilot prompts to create epics, user stories, bug reports, and more.

---

## License

[MIT](LICENSE)

