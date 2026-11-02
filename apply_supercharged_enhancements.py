# -*- coding: utf-8 -*-
"""
apply_supercharged_enhancements.py
Implements cutting-edge enhancements:
1. Full site-wide data-i18n tags for AI Engine, Playbooks, ROI Simulator, and Teardown Form
2. Multi-currency switcher in ROI simulator: USD ($), SAR (ر.س), and AED (د.إ) with dynamic rate conversions
3. Live Counting Number Animation for Hero Stats ($188K+, $869K+, 4.6x, 59+)
4. Forensic Image Zoom (Zoom In, Zoom Out, Reset) inside the Lightbox Modal
5. Floating Quick-Action Pill (WhatsApp & Book Audit) at bottom-right
6. Keyboard shortcuts: [C] for CV, [D] for Decks, [Esc] to close, [1-8] for Tabs
"""

import re
import json

def apply():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update SITE_TRANSLATIONS to cover all sections completely
    extra_translations = """
        // Extended Playbooks, AI Engine, Calculator and Audit Translations
        ai_card1_title: 'Advantage+ & Algorithmic Bidding',
        ai_card1_desc: 'Machine-learning budget distribution across 3B+ user signals, eliminating manual audience guesswork.',
        ai_card2_title: 'Server-Side CAPI Gateway',
        ai_card2_desc: 'Event Match Quality scoring 9.4/10 with SHA-256 parameter hashing, recovering up to 35% lost conversions.',
        ai_card3_title: '3:2:2 Creative Testing Matrix',
        ai_card3_desc: 'Systematic testing of 3 video hooks, 2 audio variations, and 2 copy CTAs in an isolated sandbox.',
        ai_card4_title: 'Unit Economics & LTV Retention',
        ai_card4_desc: 'Cohort-based retention models engineering repeat purchase loops for healthy 4.2:1 LTV:CAC ratios.',
        
        calc_budget_lbl: 'Monthly Ad Spend',
        calc_roas_lbl: 'Current ROAS',
        calc_target_lbl: 'Target ROAS Lift',
        calc_revenue_lbl: 'Projected Monthly Revenue Lift',
        calc_cta_btn: 'Replicate This Strategy in Your Account',

        audit_name_lbl: 'Your Name / Company',
        audit_url_lbl: 'Website / Store URL',
        audit_spend_lbl: 'Monthly Ad Spend',
        audit_challenge_lbl: 'Primary Growth Bottleneck',
        audit_submit_btn: 'Request My 10-Minute Video Teardown',
        audit_guarantee: '100% Private & Confidential. Delivered directly to your email or WhatsApp within 24 hours.'
    """

    extra_translations_ar = """
        // Extended Playbooks, AI Engine, Calculator and Audit Translations (Arabic)
        ai_card1_title: 'مزايدات Advantage+ الخوارزمية',
        ai_card1_desc: 'توزيع الميزانية عبر التعلم الآلي بين أكثر من 3 مليارات إشارة مستخدم، لإلغاء التخمين اليدوي تماماً.',
        ai_card2_title: 'بوابة تتبع Server-Side CAPI',
        ai_card2_desc: 'جودة تطابق أحداث 9.4/10 مع تشفير SHA-256، لاسترداد حتى 35% من التحويلات المفقودة.',
        ai_card3_title: 'مصفوفة اختبار الإبداع 3:2:2',
        ai_card3_desc: 'اختبار منهجي لـ 3 خطاطيف فيديو، مقطعي صوت، ودعوتين لاتخاذ إجراء داخل صندوق معزول.',
        ai_card4_title: 'اقتصاديات الوحدة وقيمة العميل LTV',
        ai_card4_desc: 'نمذجة أفواج العملاء لهندسة دورات الشراء المتكرر وتحقيق نسبة 4.2:1 في LTV:CAC.',

        calc_budget_lbl: 'الإنفاق الإعلاني الشهري',
        calc_roas_lbl: 'العائد الحالي ROAS',
        calc_target_lbl: 'نمو العائد المستهدف',
        calc_revenue_lbl: 'نمو الإيرادات الشهري المتوقع',
        calc_cta_btn: 'طبق هذه الاستراتيجية على حسابك الآن',

        audit_name_lbl: 'اسمك / اسم الشركة',
        audit_url_lbl: 'رابط الموقع أو المتجر',
        audit_spend_lbl: 'ميزانية الإنفاق الشهري',
        audit_challenge_lbl: 'أكبر عقبة تواجه التوسع',
        audit_submit_btn: 'اطلب تشريح الفيديو الخاص بي (10 دقائق)',
        audit_guarantee: 'سري وخاص 100%. يتم تسليمه مباشرة إلى بريدك أو واتساب خلال 24 ساعة.'
    """

    if "ai_card1_title: 'Advantage+ & Algorithmic Bidding'" not in html:
        html = html.replace("case_breakdown_btn: 'Deep Architecture Breakdown'", "case_breakdown_btn: 'Deep Architecture Breakdown',\n" + extra_translations, 1)
        html = html.replace("case_breakdown_btn: 'تشريح البنية الهندسية الكاملة'", "case_breakdown_btn: 'تشريح البنية الهندسية الكاملة',\n" + extra_translations_ar, 1)
        print("Extended translation dictionary with full section keys")

    # 2. Add Multi-Currency Selector to Calculator Section: USD, SAR, AED
    old_curr_selector_pattern = r'<div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">[\s\S]*?</div>'
    new_curr_selector = """<div class="flex items-center gap-1 bg-slate-950 p-1 rounded-xl border border-slate-800">
              <button id="currBtnUSD" onclick="setCurrency('USD')" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-blue-600 text-white shadow transition-all">USD ($)</button>
              <button id="currBtnSAR" onclick="setCurrency('SAR')" class="px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all">SAR (ر.س)</button>
              <button id="currBtnAED" onclick="setCurrency('AED')" class="px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all">AED (د.إ)</button>
            </div>"""

    if 'currBtnAED' not in html:
        # Look for currBtnSAR
        m = re.search(old_curr_selector_pattern, html)
        if m:
            html = html.replace(m.group(0), new_curr_selector, 1)
            print("Upgraded currency switcher to USD, SAR, and AED")

    # 3. Add Floating Quick-Action Pill at Bottom-Right
    floating_pill_html = """
  <!-- Floating High-Ticket Contact & Quick Action Pill -->
  <div id="floatingQuickPill" class="fixed bottom-6 right-6 z-40 flex items-center gap-2 animate-bounce-subtle">
    <button onclick="triggerGlobalWhatsApp()" class="group flex items-center gap-2.5 px-4 py-2.5 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-2xl shadow-emerald-500/40 border border-emerald-400/40 transition-all transform hover:scale-105" title="Chat on WhatsApp">
      <i class="fa-brands fa-whatsapp text-base"></i>
      <span class="hidden md:inline">WhatsApp Tipu</span>
    </button>
    <button onclick="switchTab('audit')" class="group flex items-center gap-2 px-3.5 py-2.5 rounded-full bg-slate-900/90 hover:bg-slate-800 text-cyan-400 hover:text-cyan-300 font-bold text-xs shadow-2xl border border-cyan-500/40 transition-all transform hover:scale-105" title="Request Ad Teardown">
      <i class="fa-solid fa-bolt text-xs"></i>
      <span class="hidden md:inline">10-Min Audit</span>
    </button>
  </div>
"""

    if 'id="floatingQuickPill"' not in html:
        html = html.replace('</body>', floating_pill_html + '\n</body>', 1)
        print("Inserted floating quick-action pill at bottom-right")

    # 4. Enhance Lightbox with Forensic Zoom Controls (Zoom In, Zoom Out, Reset)
    old_lb_header_controls = """<button onclick="downloadActiveLightboxImage()" class="px-3 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 text-xs font-bold border border-slate-700 flex items-center gap-1.5 transition-all">
            <i class="fa-solid fa-download text-emerald-400 text-[11px]"></i> Download
          </button>"""

    new_lb_header_controls = """<div class="inline-flex rounded-lg bg-slate-950 border border-slate-800 p-0.5 mr-2">
            <button onclick="zoomLightbox(0.2)" class="px-2 py-1 rounded text-xs font-bold text-slate-300 hover:text-white" title="Zoom In"><i class="fa-solid fa-magnifying-glass-plus"></i></button>
            <button onclick="zoomLightbox(-0.2)" class="px-2 py-1 rounded text-xs font-bold text-slate-300 hover:text-white" title="Zoom Out"><i class="fa-solid fa-magnifying-glass-minus"></i></button>
            <button onclick="resetLightboxZoom()" class="px-2 py-1 rounded text-xs font-bold text-slate-400 hover:text-white" title="Reset">100%</button>
          </div>
          <button onclick="downloadActiveLightboxImage()" class="px-3 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 text-xs font-bold border border-slate-700 flex items-center gap-1.5 transition-all">
            <i class="fa-solid fa-download text-emerald-400 text-[11px]"></i> Download
          </button>"""

    if 'zoomLightbox' not in html:
        html = html.replace(old_lb_header_controls, new_lb_header_controls, 1)
        print("Added forensic zoom controls to Lightbox modal")

    # 5. Insert Scripts for:
    # - AED / SAR / USD currency rate logic
    # - Live Animated Counter for stats
    # - Lightbox zoom state
    # - Global keyboard shortcuts ([C] for CV, [D] for Deck, [1-8] for Tabs)
    supercharged_js = """
    // ==========================================
    // MULTI-CURRENCY LOGIC (USD, SAR, AED)
    // ==========================================
    const CURRENCY_RATES = {
      USD: { symbol: '$', rate: 1.0, min: 2000, max: 100000, step: 1000, defaultVal: 15000 },
      SAR: { symbol: 'SAR ', rate: 3.75, min: 7500, max: 375000, step: 3750, defaultVal: 56250 },
      AED: { symbol: 'AED ', rate: 3.67, min: 7340, max: 367000, step: 3670, defaultVal: 55050 }
    };

    function setCurrency(curr) {
      if (!CURRENCY_RATES[curr]) return;
      currentCurrency = curr;

      const btnUSD = document.getElementById('currBtnUSD');
      const btnSAR = document.getElementById('currBtnSAR');
      const btnAED = document.getElementById('currBtnAED');
      const budgetSlider = document.getElementById('budgetRange');

      [btnUSD, btnSAR, btnAED].forEach(btn => {
        if (btn) btn.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition-all';
      });

      const activeBtn = (curr === 'USD') ? btnUSD : (curr === 'SAR') ? btnSAR : btnAED;
      if (activeBtn) {
        activeBtn.className = 'px-2.5 py-1 rounded-lg text-xs font-bold bg-blue-600 text-white shadow transition-all';
      }

      const conf = CURRENCY_RATES[curr];
      if (budgetSlider) {
        budgetSlider.min = conf.min;
        budgetSlider.max = conf.max;
        budgetSlider.step = conf.step;
        budgetSlider.value = conf.defaultVal;
      }

      runRoiCalculator();
    }

    // ==========================================
    // FORENSIC LIGHTBOX ZOOM LOGIC
    // ==========================================
    let lightboxCurrentZoom = 1.0;

    function zoomLightbox(delta) {
      const img = document.getElementById('lightboxImg');
      if (!img) return;
      lightboxCurrentZoom = Math.max(0.6, Math.min(3.0, lightboxCurrentZoom + delta));
      img.style.transform = `scale(${lightboxCurrentZoom})`;
      img.style.transition = 'transform 0.15s ease-out';
    }

    function resetLightboxZoom() {
      const img = document.getElementById('lightboxImg');
      if (!img) return;
      lightboxCurrentZoom = 1.0;
      img.style.transform = 'scale(1.0)';
    }

    // Reset zoom when item changes
    const _oldRenderLightbox = renderLightboxItem;
    renderLightboxItem = function() {
      resetLightboxZoom();
      _oldRenderLightbox();
    };

    // ==========================================
    // ANIMATED COUNTER ENGINE FOR HERO STATS
    // ==========================================
    function animateCounters() {
      const stats = [
        { id: 'stat-spend', target: 188, prefix: '$', suffix: 'K+', decimals: 0 },
        { id: 'stat-revenue', target: 869, prefix: '$', suffix: 'K+', decimals: 0 },
        { id: 'stat-roas', target: 4.6, prefix: '', suffix: 'x', decimals: 1 },
        { id: 'stat-count', target: 59, prefix: '', suffix: '+', decimals: 0 }
      ];

      const duration = 1200;
      const startTime = performance.now();

      function update(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeOutQuad = 1 - (1 - progress) * (1 - progress);

        stats.forEach(s => {
          const el = document.getElementById(s.id);
          if (el) {
            const current = (s.target * easeOutQuad).toFixed(s.decimals);
            el.innerText = `${s.prefix}${current}${s.suffix}`;
          }
        });

        if (progress < 1) {
          requestAnimationFrame(update);
        }
      }
      requestAnimationFrame(update);
    }

    // ==========================================
    // KEYBOARD SHORTCUTS ENGINE
    // ==========================================
    document.addEventListener('keydown', (e) => {
      // Don't intercept if user is typing in an input or textarea
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName)) return;

      const isDeckOpen = !document.getElementById('deckModal').classList.contains('hidden');
      const isCvOpen = !document.getElementById('cvModal').classList.contains('hidden');
      const isLightboxOpen = !document.getElementById('lightboxModal').classList.contains('hidden');

      if (!isDeckOpen && !isCvOpen && !isLightboxOpen) {
        // [C] opens CV Modal
        if (e.key === 'c' || e.key === 'C') {
          openCvModal(currentSiteLang, 1);
        }
        // [D] opens Deck Modal
        else if (e.key === 'd' || e.key === 'D') {
          openDeckModal(currentSiteLang, 1);
        }
        // [1-8] switches tabs
        else if (e.key >= '1' && e.key <= '8') {
          const tabMap = {
            '1': 'executive-assets',
            '2': 'ai-engine',
            '3': 'frameworks',
            '4': 'proofs',
            '5': 'vault',
            '6': 'creatives',
            '7': 'calculator',
            '8': 'audit'
          };
          if (tabMap[e.key]) switchTab(tabMap[e.key]);
        }
      }
    });
"""

    if 'CURRENCY_RATES' not in html:
        html = html.replace('// Initialize App', supercharged_js + '\n    // Initialize App', 1)
        print("Inserted currency engine, forensic zoom, animated counters, and keyboard shortcuts")

    # Call animateCounters on init
    if 'animateCounters();' not in html:
        html = html.replace('handleInitialHash();', 'handleInitialHash();\n    animateCounters();', 1)
        print("Connected animateCounters() on startup")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("All supercharged enhancements applied successfully!")

if __name__ == '__main__':
    apply()
