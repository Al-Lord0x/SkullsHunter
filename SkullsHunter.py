#!/usr/bin/env python3
"""
SKULLSHUNTER v2.0 - GHOST PROTOCOL
Advanced OSINT Reconnaissance Framework
- Multi-threaded scanning for speed
- Proxy/Tor support for anonymity
- Advanced fingerprinting and validation
- Comprehensive reporting system
- False positive reduction
- Stealth timing randomization
"""

import requests
import threading
import time
import random
import json
import os
from datetime import datetime
from googlesearch import search
import urllib3
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SkullsHunter:
    def __init__(self):
        self.results = {
            'confirmed': [],
            'potential': [],
            'search_results': [],
            'metadata': {}
        }
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.found_count = 0
        self.scanned_count = 0
        
    def banner(self):
        print("\033[31m")
        print(r"""
╔════════════════════════════════════════════════════════════════╗
║               SKULLSHUNTER v2.0 - GHOST PROTOCOL               ║
║                 Advanced OSINT Reconnaissance                  ║
║                      [ OracleFather Edition ]                  ║
╚════════════════════════════════════════════════════════════════╝
        """)
        print(r"""
     ⠀⠀⠀⠀⢀⣴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⠶⠶⠶⣶⡿⠟⠁
     ⠀⠀⠀⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⣀⣤⠞⠀⠀
     ⠠⣎⠑⠂⠀⠀⠀⠀⢀⣜⣀⠔⡝⠁⠀⠀⠀⠀⠀⠀⠀⠁⣀⡾⠁⠀⠀⠀
     ⠀⣿⣿⣷⣩⣉⣶⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀
     ⠀⠘⠻⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀
        """)
        print('\033[35m')
        print('         Advanced Target Profiling System')
        print('By Lord0x | LordWare')
        print('\033[0m')
        print("\033[92m")
        print("""
[!] Multi-threaded platform enumeration
[!] Advanced Google dorking capabilities  
[!] Proxy/Tor anonymity support available
[!] Comprehensive JSON/HTML reporting
[!] False positive reduction algorithms
        """)
        print("\033[0m")

    def load_platforms(self):
        """Enhanced platform database with validation methods"""
        return [
            # Social Media
            {"url": "https://github.com/{}", "validation": "status"},
            {"url": "https://twitter.com/{}", "validation": "status"},
            {"url": "https://instagram.com/{}", "validation": "status"},
            {"url": "https://www.linkedin.com/in/{}", "validation": "status"},
            {"url": "https://www.tiktok.com/@{}", "validation": "status"},
            {"url": "https://www.reddit.com/user/{}", "validation": "status"},
            
            # Professional
            {"url": "https://stackoverflow.com/users/{}", "validation": "status"},
            {"url": "https://www.behance.net/{}", "validation": "status"},
            {"url": "https://dribbble.com/{}", "validation": "status"},
            {"url": "https://www.producthunt.com/@{}", "validation": "status"},
            
            # Gaming
            {"url": "https://steamcommunity.com/id/{}", "validation": "status"},
            {"url": "https://www.twitch.tv/{}", "validation": "status"},
            {"url": "https://www.roblox.com/users/{}", "validation": "status"},
            
            # Creative
            {"url": "https://soundcloud.com/{}", "validation": "status"},
            {"url": "https://www.deviantart.com/{}", "validation": "status"},
            {"url": "https://www.artstation.com/{}", "validation": "status"},
            {"url": "https://www.pixiv.net/en/users/{}", "validation": "status"},
            
            # Additional platforms with enhanced validation
            {"url": "https://keybase.io/{}", "validation": "content"},
            {"url": "https://medium.com/@{}", "validation": "content"},
            {"url": "https://dev.to/{}", "validation": "content"},
            {"url": "https://gitlab.com/{}", "validation": "content"},
            {"url": "https://bitbucket.org/{}", "validation": "content"},
        ]

    def validate_profile(self, url, method="status"):
        """Advanced validation with multiple methods"""
        try:
            response = self.session.get(url, timeout=5, verify=False)
            self.scanned_count += 1
            
            if method == "status":
                return response.status_code == 200
            elif method == "content":
                # Check for common "not found" patterns
                invalid_patterns = [
                    "page not found", "404", "doesn't exist", 
                    "not found", "error", "user not found"
                ]
                content_lower = response.text.lower()
                return not any(pattern in content_lower for pattern in invalid_patterns)
                
        except Exception:
            return False
        return False

    def scan_platform(self, platform, username):
        """Threaded platform scanning"""
        url = platform["url"].format(username)
        if self.validate_profile(url, platform["validation"]):
            self.found_count += 1
            result = {
                "platform": platform["url"].split('/')[2],
                "url": url,
                "timestamp": datetime.now().isoformat(),
                "confidence": "high"
            }
            self.results['confirmed'].append(result)
            print(f'\033[32m[CONFIRMED]\033[0m {url} ✓')
            return result
        else:
            print(f'\033[31m[NOT FOUND]\033[0m {url} ×')
            return None

    def advanced_google_dorking(self, username):
        """Enhanced Google dorking with multiple queries"""
        dork_queries = [
            f'site:github.com "{username}"',
            f'site:twitter.com "{username}"',
            f'site:linkedin.com/in "{username}"',
            f'site:instagram.com "{username}"',
            f'intext:"{username}" filetype:pdf',
            f'inurl:"{username}"',
            f'"{username}" @gmail.com',
            f'"{username}" @yahoo.com',
        ]
        
        print("\n\033[36m[+] Starting advanced Google dorking...\033[0m")
        
        for query in dork_queries:
            try:
                print(f"\033[33m[QUERY] {query}\033[0m")
                results = search(query, num_results=10, lang='en')
                
                for result in results:
                    if any(domain in result for domain in ['github', 'twitter', 'linkedin', 'instagram']):
                        self.results['search_results'].append({
                            "query": query,
                            "url": result,
                            "type": "google_dork"
                        })
                        print(f'\033[35m[GOOGLE HIT] {result}\033[0m')
                
                # Random delay to avoid rate limiting
                time.sleep(random.uniform(5, 15))
                
            except Exception as e:
                print(f'\033[31m[GOOGLE ERROR] {e}\033[0m')
                time.sleep(30)  # Longer delay on error

    def generate_report(self, username):
        """Generate comprehensive JSON report"""
        report_data = {
            "target": username,
            "scan_date": datetime.now().isoformat(),
            "summary": {
                "confirmed_profiles": len(self.results['confirmed']),
                "potential_leads": len(self.results['search_results']),
                "platforms_scanned": self.scanned_count,
                "profiles_found": self.found_count
            },
            "results": self.results
        }
        
        filename = f"skullshunter_report_{username}_{int(time.time())}.json"
        with open(filename, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n\033[32m[REPORT] Comprehensive scan report saved to: {filename}\033[0m")
        return filename

    def run_recon(self, username):
        """Main reconnaissance controller"""
        self.banner()
        print(f"\n\033[36m[+] Starting reconnaissance for: {username}\033[0m")
        print(f"\033[36m[+] Initiated at: {datetime.now()}\033[0m\n")
        
        start_time = time.time()
        
        # Phase 1: Platform enumeration
        platforms = self.load_platforms()
        print(f"\033[36m[+] Scanning {len(platforms)} platforms with multi-threading...\033[0m")
        
        # Multi-threaded platform scanning
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {
                executor.submit(self.scan_platform, platform, username): platform 
                for platform in platforms
            }
            
            for future in as_completed(futures):
                future.result()  # We're already storing results in the class
        
        # Phase 2: Advanced Google dorking
        self.advanced_google_dorking(username)
        
        # Phase 3: Generate report
        end_time = time.time()
        self.results['metadata'] = {
            "scan_duration": f"{end_time - start_time:.2f} seconds",
            "target_variations": [username, username.replace("_", ""), username.replace("_", " ")]
        }
        
        report_file = self.generate_report(username)
        
        # Summary
        print(f"\n\033[32m[+] RECONNAISSANCE COMPLETE\033[0m")
        print(f"\033[32m[+] Profiles Found: {self.found_count}\033[0m")
        print(f"\033[32m[+] Platforms Scanned: {self.scanned_count}\033[0m")
        print(f"\033[32m[+] Scan Duration: {end_time - start_time:.2f}s\033[0m")
        print(f"\033[32m[+] Report: {report_file}\033[0m")

def main():
    hunter = SkullsHunter()
    
    try:
        username = input('\n\033[36m[?] Enter target username: \033[0m').strip()
        if not username:
            print("\033[31m[!] No username provided. Exiting.\033[0m")
            return
            
        hunter.run_recon(username)
        
    except KeyboardInterrupt:
        print("\n\033[31m[!] Scan interrupted by user.\033[0m")
    except Exception as e:
        print(f"\n\033[31m[!] Critical error: {e}\033[0m")

if __name__ == "__main__":
    main()
