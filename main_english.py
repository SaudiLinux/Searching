#!/usr/bin/env python3
"""
Main Program - Advanced Israeli Cyber Security Tools Suite
English Interface Version
"""

import os
import sys
import platform
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Add required libraries path
sys.path.insert(0, str(Path(__file__).parent))

# Import new tools
from tools.infected_links_report import InfectedLinksReport
from tools.exploit_tool import ExploitTool
from tools.google_dork_tool import GoogleDorkTool
from tools.vulnerability_links_viewer import VulnerabilityLinksViewer
from tools.sqli_scanner_tool import SQLiScannerTool
from tools.show_infected_sites import ShowInfectedSites
from tools.installer import Installer

console = Console()

class IsraeliCyberSecuritySuiteEnglish:
    """Main class for Israeli Cyber Security Tools Suite - English Version"""
    
    def __init__(self):
        self.console = Console()
        self.tools = {
            1: {"name": "Display Israeli Infected Sites", "tool": InfectedLinksReport},
            2: {"name": "Security Vulnerability Testing & Exploitation", "tool": ExploitTool},
            3: {"name": "Advanced Google Dorking Search", "tool": GoogleDorkTool},
            4: {"name": "Vulnerability Links with Test URLs", "tool": VulnerabilityLinksViewer},
            5: {"name": "SQL Injection Scanning for Israeli Sites", "tool": SQLiScannerTool},
            6: {"name": "Quick Display of Infected Sites", "tool": ShowInfectedSites},
            7: {"name": "Install/Update Tools", "tool": Installer},
        }
    
    def display_banner(self):
        """Display main banner"""
        banner = """
[bold red]╔═══════════════════════════════════════════════════════════════════════════════╗[/bold red]
[bold red]║[/bold red]     [bold yellow]🚨 Advanced Israeli Cyber Security Tools Suite 🚨[/bold yellow]      [bold red]║[/bold red]
[bold red]║[/bold red]        [bold cyan]Comprehensive Security Testing for Israeli Sites[/bold cyan]        [bold red]║[/bold red]
[bold red]║[/bold red]                   [bold green]English Interface Version[/bold green]                    [bold red]║[/bold red]
[bold red]╚═══════════════════════════════════════════════════════════════════════════════╝[/bold red]
        """
        self.console.print(Panel(banner, style="bold red"))
    
    def display_menu(self):
        """Display tools menu"""
        table = Table(title="📋 Available Tools", show_header=True, header_style="bold magenta")
        table.add_column("Number", style="cyan", width=8)
        table.add_column("Tool Name", style="green", width=50)
        table.add_column("Status", style="yellow", width=10)
        
        for key, tool_info in self.tools.items():
            table.add_row(str(key), tool_info["name"], "✅ Ready")
        
        table.add_row("8", "Exit", "🚪")
        
        self.console.print(table)
    
    def get_user_choice(self):
        """Get user choice"""
        try:
            choice = self.console.input("\n[bold cyan]Select tool (1-8): [/bold cyan]").strip()
            return int(choice)
        except ValueError:
            return None
    
    def run_tool(self, choice):
        """Run selected tool"""
        if choice == 8:
            self.console.print("\n[bold green]👋 Thank you for using Israeli Cyber Security Tools![/bold green]")
            return False
        
        if choice in self.tools:
            tool_info = self.tools[choice]
            self.console.print(f"\n[bold yellow]🎯 Running: {tool_info['name']}...[/bold yellow]")
            
            try:
                tool_instance = tool_info["tool"]()
                if hasattr(tool_instance, 'run'):
                    tool_instance.run()
                else:
                    tool_instance()
                    
            except Exception as e:
                self.console.print(f"\n[bold red]❌ Error running tool: {str(e)}[/bold red]")
                
        else:
            self.console.print("\n[bold red]❌ Invalid choice. Please select a number from 1 to 8.[/bold red]")
        
        return True
    
    def check_system_requirements(self):
        """Check system requirements"""
        self.console.print("\n[bold blue]🔍 Checking system requirements...[/bold blue]")
        
        # Check Python version
        if sys.version_info < (3, 7):
            self.console.print("[bold red]❌ Python 3.7+ required[/bold red]")
            return False
        
        # Check required files
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
            self.console.print(f"\n[bold yellow]⚠️  Missing files: {', '.join(missing_files)}[/bold yellow]")
            self.console.print("[bold cyan]💡 Use tool installer (option 7) to install required files[/bold cyan]")
        
        return True
    
    def run(self):
        """Run main program"""
        try:
            self.display_banner()
            
            if not self.check_system_requirements():
                return
            
            while True:
                self.display_menu()
                choice = self.get_user_choice()
                
                if choice is None:
                    self.console.print("\n[bold red]❌ Please enter a valid number[/bold red]")
                    continue
                
                if not self.run_tool(choice):
                    break
                
                # Show menu again after running
                self.console.print("\n[bold cyan]Press Enter to continue...[/bold cyan]")
                input()
                
        except KeyboardInterrupt:
            self.console.print("\n\n[bold yellow]⚡ Program stopped by user[/bold yellow]")
        except Exception as e:
            self.console.print(f"\n[bold red]❌ Unexpected error: {str(e)}[/bold red]")

def main():
    """Main function"""
    if len(sys.argv) > 1:
        # Command line mode
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            console.print("""
[bold green]Usage:[/bold green]
    python main_english.py           : Run interactive interface
    python main_english.py --help    : Show this help
    python main_english.py --version : Show version
            """)
        elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
            console.print("[bold green]Israeli Cyber Security Tools Suite - Version 2.0.0[/bold green]")
        else:
            console.print(f"[bold red]❌ Unknown option: {sys.argv[1]}[/bold red]")
    else:
        # Run interactive interface
        suite = IsraeliCyberSecuritySuiteEnglish()
        suite.run()

if __name__ == "__main__":
    main()