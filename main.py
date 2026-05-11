# ============================================
# main.py - MAIN PROGRAM - RUN THIS FILE!
# ============================================
# 
# HOW TO RUN:
# 1. Add your API key to .env file
# 2. Open terminal/command prompt
# 3. Navigate to youtube_niche_finder folder
# 4. Type: python main.py
# 5. Follow the menu prompts
#
# ============================================

import os
import sys
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Create required directories
os.makedirs("results/reports", exist_ok=True)
os.makedirs("results/logs", exist_ok=True)

# Import our modules
from config import YOUTUBE_API_KEY
from niche_keywords import NICHE_KEYWORDS, get_keywords_for_niche
from youtube_analyzer import YouTubeAnalyzer
from report_generator import ReportGenerator
from display_results import DisplayManager

def main():
    """Main program entry point"""
    
    display = DisplayManager()
    display.print_banner()
    
    # Check API key
    if not YOUTUBE_API_KEY or YOUTUBE_API_KEY == "your_actual_api_key_here":
        print(f"\n{Fore.RED}❌ ERROR: YouTube API Key not found!")
        print(f"{Fore.YELLOW}Please add your API key to the .env file:")
        print(f"  YOUTUBE_API_KEY=your_key_here{Style.RESET_ALL}")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    print(f"\n{Fore.GREEN}✅ API Key Found! Connecting to YouTube...{Style.RESET_ALL}")

    # Initialize components
    try:
        analyzer = YouTubeAnalyzer()
        report_gen = ReportGenerator()
    except Exception as e:
        print(f"{Fore.RED}❌ Initialization failed: {e}{Style.RESET_ALL}")
        sys.exit(1)

    # ==========================================
    # MAIN MENU
    # ==========================================
    while True:
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.YELLOW}  MAIN MENU - Choose Analysis Type")
        print(f"{Fore.CYAN}{'='*50}")
        print(f"{Fore.WHITE}")
        print("  1. 🔍 Analyze ALL 8 Niches (Complete Analysis)")
        print("  2. 💰 Analyze Specific Niche")
        print("  3. 🏆 Quick Top Opportunity Scan")
        print("  4. 📊 View Previous Results")
        print("  5. ❌ Exit")
        print(f"{Style.RESET_ALL}")
        
        choice = input(f"{Fore.YELLOW}  Enter choice (1-5): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            run_complete_analysis(analyzer, report_gen, display)
        elif choice == "2":
            run_specific_niche(analyzer, report_gen, display)
        elif choice == "3":
            run_quick_scan(analyzer, report_gen, display)
        elif choice == "4":
            view_previous_results()
        elif choice == "5":
            print(f"\n{Fore.GREEN}👋 Thanks for using YouTube Niche Analyzer!")
            print(f"🚀 Good luck with your channel!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1-5.{Style.RESET_ALL}")

# ============================================
# OPTION 1: COMPLETE ANALYSIS (ALL NICHES)
# ============================================
def run_complete_analysis(analyzer, report_gen, display):
    """Analyze all 8 niches completely"""
    
    niches = list(NICHE_KEYWORDS.keys())
    
    print(f"\n{Fore.YELLOW}🚀 Starting COMPLETE analysis of {len(niches)} niches...")
    print(f"{Fore.WHITE}⏱️  Estimated time: 15-25 minutes")
    print(f"📊 Results will be saved to Excel automatically")
    print(f"\n{Fore.CYAN}Press Enter to start or Ctrl+C to cancel...{Style.RESET_ALL}")
    input()
    
    all_results = {}
    start_time = time.time()
    
    for niche_idx, niche_name in enumerate(niches, 1):
        print(f"\n{Fore.CYAN}[{niche_idx}/{len(niches)}] Processing: {niche_name}{Style.RESET_ALL}")
        
        niche_data = NICHE_KEYWORDS[niche_name]
        keywords = niche_data["keywords"]
        
        display.print_niche_header(
            niche_name, 
            len(keywords),
            niche_data["cpm_min"],
            niche_data["cpm_max"]
        )
        
        # Collect unique channel IDs for this niche
        unique_channels = {}
        
        for kw_idx, keyword in enumerate(keywords, 1):
            print(f"  [{kw_idx}/{len(keywords)}] Keyword: '{keyword}'")
            
            # Search for videos
            videos = analyzer.search_videos(keyword, max_results=25)
            
            # Collect unique channel IDs
            for video in videos:
                channel_id = video["channel_id"]
                if channel_id not in unique_channels:
                    unique_channels[channel_id] = video
            
            # Rate limiting
            time.sleep(1)
        
        print(f"\n  📊 Found {len(unique_channels)} unique channels")
        print(f"  🔍 Getting detailed statistics...")
        
        # Get detailed stats for all channels
        channel_ids = list(unique_channels.keys())
        channels_stats = analyzer.get_channel_stats(channel_ids)
        
        # Filter channels meeting criteria
        filtered = analyzer.filter_channels(channels_stats)
        print(f"  ✅ {len(filtered)} channels meet our criteria")
        
        # Score each channel
        scored_channels = []
        for channel in filtered:
            scored = analyzer.calculate_opportunity_score(channel)
            
            # Add revenue estimates
            revenue = analyzer.estimate_revenue(
                scored.get("total_views", 0),
                niche_data["cpm_min"],
                niche_data["cpm_max"],
                niche_data["cpm_avg"],
            )
            scored["revenue_estimate"] = revenue
            scored["niche"] = niche_name
            
            scored_channels.append(scored)
        
        # Sort by opportunity score
        scored_channels.sort(
            key=lambda x: x.get("opportunity_score", 0),
            reverse=True
        )
        
        # Display top results
        print(f"\n  🏆 TOP CHANNELS FOR {niche_name}:")
        for rank, channel in enumerate(scored_channels[:5], 1):
            display.print_channel_found(channel, rank)
        
        # Niche summary
        display.print_niche_summary(
            niche_name,
            scored_channels,
            {"min": niche_data["cpm_min"], "max": niche_data["cpm_max"]}
        )
        
        all_results[niche_name] = scored_channels
        
        # Pause between niches to avoid rate limiting
        if niche_idx < len(niches):
            print(f"\n  ⏳ Pausing 5 seconds before next niche...")
            time.sleep(5)
    
    # Final summary
    elapsed = (time.time() - start_time) / 60
    print(f"\n{Fore.GREEN}⏱️  Analysis completed in {elapsed:.1f} minutes{Style.RESET_ALL}")
    
    display.print_final_summary(all_results)
    
    # Generate reports
    print(f"\n{Fore.CYAN}📊 Generating Reports...{Style.RESET_ALL}")
    excel_file = report_gen.generate_excel_report(all_results)
    csv_file = report_gen.generate_csv_report(all_results)
    
    print(f"\n{Fore.GREEN}✅ ANALYSIS COMPLETE!")
    print(f"📁 Excel Report: {excel_file}")
    print(f"📁 CSV Report: {csv_file}{Style.RESET_ALL}")
    
    input(f"\n{Fore.YELLOW}Press Enter to return to main menu...{Style.RESET_ALL}")

# ============================================
# OPTION 2: SPECIFIC NICHE ANALYSIS
# ============================================
def run_specific_niche(analyzer, report_gen, display):
    """Analyze one specific niche"""
    
    niches = list(NICHE_KEYWORDS.keys())
    
    print(f"\n{Fore.CYAN}SELECT NICHE TO ANALYZE:{Style.RESET_ALL}\n")
    
    for i, niche in enumerate(niches, 1):
        niche_data = NICHE_KEYWORDS[niche]
        cpm_min = niche_data["cpm_min"]
        cpm_max = niche_data["cpm_max"]
        print(f"  {i}. {niche} (CPM: ${cpm_min}-${cpm_max})")
    
    print(f"\n  0. Back to Main Menu")
    
    try:
        choice = int(input(f"\n{Fore.YELLOW}  Enter number: {Style.RESET_ALL}"))
        
        if choice == 0:
            return
        
        if 1 <= choice <= len(niches):
            niche_name = niches[choice - 1]
            niche_data = NICHE_KEYWORDS[niche_name]
            keywords = niche_data["keywords"]
            
            display.print_niche_header(
                niche_name,
                len(keywords),
                niche_data["cpm_min"],
                niche_data["cpm_max"]
            )
            
            unique_channels = {}
            
            for kw_idx, keyword in enumerate(keywords, 1):
                print(f"  [{kw_idx}/{len(keywords)}] Searching: '{keyword}'")
                videos = analyzer.search_videos(keyword, max_results=30)
                
                for video in videos:
                    channel_id = video["channel_id"]
                    if channel_id not in unique_channels:
                        unique_channels[channel_id] = video
                
                time.sleep(1)
            
            print(f"\n  📊 Getting stats for {len(unique_channels)} channels...")
            
            channel_ids = list(unique_channels.keys())
            channels_stats = analyzer.get_channel_stats(channel_ids)
            filtered = analyzer.filter_channels(channels_stats)
            
            scored_channels = []
            for channel in filtered:
                scored = analyzer.calculate_opportunity_score(channel)
                revenue = analyzer.estimate_revenue(
                    scored.get("total_views", 0),
                    niche_data["cpm_min"],
                    niche_data["cpm_max"],
                    niche_data["cpm_avg"],
                )
                scored["revenue_estimate"] = revenue
                scored["niche"] = niche_name
                scored_channels.append(scored)
            
            scored_channels.sort(
                key=lambda x: x.get("opportunity_score", 0),
                reverse=True
            )
            
            # Display ALL results
            print(f"\n{Fore.YELLOW}🏆 ALL QUALIFYING CHANNELS FOR {niche_name}:{Style.RESET_ALL}")
            
            for rank, channel in enumerate(scored_channels, 1):
                display.print_channel_found(channel, rank)
            
            display.print_niche_summary(
                niche_name,
                scored_channels,
                {"min": niche_data["cpm_min"], "max": niche_data["cpm_max"]}
            )
            
            # Save results
            all_results = {niche_name: scored_channels}
            excel_file = report_gen.generate_excel_report(all_results)
            csv_file = report_gen.generate_csv_report(all_results)
            
            print(f"\n{Fore.GREEN}✅ Reports saved:")
            print(f"   Excel: {excel_file}")
            print(f"   CSV: {csv_file}{Style.RESET_ALL}")
            
        else:
            print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")
            
    except ValueError:
        print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")
    
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

# ============================================
# OPTION 3: QUICK SCAN (Top Opportunities)
# ============================================
def run_quick_scan(analyzer, report_gen, display):
    """Quick scan using top 3 keywords per niche"""
    
    print(f"\n{Fore.YELLOW}⚡ QUICK SCAN MODE")
    print(f"{Fore.WHITE}Uses top 3 keywords per niche for faster results")
    print(f"Estimated time: 5-8 minutes{Style.RESET_ALL}")
    
    input(f"\n{Fore.CYAN}Press Enter to start...{Style.RESET_ALL}")
    
    all_results = {}
    
    for niche_name, niche_data in NICHE_KEYWORDS.items():
        print(f"\n{Fore.CYAN}Scanning: {niche_name}...{Style.RESET_ALL}")
        
        # Use only top 3 keywords for speed
        keywords = niche_data["keywords"][:3]
        unique_channels = {}
        
        for keyword in keywords:
            videos = analyzer.search_videos(keyword, max_results=20)
            for video in videos:
                channel_id = video["channel_id"]
                if channel_id not in unique_channels:
                    unique_channels[channel_id] = video
            time.sleep(1)
        
        channel_ids = list(unique_channels.keys())
        channels_stats = analyzer.get_channel_stats(channel_ids)
        filtered = analyzer.filter_channels(channels_stats)
        
        scored_channels = []
        for channel in filtered:
            scored = analyzer.calculate_opportunity_score(channel)
            scored["niche"] = niche_name
            scored_channels.append(scored)
        
        scored_channels.sort(
            key=lambda x: x.get("opportunity_score", 0),
            reverse=True
        )
        
        all_results[niche_name] = scored_channels
        
        # Show quick summary
        if scored_channels:
            best = scored_channels[0]
            print(f"  Best: {best.get('channel_name', 'N/A')} | Score: {best.get('opportunity_score', 0)}/100")
            print(f"  Channels found: {len(scored_channels)}")
        
        time.sleep(2)
    
    display.print_final_summary(all_results)
    
    excel_file = report_gen.generate_excel_report(all_results)
    print(f"\n{Fore.GREEN}✅ Quick Scan Report: {excel_file}{Style.RESET_ALL}")
    
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

# ============================================
# OPTION 4: VIEW PREVIOUS RESULTS
# ============================================
def view_previous_results():
    """Show list of previously generated reports"""
    
    reports_dir = "results/reports"
    
    if not os.path.exists(reports_dir):
        print(f"\n{Fore.RED}No reports found yet. Run an analysis first!{Style.RESET_ALL}")
        input("Press Enter to continue...")
        return
    
    files = os.listdir(reports_dir)
    
    if not files:
        print(f"\n{Fore.YELLOW}No reports generated yet.{Style.RESET_ALL}")
        input("Press Enter to continue...")
        return
    
    print(f"\n{Fore.CYAN}PREVIOUS REPORTS:{Style.RESET_ALL}\n")
    
    for i, filename in enumerate(sorted(files, reverse=True), 1):
        filepath = os.path.join(reports_dir, filename)
        size = os.path.getsize(filepath) / 1024  # KB
        print(f"  {i}. {filename} ({size:.1f} KB)")
    
    print(f"\n  Reports are saved in: {os.path.abspath(reports_dir)}")
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

# ============================================
# RUN THE PROGRAM
# ============================================
if __name__ == "__main__":
    main()