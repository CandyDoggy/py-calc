# Patch Notes

## Version 3.4.31 (April 3, 2026) - Web Parity & Desktop Bug Fix 🔧

### New Features
- **Web Version Memory Toggle Moved to Sidebar**:
  - Toggle button now at sidebar bottom (matching desktop app layout)
  - Same 160x32px button styling as desktop
  - SVG icon (circle with "M") preserved

### Bug Fixes
- 🐛 **Fixed desktop memory panel close bug** - Calculator/exchanger content no longer disappears when closing memory panel
  - Removed duplicate `_create_memory_toggle_button` call from `_create_content_area`
  - Toggle button now only exists in sidebar

### Documentation
- ⚠️ **Added web version disclaimer to README**: "Web version may have fewer features and could be slightly outdated"

---

## Version 3.4.3 (April 3, 2026) - Icon Overhaul & Memory Toggle 🎨

### New Features
- **Calculator Logo**: New polished 64x64 logo icon with calculator design
  - Dark background with accent blue border
  - Display area with button grid
  - Generated via `generate_icons.py`
- **Memory Panel Toggle Icon**: New `icon_memory_panel.png` 
  - Blue circle with "M" letter
  - Used in both desktop app and web version
- **Memory Toggle Button Redesigned** (Desktop):
  - Moved from floating position in content area to sidebar bottom
  - Now uses proper PNG icon instead of text "O"
  - Better visual integration with sidebar theme
  - 160x32px button matching sidebar style
- **Web Version Toggle**: SVG icon for memory panel toggle
  - Circle with "M" letter in SVG format
  - Better sizing (36x36px with 20x20px icon)

### Bug Fixes
- 🐛 **Fixed `_create_sidebar`** - Now returns sidebar widget for proper toggle placement
- 🐛 **Fixed memory toggle visibility** - Properly shown when memory panel is hidden
- 🐛 **Fixed icon loading** - Better error handling for missing icon files
- 🐛 **Fixed sidebar layout** - Toggle button now properly packed at sidebar bottom

### Technical Changes
- Added `draw_memory_panel()` function to `generate_icons.py`
- Added `draw_logo()` function to `generate_icons.py` (64x64 logo)
- Updated `_create_memory_toggle_button()` to load and use `icon_memory_panel.png`
- Moved memory toggle button to sidebar instead of floating in content area
- Added SVG memory icon for web version
- Updated `generate_icons.py` output to include logo count
- All icons regenerated via `venv/bin/python generate_icons.py`

---

## Version 3.4.2 (April 3, 2026) - Memory Panel & Bug Fixes 🧠

### New Features
- **Memory Panel (Web Version)**: Right sidebar with visual memory management
  - ✕ close button to hide panel, O button to show it
  - Clickable memory entries to recall values
  - Individual delete buttons (✕) for each entry
  - Clear All button at bottom
  - State persistence via localStorage

### Bug Fixes
- 🐛 **Fixed keyboard input** - Added `e.preventDefault()` to prevent browser shortcuts interfering with calculator
- 🐛 **Fixed expression display** - Expression now updates after calculation (= shows result in both expression and result fields)
- 🐛 **Fixed scientific mode** - `x²` button now uses `**2` instead of `^2`, `^` button uses `**`
- 🐛 **Fixed 1/x button** - Now properly wraps current expression: `1/(expr)`
- 🐛 **Fixed negate button** - Better handling of nested negations with parentheses
- 🐛 **Fixed memory actions** - MC/MR/M+/M-/MS now refresh the memory panel display
- 🐛 **Fixed math engine** - Replaced `^` with `**` for JavaScript exponentiation, proper constant substitution for π and e
- 🐛 **Fixed empty expression display** - Shows empty string instead of "0" in expression field

### Technical Changes
- Added memory panel HTML structure to `web/index.html`
- Added memory panel CSS styles to `web/styles.css`
- Rewrote memory handling in `web/app.js` with `refreshMemoryDisplay()`, `recallMemory()`, `deleteMemory()`, `clearAllMemory()`
- Added memory panel toggle: `showMemoryPanel()`, `hideMemoryPanel()`, `saveMemoryPanelState()`, `loadMemoryPanelState()`
- Updated keyboard event handler to prevent default for all calculator keys
- Improved math engine preprocessing in `web/math.js`

---

## Version 3.4.1 (April 3, 2026) - Web Version Release 🌐

### Major Release
- **Web Version Available**: Calculator now accessible online via GitHub Pages
  - URL: https://candydoggy.github.io/py-calc-cqwen/
  - No installation required - works directly in browser
  - Cross-platform by default (Windows, macOS, Linux, iOS, Android)

### New Features
- ✅ **All 7 Calculator Modes**: Standard, Scientific, Programmer, Minimalist, Currency, Metric/Imperial, Temperature
- ✅ **9 Themes**: Fluent Dark, Fluent Light, Midnight Blue, Forest Green, Sunset Orange, Royal Purple, Rose Gold, Arctic White, Cyber Yellow
- ✅ **Responsive Design**: Optimized for both desktop and mobile screens
- ✅ **Keyboard Support**: Direct keyboard input for standard calculator mode
- ✅ **Currency Converter**: 53 currencies with search and swap functionality
- ✅ **Metric/Imperial Converter**: 9 conversion types (Length, Weight, Volume, Speed, Area, Time, Data, Energy, Pressure)
- ✅ **Temperature Converter**: Celsius, Fahrenheit, Kelvin
- ✅ **LocalStorage Persistence**: Theme and memory settings saved in browser

### Technical Changes
- Created full HTML/CSS/JavaScript implementation
- Implemented JavaScript math engine with scientific functions
- Added GitHub Actions workflow for automatic deployment
- Configured GitHub Pages for hosting
- All currency data ported to web version
- All metric/imperial conversion factors ported

### File Structure
```
web/
├── index.html          # Main calculator interface
├── styles.css          # All 9 themes + responsive design
├── math.js             # JavaScript math engine
├── currencies.js       # Currency data (53 currencies)
├── converter.js        # Metric/Imperial + Temperature converters
├── app.js              # Main application logic
└── _config.yml         # GitHub Pages configuration
```

### Documentation Updates
- Updated README.md with web version link
- Added web version features and usage instructions
- Updated QWEN.md with deployment information

---

## Version 3.3.0 (April 3, 2026) - Visual Overhaul & Expanded Converters 🎨

### Visual Enhancements
- **Sidebar Icons**: Replaced emoji icons with custom PNG icons (8 tabs)
  - Standard, Scientific, Programmer, Minimalist, Modern, Currency, Metric, Temperature
  - Clean, Fluent Design-style icons generated via PIL/Pillow
- **Currency List Icons**: 53 colored currency flag icons with country-specific colors and symbols
  - Each icon uses national flag colors + currency symbol ($, €, £, ¥, ₹, etc.)
  - Improves visual recognition in the currency converter

### New Metric/Imperial Conversion Types (5 added, 9 total)
- **Area**: Sq Meters, Sq Kilometers, Hectares → Sq Feet, Sq Yards, Acres, Sq Miles
- **Time**: Seconds, Minutes, Hours, Days, Weeks, Milliseconds, Microseconds
- **Data**: Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits
- **Energy**: Joules, Kilojoules, Calories, Kilocalories, Watt-hours, Kilowatt-hours
- **Pressure**: Pascal, Kilopascal, Bar, Millibar, Atmosphere, Torr → PSI, KSI

### Existing Type Expansions
- **Length**: Added Micrometers, Nanometers, Nautical Miles
- **Weight**: Added Milligrams, Metric Tons, Stones, Short/Long Tons
- **Volume**: Added Cubic Meters, Cubic Centimeters, Quarts, Pints, Cups, Cubic Feet, Cubic Inches
- **Speed**: Added Meters/s, Feet/s, Knots

### Bug Fixes
- 🖱️ **Fixed currency list mouse wheel scrolling** (Windows + Linux support)
  - `<MouseWheel>` for Windows, `<Button-4>`/`<Button-5>` for Linux
  - Recursive binding to all child widgets for reliable scrolling

### Technical Changes
- Added `generate_icons.py` script for regenerating all icons
- Added Pillow (PIL) dependency for image handling
- Icon loading via `ctk.CTkImage` for proper light/dark mode support
- Currency icon caching for better performance
- Expanded conversion factors with scientific notation for extreme values

---

## Version 3.2.1 (April 3, 2026) - New Calculator Modes & 50+ Currencies 🧮

### New Calculator Modes
- **Programmer**: Hex/Dec/Oct/Bin conversion, bitwise operations (AND, OR, XOR, NOT, SHL)
- **Minimalist**: Clean, essentials-only layout
- **Modern**: Extra functions (x², √, trig, constants)
- Standard, Scientific, Currency (existing)

### Currencies
- 50+ world currencies including AMD (Armenian Dram ֏)

### Themes
- Fluent Dark, Fluent Light, Fluent Mica

---

## Version 3.2.0 (April 3, 2026) - Windows 11 Fluent Design & Currency Exchange 🪟

### Major Changes
- **Complete UI Redesign**: Windows 11 Fluent Design language throughout
- **Navigation Sidebar**: Switch between Standard, Scientific, and Currency modes
- **New Theme System**: Fluent Dark, Fluent Light, Fluent Mica themes

### New Features
- 💱 **Currency Exchanger**: Convert between 20 world currencies
  - USD, EUR, GBP, JPY, CNY, AUD, CAD, CHF, INR, KRW, and more
  - Real-time conversion with swap button
- 🧠 **Memory System**: M+, M-, MR, MC, MS buttons
  - Memory persists between sessions (saved to memory.json)
  - Visual "M" indicator when memory is active
- 📜 **Persistent History**: Calculations saved automatically to calculation_history.json
  - History loads on startup
  - Saved on every calculation and app close

### Theme Updates
| Theme | Description |
|-------|-------------|
| Fluent Dark | Windows 11 dark mode aesthetic |
| Fluent Light | Clean, bright Windows 11 light mode |
| Fluent Mica | Subtle, sophisticated mica material effect |

### Technical Changes
- Rewrote UI with sidebar navigation pattern
- Added currency conversion engine with 20 currencies
- Added memory persistence system
- Added history save/load functionality
- Updated button styling to Fluent Design standards

---

## Version 3.0.4.1 (April 3, 2026) - Calculator Logo & Icon 🎨

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

**Last Updated**: April 3, 2026
**Current Version**: 3.4.3
