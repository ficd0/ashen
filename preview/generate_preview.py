#!/usr/bin/env python3

import json
from PIL import Image, ImageDraw, ImageFont


def hex_rgb(hex):
    hex = hex.lstrip("#")
    return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))


def relative_luminance(rgb):
    def channel_lum(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = map(channel_lum, rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


with open("palette.json", "r") as f:
    colors = json.load(f)
bg: str = colors["background"]
txt: str = colors["g_1"]
swatch_width, swatch_height = 130, 100
margin_x = 60
padding = 20
columns = 4


def get_contrast(hex_color):
    lum = relative_luminance(hex_rgb(hex_color))
    text_lum = relative_luminance(hex_rgb(txt))
    bg_lum = relative_luminance(hex_rgb(bg))

    contrast_with_txt = abs(lum - text_lum)
    contrast_with_bg = abs(lum - bg_lum)
    return txt if contrast_with_txt > contrast_with_bg else bg


rows = (len(colors) + columns - 1) // columns
img_width = columns * swatch_width + (columns + 1) * padding + 2 * margin_x
img_height = rows * swatch_height + (rows + 1) * padding

image = Image.new("RGB", (img_width, img_height), bg)
draw = ImageDraw.Draw(image)

try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 14)
except:
    font = ImageFont.load_default()


for i, (name, hex) in enumerate(colors.items()):
    row, col = divmod(i, columns)
    x = margin_x + padding + col * (swatch_width + padding)
    y = padding + row * (swatch_height + padding)

    draw.rectangle([x, y, x + swatch_width, y + swatch_height], fill=hex)
    text_x = x + 5
    text_y = y + swatch_height - 20
    draw.text((text_x, text_y), name, fill=get_contrast(hex), font=font)

image.save("palette.png")
