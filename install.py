#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة تثبيت متقدمة لحزمة أدوات الأمن السيبراني للمواقع الإسرائيلية
Advanced Installation Tool for Israeli Cyber Security Tools Suite
"""

import os
import sys
import subprocess
import platform
import time
import colorama
from colorama import Fore, Back, Style

def print_banner():
    """طباعة شعار الترحيب"""
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                🚨 أدوات الأمن السيبراني الإسرائيلية           ║
    ║                  Israeli Cyber Security Tools Suite          ║
    ║                        أداة التثبيت المتقدمة               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def check_python_version():
    """التحقق من إصدار Python"""
    print(Fore.YELLOW + "🔍 التحقق من إصدار Python..." + Style.RESET_ALL)
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(Fore.RED + "❌ يتطلب Python 3.7+ للعمل" + Style.RESET_ALL)
        sys.exit(1)
    print(Fore.GREEN + f"✅ Python {version.major}.{version.minor}.{version.micro} متوافق" + Style.RESET_ALL)

def install_package(package):
    """تثبيت حزمة Python"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def install_requirements():
    """تثبيت جميع المتطلبات من ملف requirements.txt"""
    print(Fore.YELLOW + "📦 تثبيت المتطلبات..." + Style.RESET_ALL)
    
    if os.path.exists("requirements.txt"):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print(Fore.GREEN + "✅ تم تثبيت جميع المتطلبات بنجاح" + Style.RESET_ALL)
            return True
        except subprocess.CalledProcessError:
            print(Fore.RED + "❌ فشل تثبيت المتطلبات" + Style.RESET_ALL)
            return False
    else:
        print(Fore.RED + "❌ ملف requirements.txt غير موجود" + Style.RESET_ALL)
        return False

def check_tools_availability():
    """التحقق من توفر جميع الأدوات"""
    tools = [
        "infected_links_report.py",
        "exploit_tool.py", 
        "google_dork_tool.py",
        "vulnerability_links_viewer.py",
        "sqli_scanner_tool.py",
        "show_infected_sites.py",
        "sqli_payloads_wordlist.txt"
    ]
    
    print(Fore.YELLOW + "🔍 التحقق من توفر الأدوات..." + Style.RESET_ALL)
    
    missing_tools = []
    for tool in tools:
        if os.path.exists(tool):
            print(Fore.GREEN + f"✅ {tool}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"❌ {tool} مفقود" + Style.RESET_ALL)
            missing_tools.append(tool)
    
    return len(missing_tools) == 0

def create_directories():
    """إنشاء المجلدات المطلوبة"""
    directories = [
        "reports",
        "logs",
        "payloads",
        "exports"
    ]
    
    print(Fore.YELLOW + "📁 إنشاء المجلدات..." + Style.RESET_ALL)
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(Fore.GREEN + f"✅ تم إنشاء مجلد {directory}" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"📁 مجلد {directory} موجود بالفعل" + Style.RESET_ALL)

def setup_permissions():
    """إعداد الصلاحيات"""
    print(Fore.YELLOW + "🔐 إعداد الصلاحيات..." + Style.RESET_ALL)
    
    # جعل الملفات قابلة للتنفيذ (Unix/Linux)
    if platform.system() != "Windows":
        tools = [
            "infected_links_report.py",
            "exploit_tool.py",
            "google_dork_tool.py", 
            "vulnerability_links_viewer.py",
            "sqli_scanner_tool.py",
            "show_infected_sites.py"
        ]
        
        for tool in tools:
            if os.path.exists(tool):
                os.chmod(tool, 0o755)
                print(Fore.GREEN + f"✅ تم تعيين صلاحيات {tool}" + Style.RESET_ALL)

def test_installation():
    """اختبار التثبيت"""
    print(Fore.YELLOW + "🧪 اختبار التثبيت..." + Style.RESET_ALL)
    
    test_commands = [
        [sys.executable, "--version"],
        [sys.executable, "-m", "pip", "--version"]
    ]
    
    for command in test_commands:
        try:
            subprocess.check_call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(Fore.GREEN + f"✅ اختبار ناجح: {' '.join(command)}" + Style.RESET_ALL)
        except subprocess.CalledProcessError:
            print(Fore.RED + f"❌ اختبار فشل: {' '.join(command)}" + Style.RESET_ALL)

def display_menu():
    """عرض قائمة الخيارات"""
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                     خيارات التثبيت                          ║
    ╠═══════════════════════════════════════════════════════════════╣
    ║  1. تثبيت كامل (مستحسن)                                     ║
    ║  2. تثبيت المتطلبات فقط                                     ║
    ║  3. فحص الأدوات فقط                                         ║
    ║  4. إصلاح المشاكل                                           ║
    ║  5. إلغاء                                                   ║
    ╚═══════════════════════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def full_install():
    """تثبيت كامل"""
    print(Fore.GREEN + "🚀 بدء التثبيت الكامل..." + Style.RESET_ALL)
    
    check_python_version()
    
    if not install_requirements():
        print(Fore.RED + "❌ فشل تثبيت المتطلبات" + Style.RESET_ALL)
        return False
    
    create_directories()
    setup_permissions()
    
    if check_tools_availability():
        test_installation()
        print(Fore.GREEN + "✅ تم التثبيت بنجاح!" + Style.RESET_ALL)
        print(Fore.CYAN + "💡 استخدم run.bat أو run_english.bat للتشغيل" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + "❌ بعض الأدوات مفقودة" + Style.RESET_ALL)
        return False

def main():
    """الدالة الرئيسية"""
    colorama.init()
    print_banner()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--full":
            full_install()
        elif sys.argv[1] == "--check":
            check_tools_availability()
        elif sys.argv[1] == "--fix":
            install_requirements()
    else:
        display_menu()
        choice = input(Fore.YELLOW + "اختر خيار (1-5): " + Style.RESET_ALL)
        
        if choice == "1":
            full_install()
        elif choice == "2":
            install_requirements()
        elif choice == "3":
            check_tools_availability()
        elif choice == "4":
            install_requirements()
        else:
            print(Fore.CYAN + "تم الإلغاء" + Style.RESET_ALL)

if __name__ == "__main__":
    main()