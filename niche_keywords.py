# ============================================
# niche_keywords.py - Search Keywords
# ============================================

NICHE_KEYWORDS = {
    
    # ==========================================
    # 💰 NICHE 1: FINANCE & INVESTING
    # CPM: $15-50
    # ==========================================
    "Finance & Investing": {
        "keywords": [
            "personal finance tips",
            "investing for beginners",
            "stock market basics",
            "how to invest money",
            "passive income investing",
            "dividend investing",
            "index funds explained",
            "financial freedom",
            "retire early investing",
            "compound interest explained",
            "how to build wealth",
            "money management tips",
            "stock market explained",
            "ETF investing beginner",
            "real estate investing basics",
        ],
        "cpm_min": 15,
        "cpm_max": 50,
        "cpm_avg": 32,
        "difficulty": "Medium",
        "monetization_speed": "Fast",
    },

    # ==========================================
    # 💰 NICHE 2: BUSINESS & ENTREPRENEURSHIP  
    # CPM: $12-40
    # ==========================================
    "Business & Entrepreneurship": {
        "keywords": [
            "how to start a business",
            "entrepreneurship tips",
            "small business ideas",
            "online business from home",
            "dropshipping for beginners",
            "ecommerce business tips",
            "side hustle ideas",
            "make money online business",
            "business ideas 2026",
            "startup tips for beginners",
            "freelancing business",
            "digital marketing basics",
            "how to grow business online",
            "business strategy tips",
            "work from home business",
        ],
        "cpm_min": 12,
        "cpm_max": 40,
        "cpm_avg": 26,
        "difficulty": "Medium",
        "monetization_speed": "Fast",
    },

    # ==========================================
    # 💰 NICHE 3: TECHNOLOGY & SOFTWARE
    # CPM: $10-35
    # ==========================================
    "Technology & Software": {
        "keywords": [
            "best software tools",
            "tech tips for beginners",
            "software tutorial beginners",
            "best apps productivity",
            "technology explained simply",
            "computer tips and tricks",
            "best tech tools 2026",
            "software review",
            "coding for beginners",
            "tech gadgets review",
            "best free software",
            "cybersecurity basics",
            "cloud computing explained",
            "automation tools",
            "no code tools beginners",
        ],
        "cpm_min": 10,
        "cpm_max": 35,
        "cpm_avg": 22,
        "difficulty": "Low-Medium",
        "monetization_speed": "Medium",
    },

    # ==========================================
    # 💰 NICHE 4: HEALTH & WELLNESS
    # CPM: $8-25
    # ==========================================
    "Health & Wellness": {
        "keywords": [
            "weight loss tips",
            "healthy habits daily",
            "mental health tips",
            "how to lose belly fat",
            "healthy meal prep",
            "intermittent fasting guide",
            "workout for beginners",
            "anxiety relief tips",
            "sleep improvement tips",
            "nutrition basics",
            "keto diet beginners",
            "stress management tips",
            "morning health routine",
            "gut health improvement",
            "natural remedies health",
        ],
        "cpm_min": 8,
        "cpm_max": 25,
        "cpm_avg": 16,
        "difficulty": "Medium",
        "monetization_speed": "Medium",
    },

    # ==========================================
    # 💰 NICHE 5: TRUE CRIME
    # CPM: $5-15
    # ==========================================
    "True Crime": {
        "keywords": [
            "true crime documentary",
            "unsolved mysteries",
            "serial killer cases",
            "cold case investigations",
            "missing persons cases",
            "criminal psychology",
            "true crime stories",
            "mysterious disappearances",
            "crime investigation",
            "forensic science explained",
            "famous criminal cases",
            "detective stories",
            "crime documentary",
            "unexplained cases",
            "real crime stories",
        ],
        "cpm_min": 5,
        "cpm_max": 15,
        "cpm_avg": 10,
        "difficulty": "Low",
        "monetization_speed": "Medium",
    },

    # ==========================================
    # 💰 NICHE 6: MOTIVATIONAL & SELF HELP
    # CPM: $5-20
    # ==========================================
    "Motivational & Self Help": {
        "keywords": [
            "self improvement tips",
            "motivation for success",
            "morning routine success",
            "habits of successful people",
            "mindset for success",
            "discipline and focus tips",
            "personal development",
            "how to be more productive",
            "success mindset",
            "overcome failure motivation",
            "self confidence building",
            "goal setting tips",
            "positive mindset habits",
            "millionaire mindset",
            "atomic habits explained",
        ],
        "cpm_min": 5,
        "cpm_max": 20,
        "cpm_avg": 12,
        "difficulty": "Low",
        "monetization_speed": "Medium",
    },

    # ==========================================
    # 💰 NICHE 7: AI & FUTURE TECHNOLOGY
    # CPM: $10-30
    # ==========================================
    "AI & Future Technology": {
        "keywords": [
            "AI tools for beginners",
            "ChatGPT tutorial",
            "artificial intelligence explained",
            "how to use AI tools",
            "AI side hustle ideas",
            "make money with AI",
            "best AI tools 2026",
            "AI future jobs",
            "machine learning basics",
            "AI automation tools",
            "ChatGPT money making",
            "AI productivity hacks",
            "midjourney tutorial",
            "AI business ideas",
            "future technology trends",
        ],
        "cpm_min": 10,
        "cpm_max": 30,
        "cpm_avg": 20,
        "difficulty": "Low-Medium",
        "monetization_speed": "Fast",
    },

    # ==========================================
    # 💰 NICHE 8: HISTORY & EDUCATION
    # CPM: $5-18
    # ==========================================
    "History & Education": {
        "keywords": [
            "history documentary",
            "ancient civilization facts",
            "world history explained",
            "historical mysteries",
            "history facts interesting",
            "educational documentary",
            "ancient history secrets",
            "historical events explained",
            "world war history",
            "biography famous people",
            "ancient egypt facts",
            "interesting history facts",
            "medieval history",
            "science history facts",
            "geography educational",
        ],
        "cpm_min": 5,
        "cpm_max": 18,
        "cpm_avg": 11,
        "difficulty": "Low",
        "monetization_speed": "Slow-Medium",
    },
}

# ============================================
# QUICK LOOKUP FUNCTIONS
# ============================================

def get_all_niches():
    """Return list of all niche names"""
    return list(NICHE_KEYWORDS.keys())

def get_keywords_for_niche(niche_name):
    """Return keywords for specific niche"""
    return NICHE_KEYWORDS.get(niche_name, {}).get("keywords", [])

def get_cpm_for_niche(niche_name):
    """Return CPM data for specific niche"""
    niche = NICHE_KEYWORDS.get(niche_name, {})
    return {
        "min": niche.get("cpm_min", 0),
        "max": niche.get("cpm_max", 0),
        "avg": niche.get("cpm_avg", 0),
    }