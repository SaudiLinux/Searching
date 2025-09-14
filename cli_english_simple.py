#!/usr/bin/env python3
"""
Command Line Interface - Israeli Cyber Security Tools Suite
Simple English Interface Version
"""

import argparse
import sys
import os
import json
import time
from datetime import datetime

def display_banner():
    """Display main banner"""
    print("\n" + "="*80)
    print("🚨 Advanced Israeli Cyber Security Tools Suite - CLI 🚨")
    print("Comprehensive Security Testing for Israeli Sites")
    print("="*80)

def display_tools():
    """Display available tools"""
    print("\n🛠️ Available Tools:")
    print("1. Display Israeli Infected Sites")
    print("2. Vulnerability Testing & Exploitation") 
    print("3. Advanced Google Dorking")
    print("4. Vulnerability Links Viewer")
    print("5. SQL Injection Scanning")
    print("6. Quick Display Infected Sites")
    print("7. Install/Update Tools")
    print("8. Exit")

def run_tool(tool_num):
    """Run specific tool"""
    tools = {
        1: "python infected_sites_report.py",
        2: "python demo_search.py",
        3: "python google_dork_tool.py", 
        4: "python vulnerability_links_viewer.py",
        5: "python sqli_scanner_tool.py",
        6: "python show_infected_sites.py",
        7: "python install.py"
    }
    
    if tool_num in tools:
        print(f"\n🎯 Running Tool {tool_num}...")
        result = os.system(tools[tool_num])
        if result != 0:
            print(f"⚠️ Tool {tool_num} encountered an issue or file not found")
    else:
        print("❌ Invalid tool number")

def run_interactive():
    """Run interactive mode"""
    display_banner()
    
    while True:
        display_tools()
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '8' or choice.lower() in ['exit', 'quit', 'q']:
                print("\n👋 Thank you for using Israeli Cyber Security Tools!")
                break
            elif choice.isdigit() and 1 <= int(choice) <= 7:
                run_tool(int(choice))
                input("\nPress Enter to continue...")
            else:
                print("❌ Please enter a valid number (1-8)")
                
        except KeyboardInterrupt:
            print("\n\n⚡ Program stopped by user")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Israeli Cyber Security Tools CLI')
    parser.add_argument('--tool', type=int, choices=range(1, 8), help='Tool number to run')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    
    args = parser.parse_args()
    
    if args.interactive or len(sys.argv) == 1:
        run_interactive()
    elif args.tool:
        run_tool(args.tool)
    else:
        run_interactive()

if __name__ == "__main__":
    main()