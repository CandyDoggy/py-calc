# How to Open Calculator

## Quick Start (Recommended)

Works on **Windows**, **macOS**, and **Linux**:

```bash
python launcher.py
```

This automatically sets up the virtual environment and installs dependencies if needed.

---

## First-Time Setup

### Step 1: Install Python

Download from: https://www.python.org/downloads/

- **Windows**: ✅ Check **"Add Python to PATH"** during install
- **macOS**: Use the installer or `brew install python3`
- **Linux**: `sudo apt install python3 python3-pip python3-venv`

### Step 2: Open the Calculator

#### Windows (App-like Experience)

**Option A: Install to Start Menu (Recommended)**
1. Double-click `install.bat`
2. Calculator now appears in your Start Menu
3. Launch from Start Menu — no CMD window!

**Option B: Double-click**
- Double-click `calculator.pyw` — runs without a CMD window

**Option C: Command Line**
```cmd
python launcher.py
```

#### macOS / Linux

```bash
python launcher.py
```

Or:
```bash
chmod +x run.sh
./run.sh
```

#### Manual Setup (Any OS)
```bash
cd calculator

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Enter numbers |
| `+ - * /` | Operators |
| `Enter` | Calculate |
| `Backspace` | Delete last character |
| `Escape` | Clear all |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python: command not found` | Install Python from python.org |
| `No module named 'customtkinter'` | Run `pip install -r requirements.txt` |
| `Permission denied` (macOS/Linux) | Run `chmod +x run.sh` first |
| Windows blocks `run.bat` | Use `python launcher.py` instead |

---

## Need Help?

- See [SETUP.md](SETUP.md) for detailed setup instructions
- See [README.md](README.md) for full documentation
- Report issues: https://github.com/CandyDoggy/py-calc-cqwen/issues
