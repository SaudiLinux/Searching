#!/usr/bin/env python3
"""
Command Line Interface - Israeli Cyber Security Tools Suite
English Interface Version
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

# Import tools directly from current directory
try:
    from infected_links_report import InfectedLinksReport
except ImportError:
    class InfectedLinksReport:
        def run_cli(self, args=None):
            print("Infected Links Report tool not available")
            return True

try:
    from exploit_tool import ExploitTool
except ImportError:
    class ExploitTool:
        def run_cli(self, args=None):
            print("Exploit Tool not available")
            return True

try:
    from google_dork_tool import GoogleDorkTool
except ImportError:
    class GoogleDorkTool:
        def run_cli(self, args=None):
            print("Google Dork Tool not available")
            return True

try:
    from vulnerability_links_viewer import VulnerabilityLinksViewer
except ImportError:
    class VulnerabilityLinksViewer:
        def run_cli(self, args=None):
            print("Vulnerability Links Viewer not available")
            return True

try:
    from sqli_scanner_tool import SQLiScannerTool
except ImportError:
    class SQLiScannerTool:
        def run_cli(self, args=None):
            print("SQLi Scanner Tool not available")
            return True

try:
    from show_infected_sites import ShowInfectedSites
except ImportError:
    class ShowInfectedSites:
        def run_cli(self, args=None):
            print("Show Infected Sites tool not available")
            return True

try:
    from install import Installer
except ImportError:
    class Installer:
        def run_cli(self, args=None):
            print("Installer tool not available")
            return True

console = Console()

class CLIEnglish:
    """Advanced CLI for Israeli Cyber Security Tools Suite - English"""
    
    def __init__(self):
        self.console = Console()
        self.tools = {
            'infected': {
                'name': 'Display Israeli Infected Sites',
                'tool': InfectedLinksReport,
                'description': 'Display list of Israeli infected sites with vulnerabilities'
            },
            'exploit': {
                'name': 'Vulnerability Testing & Exploitation',
                'tool': ExploitTool,
                'description': 'Test security vulnerabilities and exploitation'
            },
            'dork': {
                'name': 'Advanced Google Dorking',
                'tool': GoogleDorkTool,
                'description': 'Advanced Google dorking tools for finding vulnerabilities'
            },
            'vuln': {
                'name': 'Vulnerability Links',
                'tool': VulnerabilityLinksViewer,
                'description': 'Display vulnerability links with test URLs'
            },
            'sqli': {
                'name': 'SQL Injection Scanning',
                'tool': SQLiScannerTool,
                'description': 'Scan for SQL injection vulnerabilities in Israeli sites'
            },
            'show': {
                'name': 'Quick Display Infected Sites',
                'tool': ShowInfectedSites,
                'description': 'Quick display of infected sites'
            },
            'install': {
                'name': 'Install/Update Tools',
                'tool': Installer,
                'description': 'Install or update required tools'
            }
        }
    
    def display_banner(self):
        """Display main banner"""
        banner = """
[bold red]╔═══════════════════════════════════════════════════════════════════════════════╗[/bold red]
[bold red]║[/bold red]    [bold yellow]🚨 Advanced Israeli Cyber Security Tools Suite - CLI 🚨[/bold yellow]    [bold red]║[/bold red]
[bold red]║[/bold red]           [bold cyan]Comprehensive Security Testing for Israeli Sites[/bold cyan]           [bold red]║[/bold red]
[bold red]║[/bold red]                    [bold green]Command Line Interface[/bold green]                     [bold red]║[/bold red]
[bold red]╚═══════════════════════════════════════════════════════════════════════════════╝[/bold red]
        """
        self.console.print(Panel(banner, style="bold red"))
    
    def display_tools(self):
        """Display available tools"""
        table = Table(title="🛠️ Available Tools", show_header=True, header_style="bold magenta")
        table.add_column("Command", style="cyan", width=12)
        table.add_column("Name", style="green", width=30)
        table.add_column("Description", style="yellow", width=50)
        
        for cmd, info in self.tools.items():
            table.add_row(cmd, info['name'], info['description'])
        
        self.console.print(table)
    
    def run_tool(self, tool_name, args):
        """Run specific tool"""
        if tool_name not in self.tools:
            self.console.print(f"[bold red]❌ Tool not found: {tool_name}[/bold red]")
            return False
        
        tool_info = self.tools[tool_name]
        self.console.print(f"[bold yellow]🎯 Running: {tool_info['name']}...[/bold yellow]")
        
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=self.console,
            ) as progress:
                task = progress.add_task(f"Running {tool_info['name']}...", total=None)
                
                tool_instance = tool_info['tool']()
                if hasattr(tool_instance, 'run_cli'):
                    result = tool_instance.run_cli(args)
                elif hasattr(tool_instance, 'run'):
                    result = tool_instance.run()
                else:
                    tool_instance()
                    result = True
                
                progress.update(task, completed=True)
                
            self.console.print(f"[bold green]✅ Completed: {tool_info['name']}[/bold green]")
            return result
            
        except Exception as e:
            self.console.print(f"[bold red]❌ Error running tool: {str(e)}[/bold red]")
            return False
    
    def run_interactive(self):
        """Run interactive mode"""
        self.display_banner()
        self.display_tools()
        
        while True:
            try:
                self.console.print("\n[bold cyan]Enter tool name or 'help' for help or 'exit' to quit:[/bold cyan]")
                choice = input(" > ").strip().lower()
                
                if choice in ['exit', 'quit', 'q']:
                    self.console.print("\n[bold green]👋 Thank you for using Israeli Cyber Security Tools![/bold green]")
                    break
                elif choice in ['help', 'h']:
                    self.display_tools()
                elif choice in self.tools:
                    self.run_tool(choice, {})
                else:
                    self.console.print("[bold red]❌ Invalid command. Use 'help' to see available commands.[/bold red]")
                    
            except KeyboardInterrupt:
                self.console.print("\n\n[bold yellow]⚡ Program stopped by user[/bold yellow]")
                break
            except Exception as e:
                self.console.print(f"\n[bold red]❌ Unexpected error: {str(e)}[/bold red]")
    
    def run_batch(self, commands_file):
        """Run commands from file"""
        try:
            with open(commands_file, 'r', encoding='utf-8') as f:
                commands = json.load(f)
            
            self.console.print(f"[bold blue]🔄 Running batch commands from: {commands_file}[/bold blue]")
            
            for i, command in enumerate(commands, 1):
                self.console.print(f"\n[bold cyan]Command {i}/{len(commands)}:[/bold cyan]")
                
                tool_name = command.get('tool')
                args = command.get('args', {})
                
                if tool_name and tool_name in self.tools:
                    self.run_tool(tool_name, args)
                else:
                    self.console.print(f"[bold red]❌ Invalid command: {tool_name}[/bold red]")
                
                time.sleep(1)  # Delay between commands
            
            self.console.print("[bold green]✅ All batch commands completed[/bold green]")
            
        except Exception as e:
            self.console.print(f"[bold red]❌ Error running batch commands: {str(e)}[/bold red]")
    
    def generate_report(self, output_file):
        """Generate comprehensive report"""
        try:
            report = {
                'timestamp': datetime.now().isoformat(),
                'system_info': {
                    'python_version': sys.version,
                    'platform': sys.platform,
                    'cwd': str(Path.cwd())
                },
                'available_tools': list(self.tools.keys()),
                'report_generated': True
            }
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            self.console.print(f"[bold green]✅ Report generated: {output_file}[/bold green]")
            
        except Exception as e:
            self.console.print(f"[bold red]❌ Error generating report: {str(e)}[/bold red]")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Israeli Cyber Security Tools Suite - Command Line Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage Examples:
  python cli_english.py --interactive
  python cli_english.py --tool sqli --target example.com
  python cli_english.py --batch commands.json
  python cli_english.py --report report.json
        """
    )
    
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Run interactive mode')
    parser.add_argument('--tool', '-t', choices=list(CLIEnglish().tools.keys()),
                        help='Run specific tool')
    parser.add_argument('--batch', '-b', metavar='FILE',
                        help='Run commands from JSON file')
    parser.add_argument('--report', '-r', metavar='FILE',
                        help='Generate comprehensive report')
    parser.add_argument('--target', metavar='URL',
                        help='Target for testing')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List available tools')
    
    args = parser.parse_args()
    
    cli = CLIEnglish()
    
    try:
        if args.list:
            cli.display_tools()
        elif args.interactive:
            cli.run_interactive()
        elif args.tool:
            tool_args = {}
            if args.target:
                tool_args['target'] = args.target
            cli.run_tool(args.tool, tool_args)
        elif args.batch:
            cli.run_batch(args.batch)
        elif args.report:
            cli.generate_report(args.report)
        else:
            cli.display_banner()
            cli.display_tools()
            cli.run_interactive()
            
    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]⚡ Program stopped by user[/bold yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]❌ Unexpected error: {str(e)}[/bold red]")
        sys.exit(1)

if __name__ == "__main__":
    main()