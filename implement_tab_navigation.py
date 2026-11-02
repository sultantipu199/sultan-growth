# -*- coding: utf-8 -*-
"""
implement_tab_navigation.py
Transforms the portfolio website into an instant Tab / View Switcher architecture:
- No scrolling down when clicking navbar items
- Clicking any navbar item instantly switches/shows that section right in place
- Works for all 8 sections (CV & Decks, AI & Data Engine, Growth Playbooks, Case Studies, Proof Vault, Ad Creatives, ROI Engine, Audit & Diagnosis)
- Includes an Active View Status bar with a "Show All Sections" toggle
- Updates desktop navbar and mobile drawer to button triggers
- Retains URL hash capability and responsive layout
"""

import re
from bs4 import BeautifulSoup

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Desktop Navbar Links
    desktop_nav_pattern = r'(<!-- Desktop Nav Links -->\s*<div[^>]*>)([\s\S]*?)(</div>\s*<!-- Quick Action Buttons -->)'
    
    new_desktop_nav_content = """
        <button onclick="switchTab('executive-assets')" data-tab="executive-assets" class="nav-tab-btn hover:text-amber-300 transition-all flex items-center gap-1.5 text-amber-300 font-bold px-3 py-1.5 rounded-xl bg-amber-500/20 border border-amber-500/40 shadow-sm shadow-amber-500/15">
          <i class="fa-solid fa-file-shield text-xs text-amber-400"></i>
          <span>CV & Decks</span>
          <span class="px-1.5 py-0.5 rounded bg-amber-400 text-slate-950 text-[9px] font-black uppercase tracking-wider">New</span>
        </button>

        <button onclick="switchTab('ai-engine')" data-tab="ai-engine" class="nav-tab-btn hover:text-cyan-400 transition-all flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-transparent text-slate-300 font-semibold">
          <i class="fa-solid fa-microchip text-[11px] text-cyan-400"></i>
          <span>AI & Data Engine</span>
        </button>

        <button onclick="switchTab('frameworks')" data-tab="frameworks" class="nav-tab-btn hover:text-purple-400 transition-all flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-transparent text-slate-300 font-semibold">
          <i class="fa-solid fa-brain text-[11px] text-purple-400"></i>
          <span>Growth Playbooks</span>
        </button>

        <button onclick="switchTab('proofs')" data-tab="proofs" class="nav-tab-btn hover:text-emerald-400 transition-all flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-transparent text-slate-300 font-semibold">
          <i class="fa-solid fa-trophy text-[11px] text-emerald-400"></i>
          <span>Case Studies</span>
        </button>

        <button onclick="switchTab('vault')" data-tab="vault" class="nav-tab-btn hover:text-blue-400 transition-all flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-transparent text-slate-300 font-semibold">
          <i class="fa-solid fa-images text-[11px] text-blue-400"></i>
          <span>Proof Vault (59)</span>
        </button>

        <button onclick="switchTab('creatives')" data-tab="creatives" class="nav-tab-btn hover:text-indigo-400 transition-all flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-transparent text-slate-300 font-semibold">
          <i class="fa-solid fa-wand-magic-sparkles text-[11px] text-indigo-400"></i>
          <span>Ad Creatives (48)</span>
        </button>

        <button onclick="switchTab('calculator')" data-tab="calculator" class="nav-tab-btn hover:text-teal-400 transition-all flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-transparent text-slate-300 font-semibold">
          <i class="fa-solid fa-calculator text-[11px] text-teal-400"></i>
          <span>ROI Engine</span>
        </button>

        <button onclick="switchTab('audit')" data-tab="audit" class="nav-tab-btn text-emerald-400 hover:text-emerald-300 transition-all font-bold px-3 py-1.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center gap-1.5">
          <i class="fa-solid fa-bolt text-xs text-emerald-400"></i>
          <span>Audit & Diagnosis</span>
        </button>
      """

    def replace_desktop_nav(match):
        prefix = match.group(1)
        suffix = match.group(3)
        return prefix + new_desktop_nav_content + suffix

    html = re.sub(desktop_nav_pattern, replace_desktop_nav, html, count=1)
    print("Updated desktop navbar to interactive tab buttons")

    # 2. Update Mobile Menu Drawer
    mobile_menu_pattern = r'(<!-- Menu Links Grid -->\s*<div[^>]*>)([\s\S]*?)(</div>\s*<!-- Quick Action Buttons in Mobile Menu -->)'
    
    new_mobile_nav_content = """
        <button onclick="switchTab('executive-assets'); closeMobileMenu();" data-tab-mobile="executive-assets" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-amber-500/15 border border-amber-500/35 text-xs font-bold text-amber-300 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-file-shield"></i>
            </span>
            <span>Executive CV & Decks</span>
          </span>
          <span class="px-2 py-0.5 rounded-md bg-amber-400 text-slate-950 text-[10px] font-black">EN & AR</span>
        </button>

        <button onclick="switchTab('ai-engine'); closeMobileMenu();" data-tab-mobile="ai-engine" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-800/90 border border-slate-800 text-xs font-semibold text-slate-200 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-cyan-500/10 text-cyan-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-microchip"></i>
            </span>
            <span>AI & Data Engine</span>
          </span>
          <i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>
        </button>

        <button onclick="switchTab('frameworks'); closeMobileMenu();" data-tab-mobile="frameworks" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-800/90 border border-slate-800 text-xs font-semibold text-slate-200 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-purple-500/10 text-purple-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-brain"></i>
            </span>
            <span>Growth Playbooks</span>
          </span>
          <i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>
        </button>

        <button onclick="switchTab('proofs'); closeMobileMenu();" data-tab-mobile="proofs" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-800/90 border border-slate-800 text-xs font-semibold text-slate-200 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-trophy"></i>
            </span>
            <span>Case Studies (8 In-Depth)</span>
          </span>
          <span class="px-2 py-0.5 rounded-md bg-emerald-500/10 text-emerald-400 text-[10px] font-bold">8 Studies</span>
        </button>

        <button onclick="switchTab('vault'); closeMobileMenu();" data-tab-mobile="vault" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-800/90 border border-slate-800 text-xs font-semibold text-slate-200 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-blue-500/10 text-blue-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-images"></i>
            </span>
            <span>Proof Vault</span>
          </span>
          <span class="px-2 py-0.5 rounded-md bg-blue-500/10 text-blue-400 text-[10px] font-bold">59 Proofs</span>
        </button>

        <button onclick="switchTab('creatives'); closeMobileMenu();" data-tab-mobile="creatives" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-800/90 border border-slate-800 text-xs font-semibold text-slate-200 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-indigo-500/10 text-indigo-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-wand-magic-sparkles"></i>
            </span>
            <span>Ad Creatives Sandbox</span>
          </span>
          <span class="px-2 py-0.5 rounded-md bg-indigo-500/10 text-indigo-400 text-[10px] font-bold">48 Angles</span>
        </button>

        <button onclick="switchTab('calculator'); closeMobileMenu();" data-tab-mobile="calculator" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-800/90 border border-slate-800 text-xs font-semibold text-slate-200 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-teal-500/10 text-teal-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-calculator"></i>
            </span>
            <span>ROI Simulator Engine</span>
          </span>
          <i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>
        </button>

        <button onclick="switchTab('audit'); closeMobileMenu();" data-tab-mobile="audit" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 text-xs font-bold text-emerald-400 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-300 flex items-center justify-center text-xs">
              <i class="fa-solid fa-bolt"></i>
            </span>
            <span>Audit & Diagnosis Tool</span>
          </span>
          <span class="text-[10px] bg-emerald-500 text-slate-950 font-black px-2 py-0.5 rounded-md">FREE</span>
        </button>

        <button onclick="setViewMode('all'); closeMobileMenu();" class="w-full flex items-center justify-between p-2.5 rounded-xl bg-slate-900/90 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-300 transition-all">
          <span class="flex items-center gap-2.5">
            <span class="w-7 h-7 rounded-lg bg-slate-800 text-cyan-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-list-ul"></i>
            </span>
            <span>Show All Sections (Continuous)</span>
          </span>
          <i class="fa-solid fa-expand text-[10px] text-slate-400"></i>
        </button>
      """

    def replace_mobile_nav(match):
        prefix = match.group(1)
        suffix = match.group(3)
        return prefix + new_mobile_nav_content + suffix

    html = re.sub(mobile_menu_pattern, replace_mobile_nav, html, count=1)
    print("Updated mobile navbar drawer to interactive tab buttons")

    # 3. Add Tab View Control Bar right after </header> and wrap the main sections in #portfolioContentArea
    control_bar_and_wrapper_start = """
  <!-- Interactive View Stage & Mode Controller -->
  <div class="max-w-7xl mx-auto px-4 sm:px-6 mb-4 w-full">
    <div class="glass-card rounded-2xl p-2.5 sm:p-3 border border-slate-800/90 flex flex-wrap items-center justify-between gap-3 shadow-xl bg-slate-950/70">
      
      <!-- Current Active Section Indicator -->
      <div class="flex items-center gap-2.5">
        <span class="relative flex h-2.5 w-2.5">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-cyan-500"></span>
        </span>
        <span class="text-xs font-bold text-slate-400">Active View:</span>
        <span id="activeViewLabel" class="text-xs font-extrabold text-amber-300 bg-amber-500/10 px-3 py-1 rounded-lg border border-amber-500/30">
          Executive CV & Strategic Decks
        </span>
      </div>

      <!-- Quick Tab View Switcher Buttons (Desktop & Tablet) -->
      <div class="hidden lg:flex items-center gap-1.5 overflow-x-auto max-w-2xl py-0.5 custom-scrollbar" id="viewBarTabs">
        <button onclick="switchTab('executive-assets')" data-vtab="executive-assets" class="view-pill px-2.5 py-1 rounded-lg text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40">CV & Decks</button>
        <button onclick="switchTab('ai-engine')" data-vtab="ai-engine" class="view-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white bg-slate-900 border border-slate-800">AI Engine</button>
        <button onclick="switchTab('frameworks')" data-vtab="frameworks" class="view-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white bg-slate-900 border border-slate-800">Playbooks</button>
        <button onclick="switchTab('proofs')" data-vtab="proofs" class="view-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white bg-slate-900 border border-slate-800">Case Studies</button>
        <button onclick="switchTab('vault')" data-vtab="vault" class="view-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white bg-slate-900 border border-slate-800">Vault (59)</button>
        <button onclick="switchTab('creatives')" data-vtab="creatives" class="view-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white bg-slate-900 border border-slate-800">Creatives (48)</button>
        <button onclick="switchTab('calculator')" data-vtab="calculator" class="view-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white bg-slate-900 border border-slate-800">ROI Engine</button>
        <button onclick="switchTab('audit')" data-vtab="audit" class="view-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold text-emerald-400 bg-emerald-500/10 border border-emerald-500/30">Audit</button>
      </div>

      <!-- Mode Toggle: Focused Tab View vs Show All -->
      <div class="flex items-center gap-1.5 bg-slate-900 p-1 rounded-xl border border-slate-800">
        <button id="viewModeTabBtn" onclick="setViewMode('tabs')" class="px-2.5 py-1 rounded-lg text-[11px] font-bold bg-cyan-600 text-slate-950 transition-all flex items-center gap-1 shadow-sm">
          <i class="fa-solid fa-layer-group text-[10px]"></i> Single View
        </button>
        <button id="viewModeAllBtn" onclick="setViewMode('all')" class="px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white transition-all flex items-center gap-1">
          <i class="fa-solid fa-list-ul text-[10px]"></i> Show All
        </button>
      </div>

    </div>
  </div>

  <!-- Main Dynamic Portfolio Content Stage -->
  <div id="portfolioContentArea" class="w-full relative transition-all duration-300">
"""

    # Insert control bar and wrapper right after </header>
    if 'id="portfolioContentArea"' not in html:
        idx_header_end = html.find('</header>')
        if idx_header_end != -1:
            pos = idx_header_end + len('</header>')
            html = html[:pos] + "\n" + control_bar_and_wrapper_start + "\n" + html[pos:]
            print("Inserted #portfolioContentArea and control bar")

    # Close #portfolioContentArea right before <footer
    if '</div>\n\n  <!-- Footer -->' not in html and 'id="portfolioContentArea"' in html:
        idx_footer = html.find('<!-- Footer -->')
        if idx_footer != -1:
            html = html[:idx_footer] + "  </div>\n\n  " + html[idx_footer:]
            print("Closed #portfolioContentArea before Footer")

    # 4. Mark all 8 sections with class 'portfolio-tab-content'
    section_ids = [
        'executive-assets',
        'ai-engine',
        'frameworks',
        'proofs',
        'vault',
        'creatives',
        'calculator',
        'audit'
    ]

    for sid in section_ids:
        # replace <section id="sid" class="
        pattern = f'<section id="{sid}" class="'
        if pattern in html and f'<section id="{sid}" class="portfolio-tab-content ' not in html:
            html = html.replace(pattern, f'<section id="{sid}" class="portfolio-tab-content transition-all duration-300 ', 1)
            print(f"Added portfolio-tab-content class to #{sid}")

    # 5. Add JavaScript for Tab View Management
    tab_script = """
    // ==========================================
    // INTERACTIVE TAB & VIEW SWITCHER SYSTEM
    // ==========================================
    let currentActiveTab = 'executive-assets';
    let currentViewMode = 'tabs'; // 'tabs' or 'all'

    const tabLabels = {
      'executive-assets': 'Executive CV & Strategic Decks',
      'ai-engine': 'AI-Driven & Data-Engineered Engine',
      'frameworks': 'Strategic Performance Playbooks',
      'proofs': 'Verified Client Case Studies',
      'vault': 'Raw Proof Gallery (59 Verified Screenshots)',
      'creatives': 'Ad Creative Sandbox & Angle Matrix',
      'calculator': 'Interactive Funnel ROI Simulator',
      'audit': '10-Minute Ad Account Teardown Audit'
    };

    function setViewMode(mode) {
      currentViewMode = mode;
      const tabBtn = document.getElementById('viewModeTabBtn');
      const allBtn = document.getElementById('viewModeAllBtn');

      if (mode === 'all') {
        tabBtn.className = 'px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white transition-all flex items-center gap-1';
        allBtn.className = 'px-2.5 py-1 rounded-lg text-[11px] font-bold bg-cyan-600 text-slate-950 transition-all flex items-center gap-1 shadow-sm';
        
        // Show all sections
        document.querySelectorAll('.portfolio-tab-content').forEach(sec => {
          sec.classList.remove('hidden');
        });
        document.getElementById('activeViewLabel').innerText = 'All Sections (Continuous View)';
      } else {
        tabBtn.className = 'px-2.5 py-1 rounded-lg text-[11px] font-bold bg-cyan-600 text-slate-950 transition-all flex items-center gap-1 shadow-sm';
        allBtn.className = 'px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white transition-all flex items-center gap-1';
        switchTab(currentActiveTab);
      }
    }

    function switchTab(tabId) {
      currentActiveTab = tabId;
      currentViewMode = 'tabs';

      // Update View Mode Buttons
      const tabBtn = document.getElementById('viewModeTabBtn');
      const allBtn = document.getElementById('viewModeAllBtn');
      if (tabBtn && allBtn) {
        tabBtn.className = 'px-2.5 py-1 rounded-lg text-[11px] font-bold bg-cyan-600 text-slate-950 transition-all flex items-center gap-1 shadow-sm';
        allBtn.className = 'px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white transition-all flex items-center gap-1';
      }

      // Show only target section, hide all other tab sections
      document.querySelectorAll('.portfolio-tab-content').forEach(sec => {
        if (sec.id === tabId) {
          sec.classList.remove('hidden');
        } else {
          sec.classList.add('hidden');
        }
      });

      // Update Active View Label
      const label = document.getElementById('activeViewLabel');
      if (label) {
        label.innerText = tabLabels[tabId] || tabId;
        if (tabId === 'executive-assets') {
          label.className = 'text-xs font-extrabold text-amber-300 bg-amber-500/10 px-3 py-1 rounded-lg border border-amber-500/30';
        } else if (tabId === 'audit') {
          label.className = 'text-xs font-extrabold text-emerald-300 bg-emerald-500/10 px-3 py-1 rounded-lg border border-emerald-500/30';
        } else {
          label.className = 'text-xs font-extrabold text-cyan-300 bg-cyan-500/10 px-3 py-1 rounded-lg border border-cyan-500/30';
        }
      }

      // Update Desktop Navbar Styling
      document.querySelectorAll('#desktopNavTabs .nav-tab-btn').forEach(btn => {
        const bTab = btn.getAttribute('data-tab');
        if (bTab === tabId) {
          if (tabId === 'executive-assets') {
            btn.className = 'nav-tab-btn hover:text-amber-300 transition-all flex items-center gap-1.5 text-amber-300 font-bold px-3 py-1.5 rounded-xl bg-amber-500/20 border border-amber-500/50 shadow-md shadow-amber-500/20';
          } else if (tabId === 'audit') {
            btn.className = 'nav-tab-btn text-emerald-300 hover:text-emerald-200 transition-all font-bold px-3 py-1.5 rounded-xl bg-emerald-500/20 border border-emerald-500/50 shadow-md shadow-emerald-500/20 flex items-center gap-1.5';
          } else {
            btn.className = 'nav-tab-btn text-cyan-300 font-bold px-3 py-1.5 rounded-xl bg-cyan-500/20 border border-cyan-500/50 shadow-md shadow-cyan-500/20 flex items-center gap-1.5 transition-all';
          }
        } else {
          if (bTab === 'audit') {
            btn.className = 'nav-tab-btn text-emerald-400 hover:text-emerald-300 transition-all font-semibold px-3 py-1.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center gap-1.5';
          } else if (bTab === 'executive-assets') {
            btn.className = 'nav-tab-btn hover:text-amber-300 transition-all flex items-center gap-1.5 text-amber-400 font-semibold px-2.5 py-1.5 rounded-xl border border-transparent';
          } else {
            btn.className = 'nav-tab-btn hover:text-cyan-400 transition-all flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-transparent text-slate-300 font-semibold';
          }
        }
      });

      // Update Quick View Bar Tabs
      document.querySelectorAll('#viewBarTabs .view-pill').forEach(btn => {
        const vTab = btn.getAttribute('data-vtab');
        if (vTab === tabId) {
          btn.className = 'view-pill px-2.5 py-1 rounded-lg text-[11px] font-bold bg-cyan-600 text-slate-950 shadow-sm';
        } else {
          btn.className = 'view-pill px-2.5 py-1 rounded-lg text-[11px] font-semibold text-slate-400 hover:text-white bg-slate-900 border border-slate-800';
        }
      });

      // Instant Positioning without slow smooth scrolling
      const navEl = document.querySelector('nav');
      const navH = navEl ? navEl.offsetHeight : 70;
      const container = document.getElementById('portfolioContentArea');
      if (container && window.pageYOffset > (container.offsetTop - navH)) {
        window.scrollTo({
          top: container.offsetTop - navH - 10,
          behavior: 'auto'
        });
      }

      // Update URL hash without scrolling
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, null, '#' + tabId);
      }
    }
"""

    if 'function switchTab(tabId)' not in html:
        html = html.replace('// Initialize App', tab_script + '\n    // Initialize App', 1)
        print("Inserted switchTab() and setViewMode() script functions")

    # Update initial call in // Initialize App to activate executive-assets tab
    init_call = "switchTab('executive-assets');"
    if init_call not in html:
        html = html.replace('renderCreatives();', 'renderCreatives();\n    switchTab("executive-assets");', 1)
        print("Added initial switchTab call")

    # Update hero section buttons so they switch tabs directly without slow scroll
    html = html.replace(
        'href="#audit" class="px-5 py-3 rounded-xl bg-emerald-500/15',
        'href="javascript:void(0)" onclick="switchTab(\'audit\')" class="px-5 py-3 rounded-xl bg-emerald-500/15'
    )
    print("Updated Hero audit CTA to switchTab('audit')")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("All updates to index.html completed successfully!")

if __name__ == '__main__':
    update_html()
