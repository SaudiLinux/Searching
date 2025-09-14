#!/usr/bin/env python3
"""
واجهة سطر الأوامر - مجموعة أدوات الأمن السيبراني الإسرائيلية
النسخة العربية
"""

import argparse
import sys
import os
from pathlib import Path
import json
import time
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

# استيراد الأدوات مباشرة من المجلد الحالي
from infected_links_report import InfectedLinksReport
from exploit_tool import ExploitTool
from google_dork_tool import GoogleDorkTool
from vulnerability_links_viewer import VulnerabilityLinksViewer
from sqli_scanner_tool import SQLiScannerTool
from show_infected_sites import ShowInfectedSites
from install import Installer

class CLISQLSearchTool:
    def __init__(self):
        self.results = []
        self.israeli_sites = []
        self.searching = False
        self.load_israeli_domains()
        
    def load_israeli_domains(self):
        """تحميل قائمة النطاقات الإسرائيلية"""
        self.israeli_domains = [
            '.il', '.co.il', '.org.il', '.gov.il', '.ac.il', '.muni.il',
            'gov.il', 'idf.il', 'mfa.gov.il', 'knesset.gov.il',
            'jpost.com', 'ynet.co.il', 'haaretz.co.il', 'timesofisrael.com',
            'israelhayom.co.il', 'walla.co.il', 'mako.co.il', 'n12.co.il'
        ]
        
    def print_banner(self):
        """طباعة شعار الأداة"""
        banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                أداة بحث SQL المتقدمة                         ║
    ║                Advanced SQL Search Tool                      ║
    ║                                                               ║
    ║  المبرمج: SayerLinux                                          ║
    ║  الموقع: https://github.com/SaudiLinux                        ║
    ║  البريد: SayerLinux1@gmail.com                                ║
    ╚═══════════════════════════════════════════════════════════════╝
        """
        print(banner)
        
    def print_menu(self):
        """طباعة قائمة الخيارات"""
        menu = """
    ╔═══════════════════════════════════════╗
    ║            قائمة الخيارات             ║
    ╠═══════════════════════════════════════╣
    ║  [1] بدء بحث جديد                     ║
    ║  [2] عرض النتائج                    ║
    ║  [3] حفظ النتائج                     ║
    ║  [4] معلومات عن الأداة               ║
    ║  [5] الخروج                           ║
    ╚═══════════════════════════════════════╝
        """
        print(menu)
        
    def log_message(self, message, level="INFO"):
        """تسجيل الرسائل"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        colors = {
            "INFO": "\033[92m",    # أخضر
            "ERROR": "\033[91m",   # أحمر
            "WARNING": "\033[93m", # أصفر
            "RESET": "\033[0m"     # إعادة التعيين
        }
        
        color = colors.get(level, colors["INFO"])
        print(f"{color}[{timestamp}] {level}: {message}{colors['RESET']}")
        
    def is_israeli_site(self, url):
        """التحقق إذا كان الموقع إسرائيلي"""
        url_lower = url.lower()
        return any(domain.lower() in url_lower for domain in self.israeli_domains)
        
    def scan_sql_servers(self, domain):
        """مسح خوادم SQL في النطاق المحدد"""
        common_ports = [3306, 5432, 1433, 1521, 27017]
        results = []
        
        try:
            # الحصول على عنوان IP
            ip = socket.gethostbyname(domain)
            self.log_message(f"تم حل النطاق {domain} إلى {ip}")
            
            # مسح المنافذ
            for port in common_ports:
                if not self.searching:
                    break
                    
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    result = sock.connect_ex((ip, port))
                    
                    if result == 0:
                        service = self.get_service_name(port)
                        self.log_message(f"✓ تم العثور على خادم {service} على المنفذ {port}")
                        
                        results.append({
                            'domain': domain,
                            'ip': ip,
                            'port': port,
                            'service': service,
                            'is_israeli': self.is_israeli_site(domain),
                            'timestamp': datetime.now().isoformat()
                        })
                    
                    sock.close()
                    
                except Exception as e:
                    self.log_message(f"خطأ في مسح المنفذ {port}: {str(e)}", "ERROR")
                    
        except Exception as e:
            self.log_message(f"خطأ في حل النطاق {domain}: {str(e)}", "ERROR")
            
        return results
        
    def get_service_name(self, port):
        """الحصول على اسم الخدمة حسب المنفذ"""
        services = {
            3306: "MySQL",
            5432: "PostgreSQL",
            1433: "Microsoft SQL Server",
            1521: "Oracle",
            27017: "MongoDB"
        }
        return services.get(port, f"Port {port}")
        
    def start_search(self):
        """بدء عملية البحث"""
        domain = input("\nأدخل النطاق المستهدف (مثال: example.com): ").strip()
        if not domain:
            self.log_message("الرجاء إدخال نطاق صالح", "ERROR")
            return
            
        self.results = []
        self.searching = True
        
        self.log_message(f"بدء البحث عن خوادم SQL في النطاق: {domain}")
        print("-" * 60)
        
        # تشغيل البحث
        results = self.scan_sql_servers(domain)
        self.results = results
        
        print("-" * 60)
        
        if results:
            self.log_message(f"✅ تم العثور على {len(results)} خادم SQL")
            
            # عرض النتائج
            print("\nنتائج البحث:")
            for i, result in enumerate(results, 1):
                print(f"\n{i}. النطاق: {result['domain']}")
                print(f"   العنوان: {result['ip']}:{result['port']}")
                print(f"   الخدمة: {result['service']}")
                print(f"   موقع إسرائيلي: {'نعم' if result['is_israeli'] else 'لا'}")
                print(f"   الوقت: {result['timestamp']}")
        else:
            self.log_message("❌ لم يتم العثور على خوادم SQL")
            
        self.searching = False
        
    def display_results(self):
        """عرض النتائج المحفوظة"""
        if not self.results:
            self.log_message("لا توجد نتائج لعرضها", "WARNING")
            return
            
        print("\n" + "=" * 60)
        print("                    النتائج المحفوظة")
        print("=" * 60)
        
        for i, result in enumerate(self.results, 1):
            print(f"\n{i}. النطاق: {result['domain']}")
            print(f"   العنوان: {result['ip']}:{result['port']}")
            print(f"   الخدمة: {result['service']}")
            print(f"   موقع إسرائيلي: {'نعم' if result['is_israeli'] else 'لا'}")
            print(f"   الوقت: {result['timestamp']}")
            
    def save_results(self):
        """حفظ النتائج في ملف JSON"""
        if not self.results:
            self.log_message("لا توجد نتائج لحفظها", "WARNING")
            return
            
        filename = f"sql_search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, ensure_ascii=False, indent=2)
                
            self.log_message(f"✅ تم حفظ النتائج في: {filename}")
            
        except Exception as e:
            self.log_message(f"خطأ في حفظ النتائج: {str(e)}", "ERROR")
            
    def show_info(self):
        """عرض معلومات الأداة"""
        info = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                    معلومات الأداة                            ║
    ╠═══════════════════════════════════════════════════════════════╣
    ║  الاسم: أداة بحث SQL المتقدمة                                ║
    ║  الإصدار: 1.0.0                                              ║
    ║  المبرمج: SayerLinux                                          ║
    ║  الموقع: https://github.com/SaudiLinux                        ║
    ║  البريد: SayerLinux1@gmail.com                                ║
    ║                                                               ║
    ║  المميزات:                                                    ║
    ║  • مسح خوادم SQL متعددة                                     ║
    ║  • تصفية المواقع الإسرائيلية                                ║
    ║  • حفظ النتائج في JSON                                      ║
    ║  • واجهة سطر أوامر سهلة                                    ║
    ╚═══════════════════════════════════════════════════════════════╝
        """
        print(info)
        
    def run(self):
        """تشغيل الأداة"""
        self.print_banner()
        
        while True:
            self.print_menu()
            
            try:
                choice = input("\nاختر خياراً (1-5): ").strip()
                
                if choice == "1":
                    self.start_search()
                elif choice == "2":
                    self.display_results()
                elif choice == "3":
                    self.save_results()
                elif choice == "4":
                    self.show_info()
                elif choice == "5":
                    print("\nشكراً لاستخدامك أداة بحث SQL المتقدمة!")
                    break
                else:
                    self.log_message("الرجاء اختيار رقم من 1 إلى 5", "WARNING")
                    
            except KeyboardInterrupt:
                print("\n\nتم إيقاف الأداة بواسطة المستخدم.")
                break
            except Exception as e:
                self.log_message(f"خطأ غير متوقع: {str(e)}", "ERROR")

if __name__ == "__main__":
    # تمكين الألوان في Windows
    if os.name == 'nt':
        os.system('color')
        
    tool = CLISQLSearchTool()
    tool.run()