import sys, pymupdf, json, re
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'D:\tj\822\数一\老姚\老姚高数.pdf'
doc = pymupdf.open(pdf_path)

# Let's inspect page ranges for the 7 sections in Chapter 3
# Section 3.1: P41 - P44 (27 problems)
# Section 3.2: P45 - P47 (32 problems)
# Section 3.3: P48 - P48 (8 problems)
# Section 3.4: P49 - P54 (22 problems)
# Section 3.5: P55 - P57 (14 problems)
# Section 3.6: P58 - P60 (6 problems)
# Section 3.7: P61 - P62 (7 problems)

for sec_idx, (p_start, p_end, name) in enumerate([
    (41, 44, "3.1 微分中值定理"),
    (45, 47, "3.2 洛必达法则"),
    (48, 48, "3.3 泰勒公式"),
    (49, 54, "3.4 函数单调性与凹凸性"),
    (55, 57, "3.5 函数极值与最值"),
    (58, 60, "3.6 函数图形描绘"),
    (61, 62, "3.7 曲率")
]):
    print(f"\n==================== {name} (P{p_start}-P{p_end}) ====================")
    for p in range(p_start, p_end + 1):
        page = doc[p - 1]
        blocks = page.get_text('blocks')
        for b in blocks:
            txt = b[4].strip()
            if txt.startswith('例') or '补充练习' in txt:
                print(f"  [P{p}] {txt[:60]}...")
