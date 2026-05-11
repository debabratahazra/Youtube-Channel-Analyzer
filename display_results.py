# ============================================
# display_results.py - Console Display
# ============================================

from colorama import init, Fore, Back, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

class DisplayManager:
    """Handles all console output with colors and formatting"""

    def print_banner(self):
        """Print the program startup banner"""
        banner = f"""
{Fore.YELLOW}{'='*65}
{Fore.CYAN}  🎯 YOUTUBE NICHE CHANNEL ANALYZER v2.0
{Fore.WHITE}  Find HIGH VIEW / LOW SUBSCRIBER Channels
{Fore.WHITE}  Identify Your Best Niche Opportunities
{Fore.YELLOW}{'='*65}
{Fore.GREEN}  ✅ Analyzes 8 Profitable Niches
  ✅ Scores Channels 0-100 (Opportunity Rating)
  ✅ Exports Excel + CSV Reports
  ✅ Estimates Revenue Potential
  ✅ Finds Your Competition Gaps
{Fore.YELLOW}{'='*65}{Style.RESET_ALL}
        """
        print(banner)

    def print_niche_header(self, niche_name, keyword_count, cpm_min, cpm_max):
        """Print header when starting a new niche analysis"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.YELLOW}💰 ANALYZING: {niche_name}")
        print(f"{Fore.WHITE}   Keywords: {keyword_count} | CPM: ${cpm_min}-${cpm_max}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")

    def print_channel_found(self, channel, rank):
        """Print details of a found channel opportunity"""
        score = channel.get("opportunity_score", 0)
        grade_emoji = channel.get("grade_emoji", "⭐")
        
        # Color based on score
        if score >= 80:
            color = Fore.YELLOW
            border = "🏆"
        elif score >= 65:
            color = Fore.GREEN
            border = "✅"
        elif score >= 50:
            color = Fore.CYAN
            border = "📊"
        else:
            color = Fore.WHITE
            border = "📌"

        print(f"\n  {border} {color}Rank #{rank}: {channel.get('channel_name', 'Unknown')}{Style.RESET_ALL}")
        print(f"     Score: {color}{score}/100 - {channel.get('grade', '')}{Style.RESET_ALL}")
        print(f"     📊 Subscribers: {self._format_number(channel.get('subscribers', 0))}")
        print(f"     👁️  Total Views: {self._format_number(channel.get('total_views', 0))}")
        print(f"     🎬 Videos: {channel.get('video_count', 0)}")
        print(f"     📈 View/Sub Ratio: {channel.get('view_sub_ratio', 0):.1f}x")
        print(f"     🎯 Views/Video: {self._format_number(channel.get('views_per_video', 0))}")
        print(f"     🔗 {channel.get('channel_url', '')}")

    def print_niche_summary(self, niche_name, channels, cpm_data):
        """Print summary after analyzing each niche"""
        if not channels:
            print(f"\n  {Fore.RED}❌ No qualifying channels found{Style.RESET_ALL}")
            return
        
        golden = [c for c in channels if c.get("opportunity_score", 0) >= 65]
        best = max(channels, key=lambda x: x.get("opportunity_score", 0))
        avg_ratio = sum(c.get("view_sub_ratio", 0) for c in channels) / len(channels)
        
        print(f"\n{Fore.GREEN}📊 NICHE SUMMARY: {niche_name}")
        print(f"  ├── Total Channels Found: {len(channels)}")
        print(f"  ├── Golden Opportunities: {len(golden)} 🏆")
        print(f"  ├── Best Channel Score: {best.get('opportunity_score', 0)}/100")
        print(f"  ├── Average View/Sub Ratio: {avg_ratio:.1f}x")
        print(f"  ├── CPM Range: ${cpm_data['min']}-${cpm_data['max']}")
        
        # Verdict
        if len(golden) >= 5:
            print(f"  └── Verdict: {Fore.YELLOW}🔥 HIGHLY RECOMMENDED - ENTER THIS NICHE!{Style.RESET_ALL}")
        elif len(golden) >= 2:
            print(f"  └── Verdict: {Fore.GREEN}✅ GOOD OPPORTUNITY{Style.RESET_ALL}")
        elif len(channels) >= 3:
            print(f"  └── Verdict: {Fore.CYAN}⚠️  POSSIBLE BUT COMPETITIVE{Style.RESET_ALL}")
        else:
            print(f"  └── Verdict: {Fore.RED}❌ LIMITED OPPORTUNITY{Style.RESET_ALL}")

    def print_final_summary(self, all_results):
        """Print complete summary of all niches analyzed"""
        print(f"\n{Fore.YELLOW}{'='*65}")
        print(f"{Fore.CYAN}  🏆 FINAL ANALYSIS COMPLETE - TOP RECOMMENDATIONS")
        print(f"{Fore.YELLOW}{'='*65}{Style.RESET_ALL}")
        
        # Rank niches by opportunity
        ranked_niches = []
        for niche, channels in all_results.items():
            if channels:
                golden = len([c for c in channels if c.get("opportunity_score", 0) >= 65])
                best_score = max((c.get("opportunity_score", 0) for c in channels), default=0)
                ranked_niches.append((niche, len(channels), golden, best_score))
        
        ranked_niches.sort(key=lambda x: (x[2], x[3]), reverse=True)
        
        print(f"\n{Fore.WHITE}  TOP NICHES RANKED BY OPPORTUNITY:\n")
        
        medals = ["🥇", "🥈", "🥉", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ "]
        
        for i, (niche, total, golden, best) in enumerate(ranked_niches):
            medal = medals[i] if i < len(medals) else f"{i+1}."
            color = Fore.YELLOW if i == 0 else (Fore.GREEN if i <= 2 else Fore.WHITE)
            print(f"  {medal} {color}{niche}")
            print(f"      Channels: {total} | Golden: {golden} | Best Score: {best}/100{Style.RESET_ALL}")

    def print_progress(self, current, total, message):
        """Print progress indicator"""
        percent = (current / total) * 100 if total > 0 else 0
        bar_filled = int(percent / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        print(f"\r  [{bar}] {percent:.0f}% - {message}", end="", flush=True)

    def _format_number(self, number):
        """Format large numbers for display"""
        if number >= 1_000_000:
            return f"{number/1_000_000:.1f}M"
        elif number >= 1_000:
            return f"{number/1_000:.1f}K"
        return str(number)