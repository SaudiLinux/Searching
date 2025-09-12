@echo off
title Advanced SQL Search Tool - English Version
color 0A
echo.
echo ╔══════════════════════════════════════════════════════════════════════════════╗
echo ║                    Advanced SQL Search Tool - English Version                ║
echo ║                          Developed by: SayerLinux                            ║
echo ║                    GitHub: https://github.com/SaudiLinux                      ║
echo ║                    Email: SayerLinux1@gmail.com                            ║
echo ╚══════════════════════════════════════════════════════════════════════════════╝
echo.

REM Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Starting Advanced SQL Search Tool...
echo.
python cli_english.py

echo.
echo Tool execution complete.
echo Press any key to exit...
pause >nul