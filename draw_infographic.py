"""Draw the 25 November 2026 world-news front page.

One deterministic 1024x1024 PNG, drawn with Pillow only. No network,
no clock, no randomness: the same input always produces the same bytes.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 234)      # newsprint cream
INK = (26, 26, 26)        # near-black ink
RED = (176, 42, 42)       # masthead accent
BLUE = (31, 68, 120)      # story tag blue
GREY = (110, 105, 95)     # muted grey
LINE = (180, 172, 156)    # hairline rules
PANEL = (255, 255, 255)   # card white

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_icon(draw, kind, x, y, s, accent):
    """Small flat pictogram for a story card, drawn from shapes."""
    if kind == "tower":  # Riyadh skyscraper under attack
        draw.rectangle([x + s * 0.30, y + s * 0.10, x + s * 0.62, y + s * 0.95], fill=INK)
        draw.rectangle([x + s * 0.42, y, x + s * 0.50, y + s * 0.10], fill=INK)
        for row in range(5):
            yy = y + s * (0.20 + row * 0.15)
            draw.rectangle([x + s * 0.35, yy, x + s * 0.57, yy + s * 0.05], fill=(255, 210, 90))
        draw.line([x + s * 0.05, y + s * 0.05, x + s * 0.28, y + s * 0.28], fill=RED, width=4)
        draw.ellipse([x + s * 0.62, y + s * 0.02, x + s * 0.78, y + s * 0.18], fill=RED)
        draw.ellipse([x + s * 0.70, y + s * 0.22, x + s * 0.82, y + s * 0.34], fill=(255, 140, 90))
    elif kind == "shield":  # cyber breach
        draw.polygon(
            [(x + s * 0.5, y + s * 0.05), (x + s * 0.92, y + s * 0.22),
             (x + s * 0.88, y + s * 0.62), (x + s * 0.5, y + s * 0.95),
             (x + s * 0.12, y + s * 0.62), (x + s * 0.08, y + s * 0.22)],
            fill=BLUE)
        draw.line([x + s * 0.30, y + s * 0.52, x + s * 0.46, y + s * 0.68,
                   x + s * 0.74, y + s * 0.34], fill=(255, 255, 255), width=6)
    elif kind == "chip":  # Huawei verdict
        draw.rectangle([x + s * 0.22, y + s * 0.22, x + s * 0.78, y + s * 0.78],
                       fill=INK)
        draw.rectangle([x + s * 0.38, y + s * 0.38, x + s * 0.62, y + s * 0.62],
                       fill=(255, 210, 90))
        for i in range(3):
            xx = x + s * (0.32 + i * 0.18)
            draw.line([xx, y + s * 0.08, xx, y + s * 0.22], fill=INK, width=3)
            draw.line([xx, y + s * 0.78, xx, y + s * 0.92], fill=INK, width=3)
            yy = y + s * (0.32 + i * 0.18)
            draw.line([x + s * 0.08, yy, x + s * 0.22, yy], fill=INK, width=3)
            draw.line([x + s * 0.78, yy, x + s * 0.92, yy], fill=INK, width=3)
    elif kind == "rocket":  # Shenzhou launch
        draw.polygon([(x + s * 0.5, y + s * 0.02), (x + s * 0.66, y + s * 0.45),
                      (x + s * 0.5, y + s * 0.38), (x + s * 0.34, y + s * 0.45)],
                     fill=INK)
        draw.ellipse([x + s * 0.44, y + s * 0.16, x + s * 0.56, y + s * 0.30],
                     fill=(140, 200, 255))
        draw.polygon([(x + s * 0.34, y + s * 0.45), (x + s * 0.22, y + s * 0.68),
                      (x + s * 0.36, y + s * 0.58)], fill=RED)
        draw.polygon([(x + s * 0.66, y + s * 0.45), (x + s * 0.78, y + s * 0.68),
                      (x + s * 0.64, y + s * 0.58)], fill=RED)
        draw.polygon([(x + s * 0.44, y + s * 0.55), (x + s * 0.56, y + s * 0.55),
                      (x + s * 0.62, y + s * 0.80), (x + s * 0.38, y + s * 0.80)],
                     fill=(255, 140, 60))
        draw.ellipse([x + s * 0.40, y + s * 0.82, x + s * 0.60, y + s * 0.95],
                     fill=(255, 210, 90))
    elif kind == "medal":  # Medal of Freedom
        draw.ellipse([x + s * 0.22, y + s * 0.34, x + s * 0.78, y + s * 0.90],
                     fill=(255, 210, 90), outline=INK, width=3)
        draw.ellipse([x + s * 0.38, y + s * 0.50, x + s * 0.62, y + s * 0.74],
                     outline=INK, width=3)
        draw.polygon([(x + s * 0.34, y + s * 0.36), (x + s * 0.66, y + s * 0.36),
                      (x + s * 0.58, y + s * 0.08), (x + s * 0.42, y + s * 0.08)],
                     fill=RED)
        draw.polygon([(x + s * 0.42, y + s * 0.08), (x + s * 0.58, y + s * 0.08),
                      (x + s * 0.52, y), (x + s * 0.48, y)], fill=BLUE)
    elif kind == "store":  # Colombia supermarket hostages
        draw.rectangle([x + s * 0.06, y + s * 0.30, x + s * 0.94, y + s * 0.92],
                       fill=PANEL, outline=INK, width=3)
        draw.polygon([(x, y + s * 0.30), (x + s, y + s * 0.30),
                      (x + s * 0.88, y + s * 0.10), (x + s * 0.12, y + s * 0.10)],
                     fill=RED)
        draw.rectangle([x + s * 0.16, y + s * 0.46, x + s * 0.34, y + s * 0.92],
                       outline=INK, width=3)
        draw.rectangle([x + s * 0.66, y + s * 0.46, x + s * 0.84, y + s * 0.92],
                       outline=INK, width=3)
        draw.line([x + s * 0.42, y + s * 0.46, x + s * 0.58, y + s * 0.46],
                  fill=INK, width=3)


STORIES = [
    dict(tag="MIDDLE EAST", icon="tower", headline="Riyadh tower hit again",
         body="Houthi missile strikes the Saudi capital's tallest skyscraper "
              "for the second time in a week; 11 people injured."),
    dict(tag="UNITED STATES", icon="shield", headline="CIA and spy chief's office breached",
         body="Cyberattack exposes unclassified data at the CIA and ODNI."),
    dict(tag="TECH / BUSINESS", icon="chip", headline="Huawei convicted in US trial",
         body="Jury convicts Huawei of stealing trade secrets and bank fraud."),
    dict(tag="SPACE / CHINA", icon="rocket", headline="Shenzhou-24 lifts off",
         body="China's Shenzhou-24 launches with a Pakistani astronaut."),
    dict(tag="US POLITICS", icon="medal", headline="Medal of Freedom for Giuliani",
         body="Trump awards Rudy Giuliani the highest US civilian honour."),
    dict(tag="AMERICAS", icon="store", headline="25 hostages in Colombia store",
         body="Gunmen seize 25 shoppers and staff in a Colombian supermarket."),
]


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    m = 30  # margin

    # ---- Masthead -------------------------------------------------------
    f_mast = font(SERIF, 62)
    f_date = font(SANS_B, 26)
    f_kicker = font(SANS_B, 20)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_mast)
    d.text(((W - tw) / 2, 26), title, font=f_mast, fill=INK)
    d.line([m, 104, W - m, 104], fill=INK, width=3)
    d.line([m, 110, W - m, 110], fill=INK, width=1)
    date = "WEDNESDAY 25 NOVEMBER 2026"
    dw = d.textlength(date, font=f_date)
    d.text(((W - dw) / 2, 122), date, font=f_date, fill=RED)
    kick = "SIX STORIES THAT DEFINED THE DAY  \u2022  FROM RIYADH TO BEIJING"
    kw = d.textlength(kick, font=f_kicker)
    d.text(((W - kw) / 2, 158), kick, font=f_kicker, fill=GREY)
    d.line([m, 190, W - m, 190], fill=INK, width=2)

    # ---- Lead story -----------------------------------------------------
    lead = STORIES[0]
    ly0, ly1 = 204, 452
    d.rectangle([m, ly0, W - m, ly1], fill=PANEL, outline=INK, width=2)
    d.rectangle([m, ly0, W - m, ly0 + 30], fill=RED)
    f_tag = font(SANS_B, 19)
    d.text((m + 14, ly0 + 4), lead["tag"] + "  \u2014  LEAD STORY", font=f_tag,
           fill=(255, 255, 255))
    f_lead_h = font(SERIF, 44)
    f_lead_b = font(SANS, 24)
    tx = m + 24
    headline_lines = wrap(d, lead["headline"], f_lead_h, 560)
    y = ly0 + 48
    for line in headline_lines:
        d.text((tx, y), line, font=f_lead_h, fill=INK)
        y += 52
    body_lines = wrap(d, lead["body"], f_lead_b, 560)
    y += 6
    for line in body_lines:
        d.text((tx, y), line, font=f_lead_b, fill=(60, 58, 52))
        y += 31
    draw_icon(d, lead["icon"], 730, ly0 + 52, 180, RED)

    # ---- Five more stories, two columns ---------------------------------
    f_card_tag = font(SANS_B, 17)
    f_card_h = font(SERIF, 27)
    f_card_b = font(SANS, 20)
    col_w = (W - 2 * m - 20) // 2
    card_h = 148
    gx0 = [m, m + col_w + 20]
    gy0 = [ly1 + 18, ly1 + 18 + card_h + 14, ly1 + 18 + 2 * (card_h + 14)]
    positions = [(gx0[0], gy0[0]), (gx0[1], gy0[0]),
                 (gx0[0], gy0[1]), (gx0[1], gy0[1]),
                 (gx0[0], gy0[2])]
    for story, (cx, cy) in zip(STORIES[1:5], positions):
        d.rectangle([cx, cy, cx + col_w, cy + card_h], fill=PANEL,
                    outline=LINE, width=1)
        d.line([cx, cy, cx + col_w, cy], fill=BLUE, width=4)
        draw_icon(d, story["icon"], cx + 14, cy + 40, 76, BLUE)
        tx = cx + 106
        d.text((tx, cy + 12), story["tag"], font=f_card_tag, fill=BLUE)
        hl = wrap(d, story["headline"], f_card_h, col_w - 122)
        y = cy + 36
        for line in hl[:2]:
            d.text((tx, y), line, font=f_card_h, fill=INK)
            y += 32
        bl = wrap(d, story["body"], f_card_b, col_w - 122)
        for line in bl[:2]:
            d.text((tx, y), line, font=f_card_b, fill=(60, 58, 52))
            y += 25

    # ---- Sixth story, full-width bottom card ----------------------------
    story = STORIES[5]
    cx, cy = gx0[1], gy0[2]
    d.rectangle([cx, cy, cx + col_w, cy + card_h], fill=PANEL,
                outline=LINE, width=1)
    d.line([cx, cy, cx + col_w, cy], fill=BLUE, width=4)
    draw_icon(d, story["icon"], cx + 14, cy + 40, 76, BLUE)
    tx = cx + 106
    d.text((tx, cy + 12), story["tag"], font=f_card_tag, fill=BLUE)
    hl = wrap(d, story["headline"], f_card_h, col_w - 122)
    y = cy + 36
    for line in hl[:2]:
        d.text((tx, y), line, font=f_card_h, fill=INK)
        y += 32
    bl = wrap(d, story["body"], f_card_b, col_w - 122)
    for line in bl[:2]:
        d.text((tx, y), line, font=f_card_b, fill=(60, 58, 52))
        y += 25

    # ---- Bottom-left note box -------------------------------------------
    bx, by = gx0[0], gy0[2]
    d.rectangle([bx, by, bx + col_w, by + card_h], fill=(232, 226, 210),
                outline=LINE, width=1)
    f_note_h = font(SANS_B, 20)
    f_note_b = font(SANS, 19)
    d.text((bx + 16, by + 14), "THE DAY IN BRIEF", font=f_note_h, fill=INK)
    notes = ["Missiles, courts, rockets and medals:",
             "a day of conflict, justice, space",
             "and ceremony \u2014 six stories, six",
             "corners of the world."]
    y = by + 44
    for line in notes:
        d.text((bx + 16, y), line, font=f_note_b, fill=(60, 58, 52))
        y += 25

    # ---- Footer ----------------------------------------------------------
    fy = gy0[2] + card_h + 18
    d.line([m, fy, W - m, fy], fill=INK, width=2)
    f_foot = font(SANS, 18)
    foot = ("Sources: SCMP, The New York Times, Reuters, AP, The Japan Times  "
            "\u2022  All events reported 25 November 2026")
    fw = d.textlength(foot, font=f_foot)
    d.text(((W - fw) / 2, fy + 10), foot, font=f_foot, fill=GREY)

    return img


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    build().save(out, format="PNG")
    print("wrote", out)
