# -*- coding: utf-8 -*-
"""
apply_full_audit_enhancements.py
Implements all P1 and P2 optimizations identified in the comprehensive audit:
1. Technical SEO & Social Meta (Open Graph, Twitter Card, Favicon, Theme Color, Canonical)
2. Schema.org JSON-LD Structured Data
3. Arabic Typography (Google Font 'Cairo') for native Gulf/Saudi aesthetic
4. URL Hash Routing & Browser History (hashchange & initial hash loader)
5. Enhanced Lightbox with Next/Prev navigation, counter badge, and arrow keys
6. Context-Aware WhatsApp messaging (Arabic & English triggers)
"""

import re

def apply_enhancements():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update <head> with SEO, Social Meta, Favicon, and Arabic Font
    seo_meta_block = """  <title>Tipu Sultan | AI-Driven & Data-Driven Growth Architect (Riyadh, KSA)</title>
  
  <!-- Primary Meta & SEO -->
  <meta name="description" content="High-ticket performance marketing architect specializing in Meta Advantage+ ASC, Google Smart Bidding, and Server-Side CAPI systems across Saudi Arabia, GCC, and global DTC/SaaS brands. Verified $188K+ spend and 4.6x ROAS." />
  <meta name="keywords" content="Tipu Sultan, Growth Architect, Performance Marketing Riyadh, Meta Ads Saudi Arabia, Google Ads Specialist GCC, Server-Side CAPI, Tabby Tamara Marketing" />
  <meta name="author" content="Tipu Sultan" />
  <link rel="canonical" href="https://sultantipu199.github.io/sultan-growth/" />
  <link rel="icon" type="image/png" href="assets/tipu-sultan-profile.png" />
  <meta name="theme-color" content="#070b14" />

  <!-- Open Graph / Facebook / WhatsApp Preview -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://sultantipu199.github.io/sultan-growth/" />
  <meta property="og:title" content="Tipu Sultan | AI-Driven & Data-Driven Growth Architect" />
  <meta property="og:description" content="Scaled $869K+ in verified revenue at 4.6x ROAS with Meta Advantage+, CAPI 9.0+ Signal Engineering, and 3:2:2 Creative Testing. Explore Executive CV & 22-Slide Decks." />
  <meta property="og:image" content="https://sultantipu199.github.io/sultan-growth/assets/documents/deck-cover-en-preview.png" />
  <meta property="og:site_name" content="Tipu Sultan Growth Portfolio" />
  <meta property="og:locale" content="en_US" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Tipu Sultan | Growth Architect Portfolio" />
  <meta name="twitter:description" content="AI & Data-Engineered Paid Acquisition Architecture across Meta, Google & YouTube. Based in Riyadh, KSA." />
  <meta name="twitter:image" content="https://sultantipu199.github.io/sultan-growth/assets/documents/deck-cover-en-preview.png" />

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Tipu Sultan — Growth Architect",
    "image": "https://sultantipu199.github.io/sultan-growth/assets/tipu-sultan-profile.png",
    "url": "https://sultantipu199.github.io/sultan-growth/",
    "telephone": "+966566482865",
    "email": "freelancersultan143@gmail.com",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Riyadh",
      "addressCountry": "SA"
    },
    "description": "AI-Driven and Data-Driven Growth Architect specializing in full-funnel paid media architecture and signal resilience.",
    "priceRange": "$$$$"
  }
  </script>

  <!-- Tailwind CSS CDN -->"""

    # Replace <title>...</title>\n\n  <!-- Tailwind CSS CDN -->
    old_title_pattern = r'<title>.*?</title>\s*<!-- Tailwind CSS CDN -->'
    if re.search(old_title_pattern, html):
        html = re.sub(old_title_pattern, seo_meta_block, html, count=1)
        print("Updated <head> with SEO, Social Meta, Favicon, and Schema.org")

    # Update Google Fonts link to include Cairo
    old_fonts = 'family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@600;700;800;900&display=swap'
    new_fonts = 'family=Cairo:wght@400;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@600;700;800;900&display=swap'
    if old_fonts in html:
        html = html.replace(old_fonts, new_fonts, 1)
        print("Updated Google Fonts with 'Cairo' for Gulf Arabic typography")

    # Add .font-arabic CSS class in <style>
    arabic_style = """
    .font-arabic {
      font-family: 'Cairo', sans-serif;
    }
    .font-display { font-family: 'Outfit', sans-serif; }"""
    if '.font-display { font-family: \'Outfit\', sans-serif; }' in html and '.font-arabic' not in html:
        html = html.replace('.font-display { font-family: \'Outfit\', sans-serif; }', arabic_style, 1)
        print("Added .font-arabic CSS definition")

    # 2. Update Lightbox Modal with Next / Prev buttons and counter
    old_lightbox = """  <!-- Lightbox Modal for Proofs & Creatives -->
  <div id="lightboxModal" class="fixed inset-0 z-50 bg-black/95 backdrop-blur-2xl hidden flex items-center justify-center p-4">
    <div class="relative max-w-5xl w-full max-h-[92vh] flex flex-col items-center justify-center">
      <button onclick="closeLightbox()" class="absolute -top-12 right-0 text-white text-2xl hover:text-emerald-400 transition-colors">
        <i class="fa-solid fa-xmark"></i>
      </button>
      <img id="lightboxImg" src="" alt="Proof Preview" class="max-w-full max-h-[82vh] rounded-2xl object-contain shadow-2xl border border-slate-800" />
      <p id="lightboxCaption" class="mt-4 text-xs font-semibold text-slate-300 text-center"></p>
    </div>
  </div>"""

    new_lightbox = """  <!-- Enhanced Lightbox Modal with Next/Prev Gallery Navigation -->
  <div id="lightboxModal" class="fixed inset-0 z-50 bg-black/95 backdrop-blur-2xl hidden flex items-center justify-center p-2 sm:p-4">
    <div class="relative max-w-5xl w-full max-h-[94vh] flex flex-col items-center justify-center">
      
      <!-- Top Bar: Counter & Close Button -->
      <div class="w-full flex items-center justify-between pb-3">
        <span id="lightboxCounter" class="text-xs font-bold text-slate-400 bg-slate-900/80 px-3 py-1 rounded-lg border border-slate-800">
          Proof 01 / 59
        </span>
        <div class="flex items-center gap-2">
          <button onclick="downloadActiveLightboxImage()" class="px-3 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 text-xs font-bold border border-slate-700 flex items-center gap-1.5 transition-all">
            <i class="fa-solid fa-download text-emerald-400 text-[11px]"></i> Download
          </button>
          <button onclick="closeLightbox()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center transition-colors">
            <i class="fa-solid fa-xmark text-sm"></i>
          </button>
        </div>
      </div>

      <!-- Main Image Display Container with Navigation Arrows -->
      <div class="relative w-full flex items-center justify-center group">
        <!-- Prev Button -->
        <button onclick="prevLightboxItem()" class="absolute left-2 sm:-left-6 top-1/2 -translate-y-1/2 w-11 h-11 rounded-full bg-slate-900/80 hover:bg-emerald-600 text-white border border-slate-700 flex items-center justify-center shadow-xl transition-all z-20">
          <i class="fa-solid fa-chevron-left text-sm"></i>
        </button>

        <!-- Image -->
        <img id="lightboxImg" src="" alt="Verified Campaign Evidence" class="max-w-full max-h-[78vh] rounded-2xl object-contain shadow-2xl border border-slate-800" />

        <!-- Next Button -->
        <button onclick="nextLightboxItem()" class="absolute right-2 sm:-right-6 top-1/2 -translate-y-1/2 w-11 h-11 rounded-full bg-slate-900/80 hover:bg-emerald-600 text-white border border-slate-700 flex items-center justify-center shadow-xl transition-all z-20">
          <i class="fa-solid fa-chevron-right text-sm"></i>
        </button>
      </div>

      <!-- Bottom Caption & Keyboard Hints -->
      <div class="w-full flex flex-col sm:flex-row items-center justify-between gap-2 mt-3 pt-2 border-t border-slate-800/80">
        <p id="lightboxCaption" class="text-xs font-bold text-slate-200 text-center sm:text-left truncate max-w-xl"></p>
        <span class="text-[10px] text-slate-500 font-medium">Use ← → arrow keys to flip proofs, ESC to close</span>
      </div>

    </div>
  </div>"""

    if 'id="lightboxModal"' in html:
        lightbox_pattern = r'<!-- Lightbox Modal for Proofs & Creatives -->\s*<div id="lightboxModal"[\s\S]*?</div>\s*</div>'
        if re.search(lightbox_pattern, html):
            html = re.sub(lightbox_pattern, new_lightbox, html, count=1)
            print("Upgraded #lightboxModal with Next/Prev and counter")

    # 3. Add Lightbox List State and URL Hash Routing to JavaScript
    enhanced_js = """
    // ==========================================
    // ENHANCED LIGHTBOX & GALLERY NAVIGATION
    // ==========================================
    let activeLightboxList = [];
    let activeLightboxIndex = 0;

    function openLightboxWithContext(list, index) {
      activeLightboxList = list;
      activeLightboxIndex = index;
      renderLightboxItem();
      document.getElementById('lightboxModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }

    function renderLightboxItem() {
      if (!activeLightboxList || activeLightboxList.length === 0) return;
      const item = activeLightboxList[activeLightboxIndex];
      const img = document.getElementById('lightboxImg');
      const caption = document.getElementById('lightboxCaption');
      const counter = document.getElementById('lightboxCounter');

      img.src = item.file || item.src;
      caption.innerText = item.title || item.caption || 'Verified Campaign Evidence';
      counter.innerText = `Item ${activeLightboxIndex + 1} of ${activeLightboxList.length}`;
    }

    function nextLightboxItem() {
      if (activeLightboxList.length > 0) {
        activeLightboxIndex = (activeLightboxIndex + 1) % activeLightboxList.length;
        renderLightboxItem();
      }
    }

    function prevLightboxItem() {
      if (activeLightboxList.length > 0) {
        activeLightboxIndex = (activeLightboxIndex - 1 + activeLightboxList.length) % activeLightboxList.length;
        renderLightboxItem();
      }
    }

    function downloadActiveLightboxImage() {
      if (activeLightboxList.length > 0) {
        const item = activeLightboxList[activeLightboxIndex];
        const link = document.createElement('a');
        link.href = item.file || item.src;
        link.download = (item.title ? item.title.replace(/[^a-zA-Z0-9_-]/g, '_') : 'proof') + '.png';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
    }

    // Context-Aware Arabic WhatsApp Trigger
    function triggerArabicWhatsApp() {
      const msg = encodeURIComponent("السلام عليكم تيبو سلطان، اطلعت على محفظة أعمالك وعروضك الاستراتيجية، وأرغب في مناقشة تدقيق وتوسيع حملاتنا الإعلانية في الخليج.");
      window.open(`https://wa.me/${CONFIG.phone}?text=${msg}`, '_blank');
    }

    // Two-Way URL Hash Routing for Browser Back / Forward
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '');
      if (hash && tabLabels[hash]) {
        switchTab(hash);
      }
    });

    // Check Initial URL Hash on Page Load
    function handleInitialHash() {
      const hash = window.location.hash.replace('#', '');
      if (hash && tabLabels[hash]) {
        switchTab(hash);
      } else {
        switchTab('executive-assets');
      }
    }
"""

    if 'activeLightboxList' not in html:
        html = html.replace('// Initialize App', enhanced_js + '\n    // Initialize App', 1)
        print("Inserted enhanced lightbox handlers and hashchange routing")

    # Update renderVault and renderCreatives to use openLightboxWithContext
    old_vault_render = "tile.onclick = () => openLightbox(item.file, item.title);"
    new_vault_render = "tile.onclick = () => openLightboxWithContext(items, items.indexOf(item));"
    if old_vault_render in html:
        html = html.replace(old_vault_render, new_vault_render)
        print("Connected vault items to openLightboxWithContext")

    # Update keyboard listeners to handle lightbox navigation
    old_keys = "if (e.key === 'ArrowRight' && isDeckOpen) {\n        nextDeckSlide();\n      } else if (e.key === 'ArrowLeft' && isDeckOpen) {\n        prevDeckSlide();"
    new_keys = """if (e.key === 'ArrowRight') {
        if (isDeckOpen) nextDeckSlide();
        else if (isLightboxOpen) nextLightboxItem();
      } else if (e.key === 'ArrowLeft') {
        if (isDeckOpen) prevDeckSlide();
        else if (isLightboxOpen) prevLightboxItem();"""
    
    if "const isLightboxOpen = !document.getElementById('lightboxModal').classList.contains('hidden');" not in html:
        html = html.replace("const isCvOpen = !document.getElementById('cvModal').classList.contains('hidden');", "const isCvOpen = !document.getElementById('cvModal').classList.contains('hidden');\n      const isLightboxOpen = !document.getElementById('lightboxModal').classList.contains('hidden');", 1)
        html = html.replace(old_keys, new_keys, 1)
        print("Updated keyboard handler for lightbox arrow navigation")

    # Update initial call to handleInitialHash
    if "switchTab(\"executive-assets\");" in html:
        html = html.replace("switchTab(\"executive-assets\");", "handleInitialHash();", 1)
        print("Updated initialization to handleInitialHash()")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("All enhancements applied cleanly!")

if __name__ == '__main__':
    apply_enhancements()
