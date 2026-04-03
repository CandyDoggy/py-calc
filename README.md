# Scientific Calculator

A modern, feature-rich calculator application built with **Python** and **PyQt6 Fluent Widgets**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.6+-green.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

![Scientific Calculator](https://via.placeholder.com/800x450/0a0e14/00d4ff?text=Scientific+Calculator+v3.0)

---

## ✨ Features

### 🎨 Multiple Beautiful Themes
| Theme | Description |
|-------|-------------|
| **Scientific** | Deep ocean blue with cyan accents |
| **Minimalistic** | Clean GitHub-inspired dark theme |
| **Programmer** | Purple cyberpunk aesthetic |
| **Modern** | Pure black with vibrant accents |
| **Frutiger Aero** | Glossy Windows Vista-era nostalgia |

### 🧮 Calculation Modes
- **Basic Operations**: Addition, subtraction, multiplication, division
- **Scientific Functions**: sin, cos, tan, asin, acos, atan, log, ln
- **Advanced Math**: Powers (x², xʸ), roots (√), percentages, negation
- **Constants**: π (pi), e (Euler's number)
- **Programmer Mode**: Hex, Oct, Bin conversion, bitwise operations (AND, OR, XOR, NOT)

### 💾 Data Management
- **Persistent History** - All calculations saved automatically
- **Export History** - Save calculations as text files
- **Settings Persistence** - Your theme preference is remembered

### 🎯 Modern UI/UX
- **Fluent Design** - Windows 11-style aesthetics
- **Smooth Animations** - Button hover/press effects
- **Card-based Layout** - Elevated cards with shadows
- **Responsive Layout** - Proper grid alignment for all buttons
- **High DPI Support** - Crisp display on all screens

---

## 📦 Installation

### Prerequisites

- **Python 3.8** or higher
- **pip** (Python package manager)
- **PyQt6** compatible system

### Install Dependencies

```bash
# Navigate to the calculator directory
cd calculator

# Activate virtual environment (recommended)
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements

```
PyQt6>=6.6.0
PyQt6-Fluent-Widgets>=1.5.0
sympy>=1.12
numpy>=1.24.0
scipy>=1.11.0
```

---

## 🚀 Usage

### Launch the Calculator

```bash
# Using virtual environment
venv/bin/python main.py

# Or after activating the venv
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
├── PLAN.md                # Development plan
├── PATCH_NOTES.md         # Version history
├── calculation_history.json  # Saved calculations
├── settings.json          # User settings
├── ui/
│   ├── __init__.py
│   └── calculator_ui.py   # PyQt6 UI components
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

**"No module named 'PyQt6'"**
```bash
pip install PyQt6 PyQt6-Fluent-Widgets
```

**"No module named 'sympy'"**
```bash
pip install -r requirements.txt
```

**Display issues on Linux**
```bash
# For Wayland users, try running with X11:
GDK_BACKEND=x11 venv/bin/python main.py
```

**High DPI display issues**
```bash
# The app has built-in high DPI support
# If issues persist, check your system display settings
```

---

## 📝 Version History

See [PATCH_NOTES.md](PATCH_NOTES.md) for detailed version history.

### Latest: v3.0.0 (2026)
- Complete UI rewrite with PyQt6
- Fluent Design language
- 5 beautiful themes including Frutiger Aero
- Smooth animations and transitions
- Enhanced button layouts

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

- **PyQt6** - Powerful Python GUI framework
- **PyQt6-Fluent-Widgets** - Beautiful Fluent Design components
- **SymPy** - Symbolic mathematics engine
- **NumPy** - Numerical computing
- **SciPy** - Scientific computing library

---

## 📧 Contact

For questions or support, please open an issue on the project repository.

---

**Built with ❤️ using Python and PyQt6**
