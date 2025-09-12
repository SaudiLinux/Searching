#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة بحث SQL المتقدمة - Advanced SQL Search Tool
تم تطويرها بواسطة: SayerLinux
الموقع: https://github.com/SaudiLinux
البريد: SayerLinux1@gmail.com
"""

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog
except ImportError:
    print("خطأ: لم يتم العثور على tkinter")
    print("لتثبيت tkinter على Windows: تأكد من تثبيت Python مع خيار Tcl/Tk")
    print("لتثبيت tkinter على Ubuntu/Debian: sudo apt-get install python3-tk")
    print("لتثبيت tkinter على CentOS/RHEL: sudo yum install python3-tkinter")
    sys.exit(1)

import socket
import threading
import json
import os
import sys
from datetime import datetime
import subprocess
import platform
try:
    from PIL import Image, ImageGrab
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("تحذير: Pillow غير متوفر، سيتم تعطيل ميزة لقطة الشاشة")

try:
    import mysql.connector
    MYSQL_AVAILABLE = True
except ImportError:
    MYSQL_AVAILABLE = False
    print("تحذير: mysql-connector-python غير متوفر")

try:
    import psycopg2
    POSTGRES_AVAILABLE = False  # سيتم تعطيل PostgreSQL مؤقتاً
except ImportError:
    POSTGRES_AVAILABLE = False
    print("تحذير: psycopg2 غير متوفر")

class SQLSearchTool:
    def __init__(self, root):
        self.root = root
        self.root.title("أداة بحث SQL المتقدمة - Advanced SQL Search Tool")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1e1e1e")
        
        # تهيئة المتغيرات
        self.results = []
        self.israeli_sites = []
        self.searching = False
        
        # إنشاء الواجهة
        self.create_widgets()
        self.load_israeli_domains()
        
    def create_widgets(self):
        # إطار العنوان مع اللوقو
        header_frame = tk.Frame(self.root, bg="#2d2d2d", height=80)
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # عنوان الأداة
        title_label = tk.Label(header_frame, text="أداة بحث SQL المتقدمة", 
                              font=("Arial", 20, "bold"), fg="#00ff00", bg="#2d2d2d")
        title_label.pack(pady=10)
        
        # معلومات المبرمج
        info_frame = tk.Frame(self.root, bg="#1e1e1e")
        info_frame.pack(fill=tk.X, padx=10, pady=5)
        
        info_text = """المبرمج: SayerLinux | الموقع: https://github.com/SaudiLinux | البريد: SayerLinux1@gmail.com"""
        info_label = tk.Label(info_frame, text=info_text, font=("Arial", 10), 
                            fg="#ffffff", bg="#1e1e1e")
        info_label.pack()
        
        # إطار الإدخال
        input_frame = tk.LabelFrame(self.root, text="إعدادات البحث", 
                                  font=("Arial", 12, "bold"), fg="#00ff00", bg="#1e1e1e")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # حقل إدخال النطاق
        tk.Label(input_frame, text="النطاق المستهدف:", fg="#ffffff", bg="#1e1e1e").grid(row=0, column=0, padx=5, pady=5)
        self.domain_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.domain_entry.grid(row=0, column=1, padx=5, pady=5)
        self.domain_entry.insert(0, "example.com")
        
        # اختيار نوع قاعدة البيانات
        tk.Label(input_frame, text="نوع قاعدة البيانات:", fg="#ffffff", bg="#1e1e1e").grid(row=0, column=2, padx=5, pady=5)
        self.db_type = ttk.Combobox(input_frame, values=["MySQL", "PostgreSQL", "SQLite"], width=15)
        self.db_type.grid(row=0, column=3, padx=5, pady=5)
        self.db_type.set("MySQL")
        
        # إطار الأزرار
        button_frame = tk.Frame(input_frame, bg="#1e1e1e")
        button_frame.grid(row=1, column=0, columnspan=4, pady=10)
        
        self.search_button = tk.Button(button_frame, text="ابدأ البحث", 
                                     command=self.start_search,
                                     bg="#00ff00", fg="black", font=("Arial", 12, "bold"),
                                     width=15)
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(button_frame, text="إيقاف البحث", 
                                   command=self.stop_search,
                                   bg="#ff0000", fg="white", font=("Arial", 12, "bold"),
                                   width=15, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.screenshot_button = tk.Button(button_frame, text="لقطة شاشة", 
                                       command=self.take_screenshot,
                                       bg="#0080ff", fg="white", font=("Arial", 12, "bold"),
                                       width=15)
        self.screenshot_button.pack(side=tk.LEFT, padx=5)
        
        self.save_button = tk.Button(button_frame, text="حفظ النتائج", 
                                   command=self.save_results,
                                   bg="#ff8800", fg="white", font=("Arial", 12, "bold"),
                                   width=15)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        # إطار النتائج
        result_frame = tk.LabelFrame(self.root, text="نتائج البحث", 
                                   font=("Arial", 12, "bold"), fg="#00ff00", bg="#1e1e1e")
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # شريط التقدم
        self.progress = ttk.Progressbar(result_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, padx=5, pady=5)
        
        # منطقة عرض النتائج
        self.result_text = tk.Text(result_frame, height=20, width=80, 
                                 font=("Courier", 10), bg="#000000", fg="#00ff00")
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, 
                                command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # شريط الحالة
        self.status_bar = tk.Label(self.root, text="جاهز للبحث...", 
                                 bd=1, relief=tk.SUNKEN, anchor=tk.W,
                                 bg="#2d2d2d", fg="#ffffff")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def load_israeli_domains(self):
        """تحميل قائمة النطاقات الإسرائيلية"""
        israeli_domains = [
            '.il', '.co.il', '.org.il', '.gov.il', '.ac.il', '.muni.il',
            'gov.il', 'idf.il', 'mfa.gov.il', 'knesset.gov.il',
            'jpost.com', 'ynet.co.il', 'haaretz.co.il', 'timesofisrael.com',
            'israelhayom.co.il', 'walla.co.il', 'mako.co.il', 'n12.co.il'
        ]
        self.israeli_sites = israeli_domains
        
    def log_message(self, message, level="INFO"):
        """تسجيل الرسائل في واجهة المستخدم"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {level}: {message}\n"
        self.result_text.insert(tk.END, formatted_message)
        self.result_text.see(tk.END)
        self.root.update_idletasks()
        
    def is_israeli_site(self, url):
        """التحقق إذا كان الموقع إسرائيلي"""
        url_lower = url.lower()
        return any(domain.lower() in url_lower for domain in self.israeli_sites)
        
    def scan_sql_servers(self, domain):
        """مسح خوادم SQL في النطاق المحدد"""
        common_ports = [3306, 5432, 1433, 1521, 27017]  # MySQL, PostgreSQL, MSSQL, Oracle, MongoDB
        results = []
        
        try:
            # الحصول على عنوان IP
            ip = socket.gethostbyname(domain)
            self.log_message(f"تم حل النطاق {domain} إلى {ip}")
            
            # مسح المنافذ
            for port in common_ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    result = sock.connect_ex((ip, port))
                    
                    if result == 0:
                        service = self.get_service_name(port)
                        self.log_message(f"تم العثور على خادم {service} على المنفذ {port}")
                        
                        # محاولة الاتصال بقاعدة البيانات
                        db_info = self.test_sql_connection(ip, port, domain)
                        if db_info:
                            results.append({
                                'domain': domain,
                                'ip': ip,
                                'port': port,
                                'service': service,
                                'is_israeli': self.is_israeli_site(domain),
                                'db_info': db_info
                            })
                    
                    sock.close()
                    
                except Exception as e:
                    self.log_message(f"خطأ في مسح المنفذ {port}: {str(e)}", "ERROR")
                    
        except Exception as e:
            self.log_message(f"خطأ في حل النطاق {domain}: {str(e)}", "ERROR")
            
        return results
        
    def get_service_name(self, port):
        """الحصول على اسم الخدمة حسب المنفذ"""
        services = {
            3306: "MySQL",
            5432: "PostgreSQL",
            1433: "Microsoft SQL Server",
            1521: "Oracle",
            27017: "MongoDB"
        }
        return services.get(port, f"Port {port}")
        
    def test_sql_connection(self, ip, port, domain):
        """اختبار اتصال SQL"""
        try:
            if port == 3306:  # MySQL
                try:
                    conn = mysql.connector.connect(
                        host=ip,
                        user='root',
                        password='',
                        connect_timeout=5
                    )
                    if conn.is_connected():
                        return {
                            'type': 'MySQL',
                            'version': conn.get_server_info(),
                            'databases': [db[0] for db in conn.cursor().execute("SHOW DATABASES").fetchall()]
                        }
                except:
                    return {'type': 'MySQL', 'status': 'Accessible'}
                    
            elif port == 5432:  # PostgreSQL
                try:
                    conn = psycopg2.connect(
                        host=ip,
                        user='postgres',
                        password='',
                        connect_timeout=5
                    )
                    return {'type': 'PostgreSQL', 'status': 'Connected'}
                except:
                    return {'type': 'PostgreSQL', 'status': 'Accessible'}
                    
        except Exception as e:
            return {'type': self.get_service_name(port), 'status': 'Error', 'error': str(e)}
            
        return None
        
    def start_search(self):
        """بدء عملية البحث"""
        domain = self.domain_entry.get().strip()
        if not domain:
            messagebox.showerror("خطأ", "الرجاء إدخال نطاق للبحث")
            return
            
        self.search_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.results = []
        self.result_text.delete(1.0, tk.END)
        
        self.searching = True
        self.progress.start()
        
        # تشغيل البحث في خيط منفصل
        search_thread = threading.Thread(target=self.search_worker, args=(domain,))
        search_thread.daemon = True
        search_thread.start()
        
    def search_worker(self, domain):
        """عامل البحث في خيط منفصل"""
        try:
            self.status_bar.config(text="جاري البحث...")
            self.log_message(f"بدء البحث عن خوادم SQL في النطاق: {domain}")
            
            results = self.scan_sql_servers(domain)
            self.results = results
            
            if results:
                self.log_message(f"تم العثور على {len(results)} خادم SQL")
                for result in results:
                    self.log_message(f"النطاق: {result['domain']}")
                    self.log_message(f"العنوان: {result['ip']}:{result['port']}")
                    self.log_message(f"الخدمة: {result['service']}")
                    self.log_message(f"موقع إسرائيلي: {'نعم' if result['is_israeli'] else 'لا'}")
                    self.log_message("-" * 50)
            else:
                self.log_message("لم يتم العثور على خوادم SQL")
                
        except Exception as e:
            self.log_message(f"خطأ في البحث: {str(e)}", "ERROR")
        finally:
            self.searching = False
            self.progress.stop()
            self.search_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_bar.config(text="اكتمل البحث")
            
    def stop_search(self):
        """إيقاف البحث"""
        self.searching = False
        self.progress.stop()
        self.search_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_bar.config(text="تم إيقاف البحث")
        
    def take_screenshot(self):
        """أخذ لقطة شاشة"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            
            # أخذ لقطة الشاشة
            screenshot = ImageGrab.grab()
            screenshot.save(filename)
            
            self.log_message(f"تم حفظ لقطة الشاشة: {filename}")
            messagebox.showinfo("نجاح", f"تم حفظ لقطة الشاشة: {filename}")
            
        except Exception as e:
            self.log_message(f"خطأ في أخذ لقطة الشاشة: {str(e)}", "ERROR")
            
    def save_results(self):
        """حفظ النتائج في ملف JSON"""
        if not self.results:
            messagebox.showwarning("تحذير", "لا توجد نتائج لحفظها")
            return
            
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.results, f, ensure_ascii=False, indent=2)
                    
                self.log_message(f"تم حفظ النتائج في: {filename}")
                messagebox.showinfo("نجاح", "تم حفظ النتائج بنجاح")
                
            except Exception as e:
                self.log_message(f"خطأ في حفظ النتائج: {str(e)}", "ERROR")

if __name__ == "__main__":
    root = tk.Tk()
    app = SQLSearchTool(root)
    root.mainloop()