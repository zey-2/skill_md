from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "final-slides"
PDF_PATH = ROOT.parent / "presentation-token-efficient-llm-use-imagegen.pdf"
W, H = 1920, 1080

FONT_REG = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

COLORS = {
    "paper": (246, 242, 233),
    "muted": (190, 181, 166),
    "dim": (128, 121, 109),
    "cyan": (76, 244, 239),
    "amber": (247, 184, 74),
    "coral": (255, 109, 95),
    "panel": (5, 7, 7, 188),
    "panel_strong": (5, 7, 7, 214),
    "line": (255, 255, 255, 46),
}


SLIDES = [
    {
        "label": "Strategy guide",
        "title": "Token-Efficient LLM Use",
        "subtitle": "Spend tokens where they produce work, not where habit burns them.",
        "stats": [("7", "stacking levers"), ("90%", "cache read discount"), ("50-98%", "routing savings")],
    },
    {
        "label": "The problem",
        "title": "Usage grows fast. Budgets do not.",
        "subtitle": "The goal is not to slow adoption. The goal is to make the default path cheaper.",
        "bullets": [
            "Token volume rises as teams rely on AI more often.",
            "Hard caps create friction and kill useful adoption.",
            "Better defaults let usage grow while spend stays controlled.",
        ],
        "stats": [("67%", "one-generation Opus price drop"), ("90%", "cache read discount"), ("98%", "routing upside")],
    },
    {
        "label": "The playbook",
        "title": "Seven levers that stack",
        "subtitle": "Each lever helps on its own. Together they compound.",
        "bullets": [
            "1. Route to the cheapest adequate model.",
            "2. Tune reasoning effort to task difficulty.",
            "3. Cache stable prompt prefixes.",
            "4. Compress noisy context before inference.",
            "5. Keep agents away from context-rot cliffs.",
            "6. Use code for deterministic routine work.",
            "7. Measure useful output per token.",
        ],
    },
    {
        "label": "Lever 1",
        "title": "Model routing",
        "subtitle": "Do not default every request to the most expensive model.",
        "bullets": [
            "Simple formatting and extraction can use cheap models.",
            "Standard work belongs on mid-tier models.",
            "Reserve frontier models for planning and hard reasoning.",
        ],
        "callout": "Question: what is the cheapest model that is good enough?",
    },
    {
        "label": "Lever 2",
        "title": "Effort tuning",
        "subtitle": "Reasoning depth is a budget knob.",
        "bullets": [
            "Low effort is enough for simple or bulk tasks.",
            "Medium is the best default for most work.",
            "Max effort should be deliberate, not habitual.",
        ],
        "callout": "Default to medium. Escalate only when the task earns it.",
    },
    {
        "label": "Lever 3",
        "title": "Prompt caching",
        "subtitle": "Pay once for stable context, then reuse it.",
        "bullets": [
            "Put static content first and dynamic content last.",
            "Keep prefixes byte-for-byte identical across requests.",
            "Pre-warm long-running agent sessions when possible.",
        ],
        "callout": "Cache reads can be dramatically cheaper than fresh input.",
    },
    {
        "label": "Lever 4",
        "title": "Context compression",
        "subtitle": "Send signal, not sludge.",
        "bullets": [
            "Strip irrelevant logs, repeated files, and stale discussion.",
            "Keep exact names, dates, and numbers when they matter.",
            "Use compression to create headroom before the model sees context.",
        ],
        "callout": "Best use: reduce noise while preserving the task signal.",
    },
    {
        "label": "Lever 5",
        "title": "Context rot",
        "subtitle": "A bigger window is not the same as better thinking.",
        "bullets": [
            "Quality often drops before the context window is full.",
            "Split or compact work before the session gets crowded.",
            "Size agent tasks so they finish before the quality cliff.",
        ],
        "callout": "Rule of thumb: watch the 60% fill zone.",
    },
    {
        "label": "Lever 6",
        "title": "Code over inference",
        "subtitle": "The cheapest token is the one you never send.",
        "bullets": [
            "Use scripts for formatting, parsing, validation, and merging.",
            "Keep AI for judgment, ambiguity, and planning.",
            "Turn repeated prompt work into deterministic tools.",
        ],
        "callout": "Routine work should become code, not recurring model calls.",
    },
    {
        "label": "Lever 7",
        "title": "Tokenmaxxing",
        "subtitle": "Spend more only when more tokens buy more output.",
        "bullets": [
            "Measure useful output per token, not token volume alone.",
            "Spend on retrieval, review, tests, and verification.",
            "Cut tokens that do not improve the result.",
        ],
        "callout": "Less waste, not less ambition.",
    },
    {
        "label": "Case study",
        "title": "Platform discipline in practice",
        "subtitle": "Let usage grow while the platform controls waste.",
        "bullets": [
            "Gateway routes by price, cache state, and task need.",
            "Cheap defaults handle execution; frontier models handle planning.",
            "Caching, compression, and code reduce waste.",
            "Teams measure useful output, not token volume alone.",
        ],
        "callout": "The pattern: freedom for engineers, discipline in the platform.",
    },
    {
        "label": "Takeaway",
        "title": "Fewer tokens wasted. Not fewer tokens used.",
        "subtitle": "Route smarter. Cache aggressively. Compress ruthlessly. Code what you can. Spend tokens that earn their keep.",
        "stats": [("Route", "before you run"), ("Cache", "before you repeat"), ("Code", "before you infer")],
    },
]


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size=size)


def fit_cover(img):
    img = img.convert("RGB")
    iw, ih = img.size
    scale = max(W / iw, H / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - W) // 2
    top = (nh - H) // 2
    return img.crop((left, top, left + W, top + H))


def add_overlays(base, strong=False):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = overlay.load()
    for x in range(W):
        left_alpha = int(max(0, 178 * (1 - x / 1160)))
        for y in range(H):
            top_alpha = int(max(0, 70 * (1 - y / 720)))
            bottom_alpha = int(max(0, 72 * (y / H)))
            a = min(225, left_alpha + top_alpha + bottom_alpha + (25 if strong else 0))
            px[x, y] = (0, 0, 0, a)
    return Image.alpha_composite(base.convert("RGBA"), overlay)


def wrap_text(draw, text, fnt, max_width):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        trial = (line + " " + word).strip()
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(draw, text, xy, fnt, fill, max_width, line_gap=10):
    x, y = xy
    for line in wrap_text(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + line_gap
    return y


def draw_label(draw, text, x, y):
    fnt = font(26, bold=True)
    text = text.upper()
    draw.rounded_rectangle((x, y, x + draw.textlength(text, font=fnt) + 72, y + 48), radius=24, fill=(4, 9, 10, 168), outline=COLORS["cyan"], width=1)
    draw.ellipse((x + 15, y + 18, x + 25, y + 28), fill=COLORS["amber"])
    draw.text((x + 36, y + 10), text, font=fnt, fill=COLORS["cyan"])


def draw_panel(draw, box, strong=False):
    fill = COLORS["panel_strong"] if strong else COLORS["panel"]
    draw.rounded_rectangle(box, radius=22, fill=fill, outline=COLORS["line"], width=1)


def draw_bullets(draw, bullets, x, y, max_width, size=34, gap=18):
    fnt = font(size)
    for item in bullets:
        draw.ellipse((x, y + 13, x + 13, y + 26), fill=COLORS["amber"])
        y = draw_wrapped(draw, item, (x + 36, y), fnt, COLORS["paper"], max_width - 36, line_gap=8)
        y += gap
    return y


def draw_stats(draw, stats, x, y, width):
    gap = 18
    count = len(stats)
    cell_w = int((width - gap * (count - 1)) / count)
    for idx, (big, small) in enumerate(stats):
        cx = x + idx * (cell_w + gap)
        draw.rounded_rectangle((cx, y, cx + cell_w, y + 138), radius=18, fill=(5, 7, 7, 166), outline=COLORS["line"], width=1)
        big_font = font(54 if len(big) < 7 else 42, bold=True)
        draw.text((cx + 28, y + 25), big, font=big_font, fill=COLORS["paper"])
        draw_wrapped(draw, small.upper(), (cx + 28, y + 88), font(20, bold=True), COLORS["muted"], cell_w - 56, line_gap=2)


def render_slide(slide, idx):
    art_path = ROOT / f"slide-{idx:02d}-art.png"
    base = fit_cover(Image.open(art_path))
    canvas = add_overlays(base, strong=idx in {7, 8, 11})
    draw = ImageDraw.Draw(canvas)

    x = 110
    y = 110
    panel_bottom = 950
    draw_panel(draw, (72, 74, 1030, panel_bottom), strong=idx in {7, 8, 11})
    draw_label(draw, slide["label"], x, y)
    y += 90

    title_size = 88 if idx != 1 else 112
    y = draw_wrapped(draw, slide["title"], (x, y), font(title_size, bold=True), COLORS["paper"], 790, line_gap=10)
    y += 20
    y = draw_wrapped(draw, slide["subtitle"], (x, y), font(38), COLORS["muted"], 820, line_gap=8)
    y += 34

    if "bullets" in slide:
        bullet_size = 30 if idx in {3, 11} else 34
        bullet_gap = 8 if idx in {3, 11} else 18
        y = draw_bullets(draw, slide["bullets"], x, y, 820, size=bullet_size, gap=bullet_gap)

    if slide.get("callout"):
        callout_y = min(max(y + 22, 740), 820)
        draw.rounded_rectangle((x, callout_y, x + 800, callout_y + 108), radius=18, fill=(8, 38, 39, 238), outline=COLORS["cyan"], width=2)
        draw_wrapped(draw, slide["callout"], (x + 28, callout_y + 24), font(30, bold=True), COLORS["cyan"], 744, line_gap=6)

    if "stats" in slide:
        stat_y = 760 if idx == 1 else min(y + 12, 784)
        draw_stats(draw, slide["stats"], x, stat_y, 820)

    draw.line((72, 1006, 1848, 1006), fill=(255, 255, 255, 42), width=1)
    draw.text((110, 1024), "TOKEN-EFFICIENT LLM USE", font=font(18, bold=True), fill=COLORS["dim"])
    slide_no = f"{idx:02d} / {len(SLIDES):02d}"
    draw.text((1740, 1024), slide_no, font=font(18, bold=True), fill=COLORS["dim"])
    return canvas.convert("RGB")


def main():
    OUT_DIR.mkdir(exist_ok=True)
    final_images = []
    for i, slide in enumerate(SLIDES, start=1):
        img = render_slide(slide, i)
        out = OUT_DIR / f"slide-{i:02d}.png"
        img.save(out, quality=95)
        final_images.append(img)

    final_images[0].save(
        PDF_PATH,
        "PDF",
        resolution=150.0,
        save_all=True,
        append_images=final_images[1:],
    )
    print(PDF_PATH)


if __name__ == "__main__":
    main()
