# -*- coding: utf-8 -*-
"""
Script to generate the updated index.html with:
1. Executive Assets Section (#executive-assets) featuring:
   - English CV (.docx and .pdf)
   - Arabic CV (.pdf)
   - English Presentation Deck (22 slides .pptx)
   - Arabic Presentation Deck (22 slides .pptx)
2. Interactive CV Viewer Modal (supporting both English 2 pages and Arabic 3 pages)
3. Interactive Slide Deck Viewer Modal (supporting all 22 slides in both EN and AR with live language toggle)
4. Navbar updates (desktop and mobile)
5. Hero section CTA updates
"""

import json
import os
import re

def build_update():
    # Read decks data
    with open('decks_data.json', 'r', encoding='utf-8') as f:
        decks_raw = json.load(f)

    # Let's inspect the slide text and build clean presentation models
    slides_en = []
    for s in decks_raw['en']:
        num = s['num']
        texts = s['texts']
        title = texts[0] if len(texts) > 0 else f"Slide {num}"
        subtitle = texts[1] if len(texts) > 1 else ""
        points = texts[2:] if len(texts) > 2 else []
        
        # Categorize
        if num == 1:
            category = "PORTFOLIO PRESENTATION"
            image = "assets/documents/deck-cover-en-preview.webp"
        elif num in [2, 3]:
            category = "PERFORMANCE ARCHITECTURE"
            image = "assets/documents/deck_media/image-4-1.png"
        elif 4 <= num <= 10:
            category = "GROWTH PLAYBOOK"
            image = "assets/documents/deck_media/image-4-1.png"
        elif num == 11:
            category = "FUNNEL SIMULATOR"
            image = "assets/documents/deck_media/image-12-1.png"
        elif 12 <= num <= 17:
            category = "CASE STUDY"
            if num == 13:
                image = "assets/proofs/meta-ads/meta-campaign-high-roas-results-proof-06.png"
            elif num == 14:
                image = "assets/proofs/ecommerce-roas/dtc-ecommerce-website-purchases-proof-01.png"
            elif num == 15:
                image = "assets/proofs/google-ads/google-search-conversion-metrics-proof-01.png"
            elif num == 16:
                image = "assets/proofs/lead-generation/high-ticket-lead-acquisition-proof-01.png"
            elif num == 17:
                image = "assets/proofs/video-youtube/youtube-video-ads-metrics-proof-01.png"
            else:
                image = "assets/documents/deck_media/image-12-1.png"
        elif num == 18:
            category = "EVIDENCE VAULT"
            image = "assets/documents/deck_media/image-18-1.png"
        elif num == 19:
            category = "CREATIVE ENGINE"
            image = "assets/creatives/facebook-campaigns/meta-creative-hook-angle-01.jpg"
        elif num in [20, 21]:
            category = "AUDIT & ENGAGEMENT"
            image = "assets/documents/deck_media/image-21-1.png"
        else:
            category = "FULL PORTFOLIO"
            image = "assets/documents/deck_media/image-22-1.png"

        slides_en.append({
            "num": num,
            "category": category,
            "title": title,
            "subtitle": subtitle,
            "points": points[:8],
            "image": image
        })

    slides_ar = []
    for s in decks_raw['ar']:
        num = s['num']
        texts = s['texts']
        title = texts[0] if len(texts) > 0 else f"الشريحة {num}"
        subtitle = texts[1] if len(texts) > 1 else ""
        points = texts[2:] if len(texts) > 2 else []
        
        if num == 1:
            category = "عروض محفظة الأعمال"
            image = "assets/documents/deck-cover-ar-preview.webp"
        elif num in [2, 3]:
            category = "هندسة الأداء"
            image = "assets/documents/deck_media_ar/image-4-1.png"
        elif 4 <= num <= 10:
            category = "ملاعب النمو الاستراتيجية"
            image = "assets/documents/deck_media_ar/image-4-1.png"
        elif num == 11:
            category = "محاكاة القمع"
            image = "assets/documents/deck_media_ar/image-12-1.png"
        elif 12 <= num <= 17:
            category = "دراسة حالة الأداء"
            if num == 13:
                image = "assets/proofs/meta-ads/meta-campaign-high-roas-results-proof-06.png"
            elif num == 14:
                image = "assets/proofs/ecommerce-roas/dtc-ecommerce-website-purchases-proof-01.png"
            elif num == 15:
                image = "assets/proofs/google-ads/google-search-conversion-metrics-proof-01.png"
            elif num == 16:
                image = "assets/proofs/lead-generation/high-ticket-lead-acquisition-proof-01.png"
            elif num == 17:
                image = "assets/proofs/video-youtube/youtube-video-ads-metrics-proof-01.png"
            else:
                image = "assets/documents/deck_media_ar/image-12-1.png"
        elif num == 18:
            category = "خزنة الأدلة والبراهين"
            image = "assets/documents/deck_media_ar/image-18-1.png"
        elif num == 19:
            category = "محرك اختبار الإبداع"
            image = "assets/creatives/facebook-campaigns/meta-creative-hook-angle-01.jpg"
        elif num in [20, 21]:
            category = "التدقيق والتشخيص"
            image = "assets/documents/deck_media_ar/image-21-1.png"
        else:
            category = "المحفظة الكاملة"
            image = "assets/documents/deck_media_ar/image-22-1.png"

        slides_ar.append({
            "num": num,
            "category": category,
            "title": title,
            "subtitle": subtitle,
            "points": points[:8],
            "image": image
        })

    # Prepare JS data snippet
    decks_js = f"""
    const presentationDecks = {{
      en: {json.dumps(slides_en, ensure_ascii=False)},
      ar: {json.dumps(slides_ar, ensure_ascii=False)}
    }};
    """

    print("Prepared presentation decks JS data. EN slides:", len(slides_en), "AR slides:", len(slides_ar))
    return decks_js

if __name__ == '__main__':
    build_update()

