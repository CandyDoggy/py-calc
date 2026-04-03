# Patch Notes

## Version 3.0.1 (April 3, 2026) - Bug Fix Release 🔧

### Bug Fixes
- Fixed `AttributeError: 'Calculator' object has no attribute 'calculate'`
  - Changed UI `_calculate()` method to call `calculator.evaluate()` instead of `calculator.calculate()`
  - Method name mismatch between UI layer and math engine

---

## Version 3.0.0 (April 2026) - PyQt6 Revolution 🎉

### Major Changes
- **Complete UI Engine Rewrite**: Migrated from CustomTkinter to **PyQt6** with **Fluent Widgets**
- **Fluent Design Language**: Modern Windows 11-style aesthetics throughout the application
- **Enhanced Button Layouts**: Proper QGridLayout implementation for perfect alignment in all themes

### New Features
- ✨ **Smooth Animations**: Button hover/press effects with QEasingCurve animations
- 🎨 **5 Beautiful Themes**: All themes redesigned with Fluent Design principles
- 🃏 **Card-based UI**: Elevated cards with drop shadows for display and buttons
- 📜 **Fluent History Dialog**: Modern scrollable history with card items
- ⚙️ **Fluent Settings Dialog**: Theme selection with toggle buttons
- 🖥️ **High DPI Support**: Crisp display on all screen resolutions

### Theme Updates
| Theme | Changes |
|-------|---------|
| Scientific | New deep ocean blue with cyan Fluent accents |
| Minimalistic | GitHub-inspired dark with refined colors |
| Programmer | Enhanced cyberpunk purple aesthetic |
| Modern | Pure black OLED-friendly with vibrant accents |
| Frutiger Aero | Glossy Windows Vista nostalgia with Fluent touch |

### Technical Changes
- Replaced CustomTkinter with PyQt6 + PyQt6-Fluent-Widgets
- Implemented custom `AnimatedButton` class with press animations
- Added `DisplayWidget` component for expression/result display
- Refactored to use MSFluentWindow as base class
- Added proper layout management with QGridLayout

### Bug Fixes
- Fixed button alignment issues in all themes
- Improved theme switching performance
- Enhanced history dialog scrolling

---

## Version 2.1.0 (April 2026) - Frutiger Aero Update 🌊

### New Features
- 🎨 **Frutiger Aero Theme**: Glossy, vibrant Windows Vista-era aesthetic
  - Blue gradient background (#006994 → #0087C1)
  - Lime green scientific buttons (#88dd00)
  - Orange action buttons (#ff8800)
  - Characteristic Aero-era rounded corners

### Settings Menu
- ⚙️ **New Settings Dialog**: Theme selection interface
  - Select any of 5 themes
  - About section with app info
  - Theme preference saved to settings.json

### Improvements
- Added settings persistence (theme saved between sessions)
- Enhanced history window with modern design
- Added export button to history dialog

### Technical Changes
- Added `_show_settings()` method
- Added `_load_settings()` and `_save_settings()` methods
- Updated button layout for Frutiger Aero theme

---

## Version 2.0.0 (April 2026) - Modern UI & Persistent History 💾

### Major Changes
- **Modernized All Themes**: Enhanced color palettes and visual polish
- **Persistent History**: Calculations now saved to JSON file
- **Auto-save**: History saved on every calculation and app close

### New Features
- 📜 **Enhanced History Window**
  - Scrollable list of all calculations
  - Numbered entries with expression and result
  - Clear History button
  - Export to .txt file option
  
- 🎨 **Theme Improvements**
  - Larger, cleaner fonts
  - Improved corner radius for smoother buttons
  - Better spacing and padding
  - Hover color transitions for all buttons
  - Enhanced display with larger result text (48px)

### Theme Color Updates
| Theme | Primary Color | Changes |
|-------|---------------|---------|
| Minimalistic | #58a6ff | GitHub dark theme inspired |
| Scientific | #00d4ff | Deep ocean with cyan accents |
| Programmer | #7c3aed | Purple cyberpunk aesthetic |
| Modern | #a855f7 | Pure black with purple/teal |

### Technical Changes
- Added `_save_history()` method with JSON storage
- Added `_load_history()` method for session restoration
- Added `_export_history()` for text file export
- Updated `_calculate()` to auto-save after each calculation
- Added window close handler for data persistence

### Bug Fixes
- Fixed history not persisting between sessions
- Improved button hover color calculations
- Enhanced error handling in history operations

---

## Version 1.1.0 (April 2026) - UI Polish 🔧

### Improvements
- Updated all theme color schemes
- Enhanced button hover effects
- Improved display contrast
- Better spacing in mode selector

### Bug Fixes
- Fixed button alignment in Scientific mode
- Corrected color calculations for hover states

---

## Version 1.0.0 (April 2026) - Initial Release 🎉

### Features
- **4 Calculator Modes**:
  - Minimalistic: Simple, clean interface
  - Scientific: Full scientific functions
  - Programmer: Hex/Dec/Oct/Bin conversion
  - Modern: Contemporary design

- **Math Engine**:
  - Basic arithmetic (+, -, ×, ÷)
  - Scientific functions (sin, cos, tan, log, ln, sqrt, exp)
  - Constants (π, e)
  - Powers and roots

- **UI Features**:
  - CustomTkinter-based interface
  - Dark theme
  - Mode switching
  - Calculation history (session-only)
  - Keyboard support

- **Programmer Mode**:
  - Base conversion (Hex, Dec, Oct, Bin)
  - Bitwise operations (AND, OR, XOR, NOT)
  - Hexadecimal input (A-F)

### Technical Stack
- Python 3.8+
- CustomTkinter 5.2.0
- SymPy 1.12
- NumPy 1.24.0
- SciPy 1.11.0

### Known Issues
- History not persisted between sessions
- Some button hover colors inconsistent
- Layout could be improved

---

## Versioning Scheme

This project follows **Semantic Versioning** (SemVer):
- **MAJOR.MINOR.PATCH**
- **MAJOR**: Breaking changes or major rewrites (e.g., UI engine change)
- **MINOR**: New features, backward-compatible
- **PATCH**: Bug fixes and minor improvements

---

## Upgrade Guide

### From v2.x to v3.0.0
```bash
# Install new dependencies
pip install PyQt6 PyQt6-Fluent-Widgets

# Your settings and history are preserved
# They will be automatically loaded in v3.0.0
```

### From v1.x to v2.x
```bash
# No additional dependencies needed
# Just update the UI file
```

---

## Reporting Issues

Found a bug? Please include:
- Version number
- Operating system
- Steps to reproduce
- Expected vs actual behavior

---

**Last Updated**: April 2026
**Current Version**: 3.0.0
