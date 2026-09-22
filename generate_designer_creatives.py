"""
generate_designer_creatives.py
Generates 10 authentic, human-graphic-designer-style performance marketing ad creatives
for Tipu Sultan's Growth Architecture portfolio.
Crafted to look like professional Canva/Photoshop/Figma deliverables.
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

def draw_stars(draw, x, y, size=24, count=5, color=(251, 191, 36)):
    """Draws 5 star shapes"""
    for i in range(count):
        sx = x + i * (size + 8)
        # Approximate star with polygon
        pts = [
            (sx + size*0.5, y),
            (sx + size*0.62, y + size*0.38),
            (sx + size, y + size*0.38),
            (sx + size*0.7, y + size*0.62),
            (sx + size*0.82, y + size),
            (sx + size*0.5, y + size*0.76),
            (sx + size*0.18, y + size),
            (sx + size*0.3, y + size*0.62),
            (sx, y + size*0.38),
            (sx + size*0.38, y + size*0.38),
        ]
        draw.polygon(pts, fill=color)

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
# Card 27: High-Converting DTC Flash Sale Ad (Canva Style)
# -------------------------------------------------------------
def make_card_27():
    img = Image.new("RGB", (1080, 1080), color=(15, 23, 42)) # Deep navy
    draw = ImageDraw.Draw(img)
    
    # Outer frame
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(24, 33, 56), outline=(51, 65, 85), width=3)
    
    # Header Banner Pill
    draw_pill(draw, 80, 80, "⚡ LIMITED TIME OFFER • 48 HOURS ONLY", get_font(FONT_BOLD, 22), (239, 68, 68), (255, 255, 255), px=24, py=10)
    
    # Main Headline
    f_head = get_font(FONT_BOLD, 54)
    draw.text((80, 160), "ULTRA-SLIM SMART CHARGER", font=f_head, fill=(255, 255, 255))
    
    f_sub = get_font(FONT_REGULAR, 26)
    draw.text((80, 230), "Engineered for 3x faster Qi charging. No tangled cords.", font=f_sub, fill=(148, 163, 184))
    
    # Product Feature Box
    draw.rounded_rectangle([80, 290, 1000, 670], radius=24, fill=(15, 23, 42), outline=(71, 85, 105), width=2)
    
    # Visual center graphic / product badge
    draw.rounded_rectangle([120, 330, 480, 630], radius=20, fill=(30, 41, 59), outline=(99, 102, 241), width=2)
    draw_pill(draw, 140, 350, "FLAGSHIP EDITION", get_font(FONT_BOLD, 18), (99, 102, 241), (255, 255, 255), px=14, py=6)
    draw.text((150, 430), "15W MAG-TURBO", font=get_font(FONT_BOLD, 36), fill=(255, 255, 255))
    draw.text((150, 480), "Aerospace Aluminum Alloy", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    draw.text((150, 520), "Smart Thermal Safety Guard", font=get_font(FONT_REGULAR, 20), fill=(52, 211, 153))
    
    # Right column: Price & bullets
    draw.text((520, 330), "SPECIAL BUNDLE PRICE", font=get_font(FONT_BOLD, 20), fill=(245, 158, 11))
    draw.text((520, 370), "$39.99", font=get_font(FONT_BOLD, 68), fill=(255, 255, 255))
    draw.text((760, 400), "REG. $79.99", font=get_font(FONT_BOLD, 24), fill=(100, 116, 139))
    draw.line([760, 415, 910, 415], fill=(239, 68, 68), width=3) # Strikethrough
    draw_pill(draw, 520, 460, "SAVE 50% TODAY", get_font(FONT_BOLD, 20), (16, 185, 129), (255, 255, 255), px=18, py=8)
    
    bullets = [
        "✓ 100% Wireless Fast Magnetic Lock",
        "✓ Universally Compatible (iOS & Android)",
        "✓ 30-Day Risk-Free Money Back Guarantee",
        "✓ Free Worldwide Express Shipping"
    ]
    by = 520
    for b in bullets:
        draw.text((520, by), b, font=get_font(FONT_BOLD, 20), fill=(226, 232, 240))
        by += 32
        
    # Social Proof Rating Bar
    draw.rounded_rectangle([80, 690, 1000, 780], radius=20, fill=(30, 41, 59))
    draw_stars(draw, 110, 722, size=24, count=5)
    draw.text((270, 720), "4.9/5 RATING", font=get_font(FONT_BOLD, 24), fill=(255, 255, 255))
    draw.text((450, 722), "|  Over 14,200+ Verified Customer Orders", font=get_font(FONT_REGULAR, 22), fill=(148, 163, 184))
    
    # Big CTA Button
    draw_button(draw, 80, 810, 920, 100, "CLAIM 50% DISCOUNT & ORDER NOW  ➤", get_font(FONT_BOLD, 30), (16, 185, 129), (255, 255, 255), radius=20)
    
    # Bottom Subtext
    draw.text((360, 930), "🔒 256-Bit SSL Encrypted Checkout  •  Fast Dispatch", font=get_font(FONT_REGULAR, 18), fill=(100, 116, 139))
    draw.text((390, 970), "Campaign Deliverable: Project Facebook A to Z", font=get_font(FONT_BOLD, 16), fill=(71, 85, 105))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-27.jpg"), quality=95)
    print("Created Angle #27")

# -------------------------------------------------------------
# Card 28: Meta Advantage+ / 3:2:2 Dynamic Hook Angle
# -------------------------------------------------------------
def make_card_28():
    img = Image.new("RGB", (1080, 1080), color=(10, 15, 30))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(15, 23, 42), outline=(59, 130, 246), width=3)
    
    draw_pill(draw, 80, 80, "META ADVANTAGE+ SHOPPING (ASC) BLUEPRINT", get_font(FONT_BOLD, 20), (59, 130, 246), (255, 255, 255))
    
    draw.text((80, 150), "STOP TARGETING THE WRONG AUDIENCES.", font=get_font(FONT_BOLD, 46), fill=(255, 255, 255))
    draw.text((80, 215), "How AI Dynamic Creative Testing (3:2:2) delivers 4.6x Peak ROAS", font=get_font(FONT_REGULAR, 26), fill=(148, 163, 184))
    
    # Side-by-side comparison
    # Left: Old Way
    draw.rounded_rectangle([80, 280, 520, 730], radius=20, fill=(30, 41, 59), outline=(239, 68, 68), width=2)
    draw_pill(draw, 105, 305, "❌ THE OLD WAY (LOSING CASH)", get_font(FONT_BOLD, 18), (69, 10, 10), (248, 113, 113))
    old_points = [
        "• Manual interest stacking",
        "• Single ad exhaustion in 5 days",
        "• High CPMs ($45+)",
        "• 1.2x - 1.6x stagnant ROAS",
        "• Blind budget allocation"
    ]
    oy = 370
    for p in old_points:
        draw.text((110, oy), p, font=get_font(FONT_REGULAR, 22), fill=(203, 213, 225))
        oy += 45
    draw.text((110, 640), "AVERAGE LOSS: -$1,400/wk", font=get_font(FONT_BOLD, 22), fill=(239, 68, 68))
    
    # Right: 3:2:2 AI Way
    draw.rounded_rectangle([560, 280, 1000, 730], radius=20, fill=(17, 34, 46), outline=(16, 185, 129), width=2)
    draw_pill(draw, 585, 305, "✅ TIPU'S 3:2:2 AI SANDBOX", get_font(FONT_BOLD, 18), (6, 78, 59), (52, 211, 153))
    new_points = [
        "• 3 Thumb-Stopping Hooks",
        "• 2 Visual Context Angles",
        "• 2 Psychology-Driven CTAs",
        "• CAPI Event Match 9.4/10",
        "• Auto-scaling winning combos"
    ]
    ny = 370
    for p in new_points:
        draw.text((590, ny), p, font=get_font(FONT_BOLD, 22), fill=(241, 245, 249))
        ny += 45
    draw.text((590, 640), "PROVEN ROAS: 4.6X TO 6.4X", font=get_font(FONT_BOLD, 22), fill=(52, 211, 153))
    
    # Big Results Ribbon
    draw.rounded_rectangle([80, 760, 1000, 850], radius=18, fill=(30, 41, 59))
    draw.text((110, 785), "CLIENT RESULT:", font=get_font(FONT_BOLD, 24), fill=(245, 158, 11))
    draw.text((310, 785), "$187,000+ Spend Scaled at 4.1x Blended Average", font=get_font(FONT_BOLD, 24), fill=(255, 255, 255))
    
    # CTA
    draw_button(draw, 80, 880, 920, 95, "VIEW CASE STUDY & CAMPAIGN BREAKDOWN  ➤", get_font(FONT_BOLD, 28), (59, 130, 246), (255, 255, 255), radius=20)
    
    draw.text((370, 995), "Growth Marketing Architecture by Tipu Sultan", font=get_font(FONT_BOLD, 18), fill=(100, 116, 139))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-28.jpg"), quality=95)
    print("Created Angle #28")

# -------------------------------------------------------------
# Card 29: B2B SaaS / High-Ticket Lead Gen Architecture
# -------------------------------------------------------------
def make_card_29():
    img = Image.new("RGB", (1080, 1080), color=(11, 19, 43))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(20, 32, 60), outline=(0, 245, 212), width=3)
    
    draw_pill(draw, 80, 80, "HIGH-TICKET B2B ACQUISITION", get_font(FONT_BOLD, 20), (0, 180, 216), (255, 255, 255))
    
    draw.text((80, 150), "HOW WE BOOK 50+ QUALIFIED DEMOS", font=get_font(FONT_BOLD, 46), fill=(255, 255, 255))
    draw.text((80, 210), "EVERY MONTH FOR B2B & ENTERPRISE FOUNDERS", font=get_font(FONT_BOLD, 36), fill=(0, 245, 212))
    
    # 3 Framework Steps
    steps = [
        ("01", "INTENT DATA SCRAPING", "Target in-market accounts actively researching your software niche."),
        ("02", "PAID SOCIAL COLD HOOKS", "Deliver targeted pain-point ads on LinkedIn and Meta with direct ROI hooks."),
        ("03", "FRICTIONLESS DEMO FUNNEL", "Self-qualifying intake form that routes booked calls straight to CRM.")
    ]
    sy = 290
    for num, title, desc in steps:
        draw.rounded_rectangle([80, sy, 1000, sy + 130], radius=18, fill=(11, 19, 43), outline=(51, 65, 85), width=2)
        draw.text((110, sy + 25), num, font=get_font(FONT_BOLD, 52), fill=(0, 245, 212))
        draw.text((210, sy + 30), title, font=get_font(FONT_BOLD, 24), fill=(255, 255, 255))
        draw.text((210, sy + 68), desc, font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
        sy += 150
        
    # Metric Callout Row
    draw.rounded_rectangle([80, 760, 1000, 860], radius=18, fill=(15, 23, 42))
    draw.text((120, 785), "AVERAGE COST PER QUALIFIED DEMO:", font=get_font(FONT_BOLD, 20), fill=(148, 163, 184))
    draw.text((120, 815), "$48.20 (DOWN 62%)", font=get_font(FONT_BOLD, 32), fill=(52, 211, 153))
    
    draw.text((620, 785), "SHOW-UP RATE:", font=get_font(FONT_BOLD, 20), fill=(148, 163, 184))
    draw.text((620, 815), "87.4% ON-TIME", font=get_font(FONT_BOLD, 32), fill=(0, 245, 212))
    
    draw_button(draw, 80, 890, 920, 95, "SCHEDULE YOUR B2B GROWTH CALL  ➤", get_font(FONT_BOLD, 28), (0, 245, 212), (11, 19, 43), radius=20)
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-29.jpg"), quality=95)
    print("Created Angle #29")

# -------------------------------------------------------------
# Card 30: Cart Abandonment / Retargeting Hook
# -------------------------------------------------------------
def make_card_30():
    img = Image.new("RGB", (1080, 1080), color=(24, 24, 27))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(39, 39, 42), outline=(245, 158, 11), width=3)
    
    draw_pill(draw, 80, 80, "🛒 DID YOU FORGET SOMETHING?", get_font(FONT_BOLD, 22), (245, 158, 11), (24, 24, 27))
    
    draw.text((80, 155), "YOUR CART IS WAITING FOR YOU.", font=get_font(FONT_BOLD, 50), fill=(255, 255, 255))
    draw.text((80, 220), "We reserved your selected items for the next 24 hours.", font=get_font(FONT_REGULAR, 26), fill=(161, 161, 170))
    
    # Coupon Box
    draw.rounded_rectangle([80, 290, 1000, 540], radius=24, fill=(24, 24, 27), outline=(245, 158, 11), width=2)
    draw.text((120, 330), "EXCLUSIVE RETARGETING VIP PROMO:", font=get_font(FONT_BOLD, 22), fill=(245, 158, 11))
    draw.text((120, 380), "TAKE AN EXTRA 15% OFF", font=get_font(FONT_BOLD, 52), fill=(255, 255, 255))
    
    # Coupon code dashed box
    draw.rounded_rectangle([120, 455, 520, 515], radius=12, fill=(63, 63, 70))
    draw.text((140, 468), "USE PROMO CODE:  SAVE15", font=get_font(FONT_BOLD, 24), fill=(250, 204, 21))
    draw.text((560, 472), "✓ Code Auto-Applies at Checkout", font=get_font(FONT_REGULAR, 20), fill=(52, 211, 153))
    
    # Trust grid
    draw.rounded_rectangle([80, 570, 1000, 770], radius=20, fill=(30, 41, 59))
    perks = [
        "🔒 100% Secure SSL Checkout",
        "⚡ Same-Day Order Fulfillment",
        "📦 Tracked Worldwide Delivery",
        "🔄 30-Day Hassle-Free Returns"
    ]
    py = 605
    for p in perks[:2]:
        draw.text((120, py), p, font=get_font(FONT_BOLD, 24), fill=(255, 255, 255))
        py += 55
    py = 605
    for p in perks[2:]:
        draw.text((560, py), p, font=get_font(FONT_BOLD, 24), fill=(255, 255, 255))
        py += 55
        
    draw_stars(draw, 120, 720, size=24, count=5)
    draw.text((280, 718), "Over 28,000+ Happy Customers & 5-Star Reviews", font=get_font(FONT_BOLD, 20), fill=(245, 158, 11))
    
    draw_button(draw, 80, 810, 920, 100, "COMPLETE MY PURCHASE WITH 15% OFF  ➤", get_font(FONT_BOLD, 30), (245, 158, 11), (24, 24, 27), radius=20)
    
    draw.text((380, 935), "Offer valid while current warehouse inventory lasts.", font=get_font(FONT_REGULAR, 18), fill=(113, 113, 122))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-30.jpg"), quality=95)
    print("Created Angle #30")

# -------------------------------------------------------------
# Card 31: Server-Side CAPI Signal Breakdown Ad
# -------------------------------------------------------------
def make_card_31():
    img = Image.new("RGB", (1080, 1080), color=(5, 15, 25))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(10, 25, 41), outline=(16, 185, 129), width=3)
    
    draw_pill(draw, 80, 80, "SIGNAL RESILIENCE ARCHITECTURE", get_font(FONT_BOLD, 20), (16, 185, 129), (255, 255, 255))
    
    draw.text((80, 150), "WHY YOUR FACEBOOK PIXEL IS FAILING.", font=get_font(FONT_BOLD, 46), fill=(255, 255, 255))
    draw.text((80, 210), "Browser pixels miss up to 35% of purchases due to iOS and AdBlockers.", font=get_font(FONT_REGULAR, 24), fill=(148, 163, 184))
    
    # Metrics Container
    draw.rounded_rectangle([80, 275, 1000, 620], radius=24, fill=(15, 23, 42), outline=(30, 41, 59), width=2)
    
    # Left: EMQ Score
    draw.rounded_rectangle([110, 305, 520, 590], radius=18, fill=(5, 15, 25), outline=(16, 185, 129), width=2)
    draw.text((140, 335), "EVENT MATCH QUALITY", font=get_font(FONT_BOLD, 22), fill=(148, 163, 184))
    draw.text((140, 375), "9.4 / 10", font=get_font(FONT_BOLD, 74), fill=(52, 211, 153))
    draw.text((140, 470), "STATUS: EXCELLENT", font=get_font(FONT_BOLD, 24), fill=(16, 185, 129))
    draw.text((140, 515), "Server-to-Server SHA-256", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    draw.text((140, 545), "Zero Signal Loss Guarantee", font=get_font(FONT_REGULAR, 20), fill=(226, 232, 240))
    
    # Right: The Lift
    draw.rounded_rectangle([560, 305, 970, 590], radius=18, fill=(5, 15, 25), outline=(59, 130, 246), width=2)
    draw.text((590, 335), "MEASURED REVENUE LIFT", font=get_font(FONT_BOLD, 22), fill=(148, 163, 184))
    draw.text((590, 375), "+68.4%", font=get_font(FONT_BOLD, 74), fill=(96, 165, 250))
    draw.text((590, 470), "ATTRIBUTED CONVERSIONS", font=get_font(FONT_BOLD, 24), fill=(59, 130, 246))
    draw.text((590, 515), "Accurate Conversion Value", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    draw.text((590, 545), "Faster Machine Learning Exit", font=get_font(FONT_REGULAR, 20), fill=(226, 232, 240))
    
    # Callout Banner
    draw.rounded_rectangle([80, 650, 1000, 770], radius=20, fill=(30, 41, 59))
    draw.text((120, 675), "THE RESULT FOR YOUR BRAND:", font=get_font(FONT_BOLD, 22), fill=(245, 158, 11))
    draw.text((120, 715), "Lower customer acquisition costs (CAC) & stable, predictable ROAS scaling.", font=get_font(FONT_BOLD, 22), fill=(255, 255, 255))
    
    draw_button(draw, 80, 810, 920, 100, "REQUEST ZERO-COST CAPI AUDIT  ➤", get_font(FONT_BOLD, 30), (16, 185, 129), (255, 255, 255), radius=20)
    
    draw.text((370, 940), "Engineered by Tipu Sultan | Growth Architect", font=get_font(FONT_BOLD, 18), fill=(100, 116, 139))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-31.jpg"), quality=95)
    print("Created Angle #31")

# -------------------------------------------------------------
# Card 32: Social Proof / 5-Star Review Stack
# -------------------------------------------------------------
def make_card_32():
    img = Image.new("RGB", (1080, 1080), color=(17, 24, 39))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(31, 41, 55), outline=(245, 158, 11), width=3)
    
    draw_pill(draw, 80, 80, "★ ★ ★ ★ ★ OVER 15,000+ HAPPY FOUNDERS", get_font(FONT_BOLD, 20), (245, 158, 11), (17, 24, 39))
    
    draw.text((80, 150), "DON'T JUST TAKE OUR WORD FOR IT.", font=get_font(FONT_BOLD, 48), fill=(255, 255, 255))
    draw.text((80, 215), "Real founder reviews from brands scaled with our Growth Architecture.", font=get_font(FONT_REGULAR, 24), fill=(156, 163, 175))
    
    # Review Card 1
    draw.rounded_rectangle([80, 275, 1000, 460], radius=20, fill=(17, 24, 39), outline=(55, 65, 81), width=2)
    draw_stars(draw, 110, 300, size=20, count=5)
    draw.text((250, 298), "VERIFIED STORE OWNER", font=get_font(FONT_BOLD, 18), fill=(52, 211, 153))
    draw.text((110, 340), "\"We went from struggling at 1.4x ROAS to consistently hitting 4.6x within", font=get_font(FONT_REGULAR, 24), fill=(243, 244, 246))
    draw.text((110, 375), "our first 30 days. Tipu's creative testing methodology is world class.\"", font=get_font(FONT_REGULAR, 24), fill=(243, 244, 246))
    draw.text((110, 415), "— Marcus Vance, Founder of Apex Performance Apparel", font=get_font(FONT_BOLD, 18), fill=(156, 163, 175))
    
    # Review Card 2
    draw.rounded_rectangle([80, 485, 1000, 670], radius=20, fill=(17, 24, 39), outline=(55, 65, 81), width=2)
    draw_stars(draw, 110, 510, size=20, count=5)
    draw.text((250, 508), "VERIFIED E-COMMERCE BRAND", font=get_font(FONT_BOLD, 18), fill=(52, 211, 153))
    draw.text((110, 550), "\"The CAPI server tracking setup alone recovered $34,000 in untracked", font=get_font(FONT_REGULAR, 24), fill=(243, 244, 246))
    draw.text((110, 585), "revenue. Best investment our marketing team has made this year.\"", font=get_font(FONT_REGULAR, 24), fill=(243, 244, 246))
    draw.text((110, 625), "— Elena Rostova, VP of Growth at Lumina Home", font=get_font(FONT_BOLD, 18), fill=(156, 163, 175))
    
    # Proof Bar
    draw.rounded_rectangle([80, 700, 1000, 780], radius=18, fill=(55, 65, 81))
    draw.text((120, 725), "AVERAGE CLIENT LIFT:", font=get_font(FONT_BOLD, 22), fill=(245, 158, 11))
    draw.text((380, 725), "+240% NET REVENUE IN 90 DAYS", font=get_font(FONT_BOLD, 24), fill=(255, 255, 255))
    
    draw_button(draw, 80, 810, 920, 100, "START SCALING YOUR BRAND TODAY  ➤", get_font(FONT_BOLD, 30), (245, 158, 11), (17, 24, 39), radius=20)
    
    draw.text((370, 940), "Direct WhatsApp Consultation: +966 56 648 2865", font=get_font(FONT_BOLD, 18), fill=(156, 163, 175))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-32.jpg"), quality=95)
    print("Created Angle #32")

# -------------------------------------------------------------
# Card 33: Google Search / Performance Max High-Intent Ad
# -------------------------------------------------------------
def make_card_33():
    img = Image.new("RGB", (1080, 1080), color=(255, 255, 255)) # Clean white Google style
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(248, 250, 252), outline=(226, 232, 240), width=3)
    
    # Google Brand Bar
    draw.text((80, 80), "Google", font=get_font(FONT_BOLD, 42), fill=(66, 133, 244))
    draw_pill(draw, 240, 85, "PERFORMANCE MAX CAMPAIGN MOCKUP", get_font(FONT_BOLD, 16), (224, 231, 255), (67, 56, 202))
    
    # Ad Container
    draw.rounded_rectangle([80, 160, 1000, 520], radius=20, fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    
    # Sponsored tag
    draw.text((110, 190), "Sponsored", font=get_font(FONT_BOLD, 18), fill=(31, 41, 55))
    draw.text((220, 190), "•  https://yourstore.com/growth-suite", font=get_font(FONT_REGULAR, 18), fill=(75, 85, 99))
    
    # Headline
    draw.text((110, 230), "Scale Your Brand With AI Bidding | Top Rated Agency 2026", font=get_font(FONT_BOLD, 32), fill=(26, 115, 232))
    
    # Description
    draw.text((110, 290), "Eliminate wasted budget with smart bidding architectures. Maximize net margin,", font=get_font(FONT_REGULAR, 22), fill=(75, 85, 99))
    draw.text((110, 325), "scale bottom-funnel conversions, and get full ROAS transparency.", font=get_font(FONT_REGULAR, 22), fill=(75, 85, 99))
    
    # Sitelinks Grid
    sitelinks = [
        ("Proven Case Studies", "See 4.6x - 6.4x verified client lifts"),
        ("10-Min Free Ad Teardown", "Pinpoint where budget is leaking"),
        ("Google Smart Bidding Setup", "Scale tCPA & tROAS targets"),
        ("Direct WhatsApp Audit", "Chat directly with Tipu Sultan")
    ]
    sx = 110
    sy = 390
    for title, desc in sitelinks[:2]:
        draw.text((sx, sy), title, font=get_font(FONT_BOLD, 20), fill=(26, 115, 232))
        draw.text((sx, sy + 25), desc, font=get_font(FONT_REGULAR, 16), fill=(107, 114, 128))
        sx += 440
        
    sx = 110
    sy = 450
    for title, desc in sitelinks[2:]:
        draw.text((sx, sy), title, font=get_font(FONT_BOLD, 20), fill=(26, 115, 232))
        draw.text((sx, sy + 25), desc, font=get_font(FONT_REGULAR, 16), fill=(107, 114, 128))
        sx += 440

    # Lower Stats Banner
    draw.rounded_rectangle([80, 560, 1000, 770], radius=20, fill=(15, 23, 42))
    draw.text((120, 595), "GOOGLE ADS PERFORMANCE METRICS:", font=get_font(FONT_BOLD, 20), fill=(245, 158, 11))
    draw.text((120, 635), "AVERAGE CONVERSION RATE:  6.82%", font=get_font(FONT_BOLD, 30), fill=(52, 211, 153))
    draw.text((120, 680), "COST PER CONVERSION:  -$18.40 VS INDUSTRY BENCHMARK", font=get_font(FONT_BOLD, 22), fill=(255, 255, 255))
    draw.text((120, 715), "SEARCH IMPRESSION SHARE:  84.6% TOP OF PAGE", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    
    draw_button(draw, 80, 810, 920, 100, "REQUEST GOOGLE ADS PERFORMANCE PLAN  ➤", get_font(FONT_BOLD, 28), (26, 115, 232), (255, 255, 255), radius=20)
    
    draw.text((380, 940), "Google Certified Performance Partner Architecture", font=get_font(FONT_BOLD, 18), fill=(107, 114, 128))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-33.jpg"), quality=95)
    print("Created Angle #33")

# -------------------------------------------------------------
# Card 34: Scarcity & Countdown High-Velocity Hook
# -------------------------------------------------------------
def make_card_34():
    img = Image.new("RGB", (1080, 1080), color=(0, 0, 0)) # High contrast black
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(15, 15, 15), outline=(250, 204, 21), width=4)
    
    draw_pill(draw, 80, 80, "⚡ FLASH CLEARANCE • FINAL 100 UNITS", get_font(FONT_BOLD, 22), (239, 68, 68), (255, 255, 255))
    
    draw.text((80, 160), "BUY 1 GET 1 FREE.", font=get_font(FONT_BLACK, 84), fill=(250, 204, 21))
    draw.text((80, 260), "OUR BIGGEST ANNUAL EVENT ENDS TONIGHT.", font=get_font(FONT_BOLD, 36), fill=(255, 255, 255))
    
    # Countdown Clock Boxes
    draw.rounded_rectangle([80, 340, 1000, 520], radius=24, fill=(24, 24, 27), outline=(63, 63, 70), width=2)
    
    times = [("03", "HOURS"), ("42", "MINUTES"), ("18", "SECONDS")]
    tx = 150
    for val, lbl in times:
        draw.rounded_rectangle([tx, 370, tx + 200, 480], radius=16, fill=(39, 39, 42))
        draw.text((tx + 45, 380), val, font=get_font(FONT_BLACK, 64), fill=(255, 255, 255))
        draw.text((tx + 55, 450), lbl, font=get_font(FONT_BOLD, 18), fill=(250, 204, 21))
        tx += 270
        
    # Urgency Meter
    draw.rounded_rectangle([80, 560, 1000, 740], radius=20, fill=(24, 24, 27))
    draw.text((120, 590), "CURRENT WAREHOUSE ALLOCATION:", font=get_font(FONT_BOLD, 22), fill=(161, 161, 170))
    # Progress Bar
    draw.rounded_rectangle([120, 630, 960, 660], radius=15, fill=(63, 63, 70))
    draw.rounded_rectangle([120, 630, 840, 660], radius=15, fill=(239, 68, 68)) # 88% claimed
    draw.text((120, 680), "🔥 88% OF BATCH CLAIMED • ONLY 12 UNITS LEFT AT THIS PRICE", font=get_font(FONT_BOLD, 22), fill=(239, 68, 68))
    
    draw_button(draw, 80, 790, 920, 110, "LOCK IN BOGO OFFER BEFORE MIDNIGHT  ➤", get_font(FONT_BOLD, 30), (250, 204, 21), (0, 0, 0), radius=22)
    
    draw.text((370, 930), "Free Express Shipping  •  30-Day Money Back Guarantee", font=get_font(FONT_REGULAR, 20), fill=(161, 161, 170))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-34.jpg"), quality=95)
    print("Created Angle #34")

# -------------------------------------------------------------
# Card 35: High-Ticket Case Study Teardown Slide
# -------------------------------------------------------------
def make_card_35():
    img = Image.new("RGB", (1080, 1080), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(30, 41, 59), outline=(139, 92, 246), width=3)
    
    draw_pill(draw, 80, 80, "AUDITED CASE STUDY #104", get_font(FONT_BOLD, 20), (139, 92, 246), (255, 255, 255))
    
    draw.text((80, 150), "FROM $20K/MO TO $140K/MO IN 90 DAYS", font=get_font(FONT_BOLD, 46), fill=(255, 255, 255))
    draw.text((80, 215), "Performance Architecture for DTC Fitness & Athleisure Brand", font=get_font(FONT_REGULAR, 26), fill=(148, 163, 184))
    
    # 4 Metric Cards Grid
    metrics = [
        ("TOTAL AD SPEND", "$32,450", (148, 163, 184)),
        ("GROSS REVENUE", "$148,900", (52, 211, 153)),
        ("BLENDED ROAS", "4.59x", (139, 92, 246)),
        ("NET PROFIT LIFT", "+$68,200", (52, 211, 153))
    ]
    
    gx = 80
    gy = 280
    for idx, (lbl, val, col) in enumerate(metrics):
        draw.rounded_rectangle([gx, gy, gx + 430, gy + 130], radius=18, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
        draw.text((gx + 25, gy + 20), lbl, font=get_font(FONT_BOLD, 18), fill=(148, 163, 184))
        draw.text((gx + 25, gy + 55), val, font=get_font(FONT_BOLD, 46), fill=col)
        if idx % 2 == 0:
            gx += 470
        else:
            gx = 80
            gy += 150
            
    # Architecture Summary Box
    draw.rounded_rectangle([80, 600, 1000, 770], radius=20, fill=(15, 23, 42))
    draw.text((110, 625), "3 CORE GROWTH LEVERS APPLIED:", font=get_font(FONT_BOLD, 22), fill=(245, 158, 11))
    draw.text((110, 665), "1. 3:2:2 Dynamic Hook Testing — eliminated ad fatigue in 14 days", font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
    draw.text((110, 700), "2. Server-Side CAPI Gateway — recovered 38% under-reported iOS sales", font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
    draw.text((110, 735), "3. Bundle AOV Optimization — boosted cart value from $42 to $78", font=get_font(FONT_REGULAR, 22), fill=(226, 232, 240))
    
    draw_button(draw, 80, 810, 920, 100, "REQUEST YOUR BRAND'S GROWTH PLAN  ➤", get_font(FONT_BOLD, 30), (139, 92, 246), (255, 255, 255), radius=20)
    
    draw.text((370, 940), "Audited & Verified by Tipu Sultan Growth Lab", font=get_font(FONT_BOLD, 18), fill=(148, 163, 184))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-35.jpg"), quality=95)
    print("Created Angle #35")

# -------------------------------------------------------------
# Card 36: Free 10-Minute Ad Account Teardown Callout
# -------------------------------------------------------------
def make_card_36():
    img = Image.new("RGB", (1080, 1080), color=(10, 20, 30))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([40, 40, 1040, 1040], radius=32, fill=(15, 30, 45), outline=(16, 185, 129), width=3)
    
    draw_pill(draw, 80, 80, "🎯 1-ON-1 ON-CAMERA AUDIT WITH TIPU SULTAN", get_font(FONT_BOLD, 20), (16, 185, 129), (255, 255, 255))
    
    draw.text((80, 150), "IS YOUR AD SPEND SECRETLY LEAKING?", font=get_font(FONT_BOLD, 46), fill=(255, 255, 255))
    draw.text((80, 215), "Get a private, zero-cost 10-minute video audit of your ad account.", font=get_font(FONT_REGULAR, 26), fill=(148, 163, 184))
    
    # 3 Things We Check Box
    draw.rounded_rectangle([80, 280, 1000, 680], radius=24, fill=(10, 20, 30), outline=(51, 65, 85), width=2)
    
    draw.text((120, 315), "WHAT WE UNCOVER IN 10 MINUTES:", font=get_font(FONT_BOLD, 22), fill=(245, 158, 11))
    
    checks = [
        ("01", "Signal Health Check", "Detect CAPI match quality drops, pixel duplicate events & iOS loss."),
        ("02", "Creative Hook Fatigue", "Pinpoint exact ad creatives draining budget without driving purchase volume."),
        ("03", "Unit Economics & CAC Waste", "Calculate true blended ROAS and identify 2-3 instant quick-win scaling angles.")
    ]
    cy = 370
    for num, title, desc in checks:
        draw.text((120, cy), num, font=get_font(FONT_BOLD, 36), fill=(52, 211, 153))
        draw.text((190, cy + 5), title, font=get_font(FONT_BOLD, 24), fill=(255, 255, 255))
        draw.text((190, cy + 40), desc, font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
        cy += 95
        
    # Trust Bar
    draw.rounded_rectangle([80, 710, 1000, 790], radius=18, fill=(30, 41, 59))
    draw.text((120, 735), "✓ 100% Free & Confidential  •  Direct WhatsApp Delivery  •  Zero Hard Selling", font=get_font(FONT_BOLD, 22), fill=(255, 255, 255))
    
    draw_button(draw, 80, 820, 920, 100, "REQUEST YOUR FREE 10-MIN TEARDOWN  ➤", get_font(FONT_BOLD, 30), (16, 185, 129), (255, 255, 255), radius=20)
    
    draw.text((350, 950), "WhatsApp: +966 56 648 2865  •  tipusultan.growth@gmail.com", font=get_font(FONT_REGULAR, 20), fill=(148, 163, 184))
    
    img.save(os.path.join(OUTPUT_DIR, "meta-creative-hook-angle-36.jpg"), quality=95)
    print("Created Angle #36")

if __name__ == "__main__":
    make_card_27()
    make_card_28()
    make_card_29()
    make_card_30()
    make_card_31()
    make_card_32()
    make_card_33()
    make_card_34()
    make_card_35()
    make_card_36()
    print("All 10 authentic graphic designer ad creative cards rendered successfully!")
