"""
Generate calculator icon files (PNG and ICO) from scratch.
No external dependencies required.
"""
import struct
import zlib
import os

def create_icon():
    """Create a 256x256 calculator icon as PNG and ICO."""
    size = 256
    pixels = [[(0, 0, 0, 0)] * size for _ in range(size)]

    # Colors
    purple1 = (102, 126, 234)
    purple2 = (118, 75, 162)
    screen_bg = (26, 26, 46)
    screen_text = (0, 212, 255)
    btn_white = (255, 255, 255)
    btn_accent = (0, 212, 255)

    def lerp(a, b, t):
        return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

    def set_pixel(x, y, color):
        if 0 <= x < size and 0 <= y < size:
            pixels[y][x] = (*color, 255)

    def fill_rect(x1, y1, x2, y2, color):
        for y in range(y1, y2):
            for x in range(x1, x2):
                set_pixel(x, y, color)

    def draw_rounded_rect(x1, y1, x2, y2, r, color):
        for y in range(y1, y2):
            for x in range(x1, x2):
                # Check corners
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
                    set_pixel(x, y, color)

    # Background gradient
    for y in range(size):
        t = y / size
        c = lerp(purple1, purple2, t)
        for x in range(size):
            set_pixel(x, y, c)

    # Main body (rounded rectangle)
    body_x1, body_y1 = 48, 24
    body_x2, body_y2 = 208, 232
    body_r = 24
    draw_rounded_rect(body_x1, body_y1, body_x2, body_y2, body_r, lerp(purple1, purple2, 0.5))

    # Screen
    draw_rounded_rect(64, 40, 192, 96, 8, screen_bg)

    # Screen text "42" (simplified as blocks)
    # Just draw a simple display area with accent color
    fill_rect(68, 44, 188, 92, screen_bg)
    # Accent line at bottom of screen
    fill_rect(68, 90, 188, 92, btn_accent)

    # Buttons - Row 1
    btn_h, btn_r = 24, 6
    for i in range(3):
        x = 64 + i * 36
        draw_rounded_rect(x, 112, x + 28, 136, btn_r, btn_white)
    draw_rounded_rect(172, 112, 192, 136, btn_r, btn_accent)

    # Buttons - Row 2
    for i in range(3):
        x = 64 + i * 36
        draw_rounded_rect(x, 144, x + 28, 168, btn_r, btn_white)
    draw_rounded_rect(172, 144, 192, 168, btn_r, btn_accent)

    # Buttons - Row 3
    for i in range(3):
        x = 64 + i * 36
        draw_rounded_rect(x, 176, x + 28, 200, btn_r, btn_white)
    draw_rounded_rect(172, 176, 192, 200, btn_r, btn_accent)

    # Buttons - Row 4
    draw_rounded_rect(64, 208, 128, 232, btn_r, btn_white)
    draw_rounded_rect(136, 208, 164, 232, btn_r, btn_white)
    draw_rounded_rect(172, 208, 192, 232, btn_r, btn_accent)

    return pixels

def save_png(pixels, filename):
    """Save pixels as PNG."""
    size = len(pixels[0])

    def chunk(chunk_type, data):
        c = chunk_type + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

    # PNG header
    png = b'\x89PNG\r\n\x1a\n'

    # IHDR
    ihdr_data = struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0)
    png += chunk(b'IHDR', ihdr_data)

    # IDAT (image data)
    raw = b''
    for row in pixels:
        raw += b'\x00'  # filter none
        for r, g, b, a in row:
            raw += struct.pack('BBBB', r, g, b, a)

    compressed = zlib.compress(raw, 9)
    png += chunk(b'IDAT', compressed)

    # IEND
    png += chunk(b'IEND', b'')

    with open(filename, 'wb') as f:
        f.write(png)

def save_ico(pixels, filename):
    """Save pixels as ICO (256x256, 32-bit)."""
    size = len(pixels)

    # ICO header
    ico = struct.pack('<HHH', 0, 1, 1)

    # ICO directory entry
    # 256 is stored as 0 in ICO format
    ico += struct.pack('BBBB', 0, 0, 0, 0)  # width, height, color_count, reserved
    ico += struct.pack('<HHI', 1, 32, 0)  # planes, bpp, size (filled later)
    ico += struct.pack('<I', 22)  # offset to image data (header + 1 entry = 22)

    # BMP data (without file header)
    bmp_data = struct.pack('<IHHIIIIIIII',
        40,           # header size
        size * 2,     # width (doubled for ICO)
        size,         # height
        1,            # planes
        32,           # bpp
        0,            # compression
        0,            # image size (can be 0 for uncompressed)
        0, 0, 0, 0)   # colors

    # Pixel data (bottom-up for BMP)
    for row in reversed(pixels):
        for r, g, b, a in row:
            bmp_data += struct.pack('BBBB', b, g, r, a)

    # Update size in directory entry
    ico_size = len(bmp_data)
    ico = ico[:14] + struct.pack('<I', ico_size) + ico[18:]

    with open(filename, 'wb') as f:
        f.write(ico + bmp_data)

if __name__ == '__main__':
    out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)

    print("Generating calculator icon...")
    px = create_icon()

    png_path = os.path.join(out_dir, 'logo.png')
    ico_path = os.path.join(out_dir, 'logo.ico')

    save_png(px, png_path)
    print(f"Saved PNG: {png_path}")

    save_ico(px, ico_path)
    print(f"SavedICO: {ico_path}")
    print("Done!")
