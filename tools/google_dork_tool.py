#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Google Dorking Tool for Israeli Websites
Developed by: SayerLinux
GitHub: https://github.com/SaudiLinux
Email: SayerLinux1@gmail.com

This tool uses Google Dorking techniques to find Israeli websites with specific vulnerabilities.
"""

import webbrowser
import json
import time
from datetime import datetime
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows
init()

class GoogleDorkingTool:
    def __init__(self):
        self.israeli_domains = [
            'site:gov.il',
            'site:co.il',
            'site:org.il',
            'site:ac.il',
            'site:muni.il',
            'site:idf.il',
            'site:knesset.gov.il',
            'site:pmo.gov.il',
            'site:mfa.gov.il',
            'site:mod.gov.il'
        ]
        
        self.dork_categories = {
            'sql_injection': {
                'name': 'SQL Injection Vulnerabilities',
                'dorks': [
                    'inurl:php?id=',
                    'inurl:asp?id=',
                    'inurl:jsp?id=',
                    'inurl:news.php?id=',
                    'inurl:article.php?id=',
                    'inurl:product.php?id=',
                    'inurl:category.php?id=',
                    'inurl:search.php?q=',
                    'inurl:login.php?user=',
                    'inurl:register.php?name='
                ]
            },
            'admin_panels': {
                'name': 'Admin Panels',
                'dorks': [
                    'intitle:"admin login"',
                    'intitle:"admin panel"',
                    'inurl:admin',
                    'inurl:administrator',
                    'inurl:admin/login',
                    'inurl:admin.php',
                    'inurl:admin.html',
                    'intitle:"control panel"',
                    'intitle:"admin area"',
                    'inurl:cpanel'
                ]
            },
            'file_vulnerabilities': {
                'name': 'File Vulnerabilities',
                'dorks': [
                    'inurl:download.php?file=',
                    'inurl:upload.php',
                    'inurl:file.php?name=',
                    'inurl:document.php?file=',
                    'inurl:readfile.php?file=',
                    'inurl:include.php?page=',
                    'inurl:config.php',
                    'inurl:backup.sql',
                    'intitle:"index of" "backup"',
                    'intitle:"index of" "database"'
                ]
            },
            'exposed_databases': {
                'name': 'Exposed Databases',
                'dorks': [
                    'intitle:"phpMyAdmin"',
                    'intitle:"MySQL" "Welcome to phpMyAdmin"',
                    'inurl:phpmyadmin',
                    'inurl:mysql',
                    'intitle:"Welcome to phpMyAdmin"',
                    'intitle:"MySQL Error"',
                    'inurl:dbadmin',
                    'inurl:database',
                    'intitle:"SQL Server"',
                    'inurl:sqlmanager'
                ]
            },
            'login_vulnerabilities': {
                'name': 'Login Vulnerabilities',
                'dorks': [
                    'inurl:login.php',
                    'inurl:login.html',
                    'intitle:"login"',
                    'intitle:"sign in"',
                    'inurl:forgot_password.php',
                    'inurl:reset_password.php',
                    'inurl:register.php',
                    'intitle:"admin login"',
                    'intitle:"user login"',
                    'inurl:auth.php'
                ]
            },
            'sensitive_files': {
                'name': 'Sensitive Files',
                'dorks': [
                    'intitle:"index of" "passwd"',
                    'intitle:"index of" "etc"',
                    'intitle:"index of" "config"',
                    'inurl:robots.txt',
                    'inurl:.htaccess',
                    'inurl:web.config',
                    'inurl:php.ini',
                    'inurl:config.php',
                    'inurl:settings.php',
                    'inurl:database.php'
                ]
            },
            'xss_vulnerabilities': {
                'name': 'XSS Vulnerabilities',
                'dorks': [
                    'inurl:search.php?q=',
                    'inurl:comment.php?text=',
                    'inurl:contact.php?name=',
                    'inurl:feedback.php?message=',
                    'inurl:guestbook.php?text=',
                    'inurl:post.php?title=',
                    'inurl:news.php?title=',
                    'inurl:article.php?title=',
                    'inurl:product.php?name=',
                    'inurl:profile.php?user='
                ]
            },
            'backup_files': {
                'name': 'Backup Files',
                'dorks': [
                    'intitle:"index of" "backup"',
                    'intitle:"index of" "bak"',
                    'intitle:"index of" "sql"',
                    'intitle:"index of" "db"',
                    'filetype:sql',
                    'filetype:bak',
                    'filetype:backup',
                    'filetype:zip',
                    'filetype:rar',
                    'filetype:tar.gz'
                ]
            }
        }
        
        self.custom_dorks = {
            'israeli_military': [
                'site:idf.il inurl:admin',
                'site:mod.gov.il intitle:"confidential"',
                'site:gov.il filetype:pdf "classified"',
                'site:mil.il inurl:documents',
                'site:gov.il inurl:secure'
            ],
            'israeli_government': [
                'site:pmo.gov.il inurl:admin',
                'site:knesset.gov.il filetype:xls',
                'site:mfa.gov.il intitle:"database"',
                'site:justice.gov.il inurl:login',
                'site:police.gov.il filetype:pdf'
            ],
            'israeli_intelligence': [
                'site:gov.il "Mossad"',
                'site:gov.il "Shin Bet"',
                'site:gov.il "intelligence"',
                'site:gov.il "classified"',
                'site:gov.il "secret"'
            ]
        }
        
    def display_banner(self):
        """Display Google Dorking banner"""
        print(f"{Fore.GREEN}{Back.BLACK}")
        print("""
   ╔═══════════════════════════════════════════════════════════════╗
   ║                                                               ║
   ║  ███████╗ ██████╗  ██████╗ ███╗   ██╗██╗███████╗            ║
   ║  ██╔════╝██╔════╝ ██╔═══██╗████╗  ██║██║██╔════╝            ║
   ║  ███████╗██║  ███╗██║   ██║██╔██╗ ██║██║███████╗            ║
   ║  ╚════██║██║   ██║██║   ██║██║╚██╗██║██║╚════██║            ║
   ║  ███████║╚██████╔╝╚██████╔╝██║ ╚████║██║███████║            ║
   ║  ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚══════╝            ║
   ║                                                               ║
   ║  ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ███████╗██████╗   ║
   ║  ██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  ║
   ║  ██║  ██║██║   ██║██║   ██║██║  ██║██████╔╝█████╗  ██████╔╝  ║
   ║  ██║  ██║██║   ██║██║   ██║██║  ██║██╔══██╗██╔══╝  ██╔══██╗  ║
   ║  ██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝███████╗██║  ██║  ║
   ║  ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ║
   ║                                                               ║
   ║  Advanced Google Dorking Tool for Israeli Websites           ║
   ║  Security Research & Intelligence Gathering                   ║
   ║                                                               ║
   ╚═══════════════════════════════════════════════════════════════╝
        """)
        print(f"{Style.RESET_ALL}")
        print(f"{Fore.GREEN}🔍 Advanced Google Dorking Tool{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🎯 Target: Israeli Government & Media Sites{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📊 Categories: SQL Injection, Admin Panels, File Vulnerabilities{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*80}{Style.RESET_ALL}")
        
    def generate_dork_queries(self, category, israeli_domain=None):
        """Generate Google Dork queries for specific category"""
        queries = []
        
        if israeli_domain:
            domains = [israeli_domain]
        else:
            domains = self.israeli_domains
            
        if category in self.dork_categories:
            dork_list = self.dork_categories[category]['dorks']
            for domain in domains:
                for dork in dork_list:
                    query = f"{domain} {dork}"
                    queries.append({
                        'category': self.dork_categories[category]['name'],
                        'query': query,
                        'domain': domain,
                        'dork': dork,
                        'timestamp': datetime.now().isoformat()
                    })
                    
        return queries
        
    def generate_custom_dorks(self, dork_type):
        """Generate custom dorks for specific purposes"""
        if dork_type in self.custom_dorks:
            queries = []
            for dork in self.custom_dorks[dork_type]:
                queries.append({
                    'category': f'Custom - {dork_type}',
                    'query': dork,
                    'domain': 'custom',
                    'dork': dork,
                    'timestamp': datetime.now().isoformat()
                })
            return queries
        return []
        
    def open_dork_in_browser(self, query):
        """Open Google search for specific dork"""
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        print(f"{Fore.CYAN}[+] Opening: {url}{Style.RESET_ALL}")
        webbrowser.open(url)
        time.sleep(1)  # Rate limiting
        
    def generate_all_dorks(self):
        """Generate all possible dork combinations"""
        all_dorks = []
        
        # Generate dorks for each category
        for category in self.dork_categories:
            dorks = self.generate_dork_queries(category)
            all_dorks.extend(dorks)
            
        # Add custom dorks
        for custom_type in self.custom_dorks:
            custom_dorks = self.generate_custom_dorks(custom_type)
            all_dorks.extend(custom_dorks)
            
        return all_dorks
        
    def save_dorks_to_file(self, dorks, filename):
        """Save dork queries to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dorks, f, ensure_ascii=False, indent=2)
        print(f"{Fore.GREEN}[+] Dorks saved to: {filename}{Style.RESET_ALL}")
        
    def generate_html_dork_report(self, dorks):
        """Generate HTML report with clickable dork links"""
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Israeli Website Google Dorking Report</title>
    <style>
        body {{
            font-family: 'Courier New', monospace;
            background-color: #0a0a0a;
            color: #00ff00;
            margin: 0;
            padding: 20px;
        }}
        .header {{
            background: linear-gradient(45deg, #008000, #004d00);
            color: white;
            padding: 30px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .category {{
            background-color: #1a1a1a;
            border: 2px solid #00ff00;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .dork-link {{
            display: block;
            color: #00ffff;
            text-decoration: none;
            padding: 10px;
            margin: 5px 0;
            background-color: #333;
            border-radius: 5px;
            transition: background-color 0.3s;
        }}
        .dork-link:hover {{
            background-color: #555;
        }}
        .domain-badge {{
            background-color: #ff6600;
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 Israeli Website Google Dorking Report</h1>
        <p>Advanced Security Research & Intelligence Gathering</p>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
"""
        
        # Group dorks by category
        categories = {}
        for dork in dorks:
            category = dork['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(dork)
            
        for category, dork_list in categories.items():
            html_content += f"""
    <div class="category">
        <h2>📁 {category}</h2>
"""
            for dork in dork_list:
                google_url = f"https://www.google.com/search?q={dork['query'].replace(' ', '+')}"
                html_content += f"""
        <a href="{google_url}" class="dork-link" target="_blank">
            {dork['query']} <span class="domain-badge">{dork['domain']}</span>
        </a>
"""
            html_content += "</div>"
            
        html_content += """
    <div style="text-align: center; margin-top: 30px; color: #666;">
        <p>🔍 Report generated by Advanced Google Dorking Tool</p>
        <p>For security research purposes only</p>
    </div>
</body>
</html>
"""
        
        with open('google_dorks_report.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"{Fore.GREEN}[+] HTML report saved to: google_dorks_report.html{Style.RESET_ALL}")
        
    def interactive_dorking(self):
        """Interactive Google Dorking menu"""
        print(f"\n{Fore.YELLOW}🔍 Google Dorking Categories:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. SQL Injection Vulnerabilities{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. Admin Panels{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. File Vulnerabilities{Style.RESET_ALL}")
        print(f"{Fore.CYAN}4. Exposed Databases{Style.RESET_ALL}")
        print(f"{Fore.CYAN}5. Login Vulnerabilities{Style.RESET_ALL}")
        print(f"{Fore.CYAN}6. Sensitive Files{Style.RESET_ALL}")
        print(f"{Fore.CYAN}7. XSS Vulnerabilities{Style.RESET_ALL}")
        print(f"{Fore.CYAN}8. Backup Files{Style.RESET_ALL}")
        print(f"{Fore.CYAN}9. Israeli Military Sites{Style.RESET_ALL}")
        print(f"{Fore.CYAN}10. Israeli Government Sites{Style.RESET_ALL}")
        print(f"{Fore.CYAN}11. Generate All Dorks{Style.RESET_ALL}")
        print(f"{Fore.CYAN}12. Exit{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.YELLOW}Enter your choice (1-12): {Style.RESET_ALL}")
        
        if choice == '11':
            dorks = self.generate_all_dorks()
            self.save_dorks_to_file(dorks, 'all_google_dorks.json')
            self.generate_html_dork_report(dorks)
            print(f"{Fore.GREEN}[+] All dorks generated and saved!{Style.RESET_ALL}")
            
        elif choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
            categories = list(self.dork_categories.keys())
            category = categories[int(choice) - 1]
            dorks = self.generate_dork_queries(category)
            self.save_dorks_to_file(dorks, f'{category}_dorks.json')
            self.generate_html_dork_report(dorks)
            
            # Ask to open in browser
            open_choice = input(f"{Fore.YELLOW}Open dorks in browser? (y/n): {Style.RESET_ALL}")
            if open_choice.lower() == 'y':
                for dork in dorks[:5]:  # Open first 5 results
                    self.open_dork_in_browser(dork['query'])
                    
        elif choice == '9':
            dorks = self.generate_custom_dorks('israeli_military')
            self.save_dorks_to_file(dorks, 'israeli_military_dorks.json')
            self.generate_html_dork_report(dorks)
            
        elif choice == '10':
            dorks = self.generate_custom_dorks('israeli_government')
            self.save_dorks_to_file(dorks, 'israeli_government_dorks.json')
            self.generate_html_dork_report(dorks)
            
    def run_full_dorking(self):
        """Run complete Google Dorking process"""
        self.display_banner()
        
        print(f"{Fore.YELLOW}[+] Generating comprehensive Google Dorks...{Style.RESET_ALL}")
        
        # Generate all dorks
        all_dorks = self.generate_all_dorks()
        
        # Save to files
        self.save_dorks_to_file(all_dorks, 'israeli_google_dorks.json')
        self.generate_html_dork_report(all_dorks)
        
        # Display summary
        categories = {}
        for dork in all_dorks:
            category = dork['category']
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
            
        print(f"\n{Fore.GREEN}[+] Dorking Summary:{Style.RESET_ALL}")
        for category, count in categories.items():
            print(f"{Fore.CYAN}  📊 {category}: {count} dorks{Style.RESET_ALL}")
            
        print(f"\n{Fore.GREEN}[+] Total dorks generated: {len(all_dorks)}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Files saved: israeli_google_dorks.json, google_dorks_report.html{Style.RESET_ALL}")
        
        return all_dorks

if __name__ == "__main__":
    tool = GoogleDorkingTool()
    
    print(f"{Fore.YELLOW}Choose mode:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. Interactive mode{Style.RESET_ALL}")
    print(f"{Fore.CYAN}2. Full automated dorking{Style.RESET_ALL}")
    
    mode = input(f"\n{Fore.YELLOW}Enter choice (1-2): {Style.RESET_ALL}")
    
    if mode == '1':
        while True:
            tool.interactive_dorking()
            continue_choice = input(f"\n{Fore.YELLOW}Continue? (y/n): {Style.RESET_ALL}")
            if continue_choice.lower() != 'y':
                break
    else:
        tool.run_full_dorking()