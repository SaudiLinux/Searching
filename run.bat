@echo off
chcp 65001 >nul
cls
title أدوات الأمن السيبراني الإسرائيلية - Israeli Cyber Security Tools

color 0A
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                🚨 أدوات الأمن السيبراني الإسرائيلية           ║
echo ║                  Israeli Cyber Security Tools Suite          ║
echo ║                        أداة التشغيل العربية                ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 📋 الأدوات المتوفرة:
echo.
echo 1️⃣  عرض المواقع الإسرائيلية المصابة
echo 2️⃣  اختبار واستغلال الثغرات الأمنية
echo 3️⃣  البحث المتقدم باستخدام Google Dorks
echo 4️⃣  عرض روابط الثغرات مع روابط اختبار
echo 5️⃣  فحص SQL Injection للمواقع الإسرائيلية
echo 6️⃣  عرض سريع للمواقع المصابة
echo 7️⃣  تثبيت/تحديث الأدوات
echo 8️⃣  فتح الدليل الإرشادي
echo 9️⃣  الخروج
echo.

:menu
set /p choice=اختر رقم الأداة (1-9): 

if "%choice%"=="1" (
    echo.
    echo 🎯 تشغيل عرض المواقع الإسرائيلية المصابة...
    python infected_links_report.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo ⚡ تشغيل اختبار الثغرات الأمنية...
    python exploit_tool.py
    pause
    goto menu
)

if "%choice%"=="3" (
    echo.
    echo 🔍 تشغيل البحث المتقدم...
    python google_dork_tool.py
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo 🚨 تشغيل عرض روابط الثغرات...
    python vulnerability_links_viewer.py
    pause
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo 🔍 تشغيل فحص SQL Injection...
    echo.
    echo 💡 الخيارات المتوفرة:
    echo 1. وضع تلقائي (مستحسن)
    echo 2. وضع تفاعلي
    echo 3. الرجوع للقائمة الرئيسية
    echo.
    set /p sql_choice=اختر وضع الفحص (1-3): 
    
    if "%sql_choice%"=="1" (
        python sqli_scanner_tool.py --auto
    ) else if "%sql_choice%"=="2" (
        python sqli_scanner_tool.py
    ) else (
        goto menu
    )
    pause
    goto menu
)

if "%choice%"=="6" (
    echo.
    echo 🚨 تشغيل عرض سريع للمواقع المصابة...
    python show_infected_sites.py
    pause
    goto menu
)

if "%choice%"=="7" (
    echo.
    echo 🔄 تشغيل أداة التثبيت/التحديث...
    python install.py --full
    pause
    goto menu
)

if "%choice%"=="8" (
    echo.
    echo 📖 فتح الدليل الإرشادي...
    if exist "تشغيل_الادوات_بالتفصيل.md" (
        start "" "تشغيل_الادوات_بالتفصيل.md"
    ) else (
        start "" README.txt
    )
    goto menu
)

if "%choice%"=="9" (
    echo.
    echo 👋 شكراً لاستخدامك أدوات الأمن السيبراني الإسرائيلية!
    timeout /t 2 >nul
    exit
)

echo.
echo ❌ خيار غير صالح، يرجى اختيار رقم من 1 إلى 9
echo.
goto menu