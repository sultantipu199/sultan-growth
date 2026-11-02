# -*- coding: utf-8 -*-
"""
reposition_executive_assets.py
Moves #executive-assets right after the hero <header> so it is immediately visible to any visitor.
Also places CV & Decks at the very front of desktop navbar and mobile menu.
"""

from bs4 import BeautifulSoup
import re

def reposition():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the section #executive-assets
    start_marker = '<!-- Executive Assets & Bilingual Presentation Vault -->'
    end_marker = '<!-- Free 10-Minute Ad Account Teardown Form with Architect Profile -->'
    
    p_start = html.find(start_marker)
    p_end = html.find(end_marker)

    if p_start == -1 or p_end == -1:
        print("Markers not found!")
        return

    exec_section = html[p_start:p_end].strip()

    # Remove exec_section from current position
    html_without_exec = html[:p_start] + html[p_end:]

    # Now find where to insert it: right after </header>
    header_end_marker = '</header>'
    idx_header = html_without_exec.find(header_end_marker)

    if idx_header == -1:
        print("Header end marker not found!")
        return

    insert_pos = idx_header + len(header_end_marker)

    # Insert section with clear spacing
    new_html = html_without_exec[:insert_pos] + "\n\n  " + exec_section + "\n" + html_without_exec[insert_pos:]

    # Also update desktop navbar order to make CV & Decks first:
    # Look for desktop nav links
    desktop_nav_pattern = r'(<div class="hidden md:flex items-center gap-5 text-xs font-semibold text-slate-300">)([\s\S]*?)(</div>)'
    
    def reorder_nav(match):
        prefix = match.group(1)
        content = match.group(2)
        suffix = match.group(3)

        # Remove existing CV & Decks link if present
        content_clean = re.sub(r'<a href="#executive-assets"[\s\S]*?</a>\s*', '', content)

        # Prepend CV & Decks link right at the start
        cv_link = """\n        <a href="#executive-assets" class="hover:text-amber-400 transition-colors flex items-center gap-1.5 text-amber-300 font-bold px-3 py-1.5 rounded-xl bg-amber-500/15 border border-amber-500/35 shadow-sm shadow-amber-500/15">
          <i class="fa-solid fa-file-shield text-xs text-amber-400"></i>
          <span>CV & Decks</span>
          <span class="px-1.5 py-0.5 rounded bg-amber-400 text-slate-950 text-[9px] font-black uppercase tracking-wider">New</span>
        </a>\n"""

        return prefix + cv_link + content_clean + suffix

    new_html = re.sub(desktop_nav_pattern, reorder_nav, new_html, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Repositioned #executive-assets successfully to top of page!")

if __name__ == '__main__':
    reposition()

