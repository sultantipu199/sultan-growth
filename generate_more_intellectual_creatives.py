"""
generate_more_intellectual_creatives.py
Generates 12 additional highly intellectual, graphic-designer-crafted performance marketing
campaign angle cards (Angles #37 through #48) for Tipu Sultan's Growth Architecture platform.
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = r"e:\Sultan Grouth\assets\creatives\facebook-campaigns"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REGULAR = r"C:\Windows\Fonts\segoeui.ttf"
FONT_BLACK = r"C:\Windows\Fonts\impact.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def draw_pill(draw, x, y, text, font, bg_color, text_color, px=20, py=10, radius=20):
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    w = tw + px * 2
    h = th + py * 2
    draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=bg_color)
    draw.text((x + px, y + py - 2), text, font=font, fill=text_color)
    return w, h

def draw_button(draw, x, y, w, h, text, font, bg_color, text_color, radius=16):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=bg_color)
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = x + (w - tw) // 2
    ty = y + (h - th) // 2 - 2
    draw.text((tx, ty), text, font=font, fill=text_color)

# -------------------------------------------------------------
# Card 37: 3-Second Hook Retention Drop-Off Curve
# -------------------------------------------------------------
def make_card_37():
    img = Image.new("RGB", (1080, 1080), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(24, 33, 56), outline=(99, 102, 241), width=3)
    
    draw_pill(draw, 80, 80, "VIDEO CREATIVE TESTING ANALYTICS", get_font(FONT_BOLD, 20), (99, 102, 241), (255, 255, 255))
    draw.text((80, 150), "THE 3-SECOND THUMB-STOP FORMULA", font=get_font(FONT_BOLD, 46), fill=(255, 255, 255))
    draw.text((80, 215), "If you lose 80% of viewers in the first 3 seconds, your creative is dead.", font=get_font(FONT_REGULAR, 24), fill=(148, 163, 184))
    
    # Chart Box
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    
    # Left comparison: Tipu's Hook
    draw.rounded_rectangle([110, 305, 520, 650], radius=18, fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    draw_pill(draw, 130, 325, "✅ TIPU'S PATTERN INTERRUPT", get_font(FONT_BOLD, 18), (6, 78, 59), (52, 211, 153))
    draw.text((130, 395), "3-SEC RETENTION: 68.4%", font=get_font(FONT_BOLD, 28), fill=(52, 211, 153))
    draw.text((130, 445), "• 0-1s: Bold text shock trigger", font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
    draw.text((130, 490), "• 1-3s: Visual speed ramp", font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
    draw.text((130, 535), "• 3-15s: Proof demonstration", font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
    draw.text((130, 590), "OUTCOME: 3.84% CTR / 4.8x ROAS", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    # Right comparison: Standard generic UGC
    draw.rounded_rectangle([560, 305, 970, 650], radius=18, fill=(30, 41, 59), outline=(239, 68, 68), width=2)
    draw_pill(draw, 580, 325, "❌ GENERIC 'HEY GUYS' UGC", get_font(FONT_BOLD, 18), (69, 10, 10), (248, 113, 113))
    draw.text((580, 395), "3-SEC RETENTION: 21.2%", font=get_font(FONT_BOLD, 28), fill=(248, 113, 113))
    draw.text((580, 445), "• 0-1s: Boring intro talking head", font=get_font(FONT_REGULAR, 22), fill=(203, 213, 225))
    draw.text((580, 490), "• 1-3s: Slow product panning", font=get_font(FONT_REGULAR, 22), fill=(203, 213, 225))
    draw.text((580, 535), "• 3-15s: Viewer already scrolled", font=get_font(FONT_REGULAR, 22), fill=(203, 213, 225))
    draw.text((580, 590), "OUTCOME: 0.92% CTR / 1.3x ROAS", font=get_font(FONT_BOLD, 22), fill=(248, 113, 113))
    
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(30, 41, 59))
    draw.text((120, 735), "KEY TAKEAWAY: Creative hook velocity is the #1 lever for lowering Meta CPMs.", font=get_font(FONT_BOLD, 22), fill=(245, 158, 11))
    
    draw_button(draw, 80, 820, 920, 100, "LEARN THE 3:2:2 HOOK METHOD  ➤", get_font(FONT_BOLD, 30), (99, 102, 241), (255, 255, 255), radius=20)
    draw.text((370, 945), "Growth Marketing Architecture by Tipu Sultan", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-37.jpg"), quality=95)
    print("Created Angle #37")

# -------------------------------------------------------------
# Card 38: Omnichannel Attribution Triangulation
# -------------------------------------------------------------
def make_card_38():
    img = Image.new("RGB", (1080, 1080), color=(10, 15, 30))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(15, 23, 42), outline=(14, 165, 233), width=3)
    
    draw_pill(draw, 80, 80, "FIRST-PARTY DATA & ATTRIBUTION", get_font(FONT_BOLD, 20), (14, 165, 233), (255, 255, 255))
    draw.text((80, 150), "STOP TRUSTING IN-PLATFORM ROAS BLINDLY", font=get_font(FONT_BOLD, 42), fill=(255, 255, 255))
    draw.text((80, 215), "Meta claims 3.8x. Google claims 3.2x. Here is your true blended reality.", font=get_font(FONT_REGULAR, 24), fill=(148, 163, 184))
    
    # 3-Channel Box
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(10, 15, 30), outline=(51, 65, 85), width=2)
    
    channels = [
        ("META REPORTED", "3.82x ROAS", "Includes view-through & duplicated claims", (59, 130, 246)),
        ("GOOGLE REPORTED", "3.14x ROAS", "Over-attributing branded search clicks", (234, 179, 8)),
        ("TRUE BLENDED MER", "4.61x BLENDED", "Clean First-Party Bank Account Revenue", (16, 185, 129))
    ]
    cy = 305
    for title, metric, desc, col in channels:
        draw.rounded_rectangle([110, cy, 970, cy + 105], radius=16, fill=(24, 33, 56), outline=col, width=2)
        draw.text((140, cy + 18), title, font=get_font(FONT_BOLD, 18), fill=(148, 163, 184))
        draw.text((140, cy + 45), metric, font=get_font(FONT_BOLD, 36), fill=col)
        draw.text((520, cy + 40), desc, font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
        cy += 125
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(30, 41, 59))
    draw.text((120, 735), "ELIMINATED OVERLAP: -$4,200/mo in double-counted phantom conversions.", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    draw_button(draw, 80, 820, 920, 100, "REQUEST FIRST-PARTY ATTRIBUTION AUDIT  ➤", get_font(FONT_BOLD, 28), (14, 165, 233), (255, 255, 255), radius=20)
    draw.text((370, 945), "Engineered by Tipu Sultan | Data Architect", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-38.jpg"), quality=95)
    print("Created Angle #38")

# -------------------------------------------------------------
# Card 39: GCC & Saudi Market Scaling Blueprint
# -------------------------------------------------------------
def make_card_39():
    img = Image.new("RGB", (1080, 1080), color=(10, 25, 20))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(15, 35, 30), outline=(16, 185, 129), width=3)
    
    draw_pill(draw, 80, 80, "🇸🇦 GCC & SAUDI ARABIA SCALING PLAYBOOK", get_font(FONT_BOLD, 20), (16, 185, 129), (255, 255, 255))
    draw.text((80, 150), "SCALING E-COMMERCE IN RIYADH & JEDDAH", font=get_font(FONT_BOLD, 42), fill=(255, 255, 255))
    draw.text((80, 215), "How we scaled Saudi brands past 5.4x ROAS with local checkout architectures.", font=get_font(FONT_REGULAR, 24), fill=(167, 243, 208))
    
    # 3 GCC Pillars
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(10, 25, 20), outline=(5, 150, 105), width=2)
    
    pillars = [
        ("01", "TAMARA & TABBY BNPL FUNNELS", "Installments increase checkout conversion rate by +44% for AOV > 250 SAR."),
        ("02", "WHATSAPP COD CONFIRMATION BOT", "Automated confirmation brings Cash-On-Delivery rejection down from 32% to 7%."),
        ("03", "KSA NATIVE DIALECT HOOKS", "Localized Gulf creative copy crushes generic imported translations.")
    ]
    py = 310
    for num, title, desc in pillars:
        draw.text((110, py + 15), num, font=get_font(FONT_BOLD, 42), fill=(52, 211, 153))
        draw.text((190, py + 15), title, font=get_font(FONT_BOLD, 22), fill=(255, 255, 255))
        draw.text((190, py + 52), desc, font=get_font(FONT_REGULAR, 20), fill=(209, 250, 229))
        py += 115
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(6, 78, 59))
    draw.text((120, 735), "SAUDI MARKET METRIC: Over 1.4M SAR generated across KSA campaigns.", font=get_font(FONT_BOLD, 22), fill=(255, 255, 255))
    
    draw_button(draw, 80, 820, 920, 100, "SCALE YOUR BRAND IN SAUDI ARABIA  ➤", get_font(FONT_BOLD, 30), (16, 185, 129), (255, 255, 255), radius=20)
    draw.text((360, 945), "Direct Saudi WhatsApp: +966 56 648 2865", font=get_font(FONT_REGULAR, 20), fill=(167, 243, 208))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-39.jpg"), quality=95)
    print("Created Angle #39")

# -------------------------------------------------------------
# Card 40: Problem-Agitation-Solution (PAS) High-Contrast Split
# -------------------------------------------------------------
def make_card_40():
    img = Image.new("RGB", (1080, 1080), color=(20, 10, 15))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(30, 15, 22), outline=(244, 63, 94), width=3)
    
    draw_pill(draw, 80, 80, "DIRECT RESPONSE FRAMEWORK", get_font(FONT_BOLD, 20), (244, 63, 94), (255, 255, 255))
    draw.text((80, 150), "TIRED OF 'HOPE' MARKETING?", font=get_font(FONT_BOLD, 48), fill=(255, 255, 255))
    draw.text((80, 215), "Why 90% of brands fail to scale past $20,000/month in ad spend.", font=get_font(FONT_REGULAR, 24), fill=(253, 164, 175))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(20, 10, 15), outline=(51, 65, 85), width=2)
    
    # Left: The Trap
    draw.rounded_rectangle([110, 305, 520, 650], radius=18, fill=(35, 15, 20), outline=(239, 68, 68), width=2)
    draw_pill(draw, 130, 325, "THE NOVICE TRAP", get_font(FONT_BOLD, 18), (69, 10, 10), (248, 113, 113))
    draw.text((130, 395), "BURNING CAPITAL", font=get_font(FONT_BOLD, 26), fill=(248, 113, 113))
    draw.text((130, 440), "• Guessing ad creatives", font=get_font(FONT_REGULAR, 22), fill=(254, 205, 211))
    draw.text((130, 485), "• Touching campaigns daily", font=get_font(FONT_REGULAR, 22), fill=(254, 205, 211))
    draw.text((130, 530), "• Blaming the algorithm", font=get_font(FONT_REGULAR, 22), fill=(254, 205, 211))
    draw.text((130, 585), "RESULT: Net Margin = 0%", font=get_font(FONT_BOLD, 22), fill=(239, 68, 68))
    
    # Right: The Engine
    draw.rounded_rectangle([560, 305, 970, 650], radius=18, fill=(15, 35, 25), outline=(16, 185, 129), width=2)
    draw_pill(draw, 580, 325, "THE TIPU SULTAN ENGINE", get_font(FONT_BOLD, 18), (6, 78, 59), (52, 211, 153))
    draw.text((580, 395), "SCIENTIFIC SCALING", font=get_font(FONT_BOLD, 26), fill=(52, 211, 153))
    draw.text((580, 440), "• 3:2:2 Creative Sandboxes", font=get_font(FONT_REGULAR, 22), fill=(209, 250, 229))
    draw.text((580, 485), "• Advantage+ Automated Bidding", font=get_font(FONT_REGULAR, 22), fill=(209, 250, 229))
    draw.text((580, 530), "• Full Server-Side Attribution", font=get_font(FONT_REGULAR, 22), fill=(209, 250, 229))
    draw.text((580, 585), "RESULT: 35%+ Net Margin", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    draw_button(draw, 80, 710, 920, 95, "SCHEDULE YOUR 10-MINUTE ACCOUNT AUDIT  ➤", get_font(FONT_BOLD, 28), (244, 63, 94), (255, 255, 255), radius=20)
    draw_button(draw, 80, 830, 920, 95, "OR CHAT DIRECTLY ON WHATSAPP (+966566482865)", get_font(FONT_BOLD, 24), (16, 185, 129), (255, 255, 255), radius=20)
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-40.jpg"), quality=95)
    print("Created Angle #40")

# -------------------------------------------------------------
# Card 41: High-Ticket Lead Gen Objection Buster
# -------------------------------------------------------------
def make_card_41():
    img = Image.new("RGB", (1080, 1080), color=(15, 20, 35))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(20, 28, 48), outline=(168, 85, 247), width=3)
    
    draw_pill(draw, 80, 80, "HIGH-TICKET B2B ACQUISITION", get_font(FONT_BOLD, 20), (168, 85, 247), (255, 255, 255))
    draw.text((80, 150), "3 MYTHS ABOUT B2B PAID ADVERTISING", font=get_font(FONT_BOLD, 44), fill=(255, 255, 255))
    draw.text((80, 215), "Why enterprise founders waste months on cold email before testing paid ads.", font=get_font(FONT_REGULAR, 24), fill=(192, 132, 252))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(15, 20, 35), outline=(51, 65, 85), width=2)
    
    myths = [
        ("MYTH 1: 'OUR BUYERS ARE NOT ON FACEBOOK/INSTAGRAM'", "REALITY: VPs and CEOs spend 48 mins daily on Meta apps. Cold pain-point ads convert 3x higher than generic LinkedIn InMails."),
        ("MYTH 2: 'HIGH-TICKET LEADS COST $500+ EACH'", "REALITY: With self-qualifying VSL funnels, our average qualified sales call cost is $48.20 with an 87% show-up rate."),
        ("MYTH 3: 'PAID ADS BRING UNQUALIFIED JUNK'", "REALITY: Automated 4-question intake disqualifies non-decision makers before they even see your booking calendar.")
    ]
    my = 300
    for title, body in myths:
        draw.text((110, my + 10), title, font=get_font(FONT_BOLD, 20), fill=(245, 158, 11))
        draw.text((110, my + 42), body, font=get_font(FONT_REGULAR, 20), fill=(226, 232, 240))
        my += 115
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(30, 41, 59))
    draw.text((120, 735), "PROVEN PIPELINE: $1.4M+ in enterprise sales pipeline generated for B2B clients.", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    draw_button(draw, 80, 820, 920, 100, "BUILD YOUR PREDICTIVE B2B PIPELINE  ➤", get_font(FONT_BOLD, 28), (168, 85, 247), (255, 255, 255), radius=20)
    draw.text((370, 945), "Engineered by Tipu Sultan | Growth Architect", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-41.jpg"), quality=95)
    print("Created Angle #41")

# -------------------------------------------------------------
# Card 42: Dynamic Product Ads (DPA) Smart Catalog Angle
# -------------------------------------------------------------
def make_card_42():
    img = Image.new("RGB", (1080, 1080), color=(18, 18, 18))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(28, 28, 28), outline=(234, 179, 8), width=3)
    
    draw_pill(draw, 80, 80, "DYNAMIC PRODUCT ADS (DPA) ENGINE", get_font(FONT_BOLD, 20), (234, 179, 8), (18, 18, 18))
    draw.text((80, 150), "DYNAMIC CATALOG ADS THAT CONVERT", font=get_font(FONT_BOLD, 44), fill=(255, 255, 255))
    draw.text((80, 215), "Custom frame overlays that turn boring product feeds into conversion magnets.", font=get_font(FONT_REGULAR, 24), fill=(156, 163, 175))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(18, 18, 18), outline=(60, 60, 60), width=2)
    
    # Feature checklist
    features = [
        ("⚡ LIVE PRICE STRIKETHROUGHS", "Auto-displays discount percentage dynamically from your Shopify feed."),
        ("🔥 INVENTORY SCARCITY BADGE", "Triggers 'ONLY 4 LEFT IN STOCK' automatically when inventory drops."),
        ("⭐ STAR RATINGS & TRUST STAMPS", "Injects 4.9/5 star ratings directly onto product image carousels."),
        ("🚀 5.4X BLENDED RETARGETING ROAS", "Captures cart abandoners within 12 hours of viewing product pages.")
    ]
    fy = 310
    for t, d in features:
        draw.text((120, fy + 5), t, font=get_font(FONT_BOLD, 22), fill=(250, 204, 21))
        draw.text((120, fy + 40), d, font=get_font(FONT_REGULAR, 20), fill=(243, 244, 246))
        fy += 85
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(35, 35, 35))
    draw.text((120, 735), "ZERO MANUAL UPDATES: Automatically syncs 1,000+ SKUs with live inventory.", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    draw_button(draw, 80, 820, 920, 100, "OPTIMIZE YOUR SHOPIFY DPA FEED  ➤", get_font(FONT_BOLD, 28), (234, 179, 8), (18, 18, 18), radius=20)
    draw.text((370, 945), "E-Commerce Architecture by Tipu Sultan", font=get_font(FONT_REGULAR, 20), fill=(156, 163, 175))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-42.jpg"), quality=95)
    print("Created Angle #42")

# -------------------------------------------------------------
# Card 43: Cohort LTV & 60-Day Retention Engine
# -------------------------------------------------------------
def make_card_43():
    img = Image.new("RGB", (1080, 1080), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(24, 33, 56), outline=(16, 185, 129), width=3)
    
    draw_pill(draw, 80, 80, "LTV & UNIT ECONOMICS MODELING", get_font(FONT_BOLD, 20), (16, 185, 129), (255, 255, 255))
    draw.text((80, 150), "TRUE PROFIT LIVES IN THE 2ND PURCHASE", font=get_font(FONT_BOLD, 42), fill=(255, 255, 255))
    draw.text((80, 215), "Why scaling brands focus on 60-day cohort LTV instead of day-1 ROAS.", font=get_font(FONT_REGULAR, 24), fill=(148, 163, 184))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    
    cohorts = [
        ("DAY 0: FIRST PURCHASE", "$48.00 AOV", "Customer acquired at break-even CAC", (148, 163, 184)),
        ("DAY 30: POST-PURCHASE AUTOMATION", "+$38.50 LIFT", "Automated email & WhatsApp replenishment", (59, 130, 246)),
        ("DAY 60: REPEAT BUYER COHORT", "$142.00 TOTAL LTV", "Pure profit margin with $0 additional ad spend", (52, 211, 153))
    ]
    cy = 310
    for stage, val, sub, col in cohorts:
        draw.rounded_rectangle([110, cy, 970, cy + 105], radius=16, fill=(30, 41, 59), outline=col, width=2)
        draw.text((140, cy + 18), stage, font=get_font(FONT_BOLD, 18), fill=(148, 163, 184))
        draw.text((140, cy + 45), val, font=get_font(FONT_BOLD, 36), fill=col)
        draw.text((540, cy + 40), sub, font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
        cy += 120
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(30, 41, 59))
    draw.text((120, 735), "CAC:LTV RATIO: Scaled from 1:1.8 to 1:4.2 across active client portfolios.", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    draw_button(draw, 80, 820, 920, 100, "CALCULATE YOUR STORE'S LTV POTENTIAL  ➤", get_font(FONT_BOLD, 28), (16, 185, 129), (255, 255, 255), radius=20)
    draw.text((370, 945), "Retention Architecture by Tipu Sultan", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-43.jpg"), quality=95)
    print("Created Angle #43")

# -------------------------------------------------------------
# Card 44: Creative Fatigue Early Warning Radar
# -------------------------------------------------------------
def make_card_44():
    img = Image.new("RGB", (1080, 1080), color=(20, 15, 30))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(28, 22, 45), outline=(236, 72, 153), width=3)
    
    draw_pill(draw, 80, 80, "ALGORITHMIC PACING & AD FATIGUE", get_font(FONT_BOLD, 20), (236, 72, 153), (255, 255, 255))
    draw.text((80, 150), "HOW TO PREVENT AD CREATIVE BURNOUT", font=get_font(FONT_BOLD, 42), fill=(255, 255, 255))
    draw.text((80, 215), "Why your best-performing ad stops working after 14 days of scaling.", font=get_font(FONT_REGULAR, 24), fill=(244, 114, 182))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(20, 15, 30), outline=(51, 65, 85), width=2)
    
    radar = [
        ("STAGE 1: FREQUENCY 1.0 - 1.8", "GOLDEN SCALING ZONE", "CPAs are low, high volume, audience is fresh.", (52, 211, 153)),
        ("STAGE 2: FREQUENCY 1.9 - 2.4", "WARNING ZONE (FATIGUE STARTS)", "CPMs increase by 22%, audience sees ad 2+ times.", (245, 158, 11)),
        ("STAGE 3: FREQUENCY > 2.5", "CRITICAL EXHAUSTION", "CPAs surge by +65%. ROAS collapses without creative rotation.", (239, 68, 68))
    ]
    ry = 310
    for s, name, desc, col in radar:
        draw.rounded_rectangle([110, ry, 970, ry + 105], radius=16, fill=(35, 28, 55), outline=col, width=2)
        draw.text((140, ry + 18), s, font=get_font(FONT_BOLD, 18), fill=(148, 163, 184))
        draw.text((140, ry + 45), name, font=get_font(FONT_BOLD, 30), fill=col)
        draw.text((540, ry + 40), desc, font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
        ry += 120
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(35, 28, 55))
    draw.text((120, 735), "TIPU'S SOLUTION: Continuous 3:2:2 Sandbox feeds 3 new winners every week.", font=get_font(FONT_BOLD, 22), fill=(244, 114, 182))
    
    draw_button(draw, 80, 820, 920, 100, "DEPLOY CONTINUOUS CREATIVE TESTING  ➤", get_font(FONT_BOLD, 28), (236, 72, 153), (255, 255, 255), radius=20)
    draw.text((370, 945), "Creative Engine Architecture by Tipu Sultan", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-44.jpg"), quality=95)
    print("Created Angle #44")

# -------------------------------------------------------------
# Card 45: High-Converting UGC Scripting Blueprint
# -------------------------------------------------------------
def make_card_45():
    img = Image.new("RGB", (1080, 1080), color=(15, 25, 35))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(20, 35, 50), outline=(56, 189, 248), width=3)
    
    draw_pill(draw, 80, 80, "DIRECT RESPONSE CONTENT SCRIPTING", get_font(FONT_BOLD, 20), (56, 189, 248), (15, 25, 35))
    draw.text((80, 150), "THE 5-BEAT DIRECT RESPONSE UGC SCRIPT", font=get_font(FONT_BOLD, 42), fill=(255, 255, 255))
    draw.text((80, 215), "The exact creator briefing template we use to generate million-dollar ads.", font=get_font(FONT_REGULAR, 24), fill=(186, 230, 253))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(15, 25, 35), outline=(51, 65, 85), width=2)
    
    beats = [
        ("BEAT 1 (0-3s)", "PATTERN INTERRUPT", "Visually unexpected action that halts the thumb."),
        ("BEAT 2 (3-8s)", "PAIN POINT AGITATION", "Call out the exact frustration the viewer experiences."),
        ("BEAT 3 (8-20s)", "THE MECHANISM", "Demonstrate how product uniquely solves that pain."),
        ("BEAT 4 (20-35s)", "SOCIAL PROOF & UNBOXING", "Show real user reviews, packaging, and genuine reaction."),
        ("BEAT 5 (35-45s)", "SCARCITY CALL TO ACTION", "Clear discount code + urgency deadline (e.g. 50% Off Today).")
    ]
    by = 295
    for b_num, b_title, b_desc in beats:
        draw.text((110, by + 5), b_num, font=get_font(FONT_BOLD, 18), fill=(56, 189, 248))
        draw.text((280, by + 5), b_title, font=get_font(FONT_BOLD, 20), fill=(255, 255, 255))
        draw.text((280, by + 32), b_desc, font=get_font(FONT_REGULAR, 18), fill=(203, 213, 225))
        by += 72
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(20, 35, 50))
    draw.text((120, 735), "CONVERSION IMPACT: +84% higher video completion rate over unscripted UGC.", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    draw_button(draw, 80, 820, 920, 100, "DOWNLOAD THE UGC CREATOR BRIEF TEMPLATE  ➤", get_font(FONT_BOLD, 26), (56, 189, 248), (15, 25, 35), radius=20)
    draw.text((370, 945), "Scripting Protocol by Tipu Sultan", font=get_font(FONT_REGULAR, 20), fill=(186, 230, 253))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-45.jpg"), quality=95)
    print("Created Angle #45")

# -------------------------------------------------------------
# Card 46: High-AOV Offer Bundling & Cart Optimization
# -------------------------------------------------------------
def make_card_46():
    img = Image.new("RGB", (1080, 1080), color=(25, 20, 10))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(35, 28, 15), outline=(245, 158, 11), width=3)
    
    draw_pill(draw, 80, 80, "AVERAGE ORDER VALUE (AOV) MULTIPLIER", get_font(FONT_BOLD, 20), (245, 158, 11), (25, 20, 10))
    draw.text((80, 150), "HOW WE INCREASED STORE AOV BY 64%", font=get_font(FONT_BOLD, 42), fill=(255, 255, 255))
    draw.text((80, 215), "Scaling profitability doesn't always require cheaper clicks. It requires bigger carts.", font=get_font(FONT_REGULAR, 24), fill=(253, 230, 138))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(25, 20, 10), outline=(51, 65, 85), width=2)
    
    tiers = [
        ("TIER 1: SINGLE UNIT", "$45.00", "Base price, high ad CAC, marginal profit.", (148, 163, 184)),
        ("TIER 2: BUNDLE OF 2 (SAVE 20%)", "$72.00", "Customer perceived value increases, CAC stays same.", (245, 158, 11)),
        ("TIER 3: FAMILY 3-PACK + FREE GIFT", "$99.00", "Highest conversion rate on mobile. $54 net profit per sale.", (52, 211, 153))
    ]
    ty = 310
    for name, pr, note, col in tiers:
        draw.rounded_rectangle([110, ty, 970, ty + 105], radius=16, fill=(40, 32, 18), outline=col, width=2)
        draw.text((140, ty + 18), name, font=get_font(FONT_BOLD, 18), fill=(148, 163, 184))
        draw.text((140, ty + 45), pr, font=get_font(FONT_BOLD, 36), fill=col)
        draw.text((540, ty + 40), note, font=get_font(FONT_REGULAR, 22), fill=(254, 243, 199))
        ty += 120
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(40, 32, 18))
    draw.text((120, 735), "STORE IMPACT: Lifted blended ROAS from 2.1x to 4.8x simply by re-bundling.", font=get_font(FONT_BOLD, 22), fill=(245, 158, 11))
    
    draw_button(draw, 80, 820, 920, 100, "REQUEST OFFER & BUNDLE ARCHITECTURE  ➤", get_font(FONT_BOLD, 28), (245, 158, 11), (25, 20, 10), radius=20)
    draw.text((370, 945), "Offer Engineering by Tipu Sultan", font=get_font(FONT_REGULAR, 20), fill=(253, 230, 138))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-46.jpg"), quality=95)
    print("Created Angle #46")

# -------------------------------------------------------------
# Card 47: Google Search Impression Share Domination
# -------------------------------------------------------------
def make_card_47():
    img = Image.new("RGB", (1080, 1080), color=(10, 20, 35))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(15, 30, 50), outline=(66, 133, 244), width=3)
    
    draw_pill(draw, 80, 80, "GOOGLE SEARCH ARBITRAGE", get_font(FONT_BOLD, 20), (66, 133, 244), (255, 255, 255))
    draw.text((80, 150), "OWNING 85%+ TOP-OF-PAGE IMPRESSIONS", font=get_font(FONT_BOLD, 42), fill=(255, 255, 255))
    draw.text((80, 215), "How aggressive negative keyword pruning saved $3,200/mo in junk search clicks.", font=get_font(FONT_REGULAR, 24), fill=(191, 219, 254))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(10, 20, 35), outline=(51, 65, 85), width=2)
    
    stats = [
        ("SEARCH IMPRESSION SHARE (ABSOLUTE TOP)", "86.4%", "Dominating competitors on high-intent buyer searches.", (66, 133, 244)),
        ("NEGATIVE KEYWORD SHIELD", "1,420+ TERMS", "Blocked low-intent free seekers and competitor employee searches.", (239, 68, 68)),
        ("EXACT MATCH QUALITY SCORE", "9 / 10", "Lowered CPC by -34% due to high ad relevance and landing page speed.", (52, 211, 153))
    ]
    sy = 310
    for s_title, s_val, s_sub, col in stats:
        draw.rounded_rectangle([110, sy, 970, sy + 105], radius=16, fill=(20, 40, 65), outline=col, width=2)
        draw.text((140, sy + 18), s_title, font=get_font(FONT_BOLD, 18), fill=(148, 163, 184))
        draw.text((140, sy + 45), s_val, font=get_font(FONT_BOLD, 36), fill=col)
        draw.text((540, sy + 40), s_sub, font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
        sy += 120
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(20, 40, 65))
    draw.text((120, 735), "CLIENT OUTCOME: Steady 5.2x Search ROAS with predictable pipeline flow.", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    draw_button(draw, 80, 820, 920, 100, "REQUEST GOOGLE ADS KEYWORD AUDIT  ➤", get_font(FONT_BOLD, 28), (66, 133, 244), (255, 255, 255), radius=20)
    draw.text((370, 945), "Google Ads Architecture by Tipu Sultan", font=get_font(FONT_REGULAR, 20), fill=(191, 219, 254))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-47.jpg"), quality=95)
    print("Created Angle #47")

# -------------------------------------------------------------
# Card 48: The Growth Architect Manifesto & Scaling Guarantee
# -------------------------------------------------------------
def make_card_48():
    img = Image.new("RGB", (1080, 1080), color=(5, 10, 20))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(10, 20, 35), outline=(16, 185, 129), width=3)
    
    draw_pill(draw, 80, 80, "THE GROWTH ARCHITECT MANIFESTO", get_font(FONT_BOLD, 20), (16, 185, 129), (255, 255, 255))
    draw.text((80, 150), "NO VANITY METRICS. ONLY BANKABLE PROFIT.", font=get_font(FONT_BOLD, 42), fill=(255, 255, 255))
    draw.text((80, 215), "Performance marketing built on engineering principles, data integrity, and empirical proof.", font=get_font(FONT_REGULAR, 24), fill=(148, 163, 184))
    
    draw.rounded_rectangle([80, 275, 1000, 680], radius=24, fill=(5, 10, 20), outline=(51, 65, 85), width=2)
    
    pillars = [
        ("01", "CAPI SERVER-SIDE MATCH INTEGRITY", "Guaranteed 9.0+ EMQ so ad networks receive pristine signal data."),
        ("02", "SCIENTIFIC 3:2:2 CREATIVE VELOCITY", "Consistent modular testing that eliminates ad fatigue before it starts."),
        ("03", "PREDICTIVE ADVANTAGE+ & SMART BIDDING", "Algorithmically optimized auction bidding tied directly to client profit margin."),
        ("04", "100% EMPIRICAL TRANSPARENCY", "Live dashboards, cohort LTV retention tracking, and verified bank receipts.")
    ]
    py = 295
    for num, title, desc in pillars:
        draw.text((110, py + 10), num, font=get_font(FONT_BOLD, 36), fill=(52, 211, 153))
        draw.text((180, py + 10), title, font=get_font(FONT_BOLD, 22), fill=(255, 255, 255))
        draw.text((180, py + 42), desc, font=get_font(FONT_REGULAR, 18), fill=(203, 213, 225))
        py += 92
        
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(15, 23, 42))
    draw.text((120, 735), "DIRECT ARCHITECT ACCESS: Chat 1-on-1 with Tipu Sultan (WhatsApp: +966 56 648 2865)", font=get_font(FONT_BOLD, 22), fill=(245, 158, 11))
    
    draw_button(draw, 80, 820, 920, 100, "REQUEST YOUR 10-MINUTE ACCOUNT TEARDOWN  ➤", get_font(FONT_BOLD, 28), (16, 185, 129), (255, 255, 255), radius=20)
    draw.text((370, 945), "Tipu Sultan | AI-Driven & Data-Driven Growth Architect", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-48.jpg"), quality=95)
    print("Created Angle #48")

if __name__ == "__main__":
    make_card_37()
    make_card_38()
    make_card_39()
    make_card_40()
    make_card_41()
    make_card_42()
    make_card_43()
    make_card_44()
    make_card_45()
    make_card_46()
    make_card_47()
    make_card_48()
    print("All 12 additional intellectual ad creative cards created successfully!")
