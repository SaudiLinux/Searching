#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced SQL Search Tool - English Version
Developed by: SayerLinux
Website: https://github.com/SaudiLinux
Email: SayerLinux1@gmail.com
"""

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog
except ImportError:
    print("Error: tkinter not found")
    print("To install tkinter on Windows: ensure Python is installed with Tcl/Tk option")
    print("To install tkinter on Ubuntu/Debian: sudo apt-get install python3-tk")
    print("To install tkinter on CentOS/RHEL: sudo yum install python3-tkinter")
    sys.exit(1)

import socket
import threading
import json
import os
import sys
from datetime import datetime
try:
    from PIL import Image, ImageGrab
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("Warning: Pillow not available, screenshot feature will be disabled")

class AdvancedSQLSearchTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced SQL Search Tool - SayerLinux")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1e1e1e")
        self.root.iconbitmap(default="logo.ico")
        
        # Initialize variables
        self.results = []
        self.israeli_sites = []
        self.searching = False
        
        # Create widgets
        self.create_widgets()
        self.load_israeli_domains()
        
    def create_widgets(self):
        # Header frame with logo
        header_frame = tk.Frame(self.root, bg="#2d2d2d", height=80)
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Tool title
        title_label = tk.Label(header_frame, text="Advanced SQL Search Tool", 
                              font=("Arial", 24, "bold"), fg="#00ff00", bg="#2d2d2d")
        title_label.pack(pady=10)
        
        # Developer info
        info_frame = tk.Frame(self.root, bg="#1e1e1e")
        info_frame.pack(fill=tk.X, padx=10, pady=5)
        
        info_text = "Developer: SayerLinux | GitHub: https://github.com/SaudiLinux | Email: SayerLinux1@gmail.com"
        info_label = tk.Label(info_frame, text=info_text, font=("Arial", 11), 
                            fg="#ffffff", bg="#1e1e1e")
        info_label.pack()
        
        # Input frame
        input_frame = tk.LabelFrame(self.root, text="Search Configuration", 
                                  font=("Arial", 12, "bold"), fg="#00ff00", bg="#1e1e1e")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Domain input
        tk.Label(input_frame, text="Target Domain:", fg="#ffffff", bg="#1e1e1e").grid(row=0, column=0, padx=5, pady=5)
        self.domain_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.domain_entry.grid(row=0, column=1, padx=5, pady=5)
        self.domain_entry.insert(0, "example.com")
        
        # Port range
        tk.Label(input_frame, text="Port Range:", fg="#ffffff", bg="#1e1e1e").grid(row=0, column=2, padx=5, pady=5)
        self.port_start = tk.Entry(input_frame, width=8, font=("Arial", 12))
        self.port_start.grid(row=0, column=3, padx=2, pady=5)
        self.port_start.insert(0, "3300")
        
        tk.Label(input_frame, text="to", fg="#ffffff", bg="#1e1e1e").grid(row=0, column=4, padx=2)
        self.port_end = tk.Entry(input_frame, width=8, font=("Arial", 12))
        self.port_end.grid(row=0, column=5, padx=2, pady=5)
        self.port_end.insert(0, "3310")
        
        # Thread count
        tk.Label(input_frame, text="Threads:", fg="#ffffff", bg="#1e1e1e").grid(row=1, column=0, padx=5, pady=5)
        self.thread_count = tk.Entry(input_frame, width=8, font=("Arial", 12))
        self.thread_count.grid(row=1, column=1, padx=5, pady=5)
        self.thread_count.insert(0, "10")
        
        # Timeout
        tk.Label(input_frame, text="Timeout (s):", fg="#ffffff", bg="#1e1e1e").grid(row=1, column=2, padx=5, pady=5)
        self.timeout = tk.Entry(input_frame, width=8, font=("Arial", 12))
        self.timeout.grid(row=1, column=3, padx=5, pady=5)
        self.timeout.insert(0, "3")
        
        # Button frame
        button_frame = tk.Frame(input_frame, bg="#1e1e1e")
        button_frame.grid(row=2, column=0, columnspan=6, pady=10)
        
        self.search_button = tk.Button(button_frame, text="Start Search", 
                                     command=self.start_search,
                                     bg="#00ff00", fg="black", font=("Arial", 12, "bold"),
                                     width=15)
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(button_frame, text="Stop Search", 
                                   command=self.stop_search,
                                   bg="#ff0000", fg="white", font=("Arial", 12, "bold"),
                                   width=15, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.screenshot_button = tk.Button(button_frame, text="Screenshot", 
                                       command=self.take_screenshot,
                                       bg="#0080ff", fg="white", font=("Arial", 12, "bold"),
                                       width=15)
        self.screenshot_button.pack(side=tk.LEFT, padx=5)
        
        self.save_button = tk.Button(button_frame, text="Save Results", 
                                   command=self.save_results,
                                   bg="#ff8800", fg="white", font=("Arial", 12, "bold"),
                                   width=15)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(button_frame, text="Clear Results", 
                                    command=self.clear_results,
                                    bg="#800080", fg="white", font=("Arial", 12, "bold"),
                                    width=15)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        # Results frame
        result_frame = tk.LabelFrame(self.root, text="Search Results", 
                                   font=("Arial", 12, "bold"), fg="#00ff00", bg="#1e1e1e")
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(result_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, padx=5, pady=5)
        
        # Results text area
        self.result_text = tk.Text(result_frame, height=20, width=80, 
                                 font=("Courier", 10), bg="#000000", fg="#00ff00")
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, 
                                command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready to search...", 
                                 bd=1, relief=tk.SUNKEN, anchor=tk.W,
                                 bg="#2d2d2d", fg="#ffffff")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def load_israeli_domains(self):
        """Load Israeli domains database"""
        self.israeli_domains = [
            '.il', '.co.il', '.org.il', '.gov.il', '.ac.il', '.muni.il',
            '.idf.il', '.mod.gov.il', '.mfa.gov.il', '.knesset.gov.il',
            'jpost.com', 'ynet.co.il', 'haaretz.co.il', 'timesofisrael.com',
            'israelhayom.co.il', 'walla.co.il', 'mako.co.il', 'n12.co.il',
            'jpost.co.il', 'globes.co.il', 'calcalist.co.il',
            'mako.co.il', 'reshet.tv', 'kan.org.il'
        ]
        
    def log_message(self, message, level="INFO"):
        """Log messages to the interface"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        levels = {
            "INFO": "[INFO]",
            "ERROR": "[ERROR]",
            "SUCCESS": "[SUCCESS]",
            "WARNING": "[WARNING]"
        }
        
        prefix = levels.get(level, "[INFO]")
        formatted_message = f"[{timestamp}] {prefix} {message}\n"
        
        # Color coding for different levels
        if level == "ERROR":
            self.result_text.tag_config("error", foreground="#ff0000")
            self.result_text.insert(tk.END, formatted_message, "error")
        elif level == "SUCCESS":
            self.result_text.tag_config("success", foreground="#00ff00")
            self.result_text.insert(tk.END, formatted_message, "success")
        elif level == "WARNING":
            self.result_text.tag_config("warning", foreground="#ffff00")
            self.result_text.insert(tk.END, formatted_message, "warning")
        else:
            self.result_text.insert(tk.END, formatted_message)
            
        self.result_text.see(tk.END)
        self.root.update_idletasks()
        
    def is_israeli_site(self, url):
        """Check if site is Israeli"""
        url_lower = url.lower()
        return any(domain.lower() in url_lower for domain in self.israeli_domains)
        
    def scan_port(self, ip, port, results, lock):
        """Scan individual port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(float(self.timeout.get()))
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                service = self.get_service_name(port)
                with lock:
                    results.append({
                        'domain': self.current_domain,
                        'ip': ip,
                        'port': port,
                        'service': service,
                        'is_israeli': self.is_israeli_site(self.current_domain),
                        'timestamp': datetime.now().isoformat()
                    })
                    self.log_message(f"Found {service} server on port {port}", "SUCCESS")
            
            sock.close()
            
        except Exception as e:
            pass
            
    def get_service_name(self, port):
        """Get service name by port"""
        services = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            993: "IMAPS",
            995: "POP3S",
            1433: "MSSQL",
            1521: "Oracle",
            3306: "MySQL",
            3307: "MySQL",
            5432: "PostgreSQL",
            6379: "Redis",
            27017: "MongoDB",
            27018: "MongoDB",
            27019: "MongoDB"
        }
        return services.get(port, f"Port {port}")
        
    def scan_sql_servers(self, domain):
        """Scan for SQL servers in target domain"""
        try:
            # Resolve domain to IP
            ip = socket.gethostbyname(domain)
            self.log_message(f"Resolved {domain} to {ip}")
            
            # Get port range
            start_port = int(self.port_start.get())
            end_port = int(self.port_end.get())
            max_threads = int(self.thread_count.get())
            
            self.log_message(f"Scanning ports {start_port}-{end_port} with {max_threads} threads")
            
            results = []
            lock = threading.Lock()
            threads = []
            
            # Scan ports using threads
            for port in range(start_port, end_port + 1):
                if not self.searching:
                    break
                    
                while threading.active_count() > max_threads + 10:
                    time.sleep(0.1)
                    
                thread = threading.Thread(
                    target=self.scan_port,
                    args=(ip, port, results, lock)
                )
                thread.daemon = True
                thread.start()
                threads.append(thread)
                
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
                
            return results
            
        except Exception as e:
            self.log_message(f"Error scanning {domain}: {str(e)}", "ERROR")
            return []
            
    def start_search(self):
        """Start search process"""
        domain = self.domain_entry.get().strip()
        if not domain:
            messagebox.showerror("Error", "Please enter a valid domain")
            return
            
        # Validate inputs
        try:
            start_port = int(self.port_start.get())
            end_port = int(self.port_end.get())
            max_threads = int(self.thread_count.get())
            timeout = float(self.timeout.get())
            
            if start_port > end_port:
                messagebox.showerror("Error", "Start port must be less than end port")
                return
                
            if max_threads < 1 or max_threads > 100:
                messagebox.showerror("Error", "Thread count must be between 1 and 100")
                return
                
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return
            
        self.search_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.results = []
        self.current_domain = domain
        self.result_text.delete(1.0, tk.END)
        
        self.searching = True
        self.progress.start()
        
        # Start search in separate thread
        search_thread = threading.Thread(target=self.search_worker, args=(domain,))
        search_thread.daemon = True
        search_thread.start()
        
    def search_worker(self, domain):
        """Search worker thread"""
        try:
            self.status_bar.config(text="Scanning...")
            self.log_message(f"Starting SQL server scan for: {domain}")
            
            results = self.scan_sql_servers(domain)
            self.results = results
            
            if results:
                self.log_message(f"✅ Scan complete! Found {len(results)} servers")
                
                # Display summary
                israeli_count = sum(1 for r in results if r['is_israeli'])
                self.log_message(f"Israeli sites found: {israeli_count}")
                
                # Display results
                self.result_text.insert(tk.END, "\n" + "="*80 + "\n")
                self.result_text.insert(tk.END, "                    SCAN RESULTS\n")
                self.result_text.insert(tk.END, "="*80 + "\n")
                
                for i, result in enumerate(results, 1):
                    self.result_text.insert(tk.END, f"\n{i}. Domain: {result['domain']}\n")
                    self.result_text.insert(tk.END, f"   IP: {result['ip']}:{result['port']}\n")
                    self.result_text.insert(tk.END, f"   Service: {result['service']}\n")
                    self.result_text.insert(tk.END, f"   Israeli Site: {'Yes' if result['is_israeli'] else 'No'}\n")
                    self.result_text.insert(tk.END, f"   Timestamp: {result['timestamp']}\n")
                    self.result_text.insert(tk.END, "-" * 40 + "\n")
                    
            else:
                self.log_message("❌ No SQL servers found")
                
        except Exception as e:
            self.log_message(f"Search error: {str(e)}", "ERROR")
        finally:
            self.searching = False
            self.progress.stop()
            self.search_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_bar.config(text="Scan complete")
            
    def stop_search(self):
        """Stop search process"""
        self.searching = False
        self.progress.stop()
        self.search_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_bar.config(text="Search stopped")
        self.log_message("Search stopped by user")
        
    def take_screenshot(self):
        """Take screenshot"""
        if not PIL_AVAILABLE:
            messagebox.showwarning("Warning", "Screenshot feature is not available")
            return
            
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            
            screenshot = ImageGrab.grab()
            screenshot.save(filename)
            
            self.log_message(f"Screenshot saved: {filename}")
            messagebox.showinfo("Success", f"Screenshot saved: {filename}")
            
        except Exception as e:
            self.log_message(f"Screenshot error: {str(e)}", "ERROR")
            
    def save_results(self):
        """Save results to JSON file"""
        if not self.results:
            messagebox.showwarning("Warning", "No results to save")
            return
            
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Save Results"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.results, f, ensure_ascii=False, indent=2)
                    
                self.log_message(f"Results saved to: {filename}")
                messagebox.showinfo("Success", "Results saved successfully")
                
            except Exception as e:
                self.log_message(f"Save error: {str(e)}", "ERROR")
                
    def clear_results(self):
        """Clear results"""
        self.results = []
        self.result_text.delete(1.0, tk.END)
        self.log_message("Results cleared")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedSQLSearchTool(root)
    root.mainloop()