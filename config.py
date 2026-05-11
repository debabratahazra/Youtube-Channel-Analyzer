# ============================================
# config.py - Configuration Settings
# ============================================

import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# ============================================
# API CONFIGURATION
# ============================================
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# ============================================
# SEARCH SETTINGS
# ============================================
MAX_RESULTS_PER_SEARCH = 50      # Max per API call
MAX_CHANNELS_PER_NICHE = 100     # Total channels to analyze
SEARCH_PAGES = 3                  # Pages of results to scan

# ============================================
# CHANNEL FILTER CRITERIA
# ============================================
# HIGH VIEWS LOW SUBSCRIBERS CRITERIA:
MIN_VIEWS = 100_000              # Minimum total views
MAX_SUBSCRIBERS = 100_000        # Maximum subscribers
MIN_VIDEOS = 5                   # Minimum videos uploaded
MAX_VIDEOS = 500                 # Maximum videos (avoid huge channels)

# VIEW TO SUBSCRIBER RATIO THRESHOLDS:
# Higher ratio = More views per subscriber = GOLDEN OPPORTUNITY
EXCELLENT_RATIO = 50.0           # 50+ views per sub = EXCELLENT
GOOD_RATIO = 20.0                # 20-50 views per sub = GOOD
AVERAGE_RATIO = 10.0             # 10-20 views per sub = AVERAGE

# CPM ESTIMATES BY NICHE (USD)
CPM_ESTIMATES = {
    "Finance & Investing": {"min": 15, "max": 50, "avg": 32},
    "Business & Entrepreneurship": {"min": 12, "max": 40, "avg": 26},
    "Technology & Software": {"min": 10, "max": 35, "avg": 22},
    "Health & Wellness": {"min": 8, "max": 25, "avg": 16},
    "True Crime": {"min": 5, "max": 15, "avg": 10},
    "Motivational & Self Help": {"min": 5, "max": 20, "avg": 12},
    "AI & Future Technology": {"min": 10, "max": 30, "avg": 20},
    "History & Education": {"min": 5, "max": 18, "avg": 11},
}

# ============================================
# OUTPUT SETTINGS
# ============================================
OUTPUT_FOLDER = "results"
REPORTS_FOLDER = "results/reports"
LOGS_FOLDER = "results/logs"
EXCEL_FILENAME = "youtube_niche_analysis.xlsx"
CSV_FILENAME = "youtube_niche_analysis.csv"