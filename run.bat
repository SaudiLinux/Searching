@echo off
title أداة بحث SQL المتقدمة - SQL Search Tool
color 0A
echo.
echo ================================================
echo    أداة بحث SQL المتقدمة - Advanced SQL Search Tool
echo ================================================
echo    المبرمج: SayerLinux
echo    الموقع: https://github.com/SaudiLinux
echo    البريد: SayerLinux1@gmail.com
echo ================================================
echo.

:: التحقق من تثبيت Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] لم يتم العثور على Python
    echo [!] الرجاء تثبيت Python من الموقع الرسمي
    pause
    exit /b
)

:: تثبيت المتطلبات إذا لم تكن موجودة
echo [+] جاري تثبيت المتطلبات...
pip install -r requirements.txt

:: تشغيل الأداة
echo [+] جاري تشغيل الأداة...
python main.py

echo.
echo ================================================
echo    تم إغلاق الأداة بنجاح
pause