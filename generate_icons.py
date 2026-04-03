"""
Generate sidebar tab icons and currency icons using PIL/Pillow
Creates clean, simple icons for all calculator modes
"""

from PIL import Image, ImageDraw, ImageFont
import os

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_SIZE = (32, 32)
CURRENCY_ICON_SIZE = (24, 24)
BG_COLOR = (255, 255, 255, 0)  # Transparent

# Currency colors
CURRENCY_COLORS = {
    "USD": ("#3c813c", "#ffffff", "$"),    # Green
    "EUR": ("#003399", "#ffcc00", "€"),    # Blue/Yellow
    "GBP": ("#c8102e", "#00205b", "£"),    # Red/Blue
    "JPY": ("#ffffff", "#bc002d", "¥"),    # White/Red
    "CNY": ("#de2910", "#ffde00", "¥"),    # Red/Yellow
    "AUD": ("#00008b", "#ffffff", "A$"),   # Navy
    "CAD": ("#ff0000", "#ffffff", "C$"),   # Red
    "CHF": ("#ff0000", "#ffffff", "Fr"),   # Red/White
    "INR": ("#ff9933", "#138808", "₹"),    # Saffron/Green
    "KRW": ("#0047a0", "#cd2e3a", "₩"),    # Blue/Red
    "MXN": ("#006847", "#ce1126", "MX$"),  # Green/Red
    "BRL": ("#009c3b", "#ffdf00", "R$"),   # Green/Yellow
    "SGD": ("#ef3340", "#ffffff", "S$"),   # Red
    "HKD": ("#002e5d", "#ffffff", "HK$"),  # Navy
    "NZD": ("#00247d", "#cc142b", "NZ$"),  # Blue/Red
    "SEK": ("#004b87", "#fecc00", "kr"),   # Blue/Yellow
    "NOK": ("#ba0c2f", "#00205b", "kr"),   # Red/Blue
    "TRY": ("#e30a17", "#ffffff", "₺"),    # Red
    "RUB": ("#0039a6", "#d52b1e", "₽"),    # Blue/Red
    "ZAR": ("#007749", "#ffb81c", "R"),    # Green/Gold
    "AMD": ("#d90012", "#0033a0", "֏"),    # Red/Blue
    "AED": ("#00732f", "#ffffff", "د.إ"),  # Green
    "THB": ("#a51931", "#2d2a4a", "฿"),    # Red/Dark
    "IDR": ("#ff0000", "#ffffff", "Rp"),   # Red
    "MYR": ("#010066", "#ffcc00", "RM"),   # Blue/Yellow
    "PHP": ("#0038a8", "#ce1126", "₱"),    # Blue/Red
    "PLN": ("#dc143c", "#ffffff", "zł"),   # Crimson
    "CZK": ("#11457e", "#d7141a", "Kč"),   # Blue/Red
    "HUF": ("#436f4d", "#ce2939", "Ft"),   # Green/Red
    "ILS": ("#0038b8", "#ffffff", "₪"),    # Blue
    "CLP": ("#0039a6", "#d52b1e", "CL$"),  # Blue/Red
    "COP": ("#fcd116", "#003893", "CO$"),  # Yellow/Blue
    "ARS": ("#74acdf", "#f6b40e", "AR$"),  # Light blue/Yellow
    "EGP": ("#ce1126", "#000000", "E£"),   # Red/Black
    "SAR": ("#006c35", "#ffffff", "﷼"),    # Green
    "QAR": ("#86001c", "#ffffff", "﷼"),    # Maroon
    "KWD": ("#007a3d", "#ce1126", "KD"),   # Green/Red
    "BHD": ("#ce1126", "#ffffff", "BD"),   # Red
    "OMR": ("#db161b", "#ffffff", "﷼"),    # Red
    "JOD": ("#007a3d", "#ce1126", "JD"),   # Green/Red
    "LKR": ("#ffb300", "#8d153a", "₨"),    # Gold/Maroon
    "PKR": ("#01411c", "#ffffff", "₨"),    # Green
    "BDT": ("#006a4e", "#f42a41", "৳"),    # Green/Red
    "VND": ("#da251d", "#ffcd00", "₫"),    # Red/Yellow
    "NGN": ("#008751", "#ffffff", "₦"),    # Green
    "KES": ("#006600", "#bb0000", "KSh"),  # Green/Red
    "GHS": ("#006b3f", "#fcd116", "₵"),    # Green/Yellow
    "UAH": ("#005bbb", "#ffd500", "₴"),    # Blue/Yellow
    "RON": ("#002b7f", "#fcd116", "lei"),  # Blue/Yellow
    "BGN": ("#00966e", "#d62612", "лв"),   # Green/Red
    "HRK": ("#ff0000", "#171796", "kn"),   # Red/Blue
    "DKK": ("#c60c30", "#ffffff", "kr"),   # Red
    "ISK": ("#003897", "#dc1e35", "kr"),   # Blue/Red
}

def create_icon(filename, draw_func, size=ICON_SIZE):
    """Create an icon with the given drawing function."""
    img = Image.new("RGBA", size, BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    filepath = os.path.join(ASSETS_DIR, "assets", filename)
    img.save(filepath, "PNG")
    print(f"Created: {filepath}")

def create_currency_icon(code):
    """Create a currency icon with country colors and symbol."""
    colors = CURRENCY_COLORS.get(code, ("#666666", "#ffffff", code[:2]))
    primary, secondary, symbol = colors
    
    img = Image.new("RGBA", CURRENCY_ICON_SIZE, BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Circle background
    draw.ellipse([0, 0, CURRENCY_ICON_SIZE[0]-1, CURRENCY_ICON_SIZE[1]-1], fill=primary)
    
    # Symbol text
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), symbol, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (CURRENCY_ICON_SIZE[0] - text_w) // 2 - bbox[0]
    y = (CURRENCY_ICON_SIZE[1] - text_h) // 2 - bbox[1]
    
    draw.text((x, y), symbol, fill=secondary, font=font)
    
    filepath = os.path.join(ASSETS_DIR, "assets", f"currency_{code}.png")
    img.save(filepath, "PNG")
    return filepath

def draw_standard(draw):
    """Calculator icon - basic grid layout."""
    draw.rounded_rectangle([4, 4, 28, 28], radius=3, fill=(96, 205, 255, 255))
    for row in range(3):
        for col in range(3):
            x = 8 + col * 6
            y = 8 + row * 6
            draw.rounded_rectangle([x, y, x+4, y+4], radius=1, fill=(255, 255, 255, 255))

def draw_scientific(draw):
    """Scientific icon - flask/beaker."""
    draw.polygon([(16, 4), (10, 20), (10, 28), (22, 28), (22, 20)], fill=(96, 205, 255, 255))
    draw.rectangle([14, 4, 18, 12], fill=(96, 205, 255, 255))
    draw.rectangle([12, 22, 20, 26], fill=(255, 255, 255, 200))

def draw_programmer(draw):
    """Programmer icon - code brackets."""
    draw.line([(10, 8), (6, 16), (10, 24)], fill=(96, 205, 255, 255), width=2)
    draw.line([(22, 8), (26, 16), (22, 24)], fill=(96, 205, 255, 255), width=2)
    draw.line([(18, 6), (14, 26)], fill=(96, 205, 255, 255), width=2)

def draw_minimalist(draw):
    """Minimalist icon - simple lines."""
    for i in range(4):
        y = 10 + i * 4
        width = 20 - i * 2
        x = (32 - width) // 2
        draw.line([(x, y), (x + width, y)], fill=(96, 205, 255, 255), width=2)

def draw_modern(draw):
    """Modern icon - geometric shape."""
    points = [(16, 4), (26, 10), (26, 22), (16, 28), (6, 22), (6, 10)]
    draw.polygon(points, fill=(96, 205, 255, 255))
    draw.ellipse([12, 12, 20, 20], fill=(255, 255, 255, 255))

def draw_currency(draw):
    """Currency icon - dollar sign."""
    draw.ellipse([8, 8, 24, 24], fill=(96, 205, 255, 255))
    draw.arc([12, 10, 20, 16], 0, 180, fill=(255, 255, 255, 255), width=2)
    draw.arc([12, 16, 20, 22], 180, 360, fill=(255, 255, 255, 255), width=2)
    draw.line([(16, 10), (16, 22)], fill=(255, 255, 255, 255), width=2)

def draw_metric(draw):
    """Metric icon - ruler."""
    draw.rectangle([6, 10, 26, 22], fill=(96, 205, 255, 255))
    for i in range(5):
        x = 8 + i * 4
        draw.line([(x, 10), (x, 14)], fill=(255, 255, 255, 255), width=1)
    draw.polygon([(26, 12), (30, 16), (26, 20)], fill=(96, 205, 255, 255))

def draw_temperature(draw):
    """Temperature icon - thermometer."""
    draw.rounded_rectangle([12, 4, 20, 22], radius=4, fill=(96, 205, 255, 255))
    draw.ellipse([10, 20, 22, 30], fill=(96, 205, 255, 255))
    draw.rectangle([14, 12, 18, 24], fill=(255, 255, 255, 255))
    draw.ellipse([14, 22, 18, 26], fill=(255, 255, 255, 255))

def draw_memory_panel(draw):
    """Memory panel toggle icon - circle with M."""
    draw.ellipse([6, 6, 26, 26], fill=(96, 205, 255, 255))
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    except:
        font = ImageFont.load_default()
    draw.text((11, 8), "M", fill=(255, 255, 255, 255), font=font)

def draw_logo(draw):
    """Calculator logo - larger polished icon (64x64)."""
    # Outer rounded rectangle
    draw.rounded_rectangle([4, 4, 60, 60], radius=12, fill=(32, 32, 32, 255))
    # Inner accent border
    draw.rounded_rectangle([6, 6, 58, 58], radius=10, outline=(96, 205, 255, 255), width=2)
    # Display area
    draw.rounded_rectangle([12, 10, 52, 26], radius=4, fill=(96, 205, 255, 60))
    # Display text line
    draw.line([(18, 18), (46, 18)], fill=(96, 205, 255, 255), width=2)
    # Button grid
    for row in range(4):
        for col in range(4):
            x = 12 + col * 10
            y = 30 + row * 7
            draw.rounded_rectangle([x, y, x+7, y+5], radius=1, fill=(96, 205, 255, 200))

def main():
    """Generate all icons."""
    # Sidebar icons
    sidebar_icons = [
        ("icon_standard.png", draw_standard),
        ("icon_scientific.png", draw_scientific),
        ("icon_programmer.png", draw_programmer),
        ("icon_minimalist.png", draw_minimalist),
        ("icon_modern.png", draw_modern),
        ("icon_currency.png", draw_currency),
        ("icon_metric.png", draw_metric),
        ("icon_temperature.png", draw_temperature),
        ("icon_memory_panel.png", draw_memory_panel),
    ]

    print("Generating sidebar icons...")
    for filename, draw_func in sidebar_icons:
        try:
            create_icon(filename, draw_func)
        except Exception as e:
            print(f"Error creating {filename}: {e}")

    # Calculator logo (64x64)
    print("\nGenerating logo...")
    try:
        img = Image.new("RGBA", (64, 64), BG_COLOR)
        draw = ImageDraw.Draw(img)
        draw_logo(draw)
        filepath = os.path.join(ASSETS_DIR, "assets", "logo.png")
        img.save(filepath, "PNG")
        print(f"Created: {filepath}")
    except Exception as e:
        print(f"Error creating logo: {e}")
    
    # Currency icons
    print("\nGenerating currency icons...")
    currencies = [
        "USD", "EUR", "GBP", "JPY", "CNY", "AUD", "CAD", "CHF", "INR", "KRW",
        "MXN", "BRL", "SGD", "HKD", "NZD", "SEK", "NOK", "TRY", "RUB", "ZAR",
        "AMD", "AED", "THB", "IDR", "MYR", "PHP", "PLN", "CZK", "HUF", "ILS",
        "CLP", "COP", "ARS", "EGP", "SAR", "QAR", "KWD", "BHD", "OMR", "JOD",
        "LKR", "PKR", "BDT", "VND", "NGN", "KES", "GHS", "UAH", "RON", "BGN",
        "HRK", "DKK", "ISK",
    ]
    created = 0
    for code in currencies:
        try:
            filepath = create_currency_icon(code)
            print(f"Created: {filepath}")
            created += 1
        except Exception as e:
            print(f"Error creating {code}: {e}")
    
    print(f"\nAll icons generated successfully!")
    print(f"  Sidebar icons: {len(sidebar_icons)}")
    print(f"  Logo: logo.png (64x64)")
    print(f"  Currency icons: {created}")

if __name__ == "__main__":
    main()

