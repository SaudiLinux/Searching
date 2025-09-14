#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
البرنامج الرئيسي - مجموعة أدوات الأمن السيبراني الإسرائيلية المتقدمة
Main Program - Advanced Israeli Cyber Security Tools Suite
"""

import os
import sys
import platform
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.layout import Layout
from rich.align import Align

# إضافة مسار المكتبات المطلوبة
sys.path.insert(0, str(Path(__file__).parent))

# استيراد الأدوات الجديدة
from tools.infected_links_report import InfectedLinksReport
from tools.exploit_tool import ExploitTool
from tools.google_dork_tool import GoogleDorkTool
from tools.vulnerability_links_viewer import VulnerabilityLinksViewer
from tools.sqli_scanner_tool import SQLiScannerTool
from tools.show_infected_sites import ShowInfectedSites
from tools.installer import Installer

console = Console()

class IsraeliCyberSecuritySuite:
    """الفئة الرئيسية لمجموعة أدوات الأمن السيبراني الإسرائيلية"""
    
    def __init__(self):
        self.console = Console()
        self.tools = {
            1: {"name": "عرض المواقع الإسرائيلية المصابة", "tool": InfectedLinksReport},
            2: {"name": "اختبار الثغرات الأمنية والاستغلال", "tool": ExploitTool},
            3: {"name": "أداة بحث Google المتقدمة", "tool": GoogleDorkTool},
            4: {"name": "عرض روابط الثغرات مع URLs للاختبار", "tool": VulnerabilityLinksViewer},
            5: {"name": "فحص SQL Injection للمواقع الإسرائيلية", "tool": SQLiScannerTool},
            6: {"name": "عرض سريع للمواقع المصابة", "tool": ShowInfectedSites},
            7: {"name": "تثبيت/تحديث الأدوات", "tool": Installer},
        }
    
    def display_banner(self):
        """عرض البانر الرئيسي"""
        banner = """
[bold red]╔═══════════════════════════════════════════════════════════════════════════════╗[/bold red]
[bold red]║[/bold red]     [bold yellow]🚨 مجموعة أدوات الأمن السيبراني الإسرائيلية المتقدمة 🚨[/bold yellow]      [bold red]║[/bold red]
[bold red]║[/bold red]        [bold cyan]Advanced Israeli Cyber Security Tools Suite[/bold cyan]         [bold red]║[/bold red]
[bold red]║[/bold red]              [bold green]للاختبار الأمني الشامل للمواقع الإسرائيلية[/bold green]               [bold red]║[/bold red]
[bold red]╚═══════════════════════════════════════════════════════════════════════════════╝[/bold red]
        """
        self.console.print(Panel(banner, style="bold red"))
    
    def display_menu(self):
        """عرض قائمة الأدوات"""
        table = Table(title="📋 قائمة الأدوات المتاحة", show_header=True, header_style="bold magenta")
        table.add_column("الرقم", style="cyan", width=6)
        table.add_column("اسم الأداة", style="green", width=50)
        table.add_column("الحالة", style="yellow", width=10)
        
        for key, tool_info in self.tools.items():
            table.add_row(str(key), tool_info["name"], "✅ جاهز")
        
        table.add_row("8", "الخروج", "🚪")
        
        self.console.print(table)
    
    def get_user_choice(self):
        """الحصول على اختيار المستخدم"""
        try:
            choice = self.console.input("\n[bold cyan]اختر أداة (1-8): [/bold cyan]").strip()
            return int(choice)
        except ValueError:
            return None
    
    def run_tool(self, choice):
        """تشغيل الأداة المختارة"""
        if choice == 8:
            self.console.print("\n[bold green]👋 شكراً لاستخدام مجموعة أدوات الأمن السيبراني الإسرائيلية![/bold green]")
            return False
        
        if choice in self.tools:
            tool_info = self.tools[choice]
            self.console.print(f"\n[bold yellow]🎯 تشغيل: {tool_info['name']}...[/bold yellow]")
            
            try:
                tool_instance = tool_info["tool"]()
                if hasattr(tool_instance, 'run'):
                    tool_instance.run()
                else:
                    tool_instance()
                    
            except Exception as e:
                self.console.print(f"\n[bold red]❌ خطأ في تشغيل الأداة: {str(e)}[/bold red]")
                
        else:
            self.console.print("\n[bold red]❌ اختيار غير صالح. يرجى اختيار رقم من 1 إلى 8.[/bold red]")
        
        return True
    
    def check_system_requirements(self):
        """التحقق من متطلبات النظام"""
        self.console.print("\n[bold blue]🔍 فحص متطلبات النظام...[/bold blue]")
        
        # فحص إصدار Python
        if sys.version_info < (3, 7):
            self.console.print("[bold red]❌ يتطلب Python 3.7 أو أعلى[/bold red]")
            return False
        
        # فحص الملفات المطلوبة
        required_files = [
            'requirements.txt',
            'config.json',
            'sqli_payloads_wordlist.txt'
        ]
        
        missing_files = []
        for file in required_files:
            if not Path(file).exists():
                missing_files.append(file)
        
        if missing_files:
            self.console.print(f"\n[bold yellow]⚠️  ملفات مفقودة: {', '.join(missing_files)}[/bold yellow]")
            self.console.print("[bold cyan]💡 استخدم أداة التثبيت (رقم 7) لتثبيت الملفات المطلوبة[/bold cyan]")
        
        return True
    
    def run(self):
        """تشغيل البرنامج الرئيسي"""
        try:
            self.display_banner()
            
            if not self.check_system_requirements():
                return
            
            while True:
                self.display_menu()
                choice = self.get_user_choice()
                
                if choice is None:
                    self.console.print("\n[bold red]❌ يرجى إدخال رقم صحيح[/bold red]")
                    continue
                
                if not self.run_tool(choice):
                    break
                
                # إعادة عرض القائمة بعد التشغيل
                self.console.print("\n[bold cyan]اضغط Enter للمتابعة...[/bold cyan]")
                input()
                self.console.clear()
                
        except KeyboardInterrupt:
            self.console.print("\n\n[bold yellow]⚡ تم إيقاف البرنامج بواسطة المستخدم[/bold yellow]")
        except Exception as e:
            self.console.print(f"\n[bold red]❌ خطأ غير متوقع: {str(e)}[/bold red]")

def main():
    """الدالة الرئيسية للبرنامج"""
    if len(sys.argv) > 1:
        # وضع سطر الأوامر
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            console.print("""
[bold green]استخدام:[/bold green]
    python main.py           : تشغيل الواجهة التفاعلية
    python main.py --help    : عرض هذه المساعدة
    python main.py --version : عرض الإصدار
            """)
        elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
            console.print("[bold green]مجموعة أدوات الأمن السيبراني الإسرائيلية - الإصدار 2.0.0[/bold green]")
        else:
            console.print(f"[bold red]❌ خيار غير معروف: {sys.argv[1]}[/bold red]")
    else:
        # تشغيل الواجهة التفاعلية
        suite = IsraeliCyberSecuritySuite()
        suite.run()

if __name__ == "__main__":
    main()