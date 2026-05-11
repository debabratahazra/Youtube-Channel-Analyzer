---
mode: edit
description: "Generate or update the end-user documentation for a YouTube Channel Analyzer feature or command."
---

# User Documentation Prompt

You are a technical writer creating **end-user documentation** for the **YouTube Channel Analyzer** CLI application.

## Task
Generate clear, friendly user documentation for the feature or command described below. The audience is a **non-developer YouTube content creator or digital marketer**.

## Feature / Command to Document
${input:featureOrCommand:Describe the feature or CLI command (e.g., "the `analyze channel` command and its output charts")}

---

## Documentation Template

Save output to `docs/user/` with filename matching the feature (e.g., `docs/user/analyze-channel.md`).

---

# [Feature Name] — User Guide

## Overview
One paragraph: what this feature does and what problem it solves for the user. No technical jargon.

## Prerequisites
Before using this feature, ensure you have:
1. **Python 3.10+** installed.
2. A **YouTube Data API v3 key** — see [Getting a YouTube API Key](docs/user/setup-api-key.md).
3. The tool installed:
   ```bash
   pip install youtube-channel-analyzer
   ```
4. Your API key in a `.env` file:
   ```
   YOUTUBE_API_KEY=your_key_here
   ```

## Quick Start

```bash
# Analyze a channel by URL or ID
python -m youtube_analyzer <command> [OPTIONS]
```

## Step-by-Step Instructions

### Step 1: [First action]
Plain-language description with a screenshot placeholder or code block.

```bash
# Example command
```

**What you'll see:**
```
# Example output
```

### Step 2: [Second action]
...

## Understanding the Output

### Charts / Reports Generated
| Output | Description | Location |
|--------|-------------|----------|
| Subscriber Growth Chart | Line chart showing monthly subscriber growth | `output/subscriber_growth.png` |
| Top Videos by Views | Bar chart of 10 highest-viewed videos | `output/top_videos.png` |
| Engagement Rate Table | CSV with per-video engagement metrics | `output/engagement.csv` |

### Key Metrics Explained
| Metric | What It Means | How It's Calculated |
|--------|--------------|-------------------|
| Engagement Rate | % of viewers who interacted | `(likes + comments) / views × 100` |
| View Velocity | Average daily views in the last 30 days | `total_views_30d / 30` |

## Common Options

| Flag | Default | Description |
|------|---------|-------------|
| `--channel-id` | required | YouTube channel ID or URL |
| `--days` | `30` | Number of past days to analyze |
| `--output-dir` | `./output` | Where to save charts and reports |
| `--format` | `png` | Chart format: `png`, `html` (interactive) |

## Troubleshooting

### "API quota exceeded"
Your YouTube Data API free quota (10,000 units/day) has been exhausted.
**Fix**: Wait until midnight Pacific Time for the quota to reset, or request a higher quota in [Google Cloud Console](https://console.cloud.google.com).

### "Channel not found"
The channel ID may be incorrect or the channel may have been deleted.
**Fix**: Verify the channel ID from the URL: `youtube.com/channel/UC_XXXX` — the ID starts with `UC`.

### "Missing API key"
The `YOUTUBE_API_KEY` environment variable is not set.
**Fix**: Copy `.env.example` to `.env` and add your key.

## FAQ

**Q: Can I analyze a private channel?**
A: No. YouTube Data API v3 only returns public channel data.

**Q: How many videos does the tool analyze?**
A: By default, up to the 50 most recent videos. Use `--max-videos` to change this.

## Related Documentation
- [Developer Guide](../developer/architecture.md)
- [API Key Setup](setup-api-key.md)
- [Full CLI Reference](cli-reference.md)
