#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Infected Sites Report - Israeli Website Detection Report
Developed by: SayerLinux
GitHub: https://github.com/SaudiLinux
Email: SayerLinux1@gmail.com
"""

import socket
import threading
import json
import time
from datetime import datetime
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows
init()

class InfectedSitesReporter:
    def __init__(self):
        self.infected_sites = []
        self.israeli_domains = [
            '.il', '.co.il', '.org.il', '.gov.il', '.ac.il', '.muni.il',
            '.idf.il', '.mod.gov.il', '.mfa.gov.il', '.knesset.gov.il',
            'jpost.com', 'ynet.co.il', 'haaretz.co.il', 'timesofisrael.com',
            'israelhayom.co.il', 'walla.co.il', 'mako.co.il', 'n12.co.il',
            'globes.co.il', 'calcalist.co.il', 'reshet.tv', 'kan.org.il',
            'ynetnews.com', 'jpost.co.il', 'israelnationalnews.com',
            'jewishpress.com', 'algemeiner.com', 'jewishjournal.com'
        ]
        
        # Enhanced Israeli sites database
        self.israeli_sites_db = {
            'gov.il': {
                'type': 'Government',
                'category': 'Official Government',
                'severity': 'HIGH',
                'description': 'Israeli Government Portal'
            },
            'ynet.co.il': {
                'type': 'News',
                'category': 'Major News Portal',
                'severity': 'HIGH',
                'description': 'Ynet - Israeli News'
            },
            'haaretz.co.il': {
                'type': 'News',
                'category': 'Newspaper',
                'severity': 'HIGH',
                'description': 'Haaretz Israeli Newspaper'
            },
            'jpost.com': {
                'type': 'News',
                'category': 'International News',
                'severity': 'HIGH',
                'description': 'Jerusalem Post'
            },
            'timesofisrael.com': {
                'type': 'News',
                'category': 'Online News',
                'severity': 'MEDIUM',
                'description': 'Times of Israel'
            },
            'israelhayom.co.il': {
                'type': 'News',
                'category': 'Daily Newspaper',
                'severity': 'HIGH',
                'description': 'Israel Hayom'
            },
            'walla.co.il': {
                'type': 'Portal',
                'category': 'Major Portal',
                'severity': 'MEDIUM',
                'description': 'Walla! Israeli Portal'
            },
            'mako.co.il': {
                'type': 'Media',
                'category': 'TV Channel',
                'severity': 'MEDIUM',
                'description': 'Mako TV Channel'
            }
        }
        
    def display_banner(self):
        """Display infected sites banner"""
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗
║                    INFECTED SITES DETECTION REPORT                          ║
║                          Israeli Website Scanner                            ║
║                    {Fore.YELLOW}⚠️  WARNING: ISRAELI SITES DETECTED  ⚠️{Fore.RED}                       ║
║                    Developed by: {Fore.GREEN}SayerLinux{Fore.RED}                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)
        
    def scan_infected_site(self, domain):
        """Scan individual infected site"""
        try:
            print(f"{Fore.YELLOW}🔍 Scanning {domain}...{Style.RESET_ALL}")
            
            # Resolve IP
            ip = socket.gethostbyname(domain)
            
            # Get site info from database
            site_info = self.israeli_sites_db.get(domain, {
                'type': 'Unknown',
                'category': 'Israeli Site',
                'severity': 'MEDIUM',
                'description': f'Israeli website: {domain}'
            })
            
            # Scan for SQL servers
            sql_ports = [3306, 5432, 1433, 1521, 6379, 27017, 3307, 3308, 3309]
            detected_services = []
            
            for port in sql_ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((ip, port))
                    
                    if result == 0:
                        services = {
                            3306: "MySQL", 5432: "PostgreSQL", 1433: "MSSQL",
                            1521: "Oracle", 6379: "Redis", 27017: "MongoDB"
                        }
                        service = services.get(port, f"Port {port}")
                        detected_services.append({
                            'port': port,
                            'service': service,
                            'status': 'OPEN'
                        })
                        
                        print(f"{Fore.RED}   ⚠️  {service} server detected on port {port}{Style.RESET_ALL}")
                    
                    sock.close()
                    
                except:
                    pass
            
            # Create infected site record
            infected_site = {
                'domain': domain,
                'ip_address': ip,
                'israeli_type': site_info['type'],
                'category': site_info['category'],
                'severity': site_info['severity'],
                'description': site_info['description'],
                'sql_servers': detected_services,
                'detection_time': datetime.now().isoformat(),
                'status': 'INFECTED - ISRAELI SITE'
            }
            
            self.infected_sites.append(infected_site)
            
            if detected_services:
                print(f"{Fore.RED}   🚨 HIGH RISK: SQL servers found on Israeli site!{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}   ✅ Site scanned, no SQL servers exposed{Style.RESET_ALL}")
                
            return infected_site
            
        except Exception as e:
            print(f"{Fore.RED}   ❌ Error scanning {domain}: {str(e)}{Style.RESET_ALL}")
            return None
            
    def generate_infected_report(self):
        """Generate comprehensive infected sites report"""
        self.display_banner()
        
        print(f"{Fore.CYAN}📊 Starting comprehensive Israeli site scan...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}⏰ Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
        print()
        
        # List of known Israeli sites to scan
        infected_targets = [
            'gov.il',
            'ynet.co.il',
            'haaretz.co.il', 
            'jpost.com',
            'timesofisrael.com',
            'israelhayom.co.il',
            'walla.co.il',
            'mako.co.il',
            'n12.co.il',
            'globes.co.il',
            'calcalist.co.il',
            'reshet.tv',
            'kan.org.il'
        ]
        
        print(f"{Fore.RED}🎯 Targeting {len(infected_targets)} Israeli sites...{Style.RESET_ALL}")
        print()
        
        # Scan each infected site
        successful_scans = 0
        for domain in infected_targets:
            result = self.scan_infected_site(domain)
            if result:
                successful_scans += 1
            time.sleep(0.5)  # Rate limiting
            
        # Display final report
        self.display_final_report(successful_scans)
        
    def display_final_report(self, successful_scans):
        """Display final infected sites report"""
        print(f"\n{Fore.RED}{'='*100}{Style.RESET_ALL}")
        print(f"{Fore.RED}                    INFECTED SITES FINAL REPORT{Style.RESET_ALL}")
        print(f"{Fore.RED}{'='*100}{Style.RESET_ALL}")
        
        total_sites = len(self.infected_sites)
        high_risk = len([s for s in self.infected_sites if s['severity'] == 'HIGH'])
        medium_risk = len([s for s in self.infected_sites if s['severity'] == 'MEDIUM'])
        
        # Sites with SQL servers
        sql_exposed = [s for s in self.infected_sites if s['sql_servers']]
        
        print(f"\n{Fore.YELLOW}📊 SCAN STATISTICS:{Style.RESET_ALL}")
        print(f"   • Total sites scanned: {total_sites}")
        print(f"   • Successful scans: {successful_scans}")
        print(f"   • High risk sites: {Fore.RED}{high_risk}{Style.RESET_ALL}")
        print(f"   • Medium risk sites: {Fore.YELLOW}{medium_risk}{Style.RESET_ALL}")
        print(f"   • Sites with exposed SQL: {Fore.RED}{len(sql_exposed)}{Style.RESET_ALL}")
        
        print(f"\n{Fore.RED}🚨 INFECTED SITES DETECTED:{Style.RESET_ALL}")
        
        for i, site in enumerate(self.infected_sites, 1):
            severity_color = Fore.RED if site['severity'] == 'HIGH' else Fore.YELLOW
            print(f"\n{i}. {severity_color}{site['domain']}{Style.RESET_ALL}")
            print(f"   IP: {site['ip_address']}")
            print(f"   Type: {site['israeli_type']}")
            print(f"   Category: {site['category']}")
            print(f"   Risk Level: {severity_color}{site['severity']}{Style.RESET_ALL}")
            print(f"   Status: {Fore.RED}{site['status']}{Style.RESET_ALL}")
            
            if site['sql_servers']:
                print(f"   {Fore.RED}⚠️  SQL Servers Exposed:{Style.RESET_ALL}")
                for server in site['sql_servers']:
                    print(f"      • {server['service']} on port {server['port']}")
            
        # Save report
        report_filename = f"infected_sites_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_filename, 'w', encoding='utf-8') as f:
            json.dump(self.infected_sites, f, ensure_ascii=False, indent=2)
            
        print(f"\n{Fore.GREEN}📄 Report saved to: {report_filename}{Style.RESET_ALL}")
        print(f"{Fore.RED}🚨 Scan complete - Israeli sites detected and documented!{Style.RESET_ALL}")

def main():
    reporter = InfectedSitesReporter()
    reporter.generate_infected_report()

if __name__ == "__main__":
    main()