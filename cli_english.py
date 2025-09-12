#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced SQL Search Tool - English CLI Version
Developed by: SayerLinux
Website: https://github.com/SaudiLinux
Email: SayerLinux1@gmail.com
"""

import socket
import threading
import json
import os
import sys
import time
from datetime import datetime

class AdvancedSQLSearchToolCLI:
    def __init__(self):
        self.results = []
        self.searching = False
        self.current_domain = ""
        self.load_israeli_domains()
        
    def load_israeli_domains(self):
        """Load Israeli domains database"""
        self.israeli_domains = [
            '.il', '.co.il', '.org.il', '.gov.il', '.ac.il', '.muni.il',
            '.idf.il', '.mod.gov.il', '.mfa.gov.il', '.knesset.gov.il',
            'jpost.com', 'ynet.co.il', 'haaretz.co.il', 'timesofisrael.com',
            'israelhayom.co.il', 'walla.co.il', 'mako.co.il', 'n12.co.il',
            'jpost.co.il', 'globes.co.il', 'calcalist.co.il',
            'mako.co.il', 'reshet.tv', 'kan.org.il'
        ]
        
    def display_banner(self):
        """Display application banner"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    Advanced SQL Search Tool - English Version                ║
║                          Developed by: SayerLinux                            ║
║                    GitHub: https://github.com/SaudiLinux                     ║
║                    Email: SayerLinux1@gmail.com                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
        
    def log_message(self, message, level="INFO"):
        """Log messages to console"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        levels = {
            "INFO": "[INFO]",
            "ERROR": "[ERROR]",
            "SUCCESS": "[SUCCESS]",
            "WARNING": "[WARNING]"
        }
        
        prefix = levels.get(level, "[INFO]")
        formatted_message = f"[{timestamp}] {prefix} {message}"
        
        # Color coding for terminal
        colors = {
            "ERROR": "\033[91m",
            "SUCCESS": "\033[92m", 
            "WARNING": "\033[93m",
            "INFO": "\033[94m",
            "RESET": "\033[0m"
        }
        
        color = colors.get(level, colors["INFO"])
        reset = colors["RESET"]
        print(f"{color}{formatted_message}{reset}")
        
    def is_israeli_site(self, url):
        """Check if site is Israeli"""
        url_lower = url.lower()
        return any(domain.lower() in url_lower for domain in self.israeli_domains)
        
    def scan_port(self, ip, port, results, lock):
        """Scan individual port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                service = self.get_service_name(port)
                with lock:
                    results.append({
                        'domain': self.current_domain,
                        'ip': ip,
                        'port': port,
                        'service': service,
                        'is_israeli': self.is_israeli_site(self.current_domain),
                        'timestamp': datetime.now().isoformat()
                    })
                    self.log_message(f"Found {service} server on port {port}", "SUCCESS")
            
            sock.close()
            
        except Exception as e:
            pass
            
    def get_service_name(self, port):
        """Get service name by port"""
        services = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            993: "IMAPS",
            995: "POP3S",
            1433: "MSSQL",
            1521: "Oracle",
            3306: "MySQL",
            3307: "MySQL",
            5432: "PostgreSQL",
            6379: "Redis",
            27017: "MongoDB",
            27018: "MongoDB",
            27019: "MongoDB"
        }
        return services.get(port, f"Port {port}")
        
    def scan_sql_servers(self, domain, start_port, end_port, max_threads, timeout):
        """Scan for SQL servers in target domain"""
        try:
            # Resolve domain to IP
            ip = socket.gethostbyname(domain)
            self.log_message(f"Resolved {domain} to {ip}")
            
            self.log_message(f"Scanning ports {start_port}-{end_port} with {max_threads} threads")
            
            results = []
            lock = threading.Lock()
            threads = []
            
            # Scan ports using threads
            for port in range(start_port, end_port + 1):
                if not self.searching:
                    break
                    
                while threading.active_count() > max_threads + 10:
                    time.sleep(0.1)
                    
                thread = threading.Thread(
                    target=self.scan_port,
                    args=(ip, port, results, lock)
                )
                thread.daemon = True
                thread.start()
                threads.append(thread)
                
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
                
            return results
            
        except Exception as e:
            self.log_message(f"Error scanning {domain}: {str(e)}", "ERROR")
            return []
            
    def start_search(self):
        """Start search process"""
        # Get search parameters
        print("\n" + "="*60)
        print("                    SEARCH CONFIGURATION")
        print("="*60)
        
        domain = input("\nEnter target domain (e.g., example.com): ").strip()
        if not domain:
            self.log_message("Invalid domain provided", "ERROR")
            return
            
        try:
            start_port = int(input("Enter start port (default 3300): ") or "3300")
            end_port = int(input("Enter end port (default 3310): ") or "3310")
            max_threads = int(input("Enter thread count (default 10): ") or "10")
            timeout = float(input("Enter timeout in seconds (default 3): ") or "3")
            
            if start_port > end_port:
                self.log_message("Start port must be less than end port", "ERROR")
                return
                
            if max_threads < 1 or max_threads > 100:
                self.log_message("Thread count must be between 1 and 100", "ERROR")
                return
                
        except ValueError:
            self.log_message("Please enter valid numbers", "ERROR")
            return
            
        self.timeout = timeout
        self.current_domain = domain
        self.results = []
        self.searching = True
        
        self.log_message(f"Starting SQL server scan for: {domain}")
        
        results = self.scan_sql_servers(domain, start_port, end_port, max_threads, timeout)
        self.results = results
        
        if results:
            self.log_message(f"✅ Scan complete! Found {len(results)} servers")
            
            # Display summary
            israeli_count = sum(1 for r in results if r['is_israeli'])
            self.log_message(f"Israeli sites found: {israeli_count}")
            
            # Display results
            print("\n" + "="*80)
            print("                    SCAN RESULTS")
            print("="*80)
            
            for i, result in enumerate(results, 1):
                print(f"\n{i}. Domain: {result['domain']}")
                print(f"   IP: {result['ip']}:{result['port']}")
                print(f"   Service: {result['service']}")
                print(f"   Israeli Site: {'Yes' if result['is_israeli'] else 'No'}")
                print(f"   Timestamp: {result['timestamp']}")
                print("-" * 40)
                
            # Save results
            save_choice = input("\nSave results to JSON file? (y/n): ").lower()
            if save_choice == 'y':
                filename = f"scan_results_{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(self.results, f, ensure_ascii=False, indent=2)
                    self.log_message(f"Results saved to: {filename}")
                except Exception as e:
                    self.log_message(f"Save error: {str(e)}", "ERROR")
                    
        else:
            self.log_message("❌ No SQL servers found")
            
        self.searching = False
        
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("                    MAIN MENU")
        print("="*60)
        print("1. Start New Search")
        print("2. View Israeli Domains List")
        print("3. Clear Results")
        print("4. About")
        print("5. Exit")
        print("="*60)
        
    def view_israeli_domains(self):
        """Display Israeli domains list"""
        print("\n" + "="*60)
        print("                    ISRAELI DOMAINS")
        print("="*60)
        for domain in self.israeli_domains:
            print(f"  • {domain}")
        print(f"\nTotal domains: {len(self.israeli_domains)}")
        
    def display_about(self):
        """Display about information"""
        print("\n" + "="*60)
        print("                    ABOUT")
        print("="*60)
        print("Advanced SQL Search Tool - English Version")
        print("A powerful tool for scanning SQL servers and detecting")
        print("Israeli websites through domain analysis.")
        print("\nFeatures:")
        print("• Multi-threaded port scanning")
        print("• Israeli website detection")
        print("• JSON result export")
        print("• Configurable scan parameters")
        print("• Real-time progress tracking")
        print("\nDeveloper: SayerLinux")
        print("GitHub: https://github.com/SaudiLinux")
        print("Email: SayerLinux1@gmail.com")
        
    def run(self):
        """Main application loop"""
        self.display_banner()
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                self.start_search()
            elif choice == "2":
                self.view_israeli_domains()
            elif choice == "3":
                self.results = []
                self.log_message("Results cleared")
            elif choice == "4":
                self.display_about()
            elif choice == "5":
                print("\nThank you for using Advanced SQL Search Tool!")
                print("Visit https://github.com/SaudiLinux for updates")
                break
            else:
                self.log_message("Invalid choice. Please select 1-5", "ERROR")

if __name__ == "__main__":
    try:
        tool = AdvancedSQLSearchToolCLI()
        tool.run()
    except KeyboardInterrupt:
        print("\n\nTool interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)