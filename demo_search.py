#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Search - Automatic Israeli Website Scanner
Developed by: SayerLinux
"""

import socket
import threading
import json
import time
from datetime import datetime

class DemoScanner:
    def __init__(self):
        self.results = []
        self.israeli_domains = [
            '.il', '.co.il', '.org.il', '.gov.il', '.ac.il', '.muni.il',
            '.idf.il', '.mod.gov.il', '.mfa.gov.il', '.knesset.gov.il',
            'jpost.com', 'ynet.co.il', 'haaretz.co.il', 'timesofisrael.com'
        ]
        
    def scan_port(self, ip, port, results, lock):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                services = {
                    3306: "MySQL", 5432: "PostgreSQL", 1433: "MSSQL",
                    1521: "Oracle", 6379: "Redis", 27017: "MongoDB"
                }
                service = services.get(port, f"Port {port}")
                
                with lock:
                    results.append({
                        'domain': self.current_domain,
                        'ip': ip,
                        'port': port,
                        'service': service,
                        'is_israeli': True,
                        'timestamp': datetime.now().isoformat()
                    })
                    print(f"[+] Found {service} on port {port}")
            
            sock.close()
            
        except:
            pass
    
    def scan_domain(self, domain):
        print(f"\n🔍 Scanning {domain} for SQL servers...")
        
        try:
            ip = socket.gethostbyname(domain)
            print(f"✅ Resolved {domain} to {ip}")
            
            self.current_domain = domain
            results = []
            lock = threading.Lock()
            threads = []
            
            # Scan common SQL ports
            sql_ports = [3306, 5432, 1433, 1521, 6379, 27017]
            
            for port in sql_ports:
                thread = threading.Thread(
                    target=self.scan_port,
                    args=(ip, port, results, lock)
                )
                thread.daemon = True
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()
                
            return results
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return []

def main():
    scanner = DemoScanner()
    
    print("\n" + "="*70)
    print("          DEMONSTRATION: Israeli Website Scanner")
    print("="*70)
    
    # Test with Israeli domains
    test_domains = [
        "gov.il",
        "ynet.co.il", 
        "haaretz.co.il",
        "jpost.com"
    ]
    
    all_results = []
    
    for domain in test_domains:
        results = scanner.scan_domain(domain)
        all_results.extend(results)
        time.sleep(1)  # Small delay between domains
    
    # Display summary
    print("\n" + "="*70)
    print("                    SCAN SUMMARY")
    print("="*70)
    
    if all_results:
        print(f"✅ Total servers found: {len(all_results)}")
        
        # Display results
        for i, result in enumerate(all_results, 1):
            print(f"\n{i}. Domain: {result['domain']}")
            print(f"   IP: {result['ip']}:{result['port']}")
            print(f"   Service: {result['service']}")
            print(f"   Israeli Site: YES")
            print(f"   Timestamp: {result['timestamp']}")
            print("-" * 50)
        
        # Save results
        filename = f"israeli_scan_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
        
        print(f"\n📄 Results saved to: {filename}")
        
    else:
        print("❌ No SQL servers found in the test domains")
        
    print("\n🔍 Demo search complete!")

if __name__ == "__main__":
    main()