# -*- coding: utf-8 -*-
"""
generate_enhanced_portfolio.py
Updates index.html with:
1. Updated navigation (Desktop & Mobile drawer) with #executive-assets
2. Updated hero section with primary CTAs for CV & Decks
3. New #executive-assets section replacing old download section:
   - English CV (.docx and .pdf)
   - Arabic CV (.pdf)
   - English Presentation Deck (.pptx, 22 slides)
   - Arabic Presentation Deck (.pptx, 22 slides)
   - Supplementary Decks
4. Interactive CV Modal (#cvModal) with bilingual support & page switcher
5. Interactive Presentation Deck Modal (#deckModal) with 22 slides & live EN/AR toggle
6. JavaScript state management and event listeners
"""

import json
import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Desktop Navbar
    nav_creatives = '<a href="#creatives" class="hover:text-indigo-400 transition-colors flex items-center gap-1.5">'
    exec_nav_link = """<a href="#executive-assets" class="hover:text-amber-400 transition-colors flex items-center gap-1.5 text-amber-300 font-bold px-2.5 py-1 rounded-lg bg-amber-500/10 border border-amber-500/30 shadow-sm shadow-amber-500/10">
          <i class="fa-solid fa-file-shield text-[11px] text-amber-400"></i>
          <span>CV & Decks</span>
          <span class="px-1.5 py-0.5 rounded bg-amber-400 text-slate-950 text-[9px] font-black uppercase tracking-wider">New</span>
        </a>
        <a href="#creatives" class="hover:text-indigo-400 transition-colors flex items-center gap-1.5">"""
    
    if nav_creatives in html and 'href="#executive-assets"' not in html:
        html = html.replace(nav_creatives, exec_nav_link, 1)
        print("Updated desktop navbar")

    # 2. Update Mobile Menu Drawer
    mobile_creatives = '<a href="#creatives" onclick="closeMobileMenu()"'
    exec_mobile_link = """<a href="#executive-assets" onclick="closeMobileMenu()" class="flex items-center justify-between p-2.5 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 text-xs font-bold text-amber-300 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-file-shield"></i>
            </span>
            <span>Executive CV & Decks</span>
          </span>
          <span class="px-2 py-0.5 rounded-md bg-amber-400 text-slate-950 text-[10px] font-black">EN & AR</span>
        </a>

        <a href="#creatives" onclick="closeMobileMenu()\""""
    
    if mobile_creatives in html and 'Executive CV & Decks' not in html:
        html = html.replace(mobile_creatives, exec_mobile_link, 1)
        print("Updated mobile navbar drawer")

    # 3. Update Hero Section CTAs
    hero_p_end = 'turning erratic ad spend into measurable, scalable pipeline revenue.\n    </p>'
    if hero_p_end not in html:
        match = re.search(r'turning erratic ad spend into measurable, scalable pipeline revenue\.\s*</p>', html)
        if match:
            hero_p_end = match.group(0)

    hero_cta_block = hero_p_end + """

    <!-- High-Impact Executive CTAs & Availability Trust Pill -->
    <div class="mt-7 flex flex-wrap items-center justify-center gap-3 max-w-2xl mx-auto">
      <button onclick="openCvModal('en', 1)" class="px-5 py-3 rounded-xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:from-blue-500 hover:to-indigo-500 text-white font-bold text-xs sm:text-sm shadow-xl shadow-blue-500/25 flex items-center gap-2.5 transition-all transform hover:-translate-y-0.5">
        <i class="fa-solid fa-file-pdf text-rose-300 text-sm"></i>
        <span>Explore Executive CV (EN/AR)</span>
      </button>

      <button onclick="openDeckModal('en', 1)" class="px-5 py-3 rounded-xl bg-slate-900/90 hover:bg-slate-800 text-slate-200 hover:text-cyan-300 border border-slate-700/80 font-bold text-xs sm:text-sm shadow-lg flex items-center gap-2.5 transition-all transform hover:-translate-y-0.5">
        <i class="fa-solid fa-presentation-screen text-cyan-400 text-sm"></i>
        <span>View 22-Slide Decks</span>
      </button>

      <a href="#audit" class="px-5 py-3 rounded-xl bg-emerald-500/15 hover:bg-emerald-500/25 text-emerald-300 border border-emerald-500/40 font-bold text-xs sm:text-sm flex items-center gap-2 transition-all">
        <i class="fa-solid fa-bolt text-emerald-400"></i>
        <span>Free Teardown Audit</span>
      </a>
    </div>

    <!-- Gulf & Global Readiness Pill -->
    <div class="mt-4 flex items-center justify-center gap-2 text-[11px] text-slate-400">
      <i class="fa-solid fa-globe text-cyan-400 text-[10px]"></i>
      <span>Available for GCC (Riyadh, KSA) & Global High-Ticket Engagements</span>
      <span class="text-slate-600">&bull;</span>
      <span class="text-emerald-400 font-semibold"><i class="fa-solid fa-check text-[10px] mr-1"></i>Bilingual Strategy (English & العربية)</span>
    </div>"""

    if 'Explore Executive CV (EN/AR)' not in html and hero_p_end in html:
        html = html.replace(hero_p_end, hero_cta_block, 1)
        print("Updated hero CTAs")

    # 4. Replace old download section with the new #executive-assets section
    old_download_regex = r'<!-- Downloadable Presentation Decks -->\s*<section[\s\S]*?</section>'
    
    new_executive_assets_section = """<!-- Executive Assets & Bilingual Presentation Vault -->
  <section id="executive-assets" class="max-w-7xl mx-auto py-14 px-4 sm:px-6 w-full border-t border-slate-800/80">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10">
      <div>
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-md bg-amber-500/10 text-amber-400 text-xs font-bold uppercase tracking-wider border border-amber-500/20 mb-3 shadow-sm shadow-amber-500/10">
          <i class="fa-solid fa-file-shield text-amber-400"></i> Executive Assets & Bilingual Credentials
        </div>
        <h2 class="text-2xl sm:text-4xl font-display font-black text-white tracking-tight">
          Executive CV & Growth Architecture Slide Decks
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-2 max-w-2xl leading-relaxed">
          Directly inspect and download Tipu Sultan's verified Curriculum Vitae (in English & Arabic) and comprehensive 22-slide strategic presentation decks — engineered for high-ticket GCC brands, DTC founders, and venture-backed companies.
        </p>
      </div>

      <!-- Filter Controls for Assets -->
      <div class="flex flex-wrap items-center gap-2" id="asset-filter-buttons">
        <button onclick="filterAssets('all', this)" class="asset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-500 text-slate-950 shadow-md shadow-amber-500/30">
          All Assets (4)
        </button>
        <button onclick="filterAssets('cv', this)" class="asset-btn px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
          <i class="fa-solid fa-id-card mr-1 text-blue-400"></i> Curriculum Vitae (EN & AR)
        </button>
        <button onclick="filterAssets('decks', this)" class="asset-btn px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
          <i class="fa-solid fa-presentation-screen mr-1 text-cyan-400"></i> 22-Slide Decks
        </button>
      </div>
    </div>

    <!-- 4 Featured Executive Asset Cards Grid -->
    <div id="assets-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

      <!-- Asset 1: English Executive CV -->
      <div class="asset-card glass-card rounded-2xl border border-slate-800 hover:border-blue-500/50 p-5 flex flex-col justify-between transition-all group relative overflow-hidden" data-category="cv">
        <div class="absolute -right-16 -top-16 w-32 h-32 bg-blue-600/10 rounded-full blur-2xl pointer-events-none"></div>
        <div>
          <!-- Top Badges -->
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="px-2.5 py-0.5 rounded-full bg-blue-500/10 border border-blue-500/30 text-blue-400 text-[10px] font-black uppercase tracking-wider">
              Official CV • 2 Pages
            </span>
            <span class="text-[10px] text-slate-400 font-semibold flex items-center gap-1">
              <i class="fa-solid fa-check-double text-emerald-400"></i> Verified
            </span>
          </div>

          <!-- Preview Container -->
          <div class="relative h-56 rounded-xl overflow-hidden bg-slate-950 border border-slate-800/80 group-hover:border-blue-500/30 transition-all cursor-pointer mb-4" onclick="openCvModal('en', 1)">
            <img src="assets/documents/cv-card-preview-1.webp" alt="Tipu Sultan Growth Architect CV" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/30 to-transparent flex items-end justify-center p-3">
              <button class="px-3.5 py-1.5 rounded-lg bg-blue-600/90 hover:bg-blue-500 text-white text-xs font-bold shadow-lg flex items-center gap-1.5 transform group-hover:-translate-y-1 transition-all">
                <i class="fa-solid fa-eye text-[11px]"></i> Interactive Preview
              </button>
            </div>
            <span class="absolute top-2 left-2 bg-slate-900/85 backdrop-blur-md px-2 py-0.5 rounded text-[10px] font-bold text-slate-300 border border-slate-700/60">
              Page 1 of 2
            </span>
          </div>

          <!-- Title & Subtitle -->
          <h3 class="text-base font-display font-bold text-white group-hover:text-blue-400 transition-colors">
            Tipu Sultan — Executive CV (EN)
          </h3>
          <p class="text-xs text-slate-400 mt-1 line-clamp-2">
            AI-Driven & Data-Driven Growth Architect | High-Ticket Performance Marketer
          </p>

          <!-- Metric Pills -->
          <div class="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-800/80">
            <div class="bg-slate-900/80 rounded-lg p-2 text-center border border-slate-800">
              <span class="text-[10px] text-slate-400 block font-semibold">Managed Spend</span>
              <span class="text-xs font-bold text-white">$188K+</span>
            </div>
            <div class="bg-slate-900/80 rounded-lg p-2 text-center border border-slate-800">
              <span class="text-[10px] text-slate-400 block font-semibold">Blended ROAS</span>
              <span class="text-xs font-bold text-emerald-400">4.6x</span>
            </div>
          </div>
        </div>

        <!-- Download Buttons -->
        <div class="mt-5 pt-3 border-t border-slate-800/80 flex flex-col gap-2">
          <button onclick="openCvModal('en', 1)" class="w-full py-2 rounded-xl bg-blue-600/20 hover:bg-blue-600 text-blue-300 hover:text-white border border-blue-500/40 text-xs font-bold flex items-center justify-center gap-1.5 transition-all">
            <i class="fa-solid fa-expand text-[10px]"></i> View Fullscreen CV
          </button>
          <div class="grid grid-cols-2 gap-2">
            <a href="assets/documents/Tipu-Sultan-Growth-Architect-CV.pdf" download class="py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-[11px] font-bold text-slate-200 flex items-center justify-center gap-1.5 transition-all">
              <i class="fa-solid fa-file-pdf text-rose-400 text-xs"></i> PDF
            </a>
            <a href="assets/documents/Tipu-Sultan-Growth-Architect-CV.docx" download class="py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-[11px] font-bold text-slate-200 flex items-center justify-center gap-1.5 transition-all">
              <i class="fa-solid fa-file-word text-blue-400 text-xs"></i> Word (.docx)
            </a>
          </div>
        </div>
      </div>

      <!-- Asset 2: Arabic Executive CV -->
      <div class="asset-card glass-card rounded-2xl border border-slate-800 hover:border-emerald-500/50 p-5 flex flex-col justify-between transition-all group relative overflow-hidden" data-category="cv">
        <div class="absolute -right-16 -top-16 w-32 h-32 bg-emerald-600/10 rounded-full blur-2xl pointer-events-none"></div>
        <div>
          <!-- Top Badges -->
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-[10px] font-black uppercase tracking-wider">
              النسخة العربية • 3 صفحات
            </span>
            <span class="text-[10px] text-slate-400 font-semibold flex items-center gap-1">
              <i class="fa-solid fa-certificate text-emerald-400"></i> موثقة تجريبياً
            </span>
          </div>

          <!-- Preview Container -->
          <div class="relative h-56 rounded-xl overflow-hidden bg-slate-950 border border-slate-800/80 group-hover:border-emerald-500/30 transition-all cursor-pointer mb-4" onclick="openCvModal('ar', 1)">
            <img src="assets/documents/cv-ar-card-preview-1.webp" alt="السيرة الذاتية تيبو سلطان" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/30 to-transparent flex items-end justify-center p-3">
              <button class="px-3.5 py-1.5 rounded-lg bg-emerald-600/90 hover:bg-emerald-500 text-white text-xs font-bold shadow-lg flex items-center gap-1.5 transform group-hover:-translate-y-1 transition-all">
                <i class="fa-solid fa-eye text-[11px]"></i> معاينة السيرة الذاتية
              </button>
            </div>
            <span class="absolute top-2 left-2 bg-slate-900/85 backdrop-blur-md px-2 py-0.5 rounded text-[10px] font-bold text-slate-300 border border-slate-700/60">
              الصفحة 1 من 3
            </span>
          </div>

          <!-- Title & Subtitle -->
          <h3 class="text-base font-display font-bold text-white group-hover:text-emerald-400 transition-colors">
            تيبو سلطان — السيرة الذاتية (AR)
          </h3>
          <p class="text-xs text-slate-400 mt-1 line-clamp-2">
            مهندس نمو بالذكاء الاصطناعي والبيانات | مسوّق أداء عالي القيمة (السوق السعودي والخليج)
          </p>

          <!-- Metric Pills -->
          <div class="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-800/80">
            <div class="bg-slate-900/80 rounded-lg p-2 text-center border border-slate-800">
              <span class="text-[10px] text-slate-400 block font-semibold">إنفاق إعلاني</span>
              <span class="text-xs font-bold text-white">$188K+</span>
            </div>
            <div class="bg-slate-900/80 rounded-lg p-2 text-center border border-slate-800">
              <span class="text-[10px] text-slate-400 block font-semibold">عائد مدمج</span>
              <span class="text-xs font-bold text-emerald-400">4.6x</span>
            </div>
          </div>
        </div>

        <!-- Download Buttons -->
        <div class="mt-5 pt-3 border-t border-slate-800/80 flex flex-col gap-2">
          <button onclick="openCvModal('ar', 1)" class="w-full py-2 rounded-xl bg-emerald-600/20 hover:bg-emerald-600 text-emerald-300 hover:text-white border border-emerald-500/40 text-xs font-bold flex items-center justify-center gap-1.5 transition-all">
            <i class="fa-solid fa-expand text-[10px]"></i> معاينة السيرة الذاتية كاملة
          </button>
          <a href="assets/documents/Tipu-Sultan-Growth-Architect-CV-AR.pdf" download class="w-full py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-[11px] font-bold text-slate-200 flex items-center justify-center gap-1.5 transition-all">
            <i class="fa-solid fa-file-pdf text-rose-400 text-xs"></i> تحميل السيرة الذاتية PDF (عربي)
          </a>
        </div>
      </div>

      <!-- Asset 3: Arabic Presentation Deck -->
      <div class="asset-card glass-card rounded-2xl border border-slate-800 hover:border-amber-500/50 p-5 flex flex-col justify-between transition-all group relative overflow-hidden" data-category="decks">
        <div class="absolute -right-16 -top-16 w-32 h-32 bg-amber-600/10 rounded-full blur-2xl pointer-events-none"></div>
        <div>
          <!-- Top Badges -->
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="px-2.5 py-0.5 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-[10px] font-black uppercase tracking-wider">
              ARABIC / GCC • 22 SLIDES
            </span>
            <span class="text-[10px] text-amber-400 font-semibold flex items-center gap-1">
              <i class="fa-solid fa-bolt"></i> SAR 1.4M+
            </span>
          </div>

          <!-- Preview Container -->
          <div class="relative h-56 rounded-xl overflow-hidden bg-slate-950 border border-slate-800/80 group-hover:border-amber-500/30 transition-all cursor-pointer mb-4" onclick="openDeckModal('ar', 1)">
            <img src="assets/documents/deck-cover-ar-preview.webp" alt="عروض محفظة الأعمال تيبو سلطان" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent flex items-end justify-center p-3">
              <button class="px-3.5 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-black shadow-lg flex items-center gap-1.5 transform group-hover:-translate-y-1 transition-all">
                <i class="fa-solid fa-play text-[11px]"></i> استعراض 22 شريحة
              </button>
            </div>
            <span class="absolute top-2 left-2 bg-slate-900/85 backdrop-blur-md px-2 py-0.5 rounded text-[10px] font-bold text-amber-300 border border-amber-500/40">
              عروض الخليج والسعودية
            </span>
          </div>

          <!-- Title & Subtitle -->
          <h3 class="text-base font-display font-bold text-white group-hover:text-amber-400 transition-colors">
            عروض محفظة الأعمال — 22 شريحة
          </h3>
          <p class="text-xs text-slate-400 mt-1 line-clamp-2">
            هندسة إعلانات بالذكاء الاصطناعي والتجارة الخليجية (Tabby، Tamara، واتساب COD)
          </p>

          <!-- Metric Pills -->
          <div class="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-800/80">
            <div class="bg-slate-900/80 rounded-lg p-2 text-center border border-slate-800">
              <span class="text-[10px] text-slate-400 block font-semibold">إيرادات موثقة</span>
              <span class="text-xs font-bold text-amber-400">1.4M+ SAR</span>
            </div>
            <div class="bg-slate-900/80 rounded-lg p-2 text-center border border-slate-800">
              <span class="text-[10px] text-slate-400 block font-semibold">ذروة العائد</span>
              <span class="text-xs font-bold text-emerald-400">6.4x ROAS</span>
            </div>
          </div>
        </div>

        <!-- Download Buttons -->
        <div class="mt-5 pt-3 border-t border-slate-800/80 flex flex-col gap-2">
          <button onclick="openDeckModal('ar', 1)" class="w-full py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500 text-amber-300 hover:text-slate-950 border border-amber-500/40 text-xs font-bold flex items-center justify-center gap-1.5 transition-all">
            <i class="fa-solid fa-presentation-screen text-[10px]"></i> عرض الشرائح التفاعلي
          </button>
          <a href="assets/documents/tipu-sultan-portfolio-ar.pptx" download class="w-full py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-[11px] font-bold text-slate-200 flex items-center justify-center gap-1.5 transition-all">
            <i class="fa-solid fa-file-powerpoint text-amber-400 text-xs"></i> تحميل العرض (.pptx 10.2 MB)
          </a>
        </div>
      </div>

      <!-- Asset 4: English Presentation Deck -->
      <div class="asset-card glass-card rounded-2xl border border-slate-800 hover:border-cyan-500/50 p-5 flex flex-col justify-between transition-all group relative overflow-hidden" data-category="decks">
        <div class="absolute -right-16 -top-16 w-32 h-32 bg-cyan-600/10 rounded-full blur-2xl pointer-events-none"></div>
        <div>
          <!-- Top Badges -->
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="px-2.5 py-0.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-[10px] font-black uppercase tracking-wider">
              GLOBAL ENGLISH • 22 SLIDES
            </span>
            <span class="text-[10px] text-cyan-400 font-semibold flex items-center gap-1">
              <i class="fa-solid fa-microchip"></i> Full-Funnel
            </span>
          </div>

          <!-- Preview Container -->
          <div class="relative h-56 rounded-xl overflow-hidden bg-slate-950 border border-slate-800/80 group-hover:border-cyan-500/30 transition-all cursor-pointer mb-4" onclick="openDeckModal('en', 1)">
            <img src="assets/documents/deck-cover-en-preview.webp" alt="Performance Architecture Deck" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent flex items-end justify-center p-3">
              <button class="px-3.5 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-slate-950 text-xs font-black shadow-lg flex items-center gap-1.5 transform group-hover:-translate-y-1 transition-all">
                <i class="fa-solid fa-play text-[11px]"></i> Launch 22 Slides
              </button>
            </div>
            <span class="absolute top-2 left-2 bg-slate-900/85 backdrop-blur-md px-2 py-0.5 rounded text-[10px] font-bold text-cyan-300 border border-cyan-500/40">
              Global DTC & B2B
            </span>
          </div>

          <!-- Title & Subtitle -->
          <h3 class="text-base font-display font-bold text-white group-hover:text-cyan-400 transition-colors">
            Performance Architecture Deck (EN)
          </h3>
          <p class="text-xs text-slate-400 mt-1 line-clamp-2">
            Next-Gen AI & Data-Engineered Paid Acquisition Systems across Meta, Google & YouTube
          </p>

          <!-- Metric Pills -->
          <div class="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-800/80">
            <div class="bg-slate-900/80 rounded-lg p-2 text-center border border-slate-800">
              <span class="text-[10px] text-slate-400 block font-semibold">Search IS</span>
              <span class="text-xs font-bold text-cyan-400">86.4%</span>
            </div>
            <div class="bg-slate-900/80 rounded-lg p-2 text-center border border-slate-800">
              <span class="text-[10px] text-slate-400 block font-semibold">Cold CPA</span>
              <span class="text-xs font-bold text-emerald-400">&lt;$15 CPA</span>
            </div>
          </div>
        </div>

        <!-- Download Buttons -->
        <div class="mt-5 pt-3 border-t border-slate-800/80 flex flex-col gap-2">
          <button onclick="openDeckModal('en', 1)" class="w-full py-2 rounded-xl bg-cyan-600/20 hover:bg-cyan-600 text-cyan-300 hover:text-slate-950 border border-cyan-500/40 text-xs font-bold flex items-center justify-center gap-1.5 transition-all">
            <i class="fa-solid fa-presentation-screen text-[10px]"></i> Interactive Deck Viewer
          </button>
          <a href="assets/documents/tipu-sultan-portfolio-en.pptx" download class="w-full py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-[11px] font-bold text-slate-200 flex items-center justify-center gap-1.5 transition-all">
            <i class="fa-solid fa-file-powerpoint text-cyan-400 text-xs"></i> Download PPTX (.pptx 10.3 MB)
          </a>
        </div>
      </div>

    </div>

    <!-- Supplementary Focused Strategy Decks Drawer -->
    <div class="glass-card rounded-2xl p-5 sm:p-6 border border-slate-800/90 mt-8 flex flex-col md:flex-row items-center justify-between gap-5 bg-gradient-to-r from-slate-950/60 to-slate-900/60">
      <div class="flex items-center gap-4">
        <div class="w-11 h-11 rounded-xl bg-teal-500/10 border border-teal-500/30 text-teal-400 flex items-center justify-center text-lg flex-shrink-0">
          <i class="fa-solid fa-folder-open"></i>
        </div>
        <div>
          <h4 class="text-sm sm:text-base font-display font-bold text-white flex items-center gap-2">
            <span>Supplementary Deep-Dive Presentations</span>
            <span class="text-[10px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded-full border border-slate-700 font-semibold">3 More Decks</span>
          </h4>
          <p class="text-xs text-slate-400 mt-0.5">
            Download channel-specific architectural teardowns and campaign post-mortems for stakeholder review.
          </p>
        </div>
      </div>

      <div class="flex flex-wrap gap-2.5">
        <a href="assets/documents/google-ads-performance-portfolio-deck.pptx" download class="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-200 flex items-center gap-2 transition-all">
          <i class="fa-solid fa-download text-teal-400"></i> Google Ads Deck (.pptx)
        </a>
        <a href="assets/documents/growth-marketing-case-studies-deck-vol1.pptx" download class="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-200 flex items-center gap-2 transition-all">
          <i class="fa-solid fa-download text-blue-400"></i> Case Studies Vol 1 (.pptx)
        </a>
        <a href="assets/documents/growth-marketing-case-studies-deck-vol2.pptx" download class="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-200 flex items-center gap-2 transition-all">
          <i class="fa-solid fa-download text-emerald-400"></i> Case Studies Vol 2 (.pptx)
        </a>
      </div>
    </div>
  </section>"""

    if re.search(old_download_regex, html):
        html = re.sub(old_download_regex, new_executive_assets_section, html, count=1)
        print("Replaced old download section with new #executive-assets section")

    # 5. Add Modals: #cvModal and #deckModal right before </body>
    modals_html = """  <!-- Interactive CV Viewer Modal (Bilingual: English 2 Pages & Arabic 3 Pages) -->
  <div id="cvModal" class="fixed inset-0 z-50 glass bg-slate-950/90 backdrop-blur-2xl hidden flex items-center justify-center p-2 sm:p-4 overflow-y-auto">
    <div class="relative w-full max-w-6xl bg-slate-900 border border-slate-700 rounded-3xl shadow-2xl overflow-hidden my-auto flex flex-col max-h-[95vh]">
      
      <!-- Modal Top Header -->
      <div class="px-5 py-4 border-b border-slate-800 flex flex-wrap items-center justify-between gap-4 bg-slate-950/80">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-400 flex items-center justify-center text-base">
            <i class="fa-solid fa-file-pdf"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-display font-bold text-sm text-white" id="cvModalTitle">Tipu Sultan — Executive CV</span>
              <span id="cvLangBadge" class="px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/30 text-[10px] font-black uppercase">English</span>
            </div>
            <p class="text-[11px] text-slate-400" id="cvModalSubtitle">AI-Driven & Data-Driven Growth Architect | Riyadh, KSA</p>
          </div>
        </div>

        <!-- Controls: Language Toggle & Page Selector -->
        <div class="flex flex-wrap items-center gap-2">
          <!-- Language Switcher -->
          <div class="inline-flex rounded-xl bg-slate-950 border border-slate-800 p-1">
            <button id="cvLangEnBtn" onclick="switchCvLang('en')" class="px-3 py-1 rounded-lg text-xs font-bold bg-blue-600 text-white transition-all">
              English (2P)
            </button>
            <button id="cvLangArBtn" onclick="switchCvLang('ar')" class="px-3 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all">
              العربية (3 صفحات)
            </button>
          </div>

          <!-- Page Navigation Tabs -->
          <div id="cvPageTabs" class="inline-flex rounded-xl bg-slate-950 border border-slate-800 p-1">
            <!-- Dynamically injected -->
          </div>

          <!-- Download Action Dropdown/Buttons -->
          <div class="flex items-center gap-1.5" id="cvDownloadActions">
            <!-- Dynamically populated according to active language -->
          </div>

          <!-- Close Button -->
          <button onclick="closeCvModal()" class="w-9 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center transition-all ml-1">
            <i class="fa-solid fa-xmark text-sm"></i>
          </button>
        </div>
      </div>

      <!-- Modal Body (Two-Column on Desktop: Viewer + Executive Snapshot) -->
      <div class="flex-1 overflow-y-auto flex flex-col lg:flex-row">
        <!-- Main Document Visual Viewer -->
        <div class="flex-1 bg-slate-950 p-4 sm:p-6 flex flex-col items-center justify-start overflow-auto min-h-[500px]">
          <div class="relative max-w-3xl w-full rounded-2xl overflow-hidden shadow-2xl border border-slate-800 bg-white group">
            <img id="cvViewerImg" src="assets/documents/cv-preview-page-1.webp" alt="CV Page Preview" class="w-full h-auto object-contain transition-transform duration-200" />
          </div>
          <!-- Bottom Page Controls inside Viewer -->
          <div class="flex items-center gap-3 mt-4">
            <button onclick="prevCvPage()" class="px-3.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-300 flex items-center gap-1.5 transition-all">
              <i class="fa-solid fa-chevron-left text-[10px]"></i> Previous Page
            </button>
            <span id="cvPageIndicator" class="text-xs font-bold text-slate-400 px-3 py-1 rounded-lg bg-slate-900 border border-slate-800">
              Page 1 of 2
            </span>
            <button onclick="nextCvPage()" class="px-3.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-300 flex items-center gap-1.5 transition-all">
              Next Page <i class="fa-solid fa-chevron-right text-[10px]"></i>
            </button>
          </div>
        </div>

        <!-- Sidebar Snapshot & Verified Highlights -->
        <div class="w-full lg:w-80 border-t lg:border-t-0 lg:border-l border-slate-800 bg-slate-900/90 p-5 flex flex-col justify-between">
          <div>
            <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-3 flex items-center gap-2">
              <i class="fa-solid fa-shield-halved text-emerald-400"></i> Executive Highlights
            </div>

            <!-- Stats Mini Grid -->
            <div class="grid grid-cols-2 gap-2 mb-4">
              <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 block">Managed Spend</span>
                <span class="text-sm font-bold text-white">$188K+</span>
              </div>
              <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 block">Tracked Revenue</span>
                <span class="text-sm font-bold text-white">$869K+</span>
              </div>
              <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 block">Blended ROAS</span>
                <span class="text-sm font-bold text-emerald-400">4.6x</span>
              </div>
              <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 block">Verified Proofs</span>
                <span class="text-sm font-bold text-blue-400">59 Proofs</span>
              </div>
            </div>

            <!-- Core Competencies -->
            <div class="space-y-2 mb-4">
              <div class="text-[11px] font-bold text-slate-300">Core Architecture:</div>
              <ul class="text-[11px] text-slate-400 space-y-1.5">
                <li class="flex items-start gap-1.5">
                  <i class="fa-solid fa-check text-emerald-400 mt-0.5 text-[10px]"></i>
                  <span><strong>Predictive AI Bidding:</strong> Meta Advantage+ Shopping (ASC) & Google Smart Bidding</span>
                </li>
                <li class="flex items-start gap-1.5">
                  <i class="fa-solid fa-check text-cyan-400 mt-0.5 text-[10px]"></i>
                  <span><strong>Signal Engineering:</strong> Server-Side CAPI Gateway with 9.0+ EMQ & SHA-256</span>
                </li>
                <li class="flex items-start gap-1.5">
                  <i class="fa-solid fa-check text-purple-400 mt-0.5 text-[10px]"></i>
                  <span><strong>3:2:2 Creative Sandbox:</strong> 48-Angle dynamic testing before scaling</span>
                </li>
                <li class="flex items-start gap-1.5">
                  <i class="fa-solid fa-check text-amber-400 mt-0.5 text-[10px]"></i>
                  <span><strong>GCC Specialization:</strong> Tabby/Tamara BNPL & WhatsApp COD automation</span>
                </li>
              </ul>
            </div>

            <!-- Location & Availability -->
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-[11px] text-slate-400 mb-4">
              <div class="font-bold text-slate-300 mb-1 flex items-center gap-1.5">
                <i class="fa-solid fa-location-dot text-cyan-400"></i> Riyadh, Saudi Arabia
              </div>
              <p>Available for 10-minute video audits, full-funnel buildouts, and scaling retainers worldwide.</p>
            </div>
          </div>

          <!-- Direct Inquiries CTA -->
          <div class="pt-3 border-t border-slate-800 space-y-2">
            <button onclick="triggerGlobalWhatsApp()" class="w-full py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/20 transition-all">
              <i class="fa-brands fa-whatsapp text-sm"></i> Inquire via WhatsApp
            </button>
            <button onclick="closeCvModal(); document.getElementById('audit').scrollIntoView({behavior: 'smooth'});" class="w-full py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs border border-slate-700 flex items-center justify-center gap-1.5 transition-all">
              <i class="fa-solid fa-bolt text-emerald-400 text-[10px]"></i> Request Ad Account Audit
            </button>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- Interactive Presentation Deck Viewer Modal (22 Slides Bilingual: EN & AR) -->
  <div id="deckModal" class="fixed inset-0 z-50 glass bg-slate-950/95 backdrop-blur-2xl hidden flex items-center justify-center p-2 sm:p-4 overflow-y-auto">
    <div class="relative w-full max-w-6xl bg-slate-900 border border-slate-700 rounded-3xl shadow-2xl overflow-hidden my-auto flex flex-col max-h-[96vh]">
      
      <!-- Deck Modal Top Bar -->
      <div class="px-5 py-3.5 border-b border-slate-800 flex flex-wrap items-center justify-between gap-4 bg-slate-950/90">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 flex items-center justify-center text-base">
            <i class="fa-solid fa-presentation-screen"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-display font-bold text-sm text-white" id="deckHeaderTitle">Growth Architecture Deck</span>
              <span id="deckSlideCounterBadge" class="px-2 py-0.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-[10px] font-black">Slide 01 / 22</span>
            </div>
            <p class="text-[11px] text-slate-400" id="deckHeaderSubtitle">Tipu Sultan • Next-Gen AI & Data Performance Architecture</p>
          </div>
        </div>

        <!-- Controls: Language Toggle, Download PPTX, Fullscreen, Close -->
        <div class="flex items-center gap-2">
          <!-- Language Switcher -->
          <div class="inline-flex rounded-xl bg-slate-950 border border-slate-800 p-1">
            <button id="deckLangEnBtn" onclick="switchDeckLang('en')" class="px-3 py-1 rounded-lg text-xs font-bold bg-cyan-600 text-slate-950 transition-all">
              English [EN]
            </button>
            <button id="deckLangArBtn" onclick="switchDeckLang('ar')" class="px-3 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all">
              العربية [AR]
            </button>
          </div>

          <!-- Download PPTX button -->
          <a id="deckDownloadBtn" href="assets/documents/tipu-sultan-portfolio-en.pptx" download class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-bold flex items-center gap-1.5 transition-all">
            <i class="fa-solid fa-file-powerpoint text-amber-400"></i>
            <span class="hidden sm:inline">Download Deck</span>
          </a>

          <!-- Close Modal -->
          <button onclick="closeDeckModal()" class="w-9 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center transition-all ml-1">
            <i class="fa-solid fa-xmark text-sm"></i>
          </button>
        </div>
      </div>

      <!-- Slide Presentation Stage Canvas (16:9 ratio) -->
      <div class="flex-1 bg-slate-950 p-4 sm:p-8 flex items-center justify-center overflow-y-auto min-h-[460px]">
        <div id="deckSlideCard" class="relative w-full max-w-4xl aspect-[16/9] min-h-[400px] rounded-3xl p-6 sm:p-10 border border-slate-800 bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 shadow-2xl flex flex-col justify-between overflow-hidden">
          
          <!-- Decorative Background Blur -->
          <div class="absolute -right-20 -top-20 w-60 h-60 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
          <div class="absolute -left-20 -bottom-20 w-60 h-60 bg-blue-600/10 rounded-full blur-3xl pointer-events-none"></div>

          <!-- Slide Category & Counter -->
          <div class="relative z-10 flex items-center justify-between">
            <span id="deckSlideCategory" class="px-3 py-1 rounded-md bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 text-xs font-bold uppercase tracking-wider">
              PORTFOLIO PRESENTATION
            </span>
            <span id="deckSlideNumberText" class="text-xs font-display font-bold text-slate-500">
              01 / 22
            </span>
          </div>

          <!-- Slide Core Content Area -->
          <div class="relative z-10 my-auto py-4">
            <h2 id="deckSlideTitle" class="text-xl sm:text-3xl lg:text-4xl font-display font-black text-white tracking-tight leading-tight">
              Scale Predictable Revenue with AI-Driven & Data-Engineered Ad Architecture
            </h2>
            <div id="deckSlideSubtitle" class="text-sm sm:text-base text-cyan-400 font-semibold mt-2">
              Next-Gen Growth Architecture
            </div>

            <!-- Bullet Points / Breakdown List -->
            <div id="deckSlideBullets" class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mt-5">
              <!-- Dynamically populated -->
            </div>

            <!-- Optional Slide Image Thumbnail -->
            <div id="deckSlideImageContainer" class="mt-4 hidden">
              <img id="deckSlideImage" src="" alt="Slide Evidence" class="h-28 rounded-xl object-contain border border-slate-800 bg-slate-950 p-1" />
            </div>
          </div>

          <!-- Slide Footer inside Card -->
          <div class="relative z-10 flex items-center justify-between pt-3 border-t border-slate-800/80 text-[11px] text-slate-400">
            <span class="flex items-center gap-1.5">
              <i class="fa-solid fa-circle-check text-emerald-400"></i> Tipu Sultan • Empirical Evidence Vault
            </span>
            <span class="text-slate-500">Riyadh, KSA • sultantipu199.github.io/sultan-growth</span>
          </div>

        </div>
      </div>

      <!-- Slide Navigation Bottom Controller -->
      <div class="px-5 py-3 border-t border-slate-800 bg-slate-950 flex flex-wrap items-center justify-between gap-4">
        <!-- Prev Slide Button -->
        <button onclick="prevDeckSlide()" class="px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 border border-slate-700 text-xs font-bold flex items-center gap-2 transition-all">
          <i class="fa-solid fa-chevron-left text-[10px]"></i>
          <span>Previous</span>
        </button>

        <!-- Slide Number Quick Selector Strip -->
        <div id="deckSlideSelectorStrip" class="flex items-center gap-1 overflow-x-auto max-w-md py-1 custom-scrollbar">
          <!-- 22 buttons injected by JS -->
        </div>

        <!-- Next Slide Button -->
        <button onclick="nextDeckSlide()" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-black text-xs flex items-center gap-2 shadow-lg shadow-cyan-600/20 transition-all">
          <span>Next</span>
          <i class="fa-solid fa-chevron-right text-[10px]"></i>
        </button>
      </div>

    </div>
  </div>
"""

    if 'id="cvModal"' not in html:
        html = html.replace('</body>', modals_html + '\n</body>', 1)
        print("Inserted #cvModal and #deckModal")

    # 6. Insert JavaScript handlers and Presentation Decks data
    from build_executive_assets_update import build_update
    decks_js_data = build_update()

    executive_scripts = """
    // ==========================================
    // EXECUTIVE ASSETS, CV & DECK MODAL HANDLERS
    // ==========================================
""" + decks_js_data + """

    // Current State for CV Viewer
    let currentCvLang = 'en';
    let currentCvPage = 1;
    const cvMaxPages = { en: 2, ar: 3 };

    function openCvModal(lang = 'en', page = 1) {
      currentCvLang = lang;
      currentCvPage = page;
      updateCvModalUI();
      document.getElementById('cvModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }

    function closeCvModal() {
      document.getElementById('cvModal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }

    function switchCvLang(lang) {
      currentCvLang = lang;
      currentCvPage = 1;
      updateCvModalUI();
    }

    function setCvPage(page) {
      const maxP = cvMaxPages[currentCvLang] || 2;
      if (page >= 1 && page <= maxP) {
        currentCvPage = page;
        updateCvModalUI();
      }
    }

    function nextCvPage() {
      const maxP = cvMaxPages[currentCvLang] || 2;
      if (currentCvPage < maxP) {
        currentCvPage++;
        updateCvModalUI();
      }
    }

    function prevCvPage() {
      if (currentCvPage > 1) {
        currentCvPage--;
        updateCvModalUI();
      }
    }

    function updateCvModalUI() {
      const maxP = cvMaxPages[currentCvLang];
      const enBtn = document.getElementById('cvLangEnBtn');
      const arBtn = document.getElementById('cvLangArBtn');
      const badge = document.getElementById('cvLangBadge');
      const title = document.getElementById('cvModalTitle');
      const subtitle = document.getElementById('cvModalSubtitle');
      const img = document.getElementById('cvViewerImg');
      const indicator = document.getElementById('cvPageIndicator');
      const pageTabs = document.getElementById('cvPageTabs');
      const actions = document.getElementById('cvDownloadActions');

      if (currentCvLang === 'en') {
        enBtn.className = 'px-3 py-1 rounded-lg text-xs font-bold bg-blue-600 text-white transition-all shadow-md';
        arBtn.className = 'px-3 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all';
        badge.className = 'px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/30 text-[10px] font-black uppercase';
        badge.innerText = 'English';
        title.innerText = 'Tipu Sultan — Executive CV (EN)';
        subtitle.innerText = 'AI-Driven & Data-Driven Growth Architect | High-Ticket Performance Marketer';
        img.src = `assets/documents/cv-preview-page-${currentCvPage}.webp`;
        indicator.innerText = `Page ${currentCvPage} of ${maxP}`;

        // Page tabs
        pageTabs.innerHTML = `
          <button onclick="setCvPage(1)" class="px-2.5 py-1 rounded-lg text-xs font-bold ${currentCvPage === 1 ? 'bg-blue-600 text-white' : 'text-slate-400 hover:text-white'}">P1: Summary</button>
          <button onclick="setCvPage(2)" class="px-2.5 py-1 rounded-lg text-xs font-bold ${currentCvPage === 2 ? 'bg-blue-600 text-white' : 'text-slate-400 hover:text-white'}">P2: Experience</button>
        `;

        // Downloads
        actions.innerHTML = `
          <a href="assets/documents/Tipu-Sultan-Growth-Architect-CV.pdf" download class="px-3 py-1.5 rounded-lg bg-rose-600/20 hover:bg-rose-600 text-rose-300 hover:text-white border border-rose-500/40 text-xs font-bold flex items-center gap-1.5 transition-all">
            <i class="fa-solid fa-file-pdf"></i> Download PDF
          </a>
          <a href="assets/documents/Tipu-Sultan-Growth-Architect-CV.docx" download class="px-3 py-1.5 rounded-lg bg-blue-600/20 hover:bg-blue-600 text-blue-300 hover:text-white border border-blue-500/40 text-xs font-bold flex items-center gap-1.5 transition-all">
            <i class="fa-solid fa-file-word"></i> Word (.docx)
          </a>
        `;
      } else {
        arBtn.className = 'px-3 py-1 rounded-lg text-xs font-bold bg-emerald-600 text-white transition-all shadow-md';
        enBtn.className = 'px-3 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all';
        badge.className = 'px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 text-[10px] font-black uppercase';
        badge.innerText = 'العربية';
        title.innerText = 'تيبو سلطان — السيرة الذاتية التنفيذية (AR)';
        subtitle.innerText = 'مهندس نمو بالذكاء الاصطناعي والبيانات | مسوّق أداء عالي القيمة (الرياض، السعودية)';
        img.src = `assets/documents/cv-ar-preview-page-${currentCvPage}.webp`;
        indicator.innerText = `الصفحة ${currentCvPage} من ${maxP}`;

        // Page tabs
        pageTabs.innerHTML = `
          <button onclick="setCvPage(1)" class="px-2.5 py-1 rounded-lg text-xs font-bold ${currentCvPage === 1 ? 'bg-emerald-600 text-white' : 'text-slate-400 hover:text-white'}">ص 1: الملخص</button>
          <button onclick="setCvPage(2)" class="px-2.5 py-1 rounded-lg text-xs font-bold ${currentCvPage === 2 ? 'bg-emerald-600 text-white' : 'text-slate-400 hover:text-white'}">ص 2: الخبرة</button>
          <button onclick="setCvPage(3)" class="px-2.5 py-1 rounded-lg text-xs font-bold ${currentCvPage === 3 ? 'bg-emerald-600 text-white' : 'text-slate-400 hover:text-white'}">ص 3: الأدلة</button>
        `;

        // Downloads
        actions.innerHTML = `
          <a href="assets/documents/Tipu-Sultan-Growth-Architect-CV-AR.pdf" download class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold flex items-center gap-1.5 transition-all shadow-lg">
            <i class="fa-solid fa-file-pdf"></i> تحميل السيرة الذاتية PDF (عربي)
          </a>
        `;
      }
    }

    // Current State for Presentation Deck Viewer
    let currentDeckLang = 'en';
    let currentDeckSlide = 1;

    function openDeckModal(lang = 'en', slideNum = 1) {
      currentDeckLang = lang;
      currentDeckSlide = slideNum;
      renderDeckSlide();
      renderDeckThumbStrip();
      document.getElementById('deckModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }

    function closeDeckModal() {
      document.getElementById('deckModal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }

    function switchDeckLang(lang) {
      currentDeckLang = lang;
      renderDeckSlide();
      renderDeckThumbStrip();
    }

    function setDeckSlide(slideNum) {
      if (slideNum >= 1 && slideNum <= 22) {
        currentDeckSlide = slideNum;
        renderDeckSlide();
        renderDeckThumbStrip();
      }
    }

    function nextDeckSlide() {
      if (currentDeckSlide < 22) {
        currentDeckSlide++;
        renderDeckSlide();
        renderDeckThumbStrip();
      }
    }

    function prevDeckSlide() {
      if (currentDeckSlide > 1) {
        currentDeckSlide--;
        renderDeckSlide();
        renderDeckThumbStrip();
      }
    }

    function renderDeckSlide() {
      const slides = presentationDecks[currentDeckLang] || presentationDecks.en;
      const slide = slides.find(s => s.num === currentDeckSlide) || slides[0];

      // UI elements
      const enBtn = document.getElementById('deckLangEnBtn');
      const arBtn = document.getElementById('deckLangArBtn');
      const downloadBtn = document.getElementById('deckDownloadBtn');
      const headerTitle = document.getElementById('deckHeaderTitle');
      const headerSubtitle = document.getElementById('deckHeaderSubtitle');
      const counterBadge = document.getElementById('deckSlideCounterBadge');
      
      const slideCategory = document.getElementById('deckSlideCategory');
      const slideNumberText = document.getElementById('deckSlideNumberText');
      const slideTitle = document.getElementById('deckSlideTitle');
      const slideSubtitle = document.getElementById('deckSlideSubtitle');
      const slideBullets = document.getElementById('deckSlideBullets');
      const slideImgContainer = document.getElementById('deckSlideImageContainer');
      const slideImg = document.getElementById('deckSlideImage');

      // Update Top Bar
      if (currentDeckLang === 'en') {
        enBtn.className = 'px-3 py-1 rounded-lg text-xs font-bold bg-cyan-600 text-slate-950 transition-all shadow-md';
        arBtn.className = 'px-3 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all';
        downloadBtn.href = 'assets/documents/tipu-sultan-portfolio-en.pptx';
        downloadBtn.innerHTML = '<i class="fa-solid fa-file-powerpoint text-cyan-400"></i> <span class="hidden sm:inline">Download Deck (.pptx 10.3 MB)</span>';
        headerTitle.innerText = 'Next-Gen Performance Architecture Deck (EN)';
        headerSubtitle.innerText = 'Tipu Sultan • AI-Driven & Data-Driven Growth Architect';
      } else {
        arBtn.className = 'px-3 py-1 rounded-lg text-xs font-bold bg-amber-500 text-slate-950 transition-all shadow-md';
        enBtn.className = 'px-3 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all';
        downloadBtn.href = 'assets/documents/tipu-sultan-portfolio-ar.pptx';
        downloadBtn.innerHTML = '<i class="fa-solid fa-file-powerpoint text-amber-400"></i> <span class="hidden sm:inline">تحميل العرض (.pptx 10.2 MB)</span>';
        headerTitle.innerText = 'عروض محفظة الأعمال الاستراتيجية — 22 شريحة (AR)';
        headerSubtitle.innerText = 'تيبو سلطان • هندسة نمو بالذكاء الاصطناعي والتجارة الخليجية';
      }

      counterBadge.innerText = `Slide ${String(currentDeckSlide).padStart(2, '0')} / 22`;
      slideNumberText.innerText = `${String(currentDeckSlide).padStart(2, '0')} / 22`;
      slideCategory.innerText = slide.category;
      slideTitle.innerText = slide.title;
      slideSubtitle.innerText = slide.subtitle;

      // Render points
      slideBullets.innerHTML = '';
      if (slide.points && slide.points.length > 0) {
        slide.points.forEach(pt => {
          const item = document.createElement('div');
          item.className = 'flex items-start gap-2 p-2 rounded-xl bg-slate-900/60 border border-slate-800 text-xs text-slate-300';
          item.innerHTML = `<i class="fa-solid fa-chevron-right text-cyan-400 text-[10px] mt-1 flex-shrink-0"></i> <span>${pt}</span>`;
          slideBullets.appendChild(item);
        });
      }

      // Check if image available
      if (slide.image) {
        slideImg.src = slide.image;
        slideImgContainer.classList.remove('hidden');
      } else {
        slideImgContainer.classList.add('hidden');
      }
    }

    function renderDeckThumbStrip() {
      const strip = document.getElementById('deckSlideSelectorStrip');
      strip.innerHTML = '';
      for (let i = 1; i <= 22; i++) {
        const btn = document.createElement('button');
        const isActive = i === currentDeckSlide;
        btn.onclick = () => setDeckSlide(i);
        btn.className = `w-7 h-7 rounded-lg text-[11px] font-bold flex items-center justify-center transition-all flex-shrink-0 ${
          isActive
            ? 'bg-cyan-500 text-slate-950 shadow-md shadow-cyan-500/30 ring-2 ring-cyan-400'
            : 'bg-slate-900 text-slate-400 hover:text-white hover:bg-slate-800 border border-slate-800'
        }`;
        btn.innerText = i;
        btn.title = `Slide ${i}`;
        strip.appendChild(btn);
      }
    }

    // Filter executive assets
    function filterAssets(cat, btn) {
      document.querySelectorAll('#asset-filter-buttons .asset-btn').forEach(b => {
        b.className = 'asset-btn px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800';
      });
      btn.className = 'asset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-500 text-slate-950 shadow-md shadow-amber-500/30';

      const cards = document.querySelectorAll('#assets-grid .asset-card');
      cards.forEach(card => {
        if (cat === 'all' || card.getAttribute('data-category') === cat) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    }

    // Update Keyboard Listener to handle Deck Left/Right and CV Esc
    document.addEventListener('keydown', (e) => {
      const isDeckOpen = !document.getElementById('deckModal').classList.contains('hidden');
      const isCvOpen = !document.getElementById('cvModal').classList.contains('hidden');

      if (e.key === 'ArrowRight' && isDeckOpen) {
        nextDeckSlide();
      } else if (e.key === 'ArrowLeft' && isDeckOpen) {
        prevDeckSlide();
      } else if (e.key === 'Escape') {
        if (isDeckOpen) closeDeckModal();
        if (isCvOpen) closeCvModal();
      }
    });
"""

    # Insert scripts right before // Initialize App
    if 'currentCvLang' not in html:
        html = html.replace('// Initialize App', executive_scripts + '\n    // Initialize App', 1)
        print("Inserted executive JavaScript handlers and decks data")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated successfully!")

if __name__ == '__main__':
    main()
