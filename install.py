#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكربت تثبيت أداة بحث SQL المتقدمة
"""

import subprocess
import sys
import os

def install_package(package):
    """تثبيت حزمة Python"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ تم تثبيت {package}")
    except subprocess.CalledProcessError as e:
        print(f"✗ فشل تثبيت {package}: {e}")
        return False
    return True

def check_python_version():
    """التحقق من إصدار Python"""
    if sys.version_info < (3, 7):
        print("✗ يتطلب Python 3.7 أو أحدث")
        return False
    print(f"✓ Python {sys.version} متوافق")
    return True

def main():
    """الدالة الرئيسية للتثبيت"""
    print("=" * 60)
    print("    تثبيت أداة بحث SQL المتقدمة")
    print("=" * 60)
    print("المبرمج: SayerLinux")
    print("الموقع: https://github.com/SaudiLinux")
    print("البريد: SayerLinux1@gmail.com")
    print("=" * 60)
    print()
    
    # التحقق من Python
    if not check_python_version():
        sys.exit(1)
    
    # قائمة المتطلبات
    requirements = [
        "Pillow>=9.0.0",
        "mysql-connector-python>=8.0.0",
        "psycopg2-binary>=2.9.0",
        "requests>=2.28.0"
    ]
    
    print("جاري تثبيت المتطلبات...")
    print()
    
    failed_packages = []
    for package in requirements:
        if not install_package(package):
            failed_packages.append(package)
    
    if failed_packages:
        print()
        print("⚠️  بعض الحزم فشلت في التثبيت:")
        for package in failed_packages:
            print(f"   - {package}")
        print()
        print("يمكنك تثبيتها يدوياً باستخدام:")
        for package in failed_packages:
            print(f"   pip install {package}")
    else:
        print()
        print("✅ تم تثبيت جميع المتطلبات بنجاح!")
        print("يمكنك الآن تشغيل الأداة باستخدام: python main.py")

if __name__ == "__main__":
    main()