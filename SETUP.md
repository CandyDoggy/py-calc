# Cross-Platform Setup Guide

This calculator works on **Windows**, **macOS**, and **Linux**.

🌐 **No Installation Needed**: Use the calculator online at **https://candydoggy.github.io/py-calc-cqwen/**

## Prerequisites

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))

---

## Quick Start

### Any OS (Recommended)
```bash
python launcher.py
```
This works on Windows, macOS, and Linux — no blocked files, no admin needed.

### Windows
1. Double-click `run.bat` — done!
2. Or manually:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python main.py
   ```

### macOS
1. Open Terminal in the project folder, then:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```
2. Or manually:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python3 main.py
   ```

### Linux
1. Open Terminal in the project folder, then:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```
2. Or manually:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python3 main.py
   ```

---

## Manual Installation

If you prefer to manage your own environment:

```bash
pip install customtkinter sympy numpy scipy
python main.py
```

---

## Troubleshooting

### "No module named 'customtkinter'"
Run: `pip install -r requirements.txt`

### "Python is not recognized" (Windows)
- Install Python from [python.org](https://www.python.org/downloads/)
- During install, check **"Add Python to PATH"**

### Permission denied (macOS/Linux)
Run: `chmod +x run.sh`

### venv creation fails
Make sure you have `python3-full` (Ubuntu/Debian):
```bash
sudo apt install python3-full python3-venv
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| customtkinter | Modern UI framework |
| sympy | Symbolic math engine |
| numpy | Numerical computing |
| scipy | Scientific computing |

---

## Platform Notes

- **Windows**: Native look with Fluent Design, Start Menu shortcut available
- **macOS**: Full support, Retina display compatible
- **Linux**: Works on all major distros (Ubuntu, Fedora, Arch, etc.)

---

## Features

- **Standard Mode**: Basic arithmetic with memory (MC, MR, M+, M-, MS)
- **Scientific Mode**: Trig, logs, constants, powers
- **Programmer Mode**: Hex/Dec/Oct/Bin conversion, bitwise operations
- **Minimalist Mode**: Clean, essentials-only interface
- **Currency Converter**: 53 world currencies with real-time conversion
- **Metric/Imperial Converter**: 9 conversion types (Length, Weight, Volume, Speed, Area, Time, Data, Energy, Pressure)
- **Temperature Converter**: Celsius, Fahrenheit, Kelvin
- **9 Themes**: Fluent Dark, Fluent Light, Midnight Blue, Forest Green, Sunset Orange, Royal Purple, Rose Gold, Arctic White, Cyber Yellow
- **Persistent History**: Auto-saved between sessions
- **Memory Persistence**: Saved values survive app restarts
