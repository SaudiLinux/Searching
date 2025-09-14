═══════════════════════════════════════════════════════════════════════════════
                           🚨 أدوات الأمن السيبراني
                    للمواقع الإسرائيلية - دليل الاستخدام
═══════════════════════════════════════════════════════════════════════════════

📋 نظرة عامة:
تم إنشاء مجموعة متكاملة من الأدوات الأمنية المتخصصة في تحليل واستغلال 
المواقع الإسرائيلية، تضم سبع أدوات متقدمة تعمل بشكل متكامل.

═══════════════════════════════════════════════════════════════════════════════

🔧 الأدوات المتوفرة:

1️⃣ **infected_links_report.py**
   📊 عرض المواقع الإسرائيلية المصابة (13 موقع)
   🎯 روابط مباشرة مع IP لكل موقع
   🎨 تقرير HTML تفاعلي

2️⃣ **exploit_tool.py**
   ⚡ اختبار واستغلال الثغرات الأمنية
   🔍 SQL Injection, XSS, LFI, Command Injection
   📋 تقارير HTML وJSON

3️⃣ **google_dork_tool.py**
   🔎 815 استعلام بحث متخصص
   🎯 Google Dorking للمواقع الإسرائيلية
   📊 فئات متعددة: عسكرية، حكومية، استخبارات

4️⃣ **vulnerability_links_viewer.py**
   🚨 عرض روابط الثغرات مع روابط اختبار مباشرة
   🔗 9 ثغرة في 4 فئات
   🧪 روابط اختبار فورية

5️⃣ **sqli_payloads_wordlist.txt**
   💉 قائمة حمولات SQL Injection المتقدمة
   🎯 200+ حمولة لـ MySQL, PostgreSQL, MSSQL, Oracle, NoSQL
   🇮🇱 حمولات خاصة بالمواقع الإسرائيلية

6️⃣ **sqli_scanner_tool.py**
   🔍 أداة مسح تلقائي للمواقع الإسرائيلية
   🎯 30 موقع مستهدف
   📊 تقارير JSON وHTML مع روابط مباشرة

7️⃣ **show_infected_sites.py**
   🚨 عرض سريع لروابط المواقع المصابة
   🔗 10 موقع إسرائيلي مصاب
   🌐 تقارير HTML تفاعلية

═══════════════════════════════════════════════════════════════════════════════

🚀 طريقة التشغيل السريعة:

الطريقة 1: التشغيل التلقائي الكامل
─────────────────────────────────
python infected_links_report.py
echo 2 | python exploit_tool.py
echo 2 | python google_dork_tool.py
python vulnerability_links_viewer.py
الطريقة 2: التشغيل الفردي
────────────────────────
python infected_links_report.py     # عرض المواقع
python exploit_tool.py             # اختبار الثغرات
python google_dork_tool.py         # البحث المتقدم
python vulnerability_links_viewer.py # عرض الروابط
python sqli_scanner_tool.py --auto # استخدام حمولات SQLi
python show_infected_sites.py      # عرض المواقع المصابة سريعاً

═══════════════════════════════════════════════════════════════════════════════

📁 الملفات الناتجة:

📊 **التقارير التفاعلية:**
• infected_links_report.html      - قائمة المواقع المصابة
• exploitation_report.html        - نتائج الاستغلال
• google_dorks_report.html        - استعلامات البحث
• vulnerability_links_report.html - روابط الثغرات
• sqli_report.html              - تقرير فحص SQLi
• infected_sites_report.html      - تقرير المواقع المصابة سريع

📋 **ملفات البيانات:**
• infected_links.json
• exploitation_report.json
• israeli_google_dorks.json
• vulnerability_links.json
• sqli_scan_results.json
• infected_sites.json

📖 **الملفات الإرشادية:**
• تشغيل_الادوات_بالتفصيل.md  - دليل الاستخدام الكامل
• README.txt                  - هذا الملف

═══════════════════════════════════════════════════════════════════════════════

🎯 المواقع الإسرائيلية المستهدفة (30 موقع):
• https://www.gov.il - الحكومة الإسرائيلية
• https://www.mossad.gov.il - الموساد
• https://www.shabak.gov.il - الشاباك
• https://www.idf.il - الجيش الإسرائيلي
• https://www.bankisrael.gov.il - بنك إسرائيل
• https://www.calcalist.co.il - كلكاليست
• https://www.haaretz.co.il - هآرتس
• https://www.jpost.com - القدس بوست
• https://www.ynet.co.il - واي نت
• https://www.walla.co.il - واللا
• https://www.mako.co.il - ماكو
• https://www.n12.co.il - ن12
• https://www.timesofisrael.com - تايمز أوف إسرائيل
• https://www.globes.co.il - جلوبس
• https://www.bankleumi.co.il - بنك لئومي
• https://www.bankhapoalim.co.il - بنك هبوعليم
• https://www.discountbank.co.il - بنك ديسكاونت
• https://www.fibi.co.il - البنك الأول
• https://www.mizrahi-tefahot.co.il - مزراحي تفاهوت
• https://www.isracard.co.il - إسراكارد
• https://www.americanexpress.co.il - أمريكان إكسبرس
• https://www.paypal.co.il - بايبال إسرائيل
• https://www.microsoft.com/he-il - مايكروسوفت إسرائيل
• https://www.apple.com/il - آبل إسرائيل
• https://www.google.co.il - جوجل إسرائيل
• https://www.amazon.co.il - أمازون إسرائيل
• https://www.facebook.com - فيسبوك (إسرائيل)
• https://www.twitter.com - تويتر (إسرائيل)
• https://www.instagram.com - إنستغرام (إسرائيل)
• https://www.linkedin.com - لينكدإن (إسرائيل)

═══════════════════════════════════════════════════════════════════════════════

🔍 أنواع الثغرات المكتشفة:

• **SQL Injection (MySQL, PostgreSQL, MSSQL, Oracle, NoSQL)** - ثغرات حقن SQL
• **XSS** - Cross-Site Scripting
• **LFI** - Local File Inclusion
• **Command Injection** - حقن الأوامر
• **Admin Panels** - لوحات التحكم الإدارية
• **File Vulnerabilities** - ثغرات الملفات
• **RCE** - Remote Code Execution
• **Directory Traversal** - تجاوز الدلائل
• **Information Disclosure** - تسريب المعلومات
• **Authentication Bypass** - تجاوز المصادقة
• **Session Hijacking** - اختطاف الجلسة
• **SSRF** - Server-Side Request Forgery
• **XXE** - XML External Entity
• **LDAP Injection** - حقن LDAP

═══════════════════════════════════════════════════════════════════════════════

⚡ أوامر فتح التقارير:

Windows:
start infected_links_report.html
start exploitation_report.html
start google_dorks_report.html
start vulnerability_links_report.html
start sqli_report.html
start infected_sites_report.html

أو ببساطة انقر نقرًا مزدوجًا على أي ملف HTML

═══════════════════════════════════════════════════════════════════════════════

🛡️ ملاحظات أمان مهمة:

⚠️ **هذه الأدوات مخصصة للبحث الأمني القانوني فقط**
⚠️ **لا تستخدمها في مواقع غير مصرح بها**
⚠️ **استخدم VPN عند الاختبار**
⚠️ **احفظ النتائج بشكل آمن**
⚠️ **اتبع الأخلاقيات الأمنية**
🌐 **خصص لتحليل الأمن السيبراني للمواقع الإسرائيلية فقط**
⚡ **استخدم VPN وTor للحماية أثناء الاختبار**

═══════════════════════════════════════════════════════════════════════════════

📞 الدعم والمساعدة:

إذا واجهت مشاكل:
1. تأكد من تثبيت Python 3.7+
2. تأكد من صلاحيات تشغيل الملفات
3. افتح CMD كمسؤول إذا لزم الأمر
4. تأكد من اتصال الإنترنت
5. استخدم VPN إذا كانت المواقع محظورة
6. تأكد من تثبيت المكتبات المطلوبة: pip install requests beautifulsoup4 selenium
7. استخدم --help لعرض خيارات كل أداة
8. تحقق من وجود الملفات المطلوبة (sqli_payloads_wordlist.txt)

═══════════════════════════════════════════════════════════════════════════════

🔥 الخلاصة:

الآن لديك أربع أدوات متكاملة تعمل بشكل فوري:
✅ اكتشاف المواقع الإسرائيلية المصابة
✅ اختبار واستغلال الثغرات الأمنية
✅ إنشاء استعلامات بحث متقدمة
✅ عرض روابط اختبار مباشرة

كل ما عليك فعله هو تشغيل الأوامر أعلاه للحصول على جميع النتائج!

═══════════════════════════════════════════════════════════════════════════════

📊 إحصائيات الأدوات:
• 7 أدوات متخصصة (4 أدوات أساسية + 3 أدوات متقدمة)
• 30 موقع إسرائيلي مستهدف
• 200+ حمولة SQL Injection
• 815 استعلام بحث متقدم
• 15+ ثغرة أمنية مختلفة
• تقارير HTML وJSON متكاملة
• واجهة رسومية تفاعلية
• وضع تلقائي وتفاعلي للمسح

🎉 تم التحديث: 2025-12-19
═══════════════════════════════════════════════════════════════════════════════