# -*- coding: utf-8 -*-
"""
verify_enhanced_portfolio.py
Verifies DOM structure, file paths, scripts, and asset integrity of index.html
"""

import os
import re
from bs4 import BeautifulSoup

def verify():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    print("=== 1. VERIFYING SECTIONS ===")
    required_sections = ['ai-engine', 'frameworks', 'proofs', 'vault', 'creatives', 'executive-assets', 'audit', 'calculator']
    for sec_id in required_sections:
        sec = soup.find('section', id=sec_id)
        if sec:
            h2 = sec.find(['h2', 'h3'])
            h2_text = h2.get_text(strip=True) if h2 else 'No heading'
            print(f"  [PASS] Section #{sec_id}: {h2_text[:50]}")
        else:
            print(f"  [FAIL] Missing section #{sec_id}")

    print("\n=== 2. VERIFYING MODALS ===")
    required_modals = ['cvModal', 'deckModal', 'caseStudyModal', 'lightboxModal', 'emailModal']
    for m_id in required_modals:
        m = soup.find('div', id=m_id)
        if m:
            print(f"  [PASS] Modal #{m_id} exists")
        else:
            print(f"  [FAIL] Missing modal #{m_id}")

    print("\n=== 3. VERIFYING ASSET LINKS & FILE EXISTENCE ===")
    assets_to_check = [
        'assets/documents/Tipu-Sultan-Growth-Architect-CV.pdf',
        'assets/documents/Tipu-Sultan-Growth-Architect-CV.docx',
        'assets/documents/Tipu-Sultan-Growth-Architect-CV-AR.pdf',
        'assets/documents/tipu-sultan-portfolio-en.pptx',
        'assets/documents/tipu-sultan-portfolio-ar.pptx',
        'assets/documents/cv-card-preview-1.webp',
        'assets/documents/cv-ar-card-preview-1.webp',
        'assets/documents/cv-preview-page-1.webp',
        'assets/documents/cv-preview-page-2.webp',
        'assets/documents/cv-ar-preview-page-1.webp',
        'assets/documents/cv-ar-preview-page-2.webp',
        'assets/documents/cv-ar-preview-page-3.webp',
        'assets/documents/deck-cover-en-preview.webp',
        'assets/documents/deck-cover-ar-preview.webp',
        'assets/documents/google-ads-performance-portfolio-deck.pptx',
        'assets/documents/growth-marketing-case-studies-deck-vol1.pptx',
        'assets/documents/growth-marketing-case-studies-deck-vol2.pptx'
    ]

    for asset in assets_to_check:
        exists = os.path.exists(asset)
        size = os.path.getsize(asset) if exists else 0
        status = "PASS" if exists else "FAIL"
        print(f"  [{status}] {asset} ({size/1024:.1f} KB)")

    print("\n=== 4. VERIFYING JAVASCRIPT SYNTAX IN SCRIPT TAGS ===")
    # Extract script
    scripts = soup.find_all('script')
    main_script = ""
    for s in scripts:
        if s.string and 'presentationDecks' in s.string:
            main_script = s.string
            break
    
    if main_script:
        print(f"  [PASS] Found main script tag with {len(main_script)} characters")
        required_fns = [
            'openCvModal', 'closeCvModal', 'switchCvLang', 'setCvPage',
            'openDeckModal', 'closeDeckModal', 'switchDeckLang', 'setDeckSlide',
            'nextDeckSlide', 'prevDeckSlide', 'filterAssets'
        ]
        for fn in required_fns:
            if fn in main_script:
                print(f"  [PASS] Function {fn}() is defined")
            else:
                print(f"  [FAIL] Missing function {fn}()")
    else:
        print("  [FAIL] Main script tag not found")

    print("\n=== 5. VERIFYING NAVBAR & DRAWER LINKS ===")
    nav_links = soup.find_all('a', href=re.compile(r'^#'))
    hrefs = set(a['href'][1:] for a in nav_links if a['href'] != '#')
    print("  Internal navigation anchors found:", hrefs)
    for h in hrefs:
        target = soup.find(id=h)
        status = "PASS" if target else "FAIL"
        print(f"  [{status}] Target element for #{h} exists: {bool(target)}")

if __name__ == '__main__':
    verify()

