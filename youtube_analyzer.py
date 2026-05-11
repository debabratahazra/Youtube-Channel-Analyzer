# ============================================
# youtube_analyzer.py - Core Analysis Engine
# ============================================

import time
import logging
from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import (
    YOUTUBE_API_KEY,
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    MAX_RESULTS_PER_SEARCH,
    MIN_VIEWS,
    MAX_SUBSCRIBERS,
    MIN_VIDEOS,
    MAX_VIDEOS,
    EXCELLENT_RATIO,
    GOOD_RATIO,
    AVERAGE_RATIO,
)

# Setup logging
logging.basicConfig(
    filename='results/logs/analyzer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class YouTubeAnalyzer:
    """
    Main YouTube Channel Analyzer
    Finds channels with HIGH VIEWS but LOW SUBSCRIBERS
    These represent golden niche opportunities!
    """

    def __init__(self):
        """Initialize the YouTube API client"""
        try:
            self.youtube = build(
                YOUTUBE_API_SERVICE_NAME,
                YOUTUBE_API_VERSION,
                developerKey=YOUTUBE_API_KEY
            )
            print("✅ YouTube API Connected Successfully!")
            logging.info("YouTube API initialized successfully")
        except Exception as e:
            print(f"❌ API Connection Failed: {e}")
            logging.error(f"API initialization failed: {e}")
            raise

    # ==========================================
    # SEARCH FOR VIDEOS BY KEYWORD
    # ==========================================
    def search_videos(self, keyword, max_results=50):
        """
        Search YouTube for videos matching keyword
        Returns list of video IDs and channel IDs
        """
        try:
            print(f"  🔍 Searching: '{keyword}'...")
            
            request = self.youtube.search().list(
                part="snippet",
                q=keyword,
                type="video",
                maxResults=max_results,
                order="viewCount",        # Most viewed first
                videoDuration="medium",   # 4-20 minute videos
                relevanceLanguage="en",   # English content
                safeSearch="moderate",
            )
            
            response = request.execute()
            
            results = []
            for item in response.get("items", []):
                results.append({
                    "video_id": item["id"]["videoId"],
                    "channel_id": item["snippet"]["channelId"],
                    "channel_title": item["snippet"]["channelTitle"],
                    "video_title": item["snippet"]["title"],
                    "published_at": item["snippet"]["publishedAt"],
                })
            
            # Respect API rate limits
            time.sleep(0.5)
            
            logging.info(f"Found {len(results)} videos for '{keyword}'")
            return results

        except HttpError as e:
            if e.resp.status == 403:
                print("  ⚠️  API quota exceeded! Try again tomorrow.")
                logging.error("API quota exceeded")
            else:
                print(f"  ❌ Search error: {e}")
                logging.error(f"Search error for '{keyword}': {e}")
            return []

    # ==========================================
    # GET DETAILED CHANNEL STATISTICS
    # ==========================================
    def get_channel_stats(self, channel_ids):
        """
        Get detailed statistics for multiple channels
        Returns subscriber count, views, video count, etc.
        Can process up to 50 channels per API call!
        """
        if not channel_ids:
            return {}

        try:
            # Process in batches of 50 (API limit)
            all_channel_data = {}
            
            for i in range(0, len(channel_ids), 50):
                batch = channel_ids[i:i+50]
                
                request = self.youtube.channels().list(
                    part="snippet,statistics,brandingSettings,contentDetails",
                    id=",".join(batch)
                )
                
                response = request.execute()
                
                for item in response.get("items", []):
                    channel_id = item["id"]
                    stats = item.get("statistics", {})
                    snippet = item.get("snippet", {})
                    branding = item.get("brandingSettings", {})
                    
                    # Extract all available data
                    all_channel_data[channel_id] = {
                        # Identity
                        "channel_id": channel_id,
                        "channel_name": snippet.get("title", "Unknown"),
                        "channel_url": f"https://youtube.com/channel/{channel_id}",
                        "custom_url": snippet.get("customUrl", ""),
                        "description": snippet.get("description", "")[:200],
                        "country": snippet.get("country", "Unknown"),
                        
                        # Statistics
                        "subscribers": int(stats.get("subscriberCount", 0)),
                        "total_views": int(stats.get("viewCount", 0)),
                        "video_count": int(stats.get("videoCount", 0)),
                        "hidden_subscribers": stats.get("hiddenSubscriberCount", False),
                        
                        # Dates
                        "created_date": snippet.get("publishedAt", "")[:10],
                        "channel_age_days": self._calculate_age(
                            snippet.get("publishedAt", "")
                        ),
                    }
                
                # Rate limiting
                time.sleep(0.3)
            
            return all_channel_data

        except HttpError as e:
            print(f"  ❌ Error getting channel stats: {e}")
            logging.error(f"Channel stats error: {e}")
            return {}

    # ==========================================
    # CALCULATE OPPORTUNITY SCORE
    # ==========================================
    def calculate_opportunity_score(self, channel_data):
        """
        Calculate a score from 0-100 showing
        how good this channel is as a niche opportunity.
        
        Higher score = Better opportunity for new creators!
        """
        score = 0
        score_breakdown = {}
        
        subscribers = channel_data.get("subscribers", 0)
        total_views = channel_data.get("total_views", 0)
        video_count = channel_data.get("video_count", 0)
        channel_age_days = channel_data.get("channel_age_days", 1)
        
        # Avoid division by zero
        if subscribers == 0:
            subscribers = 1
        if video_count == 0:
            video_count = 1
        if channel_age_days == 0:
            channel_age_days = 1

        # ----------------------------------------
        # METRIC 1: Views to Subscriber Ratio (40 points)
        # The MOST important metric!
        # ----------------------------------------
        view_sub_ratio = total_views / subscribers
        
        if view_sub_ratio >= EXCELLENT_RATIO:
            ratio_score = 40
            ratio_label = "🏆 EXCELLENT"
        elif view_sub_ratio >= GOOD_RATIO:
            ratio_score = 30
            ratio_label = "✅ GOOD"
        elif view_sub_ratio >= AVERAGE_RATIO:
            ratio_score = 20
            ratio_label = "⚠️  AVERAGE"
        else:
            ratio_score = 10
            ratio_label = "❌ LOW"
        
        score += ratio_score
        score_breakdown["view_sub_ratio"] = {
            "value": round(view_sub_ratio, 1),
            "score": ratio_score,
            "label": ratio_label
        }

        # ----------------------------------------
        # METRIC 2: Views Per Video (25 points)
        # High views per video = popular content format
        # ----------------------------------------
        views_per_video = total_views / video_count
        
        if views_per_video >= 500_000:
            vpv_score = 25
            vpv_label = "🔥 VIRAL"
        elif views_per_video >= 100_000:
            vpv_score = 20
            vpv_label = "⚡ HIGH"
        elif views_per_video >= 50_000:
            vpv_score = 15
            vpv_label = "📈 DECENT"
        elif views_per_video >= 10_000:
            vpv_score = 10
            vpv_label = "📊 MODERATE"
        else:
            vpv_score = 5
            vpv_label = "📉 LOW"
        
        score += vpv_score
        score_breakdown["views_per_video"] = {
            "value": int(views_per_video),
            "score": vpv_score,
            "label": vpv_label
        }

        # ----------------------------------------
        # METRIC 3: Subscriber Count Penalty (20 points)
        # Lower subscribers = More opportunity for you!
        # ----------------------------------------
        if subscribers <= 5_000:
            sub_score = 20
            sub_label = "🎯 TINY (Easy to beat)"
        elif subscribers <= 20_000:
            sub_score = 16
            sub_label = "🎯 SMALL (Beatable)"
        elif subscribers <= 50_000:
            sub_score = 12
            sub_label = "📊 MEDIUM"
        elif subscribers <= 100_000:
            sub_score = 8
            sub_label = "⚠️  GROWING"
        else:
            sub_score = 3
            sub_label = "❌ LARGE"
        
        score += sub_score
        score_breakdown["subscriber_count"] = {
            "value": subscribers,
            "score": sub_score,
            "label": sub_label
        }

        # ----------------------------------------
        # METRIC 4: Channel Growth Rate (15 points)
        # Views per day since creation
        # ----------------------------------------
        daily_views = total_views / channel_age_days
        
        if daily_views >= 50_000:
            growth_score = 15
            growth_label = "🚀 EXPLOSIVE"
        elif daily_views >= 10_000:
            growth_score = 12
            growth_label = "⚡ FAST"
        elif daily_views >= 1_000:
            growth_score = 8
            growth_label = "📈 STEADY"
        elif daily_views >= 100:
            growth_score = 5
            growth_label = "🐢 SLOW"
        else:
            growth_score = 2
            growth_label = "💤 VERY SLOW"
        
        score += growth_score
        score_breakdown["growth_rate"] = {
            "value": round(daily_views, 0),
            "score": growth_score,
            "label": growth_label
        }

        # Final score calculation
        channel_data["opportunity_score"] = score
        channel_data["score_breakdown"] = score_breakdown
        channel_data["view_sub_ratio"] = round(total_views / subscribers, 1)
        channel_data["views_per_video"] = int(total_views / video_count)
        channel_data["daily_views"] = round(daily_views, 0)
        
        # Assign grade
        if score >= 80:
            channel_data["grade"] = "A+ GOLDEN OPPORTUNITY"
            channel_data["grade_emoji"] = "🏆"
        elif score >= 65:
            channel_data["grade"] = "A EXCELLENT"
            channel_data["grade_emoji"] = "⭐⭐⭐⭐⭐"
        elif score >= 50:
            channel_data["grade"] = "B GOOD"
            channel_data["grade_emoji"] = "⭐⭐⭐⭐"
        elif score >= 35:
            channel_data["grade"] = "C AVERAGE"
            channel_data["grade_emoji"] = "⭐⭐⭐"
        else:
            channel_data["grade"] = "D LOW OPPORTUNITY"
            channel_data["grade_emoji"] = "⭐"

        return channel_data

    # ==========================================
    # FILTER CHANNELS BY CRITERIA
    # ==========================================
    def filter_channels(self, channels_data):
        """
        Filter channels that meet our criteria:
        - High views (potential)
        - Low subscribers (opportunity)
        - Active channel (not abandoned)
        """
        filtered = []
        
        for channel_id, data in channels_data.items():
            
            # Skip if subscriber count is hidden
            if data.get("hidden_subscribers"):
                continue
            
            subscribers = data.get("subscribers", 0)
            total_views = data.get("total_views", 0)
            video_count = data.get("video_count", 0)
            
            # Apply filters
            if (
                total_views >= MIN_VIEWS and
                subscribers <= MAX_SUBSCRIBERS and
                video_count >= MIN_VIDEOS and
                video_count <= MAX_VIDEOS and
                subscribers > 0
            ):
                filtered.append(data)
        
        return filtered

    # ==========================================
    # HELPER: CALCULATE CHANNEL AGE
    # ==========================================
    def _calculate_age(self, created_date_str):
        """Calculate channel age in days from creation date"""
        try:
            if not created_date_str:
                return 365  # Default to 1 year
            
            created_date = datetime.fromisoformat(
                created_date_str.replace("Z", "+00:00")
            )
            age_delta = datetime.now(created_date.tzinfo) - created_date
            return max(age_delta.days, 1)
        except:
            return 365

    # ==========================================
    # ESTIMATE REVENUE POTENTIAL
    # ==========================================
    def estimate_revenue(self, total_views, cpm_min, cpm_max, cpm_avg):
        """
        Estimate potential monthly revenue if you 
        replicated this channel's success
        """
        # Assume 10% of total views happen monthly for established channel
        monthly_views = total_views * 0.10
        
        # Calculate revenue (CPM is per 1000 views, only 60% are monetized)
        monetizable_views = monthly_views * 0.60
        views_in_thousands = monetizable_views / 1000
        
        return {
            "monthly_views_estimate": int(monthly_views),
            "revenue_min": round(views_in_thousands * cpm_min, 2),
            "revenue_max": round(views_in_thousands * cpm_max, 2),
            "revenue_avg": round(views_in_thousands * cpm_avg, 2),
        }