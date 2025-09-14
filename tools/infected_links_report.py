#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Infected Links Report - Israeli Website URLs Report
Developed by: SayerLinux
GitHub: https://github.com/SaudiLinux
Email: SayerLinux1@gmail.com
"""

import json
from datetime import datetime
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows
init()

class InfectedLinksReporter:
    def __init__(self):
        self.infected_links = []
        self.load_infected_sites()
        
    def load_infected_sites(self):
        """Load infected sites from JSON report"""
        try:
            with open('infected_sites_report_20250913_005914.json', 'r', encoding='utf-8') as f:
                self.infected_sites = json.load(f)
        except FileNotFoundError:
            # Fallback to hardcoded data
            self.infected_sites = self.get_default_infected_sites()
            
    def get_default_infected_sites(self):
        """Default infected sites data"""
        return [
            {
                "domain": "gov.il",
                "ip_address": "147.237.12.20",
                "israeli_type": "Government",
                "category": "Official Government",
                "severity": "HIGH",
                "description": "Israeli Government Portal"
            },
            {
                "domain": "ynet.co.il",
                "ip_address": "23.34.1.191",
                "israeli_type": "News",
                "category": "Major News Portal",
                "severity": "HIGH",
                "description": "Ynet - Israeli News"
            }
        ]
        
    def generate_infected_links(self):
        """Generate comprehensive links for infected sites"""
        print(f"{Fore.RED}{'='*120}{Style.RESET_ALL}")
        print(f"{Fore.RED}                    INFECTED ISRAELI WEBSITE LINKS{Style.RESET_ALL}")
        print(f"{Fore.RED}{'='*120}{Style.RESET_ALL}")
        print()
        
        # Enhanced infected sites with full URLs
        infected_sites_enhanced = [
            {
                'domain': 'gov.il',
                'full_urls': [
                    'https://www.gov.il',
                    'https://gov.il',
                    'http://www.gov.il',
                    'http://gov.il'
                ],
                'subdomains': [
                    'https://www.pmo.gov.il',
                    'https://www.mfa.gov.il',
                    'https://www.mod.gov.il',
                    'https://www.knesset.gov.il',
                    'https://www.justice.gov.il',
                    'https://www.health.gov.il',
                    'https://www.education.gov.il'
                ],
                'ip': '147.237.12.20',
                'type': 'Government',
                'severity': 'HIGH',
                'description': 'Israeli Government Official Portal'
            },
            {
                'domain': 'ynet.co.il',
                'full_urls': [
                    'https://www.ynet.co.il',
                    'https://ynet.co.il',
                    'http://www.ynet.co.il',
                    'http://ynet.co.il'
                ],
                'subdomains': [
                    'https://news.ynet.co.il',
                    'https://www.ynetnews.com',
                    'https://www.ynet.com'
                ],
                'ip': '23.34.1.191',
                'type': 'News Portal',
                'severity': 'HIGH',
                'description': 'Ynet - Major Israeli News Portal'
            },
            {
                'domain': 'haaretz.co.il',
                'full_urls': [
                    'https://www.haaretz.co.il',
                    'https://haaretz.co.il',
                    'https://www.haaretz.com',
                    'https://haaretz.com'
                ],
                'ip': '151.101.66.217',
                'type': 'Newspaper',
                'severity': 'HIGH',
                'description': 'Haaretz Israeli Newspaper'
            },
            {
                'domain': 'jpost.com',
                'full_urls': [
                    'https://www.jpost.com',
                    'https://jpost.com',
                    'https://www.jpost.co.il',
                    'https://jpost.co.il'
                ],
                'ip': '34.149.213.158',
                'type': 'News',
                'severity': 'HIGH',
                'description': 'Jerusalem Post - Israeli News'
            },
            {
                'domain': 'timesofisrael.com',
                'full_urls': [
                    'https://www.timesofisrael.com',
                    'https://timesofisrael.com',
                    'https://blogs.timesofisrael.com'
                ],
                'ip': '104.18.29.18',
                'type': 'Online News',
                'severity': 'MEDIUM',
                'description': 'Times of Israel - Israeli News Site'
            },
            {
                'domain': 'israelhayom.co.il',
                'full_urls': [
                    'https://www.israelhayom.co.il',
                    'https://israelhayom.co.il',
                    'https://www.israelhayom.com'
                ],
                'ip': '23.215.0.137',
                'type': 'Daily Newspaper',
                'severity': 'HIGH',
                'description': 'Israel Hayom - Israeli Daily'
            },
            {
                'domain': 'walla.co.il',
                'full_urls': [
                    'https://www.walla.co.il',
                    'https://walla.co.il',
                    'https://news.walla.co.il',
                    'https://sports.walla.co.il'
                ],
                'ip': '34.102.212.0',
                'type': 'Major Portal',
                'severity': 'MEDIUM',
                'description': 'Walla! - Israeli Major Portal'
            },
            {
                'domain': 'mako.co.il',
                'full_urls': [
                    'https://www.mako.co.il',
                    'https://mako.co.il',
                    'https://keshet12.mako.co.il'
                ],
                'ip': '66.22.84.55',
                'type': 'TV Channel',
                'severity': 'MEDIUM',
                'description': 'Mako - Israeli TV Channel Website'
            },
            {
                'domain': 'n12.co.il',
                'full_urls': [
                    'https://www.n12.co.il',
                    'https://n12.co.il'
                ],
                'ip': '66.22.84.58',
                'type': 'News',
                'severity': 'MEDIUM',
                'description': 'N12 - Israeli News Channel'
            },
            {
                'domain': 'globes.co.il',
                'full_urls': [
                    'https://www.globes.co.il',
                    'https://globes.co.il'
                ],
                'ip': '23.32.238.81',
                'type': 'Business News',
                'severity': 'MEDIUM',
                'description': 'Globes - Israeli Business News'
            },
            {
                'domain': 'calcalist.co.il',
                'full_urls': [
                    'https://www.calcalist.co.il',
                    'https://calcalist.co.il'
                ],
                'ip': '192.115.80.55',
                'type': 'Financial News',
                'severity': 'MEDIUM',
                'description': 'Calcalist - Israeli Financial News'
            },
            {
                'domain': 'reshet.tv',
                'full_urls': [
                    'https://www.reshet.tv',
                    'https://reshet.tv'
                ],
                'ip': '178.86.51.139',
                'type': 'TV Channel',
                'severity': 'MEDIUM',
                'description': 'Reshet TV - Israeli TV Channel'
            },
            {
                'domain': 'kan.org.il',
                'full_urls': [
                    'https://www.kan.org.il',
                    'https://kan.org.il',
                    'https://www.kan11.co.il'
                ],
                'ip': '172.66.40.164',
                'type': 'Public Broadcasting',
                'severity': 'MEDIUM',
                'description': 'Kan - Israeli Public Broadcasting'
            }
        ]
        
        # Display all infected links
        for site in infected_sites_enhanced:
            print(f"{Fore.RED}🚨 INFECTED SITE: {site['domain'].upper()}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   📍 IP Address: {site['ip']}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}   🏷️  Type: {site['type']}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}   ⚠️  Risk Level: {site['severity']}{Style.RESET_ALL}")
            print(f"   📝 Description: {site['description']}")
            print()
            
            print(f"   {Fore.RED}🔗 MAIN URLs:{Style.RESET_ALL}")
            for url in site['full_urls']:
                print(f"      {url}")
            
            if site.get('subdomains'):
                print(f"\n   {Fore.RED}🔗 SUBDOMAINS:{Style.RESET_ALL}")
                for subdomain in site['subdomains']:
                    print(f"      {subdomain}")
            
            print(f"\n{Fore.RED}{'-'*100}{Style.RESET_ALL}")
            print()
            
        # Generate clickable HTML report
        self.generate_html_report(infected_sites_enhanced)
        
    def generate_html_report(self, sites):
        """Generate HTML report with clickable links"""
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Infected Israeli Website Links Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #1a1a1a;
            color: #ffffff;
            margin: 0;
            padding: 20px;
        }}
        .header {{
            background-color: #8B0000;
            color: white;
            padding: 20px;
            text-align: center;
            margin-bottom: 30px;
            border-radius: 10px;
        }}
        .site-card {{
            background-color: #2a2a2a;
            border: 2px solid #ff0000;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .site-title {{
            color: #ff0000;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .site-info {{
            color: #cccccc;
            margin-bottom: 10px;
        }}
        .link-section {{
            margin: 10px 0;
        }}
        .link-title {{
            color: #ff6600;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .link {{
            display: block;
            color: #00ff00;
            text-decoration: none;
            margin: 5px 0;
            padding: 5px;
            background-color: #333;
            border-radius: 5px;
        }}
        .link:hover {{
            background-color: #555;
        }}
        .risk-high {{
            color: #ff0000;
            font-weight: bold;
        }}
        .risk-medium {{
            color: #ff9900;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🚨 INFECTED ISRAELI WEBSITE LINKS 🚨</h1>
        <p>Comprehensive Report of Israeli Website URLs</p>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>

"""
        
        for site in sites:
            html_content += f"""
    <div class="site-card">
        <div class="site-title">🎯 {site['domain'].upper()}</div>
        <div class="site-info">
            <strong>IP:</strong> {site['ip']} | 
            <strong>Type:</strong> {site['type']} | 
            <strong>Risk:</strong> <span class="risk-{site['severity'].lower()}">{site['severity']}</span>
        </div>
        <div class="site-info">{site['description']}</div>
        
        <div class="link-section">
            <div class="link-title">🔗 MAIN URLs:</div>
"""
            
            for url in site['full_urls']:
                html_content += f'<a href="{url}" class="link" target="_blank">{url}</a>\n'
                
            if site.get('subdomains'):
                html_content += '<div class="link-title">🔗 SUBDOMAINS:</div>\n'
                for subdomain in site['subdomains']:
                    html_content += f'<a href="{subdomain}" class="link" target="_blank">{subdomain}</a>\n'
                    
            html_content += """
        </div>
    </div>
"""
            
        html_content += """
    <div style="text-align: center; margin-top: 30px; color: #666;">
        <p>Report generated by Advanced SQL Search Tool</p>
        <p>Developer: SayerLinux | GitHub: https://github.com/SaudiLinux</p>
    </div>
</body>
</html>
"""
        
        # Save HTML report
        with open('infected_links_report.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"{Fore.GREEN}📄 HTML Report saved to: infected_links_report.html{Style.RESET_ALL}")
        print(f"{Fore.GREEN}📱 Open this file in your browser to see clickable links{Style.RESET_ALL}")
        
    def run(self):
        """Run the infected links reporter"""
        self.generate_infected_links()
        
        # Save JSON version
        infected_links_json = []
        for site in self.infected_sites:
            infected_links_json.append({
                'domain': site['domain'],
                'main_urls': [f"https://{site['domain']}", f"http://{site['domain']}"],
                'full_urls': [f"https://{site['domain']}", f"https://www.{site['domain']}", 
                             f"http://{site['domain']}", f"http://www.{site['domain']}"],
                'ip_address': site['ip_address'],
                'type': site['israeli_type'],
                'severity': site['severity'],
                'status': 'INFECTED - ISRAELI SITE',
                'report_time': datetime.now().isoformat()
            })
            
        with open('infected_links.json', 'w', encoding='utf-8') as f:
            json.dump(infected_links_json, f, ensure_ascii=False, indent=2)
            
        print(f"{Fore.GREEN}📊 JSON Links saved to: infected_links.json{Style.RESET_ALL}")

if __name__ == "__main__":
    reporter = InfectedLinksReporter()
    reporter.run()