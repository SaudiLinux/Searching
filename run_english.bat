@echo off
chcp 65001 >nul
cls
title Israeli Cyber Security Tools Suite - Advanced Security Testing

color 0B
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                🚨 Israeli Cyber Security Tools Suite          ║
echo ║                    Advanced Security Testing                ║
echo ║                        English Interface                    ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 📋 Available Tools:
echo.
echo 1️⃣  Display Israeli Infected Sites
echo 2️⃣  Security Vulnerability Testing & Exploitation
echo 3️⃣  Advanced Google Dorking Search
echo 4️⃣  Vulnerability Links with Test URLs
echo 5️⃣  SQL Injection Scanning for Israeli Sites
echo 6️⃣  Quick Display of Infected Sites
echo 7️⃣  Install/Update Tools
echo 8️⃣  Open Documentation
echo 9️⃣  Exit
echo.

:menu
set /p choice=Select tool number (1-9): 

if "%choice%"=="1" (
    echo.
    echo 🎯 Running Israeli Infected Sites Report...
    python infected_links_report.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo ⚡ Running Security Vulnerability Testing...
    python exploit_tool.py
    pause
    goto menu
)

if "%choice%"=="3" (
    echo.
    echo 🔍 Running Advanced Google Dorking Search...
    python google_dork_tool.py
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo 🚨 Running Vulnerability Links Viewer...
    python vulnerability_links_viewer.py
    pause
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo 🔍 Running SQL Injection Scanning...
    echo.
    echo 💡 Available Modes:
    echo 1. Automatic Mode (Recommended)
    echo 2. Interactive Mode
    echo 3. Back to Main Menu
    echo.
    set /p sql_choice=Select scanning mode (1-3): 
    
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
    echo 🚨 Running Quick Display of Infected Sites...
    python show_infected_sites.py
    pause
    goto menu
)

if "%choice%"=="7" (
    echo.
    echo 🔄 Running Install/Update Tools...
    python install.py --full
    pause
    goto menu
)

if "%choice%"=="8" (
    echo.
    echo 📖 Opening Documentation...
    if exist "README.txt" (
        start "" README.txt
    ) else if exist "تشغيل_الادوات_بالتفصيل.md" (
        start "" "تشغيل_الادوات_بالتفصيل.md"
    ) else (
        echo 📋 Documentation files not found
    )
    goto menu
)

if "%choice%"=="9" (
    echo.
    echo 👋 Thank you for using Israeli Cyber Security Tools!
    timeout /t 2 >nul
    exit
)

echo.
echo ❌ Invalid choice, please select a number from 1 to 9
echo.
goto menu