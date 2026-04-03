# Calculator

A modern, feature-rich calculator application built with **Python** and **CustomTkinter**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2+-green.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Version](https://img.shields.io/badge/v3.4.3-Icon%20Overhaul-60cdff)

🌐 **[Try it Online →](https://candydoggy.github.io/py-calc-cqwen/)**

---

## 🌐 Web Version

Access the calculator directly in your browser at: **https://candydoggy.github.io/py-calc-cqwen/**

The web version includes all features of the desktop app with no installation required:
- ✅ All 7 calculator modes
- ✅ 9 beautiful themes
- ✅ Responsive design for mobile and desktop
- ✅ Keyboard support
- ✅ Cross-platform compatibility

---

## ✨ Features

### 🎨 Windows 11 Fluent Design Themes
| Theme | Description |
|-------|-------------|
| **Fluent Dark** | Windows 11 dark mode aesthetic |
| **Fluent Light** | Clean, bright Windows 11 light mode |
| **Fluent Mica** | Subtle, sophisticated mica material effect |

### 🧮 Calculator Modes
- **Standard Mode**: Basic arithmetic (+, -, ×, ÷), percentages, sign toggle
- **Scientific Mode**: sin, cos, tan, log, ln, sqrt, powers, constants (π, e)
- **Programmer Mode**: Hex/Dec/Oct/Bin conversion, bitwise operations
- **Minimalist Mode**: Clean, essentials-only interface
- **Modern Mode**: Extra functions with contemporary design
- **Currency Converter**: 53 world currencies with custom flag icons
- **Metric/Imperial Converter**: 9 conversion types (Length, Weight, Volume, Speed, Area, Time, Data, Energy, Pressure)
- **Temperature Converter**: Celsius, Fahrenheit, Kelvin

### 🖼️ Custom Icons
- Clean, modern PNG icons for all sidebar tabs
- Currency-specific colored icons with national flag colors and symbols
- Icons generated via PIL/Pillow (rerunnable with `generate_icons.py`)

### 🧠 Memory System
- **MC** (Memory Clear), **MR** (Memory Recall), **M+** (Memory Add)
- **M-** (Memory Subtract), **MS** (Memory Store)
- Memory persists between sessions automatically

### 💾 Data Management
- **Persistent History** - All calculations saved automatically to JSON
- **History loads on startup** - Pick up where you left off
- **Memory Persistence** - Saved memory survives app restarts

### 🎯 Modern UI/UX
- **Navigation Sidebar** - Switch between modes seamlessly
- **Fluent Design** - Windows 11-style aesthetics
- **Responsive Layout** - Proper grid alignment for all buttons
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Mouse Wheel Scrolling** - Works in currency converter list

---

## 📦 Installation

### Prerequisites

- **Python 3.8** or higher
- **pip** (Python package manager)

### Quick Start

**Any OS (Recommended):**
```bash
python launcher.py
```

**Windows (alternative):** Double-click `run.bat`

**macOS / Linux (alternative):**
```bash
chmod +x run.sh
./run.sh
```

### Manual Install

```bash
# Navigate to the calculator directory
cd calculator

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements

```
customtkinter>=5.2.0
sympy>=1.12
numpy>=1.24.0
scipy>=1.11.0
```

---

## 🚀 Usage

### Launch the Calculator

```bash
python main.py
```

### Keyboard Support

| Key | Action |
|-----|--------|
| **Enter** | Calculate result (=) |
| **Backspace** | Delete last character (⌫) |
| **Escape** | Clear all (C) |
| **0-9** | Input numbers |
| **. ** | Decimal point |
| **+ - * /** | Basic operations |

---

## 🎨 Supported Operations

### Basic Arithmetic
| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | + | 5 + 3 = 8 |
| Subtraction | - | 10 - 4 = 6 |
| Multiplication | × | 7 × 6 = 42 |
| Division | ÷ | 20 ÷ 4 = 5 |

### Scientific Functions
| Function | Button | Example | Result |
|----------|--------|---------|--------|
| Sine | sin | sin(π/2) | 1.0 |
| Cosine | cos | cos(0) | 1.0 |
| Tangent | tan | tan(π/4) | 1.0 |
| Log (base 10) | log | log(100) | 2.0 |
| Natural Log | ln | ln(e) | 1.0 |
| Square Root | √ | sqrt(16) | 4.0 |
| Square | x² | 5² | 25 |
| Power | xʸ | 2ʸ3 | 8 |
| Reciprocal | 1/x | 1/4 | 0.25 |

### Constants
| Constant | Button | Value |
|----------|--------|-------|
| Pi | π | 3.14159... |
| Euler's Number | e | 2.71828... |

### Examples

| Expression | Result |
|------------|--------|
| `2 + 3 × 4` | 14 |
| `(5 + 3) × 2` | 16 |
| `sin(π/2)` | 1.0 |
| `sqrt(16) + 2²` | 8.0 |
| `log(1000) + ln(e²)` | 5.0 |
| `2^10` | 1024 |

---

## 📁 Project Structure

```
calculator/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── SETUP.md               # Cross-platform setup guide
├── PATCH_NOTES.md         # Version history
├── run.bat                # Windows launcher
├── run.sh                 # macOS/Linux launcher
├── calculation_history.json  # Saved calculations
├── settings.json          # User settings
├── ui/
│   ├── __init__.py
│   └── calculator_ui.py   # CustomTkinter UI components
├── math_engine/
│   ├── __init__.py
│   └── calculator.py      # Math logic (SymPy)
└── venv/                  # Virtual environment
```

---

## 🖼️ Themes

### Scientific (Default)
- Deep ocean blue background
- Cyan operator buttons
- Lime green scientific functions
- Perfect for complex calculations

### Minimalistic
- Clean GitHub dark theme
- Subtle orange accents
- Reduced visual clutter
- Focus on essentials

### Programmer
- Dark purple/cyberpunk aesthetic
- Hexadecimal support
- Bitwise operations
- Base conversion (Hex/Dec/Oct/Bin)

### Modern
- Pure black OLED-friendly
- Purple and teal accents
- Streamlined layout
- Contemporary design

### Frutiger Aero
- Glossy blue gradient (Windows Vista style)
- Vibrant lime green buttons
- Orange action buttons
- Nostalgic 2000s aesthetic

---

## 🔧 Troubleshooting

### Common Issues

**"No module named 'customtkinter'"**
```bash
pip install -r requirements.txt
```

**"No module named 'sympy'"**
```bash
pip install -r requirements.txt
```

**Python not found (Windows)**
- Install Python from [python.org](https://www.python.org/downloads/)
- During install, check **"Add Python to PATH"**

**Permission denied (macOS/Linux)**
```bash
chmod +x run.sh
./run.sh
```

---

## 📝 Version History

See [PATCH_NOTES.md](PATCH_NOTES.md) for detailed version history.

### Latest: v3.4.3 (2026) - Icon Overhaul & Memory Toggle
- 🎨 New calculator logo (64x64 polished icon)
- Memory panel toggle icon with "M" circle design
- Moved memory toggle to sidebar bottom (instead of floating)
- SVG icon for web version memory toggle
- Fixed sidebar layout and icon loading
- 4 bug fixes total

### v3.4.2 (2026) - Memory Panel & Bug Fixes
- 🧠 Memory panel with right sidebar (✕ to close, O to open)
- Clickable memory entries with individual delete buttons
- Fixed keyboard input preventing browser shortcuts
- Fixed expression display and scientific mode calculations
- Fixed math engine for JavaScript exponentiation
- 8 bug fixes total

### v3.4.1 (2026) - Web Version Release
- 🌐 Full web version available at https://candydoggy.github.io/py-calc-cqwen/
- All 7 calculator modes: Standard, Scientific, Programmer, Minimalist, Currency, Metric/Imperial, Temperature
- 9 beautiful themes with localStorage persistence
- Responsive design for mobile and desktop
- 53 currencies with search functionality
- 9 metric/imperial conversion types
- Temperature converter (Celsius, Fahrenheit, Kelvin)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. **Report bugs** - Open an issue with details
2. **Suggest features** - Share your ideas
3. **Submit PRs** - Help improve the codebase

### Development Setup

```bash
# Clone the repository
git clone <repository-url>
cd calculator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

## 📄 License

This project is licensed under the **MIT License**.

```
Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## 🙏 Acknowledgments

- **CustomTkinter** - Modern cross-platform UI framework
- **SymPy** - Symbolic mathematics engine
- **NumPy** - Numerical computing
- **SciPy** - Scientific computing library

---

## 📧 Contact

For questions or support, please open an issue on the project repository.

---

**Built with ❤️ using Python and CustomTkinter**
