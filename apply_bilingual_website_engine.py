# -*- coding: utf-8 -*-
"""
apply_bilingual_website_engine.py
Implements full bilingual website internationalization (i18n):
- Navbar toggle: [Always English] and [العربية]
- Mobile drawer language toggle
- localStorage persistence
- Document direction (RTL / LTR) switching
- Cairo font application for Arabic
- Complete bilingual translations for projectsData (9 case studies)
- Data-i18n translation engine for all sections, headings, badges, and buttons
"""

import json
import re

def update_portfolio_bilingual():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('projects_bilingual.json', 'r', encoding='utf-8') as pf:
        projects_bilingual = json.load(pf)

    # 1. Update Navbar with Language Selector Button
    # Insert right before quick action buttons (WhatsApp & Email)
    lang_selector_html = """
      <!-- Language Selector Toggle: Always English vs Arabic -->
      <div class="hidden sm:inline-flex items-center rounded-xl bg-slate-900/90 border border-slate-700/80 p-0.5 shadow-md">
        <button id="langBtnEn" onclick="setSiteLanguage('en')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-blue-600 text-white shadow-sm" title="Switch to English">
          <i class="fa-solid fa-globe text-[10px]"></i> Always English
        </button>
        <button id="langBtnAr" onclick="setSiteLanguage('ar')" class="px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all flex items-center gap-1.5" title="التبديل إلى العربية">
          <span>العربية</span>
        </button>
      </div>
"""

    if 'id="langBtnEn"' not in html:
        quick_action_marker = '<!-- Quick Action Buttons -->'
        html = html.replace(quick_action_marker, lang_selector_html + '\n      ' + quick_action_marker, 1)
        print("Inserted desktop language switcher button")

    # 2. Update Mobile Menu with Language Selector
    mob_lang_selector_html = """
      <!-- Mobile Language Selector -->
      <div class="pt-2 border-t border-slate-800">
        <div class="text-[10px] uppercase tracking-wider text-slate-400 font-bold px-1 mb-1.5 flex items-center justify-between">
          <span>Language / اللغة</span>
          <span class="text-cyan-400 font-semibold" id="mobCurrentLangBadge">English</span>
        </div>
        <div class="grid grid-cols-2 gap-2 p-1 rounded-xl bg-slate-950 border border-slate-800">
          <button id="mobLangBtnEn" onclick="setSiteLanguage('en'); closeMobileMenu();" class="py-2 rounded-lg text-xs font-bold bg-blue-600 text-white transition-all flex items-center justify-center gap-1.5">
            <i class="fa-solid fa-globe text-xs"></i> Always English
          </button>
          <button id="mobLangBtnAr" onclick="setSiteLanguage('ar'); closeMobileMenu();" class="py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all flex items-center justify-center gap-1.5">
            <span>العربية (Arabic)</span>
          </button>
        </div>
      </div>
"""

    if 'id="mobLangBtnEn"' not in html:
        mob_quick_action_marker = '<!-- Quick Action Buttons in Mobile Menu -->'
        html = html.replace(mob_quick_action_marker, mob_lang_selector_html + '\n      ' + mob_quick_action_marker, 1)
        print("Inserted mobile language switcher button")

    # 3. Replace projectsData array in index.html with projects_bilingual
    bilingual_projects_js = f"const projectsData = {json.dumps(projects_bilingual, ensure_ascii=False, indent=6)};"
    
    old_projects_pattern = r'const projectsData = \[[\s\S]*?\n    \];'
    if re.search(old_projects_pattern, html):
        html = re.sub(old_projects_pattern, bilingual_projects_js, html, count=1)
        print("Replaced projectsData with pure bilingual English & Arabic models")

    # 4. Prepare full i18n Translation Dictionary and setSiteLanguage JavaScript engine
    i18n_engine_js = """
    // ==========================================
    // BILINGUAL WEBSITE INTERNATIONALIZATION (i18n)
    // ==========================================
    let currentSiteLang = localStorage.getItem('sultan_site_language') || 'en';

    const SITE_TRANSLATIONS = {
      en: {
        dir: 'ltr',
        fontClass: '',
        nav_cv: 'CV & Decks',
        nav_ai: 'AI & Data Engine',
        nav_frameworks: 'Growth Playbooks',
        nav_proofs: 'Case Studies',
        nav_vault: 'Proof Vault (59)',
        nav_creatives: 'Ad Creatives (48)',
        nav_calculator: 'ROI Engine',
        nav_audit: 'Audit & Diagnosis',
        hero_badge: 'Verified Growth Architect • Riyadh, KSA',
        hero_title_1: 'Scale Predictable Revenue with',
        hero_title_2: 'AI-Driven & Data-Engineered Ad Architecture',
        hero_desc: 'I architect full-funnel paid media campaigns powered by Meta Advantage+ AI, Google Smart Bidding, Server-Side CAPI tracking, and Predictive Algorithmic Creative Testing — turning erratic ad spend into measurable, scalable pipeline revenue.',
        hero_cta_cv: 'Explore Executive CV (EN/AR)',
        hero_cta_decks: 'View 22-Slide Decks',
        hero_cta_audit: 'Free Teardown Audit',
        hero_trust_pill: 'Available for GCC (Riyadh, KSA) & Global High-Ticket Engagements',
        hero_trust_bilingual: 'Bilingual Strategy (English & العربية)',
        stat_spend_lbl: 'Managed Spend',
        stat_spend_sub: 'Across Verified Accounts',
        stat_rev_lbl: 'Tracked Revenue',
        stat_rev_sub: 'Attributed Purchases',
        stat_roas_lbl: 'Blended ROAS',
        stat_roas_sub: 'Average Multiplier',
        stat_proofs_lbl: 'Verified Proofs',
        stat_proofs_sub: 'Screenshots & Case Studies',
        view_active_lbl: 'Active View:',
        view_single_btn: 'Single View',
        view_all_btn: 'Show All',
        exec_badge: 'Executive Assets & Bilingual Credentials',
        exec_title: 'Executive CV & Growth Architecture Slide Decks',
        exec_desc: 'Directly inspect and download Tipu Sultan\\'s verified Curriculum Vitae (in English & Arabic) and comprehensive 22-slide strategic presentation decks — engineered for high-ticket GCC brands, DTC founders, and venture-backed companies.',
        ai_badge: 'Next-Gen Performance Architecture',
        ai_title: 'AI-Driven & Data-Engineered Acquisition Engine',
        frameworks_badge: 'Algorithmic Growth Intelligence',
        frameworks_title: 'Strategic Performance Playbooks',
        proofs_badge: 'Performance Case Studies',
        proofs_title: 'Verified Client Campaign Teardowns',
        proofs_desc: 'Real accounts, real ad spend, real revenue. Each study includes the 3-layer architecture, CPA drops, and actual screenshots.',
        vault_badge: 'Empirical Evidence Vault',
        vault_title: 'Raw Proof Gallery (59 Verified Screenshots)',
        creatives_badge: 'Creative Testing Engine',
        creatives_title: 'Ad Creative Sandbox & Angle Matrix',
        calculator_badge: 'Interactive Funnel Simulator',
        calculator_title: 'Calculate Your Projected Revenue Lift with Optimized Ad Architecture',
        audit_badge: 'Zero-Cost Opportunity Analysis',
        audit_title: 'Request Your 10-Minute Ad Account Teardown',
        audit_desc: 'Submit your brand or store URL. I will personally review your tracking setup, identify ad fatigue, and pinpoint where your budget is leaking — delivered via a private video teardown.',
        audit_btn: 'Request My 10-Min Video Teardown',
        case_challenge_title: 'The Scaling Bottleneck',
        case_strategy_title: 'Engineering Architecture & Strategy',
        case_results_title: 'Impact & Verified Dashboard Proof',
        case_breakdown_btn: 'Deep Architecture Breakdown'
      },
      ar: {
        dir: 'rtl',
        fontClass: 'font-arabic',
        nav_cv: 'السيرة والعروض',
        nav_ai: 'محرك الذكاء والبيانات',
        nav_frameworks: 'ملاعب النمو',
        nav_proofs: 'دراسات الحالة',
        nav_vault: 'خزنة البراهين (59)',
        nav_creatives: 'صندوق الإبداع (48)',
        nav_calculator: 'حاسبة العائد',
        nav_audit: 'التدقيق والتشخيص',
        hero_badge: 'مهندس نمو موثق • الرياض، المملكة العربية السعودية',
        hero_title_1: 'مضاعفة الإيرادات المتوقعة عبر',
        hero_title_2: 'هندسة إعلانات بالذكاء الاصطناعي والبيانات',
        hero_desc: 'أقوم بهندسة حملات إعلانية مدفوعة كاملة القمع مدعومة بالذكاء الاصطناعي Meta Advantage+، ومزايدات Google الذكية، وتتبع Server-Side CAPI، واختبارات الإبداع التنبؤية — لتحويل الإنفاق الإعلاني العشوائي إلى إيرادات متوقعة وقابلة للتوسع.',
        hero_cta_cv: 'استعراض السيرة الذاتية (EN/AR)',
        hero_cta_decks: 'عرض الـ 22 شريحة الاستراتيجية',
        hero_cta_audit: 'طلب تدقيق مجاني لحسابك',
        hero_trust_pill: 'متاح للتعاقدات عالية القيمة في السوق الخليجي (الرياض) وعالمياً',
        hero_trust_bilingual: 'استراتيجية ثنائية اللغة (الإنجليزية والعربية)',
        stat_spend_lbl: 'إنفاق إعلاني مُدار',
        stat_spend_sub: 'عبر حسابات موثقة',
        stat_rev_lbl: 'إيرادات متتبعة',
        stat_rev_sub: 'مبيعات مسندة بدقة',
        stat_roas_lbl: 'عائد مدمج ROAS',
        stat_roas_sub: 'متوسط المضاعف الربحي',
        stat_proofs_lbl: 'براهين موثقة',
        stat_proofs_sub: 'لقطات شاشة ودراسات حالة',
        view_active_lbl: 'العرض النشط:',
        view_single_btn: 'عرض منفرد',
        view_all_btn: 'عرض الكل',
        exec_badge: 'أصول تنفيذية ومؤهلات ثنائية اللغة',
        exec_title: 'السيرة الذاتية التنفيذية وعروض استراتيجية النمو',
        exec_desc: 'استعرض وحمل السيرة الذاتية الموثقة لتيبو سلطان وعروض الشرائح الاستراتيجية المكونة من 22 شريحة — المصممة خصيصاً للعلامات التجارية الخليجية، ورواد التجارة الإلكترونية، والشركات الكبرى.',
        ai_badge: 'هندسة أداء من الجيل التالي',
        ai_title: 'محرك الاكتساب المدفوع بالذكاء الاصطناعي والبيانات',
        frameworks_badge: 'ذكاء النمو الخوارزمي',
        frameworks_title: 'ملاعب الأداء الاستراتيجية',
        proofs_badge: 'دراسات حالة الأداء',
        proofs_title: 'تشريحات موثقة لحملات عملاء حقيقيين',
        proofs_desc: 'حسابات حقيقية، إنفاق إعلاني حقيقي، وإيرادات فعلية. تشمل كل دراسة البنية ثلاثية الطبقات، انخفاض تكلفة الاكتساب، ولقطات الشاشة الفعلية.',
        vault_badge: 'خزنة الأدلة والبراهين التجريبية',
        vault_title: 'معرض البراهين الخام (59 لقطة شاشة موثقة)',
        creatives_badge: 'محرك اختبار الإبداع',
        creatives_title: 'صندوق الإبداع الإعلاني ومصفوفة الزوايا',
        calculator_badge: 'محاكاة القمع التفاعلية',
        calculator_title: 'احسب نمو الإيرادات المتوقع مع بنية إعلانية محسنة',
        audit_badge: 'تحليل الفرص بلا مقابل',
        audit_title: 'اطلب تشريح وتدقيق حسابك الإعلاني في 10 دقائق',
        audit_desc: 'أرسل رابط متجرك أو موقعك. سأقوم شخصياً بمراجعة إعدادات التتبع لديك، وتحديد إجهاد الإعلانات، ونقاط تسرب الميزانية — عبر فيديو تشريحي خاص.',
        audit_btn: 'اطلب تدقيق الفيديو الخاص بي (10 دقائق مجاناً)',
        case_challenge_title: 'عقبة التوسع الرئيسية',
        case_strategy_title: 'البنية الهندسية والاستراتيجية',
        case_results_title: 'النتائج والبراهين الموثقة من لوحة التحكم',
        case_breakdown_btn: 'تشريح البنية الهندسية الكاملة'
      }
    };

    function setSiteLanguage(lang) {
      currentSiteLang = (lang === 'ar') ? 'ar' : 'en';
      localStorage.setItem('sultan_site_language', currentSiteLang);

      const t = SITE_TRANSLATIONS[currentSiteLang];

      // Update HTML root attributes
      document.documentElement.lang = currentSiteLang;
      document.documentElement.dir = t.dir;

      // Toggle Arabic font class on body
      if (currentSiteLang === 'ar') {
        document.body.classList.add('font-arabic');
      } else {
        document.body.classList.remove('font-arabic');
      }

      // Update Desktop Navbar Language Buttons
      const btnEn = document.getElementById('langBtnEn');
      const btnAr = document.getElementById('langBtnAr');
      if (btnEn && btnAr) {
        if (currentSiteLang === 'en') {
          btnEn.className = 'px-2.5 py-1 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-blue-600 text-white shadow-sm';
          btnAr.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all flex items-center gap-1.5';
        } else {
          btnAr.className = 'px-2.5 py-1 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-emerald-600 text-white shadow-sm';
          btnEn.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all flex items-center gap-1.5';
        }
      }

      // Update Mobile Drawer Language Buttons
      const mobBtnEn = document.getElementById('mobLangBtnEn');
      const mobBtnAr = document.getElementById('mobLangBtnAr');
      const mobBadge = document.getElementById('mobCurrentLangBadge');
      if (mobBtnEn && mobBtnAr) {
        if (currentSiteLang === 'en') {
          mobBtnEn.className = 'py-2 rounded-lg text-xs font-bold bg-blue-600 text-white transition-all flex items-center justify-center gap-1.5 shadow-sm';
          mobBtnAr.className = 'py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all flex items-center justify-center gap-1.5';
          if (mobBadge) mobBadge.innerText = 'Always English';
        } else {
          mobBtnAr.className = 'py-2 rounded-lg text-xs font-bold bg-emerald-600 text-white transition-all flex items-center justify-center gap-1.5 shadow-sm';
          mobBtnEn.className = 'py-2 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all flex items-center justify-center gap-1.5';
          if (mobBadge) mobBadge.innerText = 'العربية (Arabic)';
        }
      }

      // Update all elements with data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (t[key]) {
          el.innerText = t[key];
        }
      });

      // Update dynamic tabLabels
      if (currentSiteLang === 'ar') {
        tabLabels['executive-assets'] = 'السيرة الذاتية وعروض استراتيجية النمو';
        tabLabels['ai-engine'] = 'محرك الذكاء والبيانات';
        tabLabels['frameworks'] = 'ملاعب الأداء الاستراتيجية';
        tabLabels['proofs'] = 'دراسات حالة الحملات الموثقة';
        tabLabels['vault'] = 'خزنة البراهين الخام (59 لقطة شاشة)';
        tabLabels['creatives'] = 'صندوق اختبار الإبداع الإعلاني';
        tabLabels['calculator'] = 'محاكاة القمع التفاعلية';
        tabLabels['audit'] = 'تدقيق الحساب الإعلاني في 10 دقائق';
      } else {
        tabLabels['executive-assets'] = 'Executive CV & Strategic Decks';
        tabLabels['ai-engine'] = 'AI-Driven & Data-Engineered Engine';
        tabLabels['frameworks'] = 'Strategic Performance Playbooks';
        tabLabels['proofs'] = 'Verified Client Case Studies';
        tabLabels['vault'] = 'Raw Proof Gallery (59 Verified Screenshots)';
        tabLabels['creatives'] = 'Ad Creative Sandbox & Angle Matrix';
        tabLabels['calculator'] = 'Interactive Funnel ROI Simulator';
        tabLabels['audit'] = '10-Minute Ad Account Teardown Audit';
      }

      // Update Active View label
      const activeLabel = document.getElementById('activeViewLabel');
      if (activeLabel && tabLabels[currentActiveTab]) {
        activeLabel.innerText = tabLabels[currentActiveTab];
      }

      // Re-render projects in selected language
      renderProjects(projectsData);
    }
"""

    if 'SITE_TRANSLATIONS' not in html:
        html = html.replace('// Initialize App', i18n_engine_js + '\n    // Initialize App', 1)
        print("Inserted i18n translation dictionary and setSiteLanguage engine")

    # 5. Update renderProjects() to render according to currentSiteLang
    old_render_projects_pattern = r'function renderProjects\(items\) \{[\s\S]*?grid\.appendChild\(card\);\s*\}\);'
    
    new_render_projects_js = """function renderProjects(items) {
      const grid = document.getElementById('projects-grid');
      grid.innerHTML = '';
      const isAr = (currentSiteLang === 'ar');

      items.forEach(p => {
        const title = isAr ? (p.title_ar || p.title_en || p.title) : (p.title_en || p.title);
        const tag = isAr ? (p.tag_ar || p.tag_en || p.tag) : (p.tag_en || p.tag);
        const metric = isAr ? (p.metric_ar || p.metric_en || p.metric) : (p.metric_en || p.metric);
        const challenge = isAr ? (p.challenge_ar || p.challenge_en || p.challenge) : (p.challenge_en || p.challenge);
        const strategy = isAr ? (p.strategy_ar || p.strategy_en || p.strategy) : (p.strategy_en || p.strategy);
        const breakdownBtn = isAr ? 'تشريح البنية الهندسية الكاملة' : 'Deep Architecture Breakdown';
        const challengeLbl = isAr ? 'عقبة التوسع:' : 'The Bottleneck:';
        const strategyLbl = isAr ? 'الحل الهندسي:' : 'The Architecture:';

        const card = document.createElement('div');
        card.className = 'glass-card rounded-2xl overflow-hidden flex flex-col justify-between group border border-slate-800 hover:border-cyan-500/40 transition-all';
        card.innerHTML = `
          <div>
            <div class="relative h-48 w-full overflow-hidden bg-slate-950 cursor-pointer" onclick="openModal(${p.id})">
              <img src="${p.image}" alt="${title}" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/20 to-transparent"></div>
              <span class="absolute top-3 left-3 bg-slate-900/90 backdrop-blur-md px-2.5 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider text-cyan-400 border border-slate-700">
                ${tag}
              </span>
            </div>

            <div class="p-6">
              <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-bold border border-emerald-500/20 mb-3">
                <i class="fa-solid fa-arrow-trend-up"></i> ${metric}
              </div>
              <h3 class="text-base sm:text-lg font-display font-bold text-white group-hover:text-cyan-400 transition-colors leading-snug">
                ${title}
              </h3>

              <div class="mt-4 space-y-2 text-xs text-slate-300">
                <p class="line-clamp-2"><strong class="text-slate-400">${challengeLbl}</strong> ${challenge}</p>
                <p class="line-clamp-2"><strong class="text-cyan-400">${strategyLbl}</strong> ${strategy}</p>
              </div>
            </div>
          </div>

          <div class="p-6 pt-0">
            <button onclick="openModal(${p.id})" class="w-full py-2.5 px-4 rounded-xl bg-slate-900/90 hover:bg-slate-800 text-slate-200 border border-slate-700/80 text-xs font-bold flex items-center justify-center gap-2 group-hover:border-cyan-500/40 transition-all">
              <span>${breakdownBtn}</span>
              <i class="fa-solid fa-arrow-up-right-from-square text-[10px] text-cyan-400"></i>
            </button>
          </div>
        `;
        grid.appendChild(card);
      });"""

    if re.search(old_render_projects_pattern, html):
        html = re.sub(old_render_projects_pattern, new_render_projects_js, html, count=1)
        print("Updated renderProjects() to dynamically handle English and Arabic")

    # 6. Add data-i18n tags to static elements in index.html
    # Desktop nav
    html = html.replace('<span>CV & Decks</span>', '<span data-i18n="nav_cv">CV & Decks</span>')
    html = html.replace('<span>AI & Data Engine</span>', '<span data-i18n="nav_ai">AI & Data Engine</span>')
    html = html.replace('<span>Growth Playbooks</span>', '<span data-i18n="nav_frameworks">Growth Playbooks</span>')
    html = html.replace('<span>Case Studies</span>', '<span data-i18n="nav_proofs">Case Studies</span>')
    html = html.replace('<span>Proof Vault (59)</span>', '<span data-i18n="nav_vault">Proof Vault (59)</span>')
    html = html.replace('<span>Ad Creatives (48)</span>', '<span data-i18n="nav_creatives">Ad Creatives (48)</span>')
    html = html.replace('<span>ROI Engine</span>', '<span data-i18n="nav_calculator">ROI Engine</span>')
    html = html.replace('<span>Audit & Diagnosis</span>', '<span data-i18n="nav_audit">Audit & Diagnosis</span>')

    # Hero section
    html = html.replace(
        '<span class="text-emerald-400 font-bold">Verified Growth Architect</span>\n      <span class="text-slate-600">&bull;</span>\n      <span class="text-slate-400 font-medium"><i class="fa-solid fa-location-dot text-cyan-400 mr-1 text-[10px]"></i>Riyadh, KSA</span>',
        '<span data-i18n="hero_badge" class="text-emerald-400 font-bold">Verified Growth Architect • Riyadh, KSA</span>'
    )
    html = html.replace(
        'Scale Predictable Revenue with <br />',
        '<span data-i18n="hero_title_1">Scale Predictable Revenue with</span> <br />'
    )
    html = html.replace(
        'AI-Driven & Data-Engineered Ad Architecture\n      </span>',
        'AI-Driven & Data-Engineered Ad Architecture</span>'
    )
    html = html.replace(
        '<span>Explore Executive CV (EN/AR)</span>',
        '<span data-i18n="hero_cta_cv">Explore Executive CV (EN/AR)</span>'
    )
    html = html.replace(
        '<span>View 22-Slide Decks</span>',
        '<span data-i18n="hero_cta_decks">View 22-Slide Decks</span>'
    )
    html = html.replace(
        '<span>Free Teardown Audit</span>',
        '<span data-i18n="hero_cta_audit">Free Teardown Audit</span>'
    )

    # Call setSiteLanguage on init
    init_pattern = r'handleInitialHash\(\);'
    new_init = "handleInitialHash();\n    setSiteLanguage(currentSiteLang);"
    if init_pattern in html and 'setSiteLanguage(currentSiteLang);' not in html:
        html = html.replace(init_pattern, new_init, 1)
        print("Added setSiteLanguage initial invocation")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Bilingual website internationalization successfully applied to index.html!")

if __name__ == '__main__':
    update_portfolio_bilingual()
