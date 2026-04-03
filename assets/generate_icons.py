"""
Generate all calculator icons as PNG files.
Creates icons for modes and currencies.
"""
import os
import struct
import zlib

def create_icon_pixels(width, height, draw_func):
    """Create icon pixels array and apply drawing function."""
    pixels = [[(0, 0, 0, 0)] * width for _ in range(height)]
    draw_func(pixels, width, height)
    return pixels

def set_pixel(pixels, x, y, color):
    """Set a pixel with bounds checking."""
    h, w = len(pixels), len(pixels[0])
    if 0 <= x < w and 0 <= y < h:
        pixels[y][x] = color

def draw_rect(pixels, x1, y1, x2, y2, color):
    """Draw a filled rectangle."""
    for y in range(y1, y2):
        for x in range(x1, x2):
            set_pixel(pixels, x, y, color)

def draw_rounded_rect(pixels, x1, y1, x2, y2, r, color):
    """Draw a rounded rectangle."""
    for y in range(y1, y2):
        for x in range(x1, x2):
            in_corner = False
            if x < x1 + r and y < y1 + r:
                dx, dy = x1 + r - x, y1 + r - y
                if dx*dx + dy*dy > r*r: in_corner = True
            elif x >= x2 - r and y < y1 + r:
                dx, dy = x - (x2 - r), y1 + r - y
                if dx*dx + dy*dy > r*r: in_corner = True
            elif x < x1 + r and y >= y2 - r:
                dx, dy = x1 + r - x, y - (y2 - r)
                if dx*dx + dy*dy > r*r: in_corner = True
            elif x >= x2 - r and y >= y2 - r:
                dx, dy = x - (x2 - r), y - (y2 - r)
                if dx*dx + dy*dy > r*r: in_corner = True
            if not in_corner:
                set_pixel(pixels, x, y, color)

# Accent color
ACCENT = (96, 205, 255, 255)
WHITE = (255, 255, 255, 255)
DARK = (32, 32, 32, 255)
GRAY = (160, 160, 160, 255)
RED = (255, 80, 80, 255)

def draw_standard(pixels, w, h):
    draw_rounded_rect(pixels, 12, 4, 52, 60, 6, ACCENT)
    draw_rounded_rect(pixels, 16, 8, 48, 22, 3, DARK)
    draw_rounded_rect(pixels, 16, 26, 24, 32, 2, WHITE)
    draw_rounded_rect(pixels, 28, 26, 36, 32, 2, WHITE)
    draw_rounded_rect(pixels, 40, 26, 48, 32, 2, WHITE)
    draw_rounded_rect(pixels, 16, 35, 24, 41, 2, WHITE)
    draw_rounded_rect(pixels, 28, 35, 36, 41, 2, WHITE)
    draw_rounded_rect(pixels, 40, 35, 48, 41, 2, WHITE)
    draw_rounded_rect(pixels, 16, 44, 24, 50, 2, WHITE)
    draw_rounded_rect(pixels, 28, 44, 36, 50, 2, WHITE)
    draw_rounded_rect(pixels, 40, 44, 48, 50, 2, WHITE)
    draw_rounded_rect(pixels, 16, 53, 36, 59, 2, WHITE)
    draw_rounded_rect(pixels, 40, 53, 48, 59, 2, WHITE)

def draw_scientific(pixels, w, h):
    draw_rounded_rect(pixels, 12, 4, 52, 60, 6, ACCENT)
    draw_rounded_rect(pixels, 16, 8, 48, 22, 3, DARK)
    # sin, cos labels
    draw_rounded_rect(pixels, 16, 26, 24, 32, 2, WHITE)
    draw_rounded_rect(pixels, 28, 26, 36, 32, 2, WHITE)
    draw_rounded_rect(pixels, 40, 26, 48, 32, 2, WHITE)
    # Numbers
    draw_rounded_rect(pixels, 16, 35, 24, 41, 2, WHITE)
    draw_rounded_rect(pixels, 28, 35, 36, 41, 2, WHITE)
    draw_rounded_rect(pixels, 40, 35, 48, 41, 2, WHITE)
    draw_rounded_rect(pixels, 16, 44, 24, 50, 2, WHITE)
    draw_rounded_rect(pixels, 28, 44, 36, 50, 2, WHITE)
    draw_rounded_rect(pixels, 40, 44, 48, 50, 2, WHITE)
    draw_rounded_rect(pixels, 16, 53, 36, 59, 2, WHITE)
    draw_rounded_rect(pixels, 40, 53, 48, 59, 2, WHITE)
    # Pi symbol area
    set_pixel(pixels, 18, 28, ACCENT)
    set_pixel(pixels, 19, 28, ACCENT)
    set_pixel(pixels, 20, 28, ACCENT)
    set_pixel(pixels, 19, 29, ACCENT)
    set_pixel(pixels, 19, 30, ACCENT)

def draw_programmer(pixels, w, h):
    draw_rounded_rect(pixels, 12, 4, 52, 60, 6, ACCENT)
    draw_rounded_rect(pixels, 16, 8, 48, 22, 3, DARK)
    # Hex buttons
    for i in range(4):
        draw_rounded_rect(pixels, 16 + i*8, 26, 22 + i*8, 32, 2, WHITE)
    for i in range(4):
        draw_rounded_rect(pixels, 16 + i*8, 35, 22 + i*8, 41, 2, WHITE)
    for i in range(4):
        draw_rounded_rect(pixels, 16 + i*8, 44, 22 + i*8, 50, 2, WHITE)
    for i in range(4):
        draw_rounded_rect(pixels, 16 + i*8, 53, 22 + i*8, 59, 2, WHITE)

def draw_minimalist(pixels, w, h):
    draw_rounded_rect(pixels, 12, 4, 52, 60, 6, ACCENT)
    draw_rounded_rect(pixels, 16, 8, 48, 22, 3, DARK)
    # Clean 2-column layout
    draw_rounded_rect(pixels, 16, 26, 30, 34, 2, WHITE)
    draw_rounded_rect(pixels, 34, 26, 48, 34, 2, WHITE)
    draw_rounded_rect(pixels, 16, 38, 30, 46, 2, WHITE)
    draw_rounded_rect(pixels, 34, 38, 48, 46, 2, WHITE)
    draw_rounded_rect(pixels, 16, 50, 48, 58, 2, WHITE)

def draw_modern(pixels, w, h):
    draw_rounded_rect(pixels, 12, 4, 52, 60, 6, ACCENT)
    draw_rounded_rect(pixels, 16, 8, 48, 22, 3, DARK)
    # Extra function buttons
    draw_rounded_rect(pixels, 16, 26, 24, 32, 2, WHITE)
    draw_rounded_rect(pixels, 28, 26, 36, 32, 2, WHITE)
    draw_rounded_rect(pixels, 40, 26, 48, 32, 2, WHITE)
    draw_rounded_rect(pixels, 16, 35, 24, 41, 2, WHITE)
    draw_rounded_rect(pixels, 28, 35, 36, 41, 2, WHITE)
    draw_rounded_rect(pixels, 40, 35, 48, 41, 2, WHITE)
    draw_rounded_rect(pixels, 16, 44, 24, 50, 2, WHITE)
    draw_rounded_rect(pixels, 28, 44, 36, 50, 2, WHITE)
    draw_rounded_rect(pixels, 40, 44, 48, 50, 2, WHITE)
    draw_rounded_rect(pixels, 16, 53, 36, 59, 2, WHITE)
    draw_rounded_rect(pixels, 40, 53, 48, 59, 2, WHITE)

def draw_currency(pixels, w, h):
    draw_rounded_rect(pixels, 12, 4, 52, 60, 6, ACCENT)
    # Dollar sign
    set_pixel(pixels, 30, 16, DARK)
    set_pixel(pixels, 30, 17, DARK)
    set_pixel(pixels, 30, 18, DARK)
    set_pixel(pixels, 30, 19, DARK)
    set_pixel(pixels, 30, 20, DARK)
    set_pixel(pixels, 30, 21, DARK)
    set_pixel(pixels, 30, 22, DARK)
    set_pixel(pixels, 30, 23, DARK)
    set_pixel(pixels, 30, 24, DARK)
    set_pixel(pixels, 30, 25, DARK)
    set_pixel(pixels, 30, 26, DARK)
    set_pixel(pixels, 30, 27, DARK)
    set_pixel(pixels, 30, 28, DARK)
    set_pixel(pixels, 30, 29, DARK)
    set_pixel(pixels, 30, 30, DARK)
    # S curve
    for x in range(26, 35):
        set_pixel(pixels, x, 20, DARK)
        set_pixel(pixels, x, 24, DARK)
        set_pixel(pixels, x, 28, DARK)
    # Arrows up/down
    set_pixel(pixels, 20, 36, WHITE)
    set_pixel(pixels, 19, 37, WHITE)
    set_pixel(pixels, 21, 37, WHITE)
    set_pixel(pixels, 44, 48, WHITE)
    set_pixel(pixels, 43, 47, WHITE)
    set_pixel(pixels, 45, 47, WHITE)

def draw_metric(pixels, w, h):
    draw_rounded_rect(pixels, 12, 4, 52, 60, 6, ACCENT)
    # Ruler
    draw_rect(pixels, 16, 16, 48, 24, WHITE)
    for i in range(0, 32, 4):
        draw_rect(pixels, 16 + i, 16, 16 + i + 1, 20, DARK)
    # Arrow
    set_pixel(pixels, 32, 30, WHITE)
    set_pixel(pixels, 31, 31, WHITE)
    set_pixel(pixels, 33, 31, WHITE)
    set_pixel(pixels, 32, 32, WHITE)
    set_pixel(pixels, 32, 33, WHITE)
    set_pixel(pixels, 32, 34, WHITE)
    set_pixel(pixels, 32, 35, WHITE)
    set_pixel(pixels, 32, 36, WHITE)
    set_pixel(pixels, 32, 37, WHITE)
    set_pixel(pixels, 32, 38, WHITE)
    set_pixel(pixels, 32, 39, WHITE)
    set_pixel(pixels, 32, 40, WHITE)
    set_pixel(pixels, 32, 41, WHITE)
    set_pixel(pixels, 32, 42, WHITE)
    set_pixel(pixels, 32, 43, WHITE)
    set_pixel(pixels, 32, 44, WHITE)
    set_pixel(pixels, 32, 45, WHITE)
    set_pixel(pixels, 32, 46, WHITE)
    set_pixel(pixels, 32, 47, WHITE)
    set_pixel(pixels, 32, 48, WHITE)

def draw_temperature(pixels, w, h):
    draw_rounded_rect(pixels, 12, 4, 52, 60, 6, ACCENT)
    # Thermometer
    draw_rounded_rect(pixels, 28, 12, 36, 40, 4, WHITE)
    draw_rounded_rect(pixels, 26, 40, 38, 52, 6, WHITE)
    # Mercury
    draw_rounded_rect(pixels, 30, 20, 34, 40, 2, RED)
    draw_rounded_rect(pixels, 28, 42, 36, 50, 4, RED)

def draw_currency_icon(pixels, w, h):
    draw_rounded_rect(pixels, 8, 8, 56, 56, 12, ACCENT)
    # Dollar/Euro symbols
    set_pixel(pixels, 32, 20, DARK)
    set_pixel(pixels, 32, 21, DARK)
    set_pixel(pixels, 32, 22, DARK)
    set_pixel(pixels, 32, 23, DARK)
    set_pixel(pixels, 32, 24, DARK)
    set_pixel(pixels, 32, 25, DARK)
    set_pixel(pixels, 32, 26, DARK)
    set_pixel(pixels, 32, 27, DARK)
    set_pixel(pixels, 32, 28, DARK)
    set_pixel(pixels, 32, 29, DARK)
    set_pixel(pixels, 32, 30, DARK)
    set_pixel(pixels, 32, 31, DARK)
    set_pixel(pixels, 32, 32, DARK)
    set_pixel(pixels, 32, 33, DARK)
    set_pixel(pixels, 32, 34, DARK)
    set_pixel(pixels, 32, 35, DARK)
    set_pixel(pixels, 32, 36, DARK)
    set_pixel(pixels, 32, 37, DARK)
    set_pixel(pixels, 32, 38, DARK)
    set_pixel(pixels, 32, 39, DARK)
    set_pixel(pixels, 32, 40, DARK)
    set_pixel(pixels, 32, 41, DARK)
    set_pixel(pixels, 32, 42, DARK)
    set_pixel(pixels, 32, 43, DARK)
    set_pixel(pixels, 32, 44, DARK)
    # S curves
    for x in range(26, 39):
        set_pixel(pixels, x, 24, DARK)
        set_pixel(pixels, x, 32, DARK)
        set_pixel(pixels, x, 40, DARK)

def save_png(pixels, filename):
    """Save pixels as PNG."""
    size = len(pixels[0])
    height = len(pixels)

    def chunk(chunk_type, data):
        c = chunk_type + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

    png = b'\x89PNG\r\n\x1a\n'
    ihdr_data = struct.pack('>IIBBBBB', size, height, 8, 6, 0, 0, 0)
    png += chunk(b'IHDR', ihdr_data)

    raw = b''
    for row in pixels:
        raw += b'\x00'
        for r, g, b, a in row:
            raw += struct.pack('BBBB', r, g, b, a)

    compressed = zlib.compress(raw, 9)
    png += chunk(b'IDAT', compressed)
    png += chunk(b'IEND', b'')

    with open(filename, 'wb') as f:
        f.write(png)

if __name__ == '__main__':
    out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)

    icons = {
        'icon_standard.png': draw_standard,
        'icon_scientific.png': draw_scientific,
        'icon_programmer.png': draw_programmer,
        'icon_minimalist.png': draw_minimalist,
        'icon_modern.png': draw_modern,
        'icon_currency.png': draw_currency,
        'icon_metric.png': draw_metric,
        'icon_temperature.png': draw_temperature,
        'icon_currency_list.png': draw_currency_icon,
    }

    for name, draw_func in icons.items():
        pixels = create_icon_pixels(64, 64, draw_func)
        save_png(pixels, os.path.join(out_dir, name))
        print(f"Saved: {name}")

    print("Done!")
