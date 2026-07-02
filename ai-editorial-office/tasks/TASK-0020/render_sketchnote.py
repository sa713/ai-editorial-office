from __future__ import annotations

import math
import random
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


TASK_DIR = Path(__file__).resolve().parent
OUT = TASK_DIR / "visual-conspect-blog.png"

W, H = 1600, 900
random.seed(20)

PAPER = (248, 244, 232)
INK = (43, 39, 34)
MUTED = (92, 86, 76)
BLUE = (43, 112, 143)
RED = (178, 72, 64)
GREEN = (68, 129, 88)
YELLOW = (237, 190, 74)
PURPLE = (118, 90, 154)
ORANGE = (216, 132, 66)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


FONT_MAIN = "/System/Library/Fonts/Supplemental/Comic Sans MS.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Comic Sans MS Bold.ttf"
FONT_FALLBACK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

try:
    title_font = font(FONT_BOLD, 48)
    h_font = font(FONT_BOLD, 32)
    body_font = font(FONT_MAIN, 25)
    small_font = font(FONT_MAIN, 21)
    mini_font = font(FONT_MAIN, 18)
except OSError:
    title_font = font(FONT_FALLBACK, 48)
    h_font = font(FONT_FALLBACK, 32)
    body_font = font(FONT_FALLBACK, 25)
    small_font = font(FONT_FALLBACK, 21)
    mini_font = font(FONT_FALLBACK, 18)


def jitter(value: float, amount: float = 3) -> float:
    return value + random.uniform(-amount, amount)


def sketch_line(draw: ImageDraw.ImageDraw, p1, p2, fill=INK, width=3, passes=2):
    x1, y1 = p1
    x2, y2 = p2
    for _ in range(passes):
        draw.line(
            (jitter(x1), jitter(y1), jitter(x2), jitter(y2)),
            fill=fill,
            width=width,
            joint="curve",
        )


def sketch_rect(draw, box, outline=INK, width=3, radius=20, fill=None, passes=2):
    x1, y1, x2, y2 = box
    if fill:
        draw.rounded_rectangle(box, radius=radius, fill=fill)
    for _ in range(passes):
        draw.rounded_rectangle(
            (jitter(x1), jitter(y1), jitter(x2), jitter(y2)),
            radius=radius + random.uniform(-3, 3),
            outline=outline,
            width=width,
        )


def sketch_ellipse(draw, box, outline=INK, width=3, fill=None, passes=2):
    if fill:
        draw.ellipse(box, fill=fill)
    x1, y1, x2, y2 = box
    for _ in range(passes):
        draw.ellipse(
            (jitter(x1), jitter(y1), jitter(x2), jitter(y2)),
            outline=outline,
            width=width,
        )


def dashed_ellipse(draw, box, outline=INK, width=3, dash=18, gap=13):
    x1, y1, x2, y2 = box
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    rx, ry = (x2 - x1) / 2, (y2 - y1) / 2
    steps = 180
    on = True
    count = 0
    last = None
    for i in range(steps + 1):
        t = 2 * math.pi * i / steps
        point = (cx + rx * math.cos(t), cy + ry * math.sin(t))
        count += 1
        if last and on:
            sketch_line(draw, last, point, outline, width=width, passes=1)
        last = point
        if on and count >= dash:
            on = False
            count = 0
            last = None
        elif not on and count >= gap:
            on = True
            count = 0
            last = point


def arrow(draw, p1, p2, fill=INK, width=3):
    sketch_line(draw, p1, p2, fill=fill, width=width, passes=2)
    x1, y1 = p1
    x2, y2 = p2
    ang = math.atan2(y2 - y1, x2 - x1)
    size = 16
    for delta in (0.75, -0.75):
        x3 = x2 - size * math.cos(ang + delta)
        y3 = y2 - size * math.sin(ang + delta)
        sketch_line(draw, (x2, y2), (x3, y3), fill=fill, width=width, passes=2)


def draw_wrapped(draw, text, xy, font_obj, fill=INK, max_width=260, line_gap=5):
    x, y = xy
    words = text.split()
    lines = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font_obj)[2] <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    for line in lines:
        draw.text((x + random.uniform(-1.2, 1.2), y), line, font=font_obj, fill=fill)
        y += font_obj.size + line_gap
    return y


def chip(draw, box, text, color, font_obj=small_font):
    x1, y1, x2, y2 = box
    sketch_rect(draw, box, outline=color, fill=(255, 252, 239), radius=15, width=3)
    draw_wrapped(draw, text, (x1 + 16, y1 + 12), font_obj, fill=INK, max_width=x2 - x1 - 32)


def agent(draw, center, color=BLUE, label=None):
    x, y = center
    sketch_ellipse(draw, (x - 20, y - 18, x + 20, y + 18), outline=color, fill=(255, 253, 242), width=3)
    sketch_line(draw, (x - 30, y), (x - 20, y), color, width=2, passes=1)
    sketch_line(draw, (x + 20, y), (x + 31, y - 5), color, width=2, passes=1)
    draw.ellipse((x - 8, y - 5, x - 3, y), fill=color)
    draw.ellipse((x + 4, y - 5, x + 9, y), fill=color)
    sketch_line(draw, (x - 6, y + 8), (x + 7, y + 8), color, width=2, passes=1)
    if label:
        draw.text((x - 24, y + 24), label, font=mini_font, fill=MUTED)


def icon_map(draw, x, y):
    sketch_rect(draw, (x, y, x + 190, y + 115), outline=BLUE, width=3, radius=12, fill=(247, 252, 248))
    for i in range(5):
        sketch_line(draw, (x + 20, y + 25 + i * 18), (x + 170, y + 15 + i * 18), fill=(180, 190, 176), width=1, passes=1)
    for px, py in [(x + 45, y + 42), (x + 122, y + 76), (x + 151, y + 35)]:
        sketch_ellipse(draw, (px - 7, py - 7, px + 7, py + 7), outline=RED, fill=(255, 242, 232), width=2)
        sketch_line(draw, (px, py + 7), (px, py + 24), fill=RED, width=2, passes=1)
    draw.text((x + 62, y + 88), "?", font=h_font, fill=PURPLE)


def icon_boundary(draw, x, y):
    sketch_rect(draw, (x, y, x + 210, y + 120), outline=RED, width=3, radius=18, fill=(255, 249, 239))
    draw.text((x + 18, y + 16), "граница", font=small_font, fill=INK)
    agent(draw, (x + 75, y + 73), color=BLUE)
    arrow(draw, (x + 105, y + 72), (x + 175, y + 55), fill=RED, width=3)
    draw.text((x + 150, y + 72), "!", font=h_font, fill=RED)


def icon_controls(draw, x, y):
    labels = ["реестр", "владельцы", "runtime", "логи", "traceability"]
    for idx, label in enumerate(labels):
        cx = x + idx * 155
        sketch_ellipse(draw, (cx, y, cx + 108, y + 62), outline=GREEN, fill=(244, 253, 245), width=3)
        draw.text((cx + 16, y + 20), label, font=mini_font, fill=INK)
        if idx < len(labels) - 1:
            arrow(draw, (cx + 110, y + 31), (cx + 150, y + 31), fill=GREEN, width=2)


def add_paper_texture(img: Image.Image):
    pix = img.load()
    for _ in range(23000):
        x = random.randrange(W)
        y = random.randrange(H)
        delta = random.choice([-8, -6, 6, 8, 10])
        r, g, b = pix[x, y]
        pix[x, y] = (
            max(0, min(255, r + delta)),
            max(0, min(255, g + delta)),
            max(0, min(255, b + delta)),
        )


def main():
    img = Image.new("RGB", (W, H), PAPER)
    add_paper_texture(img)
    draw = ImageDraw.Draw(img)

    # Notebook-like outer line and a few light ruled marks.
    sketch_rect(draw, (34, 28, W - 34, H - 30), outline=(163, 146, 118), width=2, radius=28, fill=None, passes=2)
    for y in range(112, H - 70, 84):
        sketch_line(draw, (64, y), (W - 70, y + random.uniform(-3, 3)), fill=(224, 215, 195), width=1, passes=1)

    draw.text((80, 54), "Enterprise AI security: конспект статьи", font=title_font, fill=INK)
    draw.text((84, 112), "главная мысль: агенты уже работают, а контроль догоняет", font=small_font, fill=MUTED)

    # Top adoption strip.
    chip(draw, (92, 165, 430, 257), "43%: > половины сотрудников используют AI agents", BLUE)
    chip(draw, (462, 153, 790, 246), "много платформ -> сложнее единый надзор", PURPLE)
    arrow(draw, (425, 184), (462, 184), fill=PURPLE, width=3)
    chip(draw, (838, 154, 1110, 244), "старый периметр уже не объясняет риск", ORANGE)
    arrow(draw, (792, 184), (838, 184), fill=ORANGE, width=3)

    # Center agent workforce.
    dashed_ellipse(draw, (555, 260, 1046, 598), outline=(104, 99, 87), width=3)
    draw.text((622, 296), "AI agents = цифровая", font=h_font, fill=INK)
    draw.text((675, 334), "рабочая сила", font=h_font, fill=INK)
    draw.text((660, 539), "риск смещается к действиям", font=small_font, fill=RED)
    for c, col, lab in [
        ((640, 430), BLUE, "IT"),
        ((745, 402), GREEN, "sec"),
        ((850, 438), PURPLE, "CS"),
        ((775, 500), ORANGE, "eng"),
        ((935, 372), BLUE, ""),
        ((610, 515), GREEN, ""),
    ]:
        agent(draw, c, color=col, label=lab)
    arrow(draw, (930, 470), (1076, 423), fill=RED, width=4)
    draw.text((1000, 452), "за рамки", font=mini_font, fill=RED)

    # Left visibility block.
    sketch_rect(draw, (82, 295, 494, 600), outline=BLUE, width=3, radius=25, fill=(255, 253, 242), passes=2)
    draw.text((112, 314), "Видимость", font=h_font, fill=BLUE)
    draw.text((112, 350), "и ответственность", font=h_font, fill=BLUE)
    icon_map(draw, 122, 402)
    draw_wrapped(draw, "shadow AI появляется раньше, чем полная карта агентов", (332, 398), small_font, fill=INK, max_width=135)
    draw.text((126, 530), "21%: real-time registry", font=small_font, fill=INK)
    draw.text((126, 560), "владелец? аудитный след?", font=small_font, fill=PURPLE)
    arrow(draw, (494, 455), (555, 440), fill=BLUE, width=3)

    # Right behavior block.
    sketch_rect(draw, (1116, 283, 1504, 604), outline=RED, width=3, radius=25, fill=(255, 252, 244), passes=2)
    draw.text((1144, 308), "Поведение и инциденты", font=h_font, fill=RED)
    icon_boundary(draw, 1150, 365)
    draw.text((1162, 510), "53%: выход за рамки", font=small_font, fill=INK)
    draw.text((1162, 542), "47%: инциденты", font=small_font, fill=INK)
    draw.text((1350, 532), "часы/дни", font=h_font, fill=ORANGE)
    arrow(draw, (1046, 440), (1116, 435), fill=RED, width=3)

    # Bottom controls.
    sketch_rect(draw, (226, 648, 1118, 830), outline=GREEN, width=3, radius=25, fill=(251, 255, 244), passes=2)
    draw.text((258, 675), "Новая модель контроля", font=h_font, fill=GREEN)
    draw.text((260, 716), "нужны: реестр + владельцы + runtime-контроль + логи + traceability", font=small_font, fill=INK)
    icon_controls(draw, 282, 760)

    # Compliance corner.
    sketch_rect(draw, (1170, 662, 1498, 828), outline=PURPLE, width=3, radius=24, fill=(252, 248, 255), passes=2)
    draw.text((1202, 694), "compliance", font=h_font, fill=PURPLE)
    draw.text((1204, 733), "- не стратегия", font=h_font, fill=PURPLE)
    draw.text((1210, 782), "13% готовы", font=small_font, fill=INK)
    arrow(draw, (1118, 743), (1170, 742), fill=PURPLE, width=3)

    # A few live-thinking marks.
    for txt, pos, col in [
        ("инвентаризация", (448, 610), BLUE),
        ("runtime guardrails", (845, 618), GREEN),
        ("след действий", (990, 601), PURPLE),
    ]:
        draw.text(pos, txt, font=mini_font, fill=col)
    arrow(draw, (520, 630), (620, 580), fill=BLUE, width=2)
    arrow(draw, (895, 640), (858, 568), fill=GREEN, width=2)
    arrow(draw, (1030, 625), (955, 520), fill=PURPLE, width=2)

    # Tiny note in the margin: source is a survey report, not a recommendation checklist.
    draw.text((80, 842), "не пересказ PDF: карта аргумента статьи CSA/Zenity о риске AI agents", font=mini_font, fill=MUTED)

    img.save(OUT, "PNG", optimize=True)
    print(OUT)


if __name__ == "__main__":
    main()
