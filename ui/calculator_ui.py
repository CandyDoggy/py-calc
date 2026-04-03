"""
Calculator UI with Windows 11 Fluent Design Style
Features: Navigation sidebar, Currency Exchanger, Memory system, Persistent history
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime
from math_engine.calculator import Calculator, CalculatorError


# Windows 11 Fluent Design Themes
THEMES = {
    "fluent_dark": {
        "name": "Fluent Dark",
        "bg_color": "#202020",
        "sidebar_bg": "#1a1a1a",
        "card_bg": "#2d2d2d",
        "button_bg": "#3b3b3b",
        "button_hover": "#4a4a4a",
        "accent_color": "#60cdff",
        "accent_hover": "#7dd5ff",
        "text_color": "#ffffff",
        "text_secondary": "#a0a0a0",
        "border_color": "#404040",
    },
    "fluent_light": {
        "name": "Fluent Light",
        "bg_color": "#f3f3f3",
        "sidebar_bg": "#e8e8e8",
        "card_bg": "#ffffff",
        "button_bg": "#f6f6f6",
        "button_hover": "#e9e9e9",
        "accent_color": "#0078d4",
        "accent_hover": "#106ebe",
        "text_color": "#1a1a1a",
        "text_secondary": "#666666",
        "border_color": "#e0e0e0",
    },
    "fluent_mica": {
        "name": "Fluent Mica",
        "bg_color": "#2c2c2c",
        "sidebar_bg": "#252525",
        "card_bg": "#353535",
        "button_bg": "#454545",
        "button_hover": "#505050",
        "accent_color": "#76b9ed",
        "accent_hover": "#8cc4f0",
        "text_color": "#ffffff",
        "text_secondary": "#b0b0b0",
        "border_color": "#505050",
    },
}

# Currency exchange rates (base: USD)
CURRENCY_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "CNY": 7.24,
    "AUD": 1.53,
    "CAD": 1.36,
    "CHF": 0.88,
    "INR": 83.12,
    "KRW": 1325.0,
    "MXN": 17.15,
    "BRL": 4.97,
    "SGD": 1.34,
    "HKD": 7.82,
    "NZD": 1.64,
    "SEK": 10.45,
    "NOK": 10.62,
    "TRY": 30.25,
    "RUB": 92.50,
    "ZAR": 18.95,
    "AMD": 403.50,  # Armenian Dram
    "DRAM": 403.50,  # Armenian Dram (alias)
    "AED": 3.67,    # UAE Dirham
    "THB": 35.20,   # Thai Baht
    "IDR": 15650.0, # Indonesian Rupiah
    "MYR": 4.72,    # Malaysian Ringgit
    "PHP": 55.80,   # Philippine Peso
    "PLN": 4.02,    # Polish Zloty
    "CZK": 22.85,   # Czech Koruna
    "HUF": 355.0,   # Hungarian Forint
    "ILS": 3.65,    # Israeli Shekel
    "CLP": 890.0,   # Chilean Peso
    "COP": 3950.0,  # Colombian Peso
    "ARS": 350.0,   # Argentine Peso
    "EGP": 30.90,   # Egyptian Pound
    "SAR": 3.75,    # Saudi Riyal
    "QAR": 3.64,    # Qatari Riyal
    "KWD": 0.31,    # Kuwaiti Dinar
    "BHD": 0.38,    # Bahraini Dinar
    "OMR": 0.38,    # Omani Rial
    "JOD": 0.71,    # Jordanian Dinar
    "LKR": 325.0,   # Sri Lankan Rupee
    "PKR": 278.0,   # Pakistani Rupee
    "BDT": 109.50,  # Bangladeshi Taka
    "VND": 24350.0, # Vietnamese Dong
    "NGN": 770.0,   # Nigerian Naira
    "KES": 155.0,   # Kenyan Shilling
    "GHS": 12.05,   # Ghanaian Cedi
    "UAH": 36.80,   # Ukrainian Hryvnia
    "RON": 4.57,    # Romanian Leu
    "BGN": 1.80,    # Bulgarian Lev
    "HRK": 6.93,    # Croatian Kuna
    "DKK": 6.87,    # Danish Krone
    "ISK": 137.50,  # Icelandic Krona
}

CURRENCY_SYMBOLS = {
    "USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "CNY": "¥",
    "AUD": "A$", "CAD": "C$", "CHF": "Fr", "INR": "₹", "KRW": "₩",
    "MXN": "MX$", "BRL": "R$", "SGD": "S$", "HKD": "HK$", "NZD": "NZ$",
    "SEK": "kr", "NOK": "kr", "TRY": "₺", "RUB": "₽", "ZAR": "R",
    "AMD": "֏", "DRAM": "֏", "AED": "د.إ", "THB": "฿", "IDR": "Rp", "MYR": "RM",
    "PHP": "₱", "PLN": "zł", "CZK": "Kč", "HUF": "Ft", "ILS": "₪",
    "CLP": "CL$", "COP": "CO$", "ARS": "AR$", "EGP": "E£", "SAR": "﷼",
    "QAR": "﷼", "KWD": "KD", "BHD": "BD", "OMR": "﷼", "JOD": "JD",
    "LKR": "₨", "PKR": "₨", "BDT": "৳", "VND": "₫", "NGN": "₦",
    "KES": "KSh", "GHS": "₵", "UAH": "₴", "RON": "lei", "BGN": "лв",
    "HRK": "kn", "DKK": "kr", "ISK": "kr",
}

# Currency names for display
CURRENCY_NAMES = {
    "USD": "US Dollar", "EUR": "Euro", "GBP": "British Pound", "JPY": "Japanese Yen",
    "CNY": "Chinese Yuan", "AUD": "Australian Dollar", "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc", "INR": "Indian Rupee", "KRW": "South Korean Won",
    "MXN": "Mexican Peso", "BRL": "Brazilian Real", "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar", "NZD": "New Zealand Dollar", "SEK": "Swedish Krona",
    "NOK": "Norwegian Krone", "TRY": "Turkish Lira", "RUB": "Russian Ruble",
    "ZAR": "South African Rand", "AMD": "Armenian Dram", "DRAM": "Armenian Dram",
    "AED": "UAE Dirham", "THB": "Thai Baht", "IDR": "Indonesian Rupiah",
    "MYR": "Malaysian Ringgit", "PHP": "Philippine Peso", "PLN": "Polish Zloty",
    "CZK": "Czech Koruna", "HUF": "Hungarian Forint", "ILS": "Israeli Shekel",
    "CLP": "Chilean Peso", "COP": "Colombian Peso", "ARS": "Argentine Peso",
    "EGP": "Egyptian Pound", "SAR": "Saudi Riyal", "QAR": "Qatari Riyal",
    "KWD": "Kuwaiti Dinar", "BHD": "Bahraini Dinar", "OMR": "Omani Rial",
    "JOD": "Jordanian Dinar", "LKR": "Sri Lankan Rupee", "PKR": "Pakistani Rupee",
    "BDT": "Bangladeshi Taka", "VND": "Vietnamese Dong", "NGN": "Nigerian Naira",
    "KES": "Kenyan Shilling", "GHS": "Ghanaian Cedi", "UAH": "Ukrainian Hryvnia",
    "RON": "Romanian Leu", "BGN": "Bulgarian Lev", "HRK": "Croatian Kuna",
    "DKK": "Danish Krone", "ISK": "Icelandic Krona",
}


class CalculatorUI(ctk.CTk):
    """Main Calculator Application with Windows 11 Fluent Design."""

    def __init__(self):
        super().__init__()

        self.calculator = Calculator()
        self.current_theme = "fluent_dark"
        self.current_mode = "standard"  # standard, scientific, currency
        self.current_expression = ""
        self.current_result = "0"
        self.memory_list = []  # List of saved memory values
        self.selected_memory_index = -1  # Currently selected memory entry

        # File paths
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.history_file = os.path.join(self.base_dir, "calculation_history.json")
        self.memory_file = os.path.join(self.base_dir, "memory.json")

        # Load saved data
        self._load_history()
        self._load_memory()

        # Configure window
        self.title("Calculator")
        self.geometry("1100x600")
        self.minsize(800, 500)

        # Apply theme
        self._apply_theme()

        # Setup UI
        self._setup_ui()

        # Bind keyboard events
        self._bind_keys()

    def _apply_theme(self):
        """Apply current theme."""
        theme = THEMES[self.current_theme]
        ctk.set_appearance_mode("dark" if "dark" in self.current_theme or "mica" in self.current_theme else "light")
        ctk.set_default_color_theme("blue")

    def _setup_ui(self):
        """Setup the main UI components."""
        # Clear existing widgets
        for widget in self.winfo_children():
            widget.destroy()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Main container
        main_frame = ctk.CTkFrame(self, fg_color=THEMES[self.current_theme]["bg_color"])
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        # Sidebar
        self._create_sidebar(main_frame)

        # Content area
        self._create_content_area(main_frame)

        # Memory panel (right side)
        self._create_memory_panel(main_frame)

    def _create_sidebar(self, parent):
        """Create Windows 11-style navigation sidebar."""
        theme = THEMES[self.current_theme]

        sidebar = ctk.CTkFrame(parent, width=200, fg_color=theme["sidebar_bg"])
        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_propagate(False)

        # App title
        title = ctk.CTkLabel(
            sidebar, text="Calculator",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=theme["text_color"]
        )
        title.pack(pady=(30, 10), padx=20, anchor="w")

        # Separator
        sep = ctk.CTkFrame(sidebar, height=1, fg_color=theme["border_color"])
        sep.pack(fill="x", padx=20, pady=10)

        # Navigation buttons
        self.nav_buttons = {}
        nav_items = [
            ("standard", "🔢", "Standard"),
            ("scientific", "🔬", "Scientific"),
            ("programmer", "💻", "Programmer"),
            ("minimalist", "✨", "Minimalist"),
            ("modern", "🎨", "Modern"),
            ("currency", "💱", "Currency"),
            ("metric", "📏", "Metric/Imperial"),
            ("temperature", "🌡️", "Temperature"),
        ]

        for mode, icon, label in nav_items:
            btn = self._create_nav_button(sidebar, icon, label, mode)
            btn.pack(fill="x", padx=12, pady=2)
            self.nav_buttons[mode] = btn

        # Theme selector at bottom
        sep2 = ctk.CTkFrame(sidebar, height=1, fg_color=theme["border_color"])
        sep2.pack(fill="x", padx=20, pady=(20, 10))

        theme_label = ctk.CTkLabel(
            sidebar, text="Theme:",
            font=ctk.CTkFont(size=12),
            text_color=theme["text_secondary"]
        )
        theme_label.pack(padx=20, anchor="w")

        theme_names = [THEMES[k]["name"] for k in THEMES.keys()]
        self.theme_var = ctk.StringVar(value=THEMES[self.current_theme]["name"])
        self.theme_combo = ctk.CTkComboBox(
            sidebar,
            values=theme_names,
            variable=self.theme_var,
            command=self._on_theme_changed,
            width=160,
            height=32
        )
        self.theme_combo.pack(padx=20, pady=(5, 10))

        # Highlight current mode
        self._update_nav_selection()

    def _create_nav_button(self, parent, icon, label, mode):
        """Create a navigation button for the sidebar."""
        theme = THEMES[self.current_theme]
        is_selected = mode == self.current_mode

        btn = ctk.CTkButton(
            parent,
            text=f"{icon}  {label}",
            font=ctk.CTkFont(size=14),
            fg_color=theme["accent_color"] if is_selected else "transparent",
            hover_color=theme["button_hover"],
            text_color=theme["text_color"],
            anchor="w",
            height=40,
            corner_radius=8,
            command=lambda m=mode: self._switch_mode(m)
        )
        return btn

    def _update_nav_selection(self):
        """Update navigation button styles."""
        theme = THEMES[self.current_theme]
        for mode, btn in self.nav_buttons.items():
            if mode == self.current_mode:
                btn.configure(fg_color=theme["accent_color"])
            else:
                btn.configure(fg_color="transparent")

    def _switch_mode(self, mode):
        """Switch calculator mode."""
        self.current_mode = mode
        self.current_expression = ""
        self.current_result = "0"
        self._update_nav_selection()
        self._create_content_area()

    def _create_memory_panel(self, parent):
        """Create memory panel on the right side."""
        theme = THEMES[self.current_theme]

        panel = ctk.CTkFrame(parent, width=220, fg_color=theme["sidebar_bg"])
        panel.grid(row=0, column=2, sticky="ns")
        panel.grid_propagate(False)

        # Title
        title = ctk.CTkLabel(
            panel, text="Memory",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=theme["text_color"]
        )
        title.pack(pady=(20, 10))

        # Separator
        sep = ctk.CTkFrame(panel, height=1, fg_color=theme["border_color"])
        sep.pack(fill="x", padx=15, pady=5)

        # Memory list container
        self.memory_list_frame = ctk.CTkScrollableFrame(
            panel,
            fg_color=theme["sidebar_bg"],
            label_text=""
        )
        self.memory_list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.memory_list_frame.grid_columnconfigure(0, weight=1)

        # Clear all button
        clear_btn = ctk.CTkButton(
            panel,
            text="Clear All",
            font=ctk.CTkFont(size=13),
            fg_color="transparent",
            hover_color=theme["button_hover"],
            text_color=theme["text_secondary"],
            height=32,
            corner_radius=6,
            command=self._clear_all_memory
        )
        clear_btn.pack(pady=(5, 15), padx=15, fill="x")

        # Refresh memory display
        self._refresh_memory_display()

    def _refresh_memory_display(self):
        """Refresh the memory list display."""
        theme = THEMES[self.current_theme]

        # Clear existing
        for widget in self.memory_list_frame.winfo_children():
            widget.destroy()

        if not self.memory_list:
            empty_label = ctk.CTkLabel(
                self.memory_list_frame,
                text="No saved values\n\nUse MS to save\nthe current value",
                font=ctk.CTkFont(size=12),
                text_color=theme["text_secondary"]
            )
            empty_label.pack(pady=40)
            return

        for i, val in enumerate(self.memory_list):
            # Format value nicely
            if val == int(val):
                display_val = str(int(val))
            else:
                display_val = f"{val:g}"

            row_frame = ctk.CTkFrame(self.memory_list_frame, fg_color="transparent")
            row_frame.grid(row=i, column=0, sticky="ew", pady=2)
            row_frame.grid_columnconfigure(0, weight=1)

            # Index label
            idx_label = ctk.CTkLabel(
                row_frame, text=f"M{i+1}",
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=theme["accent_color"],
                width=25,
                anchor="w"
            )
            idx_label.grid(row=0, column=0, padx=(5, 5))

            # Value label
            val_label = ctk.CTkLabel(
                row_frame, text=display_val,
                font=ctk.CTkFont(size=14),
                text_color=theme["text_color"],
                anchor="e"
            )
            val_label.grid(row=0, column=1, sticky="e", padx=5)

            # Delete button
            del_btn = ctk.CTkButton(
                row_frame,
                text="✕",
                font=ctk.CTkFont(size=12),
                fg_color="transparent",
                hover_color="#ff4444",
                text_color=theme["text_secondary"],
                width=24,
                height=24,
                corner_radius=4,
                command=lambda idx=i: self._delete_memory(idx)
            )
            del_btn.grid(row=0, column=2, padx=(5, 5))

            # Make clickable (except delete button)
            for widget in row_frame.winfo_children():
                if widget != del_btn:
                    widget.bind("<Button-1>", lambda e, idx=i: self._recall_memory(idx))
            row_frame.bind("<Button-1>", lambda e, idx=i: self._recall_memory(idx))

            # Hover effect
            def on_enter(e, f=row_frame, bg=theme["button_bg"]):
                f.configure(fg_color=bg)
            def on_leave(e, f=row_frame):
                f.configure(fg_color="transparent")

            row_frame.bind("<Enter>", on_enter)
            row_frame.bind("<Leave>", on_leave)
            for widget in row_frame.winfo_children():
                if widget != del_btn:
                    widget.bind("<Enter>", on_enter)
                    widget.bind("<Leave>", on_leave)

    def _clear_all_memory(self):
        """Clear all memory entries."""
        self.memory_list = []
        self.selected_memory_index = -1
        self._save_memory()
        self._refresh_memory_display()

    def _delete_memory(self, index):
        """Delete a specific memory entry."""
        if 0 <= index < len(self.memory_list):
            self.memory_list.pop(index)
            if self.selected_memory_index >= len(self.memory_list):
                self.selected_memory_index = len(self.memory_list) - 1
            self._save_memory()
            self._refresh_memory_display()

    def _recall_memory(self, index):
        """Recall a memory value by index."""
        if 0 <= index < len(self.memory_list):
            val = self.memory_list[index]
            self.selected_memory_index = index
            self.current_expression = ""
            if val == int(val):
                self.current_result = str(int(val))
            else:
                self.current_result = f"{val:g}"
            self._update_display()

    def _create_content_area(self, parent=None):
        """Create the main content area based on current mode."""
        if parent is None:
            parent = self.grid_slaves(row=0, column=0)[0]

        # Remove old content
        for widget in parent.grid_slaves(row=0, column=1):
            widget.destroy()

        content = ctk.CTkFrame(parent, fg_color=THEMES[self.current_theme]["bg_color"])
        content.grid(row=0, column=1, sticky="nsew")
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(0, weight=1)

        if self.current_mode == "standard":
            self._create_standard_view(content)
        elif self.current_mode == "scientific":
            self._create_scientific_view(content)
        elif self.current_mode == "programmer":
            self._create_programmer_view(content)
        elif self.current_mode == "minimalist":
            self._create_minimalist_view(content)
        elif self.current_mode == "modern":
            self._create_modern_view(content)
        elif self.current_mode == "currency":
            self._create_currency_view(content)
        elif self.current_mode == "metric":
            self._create_metric_view(content)
        elif self.current_mode == "temperature":
            self._create_temperature_view(content)

    def _create_standard_view(self, parent):
        """Create standard calculator view."""
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=3)

        # Display
        self._create_display(parent, row=0)

        # Buttons
        buttons_frame = ctk.CTkFrame(parent, fg_color=THEMES[self.current_theme]["bg_color"])
        buttons_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        buttons_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        for i in range(7):
            buttons_frame.grid_rowconfigure(i, weight=1)

        # Memory row
        self._create_memory_buttons(buttons_frame, row=0)

        # Standard layout
        buttons_config = [
            [("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("÷", 1, 3)],
            [("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3)],
            [("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3)],
            [("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3)],
            [("±", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)],
        ]

        for row_data in buttons_config:
            for text, row, col in row_data:
                self._create_fluent_button(buttons_frame, text, row, col)

    def _create_scientific_view(self, parent):
        """Create scientific calculator view."""
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=3)

        # Display
        self._create_display(parent, row=0)

        # Buttons
        buttons_frame = ctk.CTkFrame(parent, fg_color=THEMES[self.current_theme]["bg_color"])
        buttons_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        for i in range(5):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(9):
            buttons_frame.grid_rowconfigure(i, weight=1)

        # Memory row
        self._create_memory_buttons(buttons_frame, row=0)

        # Scientific layout
        buttons_config = [
            [("sin", 2, 0), ("cos", 2, 1), ("tan", 2, 2), ("log", 2, 3), ("ln", 2, 4)],
            [("asin", 3, 0), ("acos", 3, 1), ("atan", 3, 2), ("√", 3, 3), ("x²", 3, 4)],
            [("π", 4, 0), ("e", 4, 1), ("(", 4, 2), (")", 4, 3), ("^", 4, 4)],
            [("C", 5, 0), ("⌫", 5, 1), ("%", 5, 2), ("÷", 5, 3), ("×", 5, 4)],
            [("7", 6, 0), ("8", 6, 1), ("9", 6, 2), ("-", 6, 3), ("+", 6, 4)],
            [("4", 7, 0), ("5", 7, 1), ("6", 7, 2), ("1/x", 7, 3), ("=", 7, 4)],
            [("1", 8, 0), ("2", 8, 1), ("3", 8, 2), ("exp", 8, 3)],
            [("0", 9, 0), (".", 9, 1), ("±", 9, 2)],
        ]

        for row_data in buttons_config:
            for text, row, col in row_data:
                self._create_fluent_button(buttons_frame, text, row, col)

    def _create_memory_buttons(self, parent, row):
        """Create memory function buttons."""
        theme = THEMES[self.current_theme]
        memory_btns = ["MC", "MR", "M+", "M-", "MS"]
        for i, text in enumerate(memory_btns):
            btn = ctk.CTkButton(
                parent,
                text=text,
                font=ctk.CTkFont(size=12),
                fg_color="transparent",
                hover_color=theme["button_hover"],
                text_color=theme["text_secondary"],
                height=28,
                corner_radius=4,
                command=lambda t=text: self._memory_action(t)
            )
            btn.grid(row=row, column=i, sticky="nsew", padx=2, pady=2)

    def _create_display(self, parent, row):
        """Create the display area."""
        theme = THEMES[self.current_theme]
        display_frame = ctk.CTkFrame(parent, height=150, fg_color=theme["card_bg"])
        display_frame.grid(row=row, column=0, sticky="ew", padx=20, pady=(20, 10))
        display_frame.grid_propagate(False)
        display_frame.grid_columnconfigure(0, weight=1)

        # Expression label
        self.expr_label = ctk.CTkLabel(
            display_frame,
            text="",
            font=ctk.CTkFont(size=18),
            text_color=theme["text_secondary"],
            anchor="e"
        )
        self.expr_label.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 5))

        # Result label
        self.result_label = ctk.CTkLabel(
            display_frame,
            text="0",
            font=ctk.CTkFont(size=48, weight="bold"),
            text_color=theme["text_color"],
            anchor="e"
        )
        self.result_label.grid(row=2, column=0, sticky="ew", padx=15, pady=(5, 15))

    def _create_fluent_button(self, parent, text, row, col):
        """Create a Windows 11 Fluent-style button."""
        theme = THEMES[self.current_theme]

        # Determine button style
        if text in ["=", "C", "⌫"]:
            fg_color = theme["accent_color"]
            hover_color = theme["accent_hover"]
            text_color = "#000000" if self.current_theme == "fluent_light" else "#ffffff"
        elif text in ["+", "-", "×", "÷", "%", "±"]:
            fg_color = theme["button_bg"]
            hover_color = theme["button_hover"]
            text_color = theme["text_color"]
        else:
            fg_color = theme["button_bg"]
            hover_color = theme["button_hover"]
            text_color = theme["text_color"]

        btn = ctk.CTkButton(
            parent,
            text=text,
            font=ctk.CTkFont(size=20, weight="bold"),
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            command=lambda t=text: self._on_button_click(t),
            height=56,
            corner_radius=8
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
        return btn

    def _create_currency_view(self, parent):
        """Create currency converter view with searchable list."""
        theme = THEMES[self.current_theme]
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        # Main container
        container = ctk.CTkFrame(parent, fg_color=theme["card_bg"], corner_radius=12)
        container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(3, weight=1)

        # Title
        title = ctk.CTkLabel(
            container, text="Currency Converter",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=theme["text_color"]
        )
        title.grid(row=0, column=0, pady=(15, 10))

        # Amount input
        amount_frame = ctk.CTkFrame(container, fg_color="transparent")
        amount_frame.grid(row=1, column=0, pady=5, padx=20, sticky="ew")
        amount_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            amount_frame, text="Amount:",
            font=ctk.CTkFont(size=14),
            text_color=theme["text_secondary"]
        ).grid(row=0, column=0, padx=(0, 10))

        self.currency_amount_var = ctk.StringVar(value="1")
        self.currency_amount = ctk.CTkEntry(
            amount_frame,
            textvariable=self.currency_amount_var,
            font=ctk.CTkFont(size=16),
            height=36,
            corner_radius=8
        )
        self.currency_amount.grid(row=0, column=1, sticky="ew")
        self.currency_amount.bind("<KeyRelease>", self._on_currency_change)

        # Selected currencies display
        selected_frame = ctk.CTkFrame(container, fg_color="transparent")
        selected_frame.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        selected_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # From currency display
        self.from_display = ctk.CTkFrame(selected_frame, fg_color=theme["button_bg"], corner_radius=8)
        self.from_display.grid(row=0, column=0, padx=5, sticky="ew")
        self.from_display.grid_columnconfigure(0, weight=1)

        self.from_label = ctk.CTkLabel(
            self.from_display, text="USD",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=theme["text_color"]
        )
        self.from_label.grid(row=0, column=0, padx=10, pady=8)

        # Swap button
        swap_btn = ctk.CTkButton(
            selected_frame,
            text="⇅",
            font=ctk.CTkFont(size=18),
            fg_color=theme["accent_color"],
            hover_color=theme["accent_hover"],
            text_color="#ffffff",
            width=40,
            height=36,
            corner_radius=8,
            command=self._swap_currencies
        )
        swap_btn.grid(row=0, column=1, padx=10)

        # To currency display
        self.to_display = ctk.CTkFrame(selected_frame, fg_color=theme["button_bg"], corner_radius=8)
        self.to_display.grid(row=0, column=2, padx=5, sticky="ew")
        self.to_display.grid_columnconfigure(0, weight=1)

        self.to_label = ctk.CTkLabel(
            self.to_display, text="EUR",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=theme["text_color"]
        )
        self.to_label.grid(row=0, column=0, padx=10, pady=8)

        # Result
        self.currency_result_label = ctk.CTkLabel(
            container,
            text="",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=theme["accent_color"]
        )
        self.currency_result_label.grid(row=3, column=0, pady=(0, 10))

        # Search bar
        search_frame = ctk.CTkFrame(container, fg_color="transparent")
        search_frame.grid(row=4, column=0, pady=(0, 10), padx=20, sticky="ew")
        search_frame.grid_columnconfigure(0, weight=1)

        self.currency_search_var = ctk.StringVar()
        self.currency_search_var.trace("w", self._filter_currencies)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            textvariable=self.currency_search_var,
            placeholder_text="🔍 Search currencies...",
            font=ctk.CTkFont(size=14),
            height=36,
            corner_radius=8
        )
        self.search_entry.grid(row=0, column=0, sticky="ew")

        # Currency list container
        list_container = ctk.CTkFrame(container, fg_color=theme["bg_color"], corner_radius=8)
        list_container.grid(row=5, column=0, sticky="nsew", padx=20, pady=(0, 15))
        list_container.grid_columnconfigure(0, weight=1)
        list_container.grid_rowconfigure(0, weight=1)

        # Scrollable frame for currencies
        self.currency_scroll = ctk.CTkScrollableFrame(
            list_container,
            fg_color=theme["bg_color"],
            label_text=""
        )
        self.currency_scroll.grid(row=0, column=0, sticky="nsew")
        self.currency_scroll.grid_columnconfigure(0, weight=1)

        # Selection mode: "from" or "to"
        self.currency_select_mode = "from"
        self.currency_from_var = ctk.StringVar(value="USD")
        self.currency_to_var = ctk.StringVar(value="EUR")

        # Build currency list
        self._build_currency_list()

        # Initial conversion
        self._on_currency_change()

    def _build_currency_list(self):
        """Build the scrollable currency list."""
        theme = THEMES[self.current_theme]

        # Clear existing
        for widget in self.currency_scroll.winfo_children():
            widget.destroy()

        # Sort currencies alphabetically
        sorted_currencies = sorted(CURRENCY_RATES.keys(), key=lambda x: x.lower())

        for i, code in enumerate(sorted_currencies):
            symbol = CURRENCY_SYMBOLS.get(code, code[:2])
            name = CURRENCY_NAMES.get(code, code)
            rate = CURRENCY_RATES[code]

            row_frame = ctk.CTkFrame(self.currency_scroll, fg_color="transparent")
            row_frame.grid(row=i, column=0, sticky="ew", padx=5, pady=1)
            row_frame.grid_columnconfigure(1, weight=1)

            # Symbol
            sym_label = ctk.CTkLabel(
                row_frame, text=symbol,
                font=ctk.CTkFont(size=16),
                text_color=theme["accent_color"],
                width=40,
                anchor="w"
            )
            sym_label.grid(row=0, column=0, padx=(10, 5))

            # Code and name
            code_label = ctk.CTkLabel(
                row_frame, text=f"{code}  {name}",
                font=ctk.CTkFont(size=13),
                text_color=theme["text_color"],
                anchor="w"
            )
            code_label.grid(row=0, column=1, sticky="w", padx=5)

            # Rate
            rate_label = ctk.CTkLabel(
                row_frame, text=f"{rate:,.2f}",
                font=ctk.CTkFont(size=12),
                text_color=theme["text_secondary"],
                anchor="e"
            )
            rate_label.grid(row=0, column=2, padx=(5, 10))

            # Make row clickable
            for widget in row_frame.winfo_children():
                widget.bind("<Button-1>", lambda e, c=code: self._on_currency_select(c))
            row_frame.bind("<Button-1>", lambda e, c=code: self._on_currency_select(c))

            # Hover effect
            def on_enter(e, f=row_frame, bg=theme["button_bg"]):
                f.configure(fg_color=bg)
            def on_leave(e, f=row_frame):
                f.configure(fg_color="transparent")

            row_frame.bind("<Enter>", on_enter)
            row_frame.bind("<Leave>", on_leave)
            for widget in row_frame.winfo_children():
                widget.bind("<Enter>", on_enter)
                widget.bind("<Leave>", on_leave)

    def _filter_currencies(self, *args):
        """Filter currency list based on search."""
        query = self.currency_search_var.get().lower()

        for widget in self.currency_scroll.winfo_children():
            # Get the code label text
            code_label = widget.winfo_children()[1]
            code = code_label.cget("text").lower()

            if query in code or query == "":
                widget.grid()
            else:
                widget.grid_remove()

    def _on_currency_select(self, code):
        """Handle currency selection from list."""
        if self.currency_select_mode == "from":
            self.currency_from_var.set(code)
            self.from_label.configure(text=code)
            self.currency_select_mode = "to"
        else:
            self.currency_to_var.set(code)
            self.to_label.configure(text=code)
            self.currency_select_mode = "from"

        self._on_currency_change()

    def _on_currency_change(self, event=None):
        """Handle currency conversion."""
        try:
            amount = float(self.currency_amount_var.get())
            from_curr = self.currency_from_var.get()
            to_curr = self.currency_to_var.get()

            # Convert: amount * (to_rate / from_rate)
            result = amount * (CURRENCY_RATES[to_curr] / CURRENCY_RATES[from_curr])

            from_sym = CURRENCY_SYMBOLS.get(from_curr, from_curr)
            to_sym = CURRENCY_SYMBOLS.get(to_curr, to_curr)

            # Show full conversion: "1 USD = 0.92 EUR" and the amount
            self.currency_result_label.configure(
                text=f"{from_sym}{amount:,.2f} {from_curr}\n=\n{to_sym}{result:,.2f} {to_curr}"
            )
        except (ValueError, KeyError):
            self.currency_result_label.configure(text="Invalid input")

    def _swap_currencies(self):
        """Swap from and to currencies."""
        from_val = self.currency_from_var.get()
        to_val = self.currency_to_var.get()
        self.currency_from_var.set(to_val)
        self.currency_to_var.set(from_val)
        self._on_currency_change()

    def _create_programmer_view(self, parent):
        """Create programmer calculator view with base conversion."""
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=3)

        # Display with base indicators
        self._create_display(parent, row=0)

        # Base indicator labels
        theme = THEMES[self.current_theme]
        base_frame = ctk.CTkFrame(parent, fg_color="transparent")
        base_frame.grid(row=0, column=0, sticky="sw", padx=20, pady=(0, 5))

        self.base_hex_label = ctk.CTkLabel(
            base_frame, text="HEX: 0",
            font=ctk.CTkFont(size=11),
            text_color=theme["text_secondary"]
        )
        self.base_hex_label.pack(anchor="w")

        self.base_dec_label = ctk.CTkLabel(
            base_frame, text="DEC: 0",
            font=ctk.CTkFont(size=11),
            text_color=theme["text_secondary"]
        )
        self.base_dec_label.pack(anchor="w")

        self.base_oct_label = ctk.CTkLabel(
            base_frame, text="OCT: 0",
            font=ctk.CTkFont(size=11),
            text_color=theme["text_secondary"]
        )
        self.base_oct_label.pack(anchor="w")

        self.base_bin_label = ctk.CTkLabel(
            base_frame, text="BIN: 0",
            font=ctk.CTkFont(size=11),
            text_color=theme["text_secondary"]
        )
        self.base_bin_label.pack(anchor="w")

        # Buttons
        buttons_frame = ctk.CTkFrame(parent, fg_color=theme["bg_color"])
        buttons_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        for i in range(5):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(7):
            buttons_frame.grid_rowconfigure(i, weight=1)

        # Memory row
        self._create_memory_buttons(buttons_frame, row=0)

        # Programmer layout with bitwise ops
        buttons_config = [
            [("AND", 1, 0), ("OR", 1, 1), ("XOR", 1, 2), ("NOT", 1, 3), ("SHL", 1, 4)],
            [("A", 2, 0), ("B", 2, 1), ("C", 2, 2), ("D", 2, 3), ("E", 2, 4)],
            [("F", 3, 0), ("7", 3, 1), ("8", 3, 2), ("9", 3, 3), ("÷", 3, 4)],
            [("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("×", 4, 3), ("-", 4, 4)],
            [("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("+", 5, 3), ("=", 5, 4)],
            [("0", 6, 0), (".", 6, 1), ("⌫", 6, 2), ("C", 6, 3), ("%", 6, 4)],
        ]

        for row_data in buttons_config:
            for text, row, col in row_data:
                self._create_fluent_button(buttons_frame, text, row, col)

    def _create_minimalist_view(self, parent):
        """Create minimalist calculator view - clean and simple."""
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=3)

        # Display
        self._create_display(parent, row=0)

        # Buttons
        buttons_frame = ctk.CTkFrame(parent, fg_color=THEMES[self.current_theme]["bg_color"])
        buttons_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        buttons_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)

        # Minimalist layout - only essentials
        buttons_config = [
            [("C", 0, 0), ("⌫", 0, 1), ("%", 0, 2), ("÷", 0, 3)],
            [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("×", 1, 3)],
            [("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3)],
            [("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3)],
            [("±", 4, 0), ("0", 4, 1), (".", 4, 2), ("=", 4, 3)],
        ]

        for row_data in buttons_config:
            for text, row, col in row_data:
                self._create_fluent_button(buttons_frame, text, row, col)

    def _create_modern_view(self, parent):
        """Create modern calculator view with extra functions."""
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=3)

        # Display
        self._create_display(parent, row=0)

        # Buttons
        buttons_frame = ctk.CTkFrame(parent, fg_color=THEMES[self.current_theme]["bg_color"])
        buttons_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        for i in range(5):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(7):
            buttons_frame.grid_rowconfigure(i, weight=1)

        # Memory row
        self._create_memory_buttons(buttons_frame, row=0)

        # Modern layout with extra functions
        buttons_config = [
            [("x²", 1, 0), ("√", 1, 1), ("^", 1, 2), ("π", 1, 3), ("e", 1, 4)],
            [("sin", 2, 0), ("cos", 2, 1), ("tan", 2, 2), ("log", 2, 3), ("ln", 2, 4)],
            [("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("÷", 3, 3), ("×", 3, 4)],
            [("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3), ("+", 4, 4)],
            [("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("C", 5, 3), ("=", 5, 4)],
            [("0", 6, 0), (".", 6, 1), ("⌫", 6, 2), ("%", 6, 3)],
        ]

        for row_data in buttons_config:
            for text, row, col in row_data:
                self._create_fluent_button(buttons_frame, text, row, col)

    def _create_metric_view(self, parent):
        """Create Metric to Imperial converter view."""
        theme = THEMES[self.current_theme]
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        container = ctk.CTkFrame(parent, fg_color=theme["card_bg"], corner_radius=12)
        container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        container.grid_columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(
            container, text="Metric ↔ Imperial",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=theme["text_color"]
        )
        title.grid(row=0, column=0, pady=(20, 10))

        # Conversion type selector
        self.metric_type_var = ctk.StringVar(value="Length")
        type_frame = ctk.CTkFrame(container, fg_color="transparent")
        type_frame.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        type_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            type_frame, text="Type:",
            font=ctk.CTkFont(size=14),
            text_color=theme["text_secondary"]
        ).grid(row=0, column=0, padx=(0, 10))

        self.metric_type_combo = ctk.CTkComboBox(
            type_frame,
            values=["Length", "Weight", "Volume", "Speed"],
            variable=self.metric_type_var,
            command=self._on_metric_type_change,
            height=36,
            corner_radius=8
        )
        self.metric_type_combo.grid(row=0, column=1, sticky="ew")

        # Input frame
        input_frame = ctk.CTkFrame(container, fg_color="transparent")
        input_frame.grid(row=2, column=0, pady=15, padx=20, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            input_frame, text="Value:",
            font=ctk.CTkFont(size=14),
            text_color=theme["text_secondary"]
        ).grid(row=0, column=0, padx=(0, 10))

        self.metric_value_var = ctk.StringVar(value="1")
        self.metric_value = ctk.CTkEntry(
            input_frame,
            textvariable=self.metric_value_var,
            font=ctk.CTkFont(size=16),
            height=36,
            corner_radius=8
        )
        self.metric_value.grid(row=0, column=1, sticky="ew")
        self.metric_value.bind("<KeyRelease>", self._on_metric_convert)

        # Metric input
        metric_frame = ctk.CTkFrame(container, fg_color="transparent")
        metric_frame.grid(row=3, column=0, pady=10, padx=20, sticky="ew")
        metric_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            metric_frame, text="Metric:",
            font=ctk.CTkFont(size=14),
            text_color=theme["text_secondary"]
        ).grid(row=0, column=0, padx=(0, 10))

        self.metric_unit_var = ctk.StringVar(value="Meters")
        self.metric_unit = ctk.CTkComboBox(
            metric_frame,
            values=["Meters", "Kilometers", "Grams", "Kilograms", "Liters", "Km/h"],
            variable=self.metric_unit_var,
            command=self._on_metric_convert,
            height=36,
            corner_radius=8
        )
        self.metric_unit.grid(row=0, column=1, sticky="ew")

        # Imperial input
        imperial_frame = ctk.CTkFrame(container, fg_color="transparent")
        imperial_frame.grid(row=4, column=0, pady=10, padx=20, sticky="ew")
        imperial_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            imperial_frame, text="Imperial:",
            font=ctk.CTkFont(size=14),
            text_color=theme["text_secondary"]
        ).grid(row=0, column=0, padx=(0, 10))

        self.imperial_unit_var = ctk.StringVar(value="Feet")
        self.imperial_unit = ctk.CTkComboBox(
            imperial_frame,
            values=["Feet", "Miles", "Ounces", "Pounds", "Gallons", "Mph"],
            variable=self.imperial_unit_var,
            command=self._on_metric_convert,
            height=36,
            corner_radius=8
        )
        self.imperial_unit.grid(row=0, column=1, sticky="ew")

        # Result
        self.metric_result_label = ctk.CTkLabel(
            container,
            text="",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=theme["accent_color"]
        )
        self.metric_result_label.grid(row=5, column=0, pady=(20, 30))

        # Initial conversion
        self._on_metric_type_change()

    def _on_metric_type_change(self, event=None):
        """Update units when conversion type changes."""
        type_map = {
            "Length": ("Meters", "Feet"),
            "Weight": ("Kilograms", "Pounds"),
            "Volume": ("Liters", "Gallons"),
            "Speed": ("Km/h", "Mph"),
        }
        t = self.metric_type_var.get()
        metric_u, imperial_u = type_map.get(t, ("Meters", "Feet"))

        length_units = ["Meters", "Kilometers", "Centimeters", "Millimeters"]
        weight_units = ["Grams", "Kilograms"]
        volume_units = ["Milliliters", "Liters"]
        speed_units = ["Km/h", "Mph"]

        unit_map = {
            "Length": (length_units, ["Feet", "Miles", "Inches", "Yards"]),
            "Weight": (weight_units, ["Ounces", "Pounds"]),
            "Volume": (volume_units, ["Fluid Ounces", "Gallons"]),
            "Speed": (speed_units, speed_units[1:]),
        }

        metric_opts, imperial_opts = unit_map.get(t, (["Meters"], ["Feet"]))
        self.metric_unit.configure(values=metric_opts)
        self.imperial_unit.configure(values=imperial_opts)
        self.metric_unit_var.set(metric_opts[0])
        self.imperial_unit_var.set(imperial_opts[0])
        self._on_metric_convert()

    def _on_metric_convert(self, event=None):
        """Perform metric to imperial conversion."""
        try:
            value = float(self.metric_value_var.get())
        except ValueError:
            self.metric_result_label.configure(text="Invalid input")
            return

        t = self.metric_type_var.get()
        metric_u = self.metric_unit_var.get()
        imperial_u = self.imperial_unit_var.get()

        # Conversion factors to base unit, then to target
        # Length (base: meters)
        length_to_m = {"Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Millimeters": 0.001}
        m_to_imperial = {"Feet": 3.28084, "Miles": 0.000621371, "Inches": 39.3701, "Yards": 1.09361}

        # Weight (base: kg)
        weight_to_kg = {"Kilograms": 1, "Grams": 0.001}
        kg_to_imperial = {"Pounds": 2.20462, "Ounces": 35.274}

        # Volume (base: liters)
        volume_to_l = {"Liters": 1, "Milliliters": 0.001}
        l_to_imperial = {"Gallons": 0.264172, "Fluid Ounces": 33.814}

        # Speed (base: km/h)
        speed_to_kmh = {"Km/h": 1, "Mph": 1.60934}
        kmh_to_imperial = {"Mph": 0.621371}

        result = None
        if t == "Length":
            meters = value * length_to_m.get(metric_u, 1)
            result = meters * m_to_imperial.get(imperial_u, 1)
        elif t == "Weight":
            kg = value * weight_to_kg.get(metric_u, 1)
            result = kg * kg_to_imperial.get(imperial_u, 1)
        elif t == "Volume":
            liters = value * volume_to_l.get(metric_u, 1)
            result = liters * l_to_imperial.get(imperial_u, 1)
        elif t == "Speed":
            kmh = value * speed_to_kmh.get(metric_u, 1)
            result = kmh * kmh_to_imperial.get(imperial_u, 1)

        if result is not None:
            if result == int(result):
                result_str = str(int(result))
            else:
                result_str = f"{result:.4f}".rstrip('0').rstrip('.')
            self.metric_result_label.configure(
                text=f"{value:g} {metric_u}\n=\n{result_str} {imperial_u}"
            )
        else:
            self.metric_result_label.configure(text="Invalid conversion")

    def _create_temperature_view(self, parent):
        """Create Temperature converter view."""
        theme = THEMES[self.current_theme]
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        container = ctk.CTkFrame(parent, fg_color=theme["card_bg"], corner_radius=12)
        container.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
        container.grid_columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(
            container, text="Temperature Converter",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=theme["text_color"]
        )
        title.grid(row=0, column=0, pady=(20, 15))

        # Input
        input_frame = ctk.CTkFrame(container, fg_color="transparent")
        input_frame.grid(row=1, column=0, pady=10, padx=30, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            input_frame, text="Value:",
            font=ctk.CTkFont(size=14),
            text_color=theme["text_secondary"]
        ).grid(row=0, column=0, padx=(0, 10))

        self.temp_value_var = ctk.StringVar(value="100")
        self.temp_value = ctk.CTkEntry(
            input_frame,
            textvariable=self.temp_value_var,
            font=ctk.CTkFont(size=16),
            height=36,
            corner_radius=8
        )
        self.temp_value.grid(row=0, column=1, sticky="ew")
        self.temp_value.bind("<KeyRelease>", self._on_temp_convert)

        # From unit
        from_frame = ctk.CTkFrame(container, fg_color="transparent")
        from_frame.grid(row=2, column=0, pady=15, padx=30, sticky="ew")
        from_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            from_frame, text="From:",
            font=ctk.CTkFont(size=14),
            text_color=theme["text_secondary"]
        ).grid(row=0, column=0, padx=(0, 10))

        self.temp_from_var = ctk.StringVar(value="Celsius")
        self.temp_from = ctk.CTkComboBox(
            from_frame,
            values=["Celsius", "Fahrenheit", "Kelvin"],
            variable=self.temp_from_var,
            command=self._on_temp_convert,
            height=36,
            corner_radius=8
        )
        self.temp_from.grid(row=0, column=1, sticky="ew")

        # To unit
        to_frame = ctk.CTkFrame(container, fg_color="transparent")
        to_frame.grid(row=3, column=0, pady=15, padx=30, sticky="ew")
        to_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            to_frame, text="To:",
            font=ctk.CTkFont(size=14),
            text_color=theme["text_secondary"]
        ).grid(row=0, column=0, padx=(0, 10))

        self.temp_to_var = ctk.StringVar(value="Fahrenheit")
        self.temp_to = ctk.CTkComboBox(
            to_frame,
            values=["Celsius", "Fahrenheit", "Kelvin"],
            variable=self.temp_to_var,
            command=self._on_temp_convert,
            height=36,
            corner_radius=8
        )
        self.temp_to.grid(row=0, column=1, sticky="ew")

        # Swap button
        swap_btn = ctk.CTkButton(
            container,
            text="⇅  Swap",
            font=ctk.CTkFont(size=14),
            fg_color=theme["button_bg"],
            hover_color=theme["button_hover"],
            text_color=theme["text_color"],
            height=36,
            corner_radius=8,
            command=self._swap_temps
        )
        swap_btn.grid(row=4, column=0, pady=10)

        # Result
        self.temp_result_label = ctk.CTkLabel(
            container,
            text="",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=theme["accent_color"]
        )
        self.temp_result_label.grid(row=5, column=0, pady=(20, 30))

        # Initial conversion
        self._on_temp_convert()

    def _swap_temps(self):
        """Swap from and to temperature units."""
        from_val = self.temp_from_var.get()
        to_val = self.temp_to_var.get()
        self.temp_from_var.set(to_val)
        self.temp_to_var.set(from_val)
        self._on_temp_convert()

    def _on_temp_convert(self, event=None):
        """Perform temperature conversion."""
        try:
            value = float(self.temp_value_var.get())
        except ValueError:
            self.temp_result_label.configure(text="Invalid input")
            return

        from_u = self.temp_from_var.get()
        to_u = self.temp_to_var.get()

        # Convert to Celsius first
        if from_u == "Celsius":
            celsius = value
        elif from_u == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_u == "Kelvin":
            celsius = value - 273.15

        # Convert from Celsius to target
        if to_u == "Celsius":
            result = celsius
        elif to_u == "Fahrenheit":
            result = celsius * 9/5 + 32
        elif to_u == "Kelvin":
            result = celsius + 273.15

        # Format nicely
        if result == int(result):
            result_str = str(int(result))
        else:
            result_str = f"{result:.2f}".rstrip('0').rstrip('.')

        self.temp_result_label.configure(
            text=f"{value:g}° {from_u}\n=\n{result_str}° {to_u}"
        )

    def _on_button_click(self, text: str):
        """Handle button click."""
        if text == "=":
            self._calculate()
        elif text == "C":
            self._clear()
        elif text == "⌫":
            self._backspace()
        elif text == "±":
            self._toggle_sign()
        elif text == "π":
            self._append_constant("pi")
        elif text == "e":
            self._append_constant("e")
        elif text == "×":
            self._append_operator("*")
        elif text == "÷":
            self._append_operator("/")
        elif text == "x²":
            self._append_function("sqr")
        elif text == "√":
            self._append_function("sqrt")
        elif text == "1/x":
            self._append_function("recip")
        elif text == "sin":
            self._append_function("sin")
        elif text == "cos":
            self._append_function("cos")
        elif text == "tan":
            self._append_function("tan")
        elif text == "asin":
            self._append_function("asin")
        elif text == "acos":
            self._append_function("acos")
        elif text == "atan":
            self._append_function("atan")
        elif text == "log":
            self._append_function("log")
        elif text == "ln":
            self._append_function("ln")
        elif text == "exp":
            self._append_function("exp")
        elif text in ["AND", "OR", "XOR", "NOT", "SHL"]:
            self._append_bitwise(text)
        elif text in ["A", "B", "C", "D", "E", "F"]:
            self._append_text(text.lower())
        else:
            self._append_text(text)

        self._update_display()
        self._update_base_indicators()

    def _append_text(self, text: str):
        """Append text to expression."""
        if self.current_result != "0" and self.current_expression == "":
            self.current_expression = self.current_result
        self.current_expression += str(text)

    def _append_operator(self, op: str):
        """Append operator to expression."""
        if self.current_expression:
            self.current_expression += f" {op} "
        elif self.current_result != "0":
            self.current_expression = f"{self.current_result} {op} "

    def _append_constant(self, const: str):
        """Append constant to expression."""
        if self.current_result != "0" and self.current_expression == "":
            self.current_expression = self.current_result
        self.current_expression += const

    def _append_function(self, func: str):
        """Append function to expression."""
        if self.current_expression:
            self.current_expression += f" {func}("
        else:
            self.current_expression = f"{func}("

    def _calculate(self):
        """Calculate the result."""
        if not self.current_expression:
            return

        try:
            result = self.calculator.evaluate(self.current_expression)
            result_str = str(result)

            self.current_result = result_str
            self.current_expression = ""

            # Save history
            self._save_history()
        except CalculatorError as e:
            self.current_result = "Error"
            self.current_expression = ""

        self._update_display()

    def _clear(self):
        """Clear the calculator."""
        self.current_expression = ""
        self.current_result = "0"
        self._update_display()

    def _backspace(self):
        """Delete last character."""
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
        self._update_display()

    def _toggle_sign(self):
        """Toggle sign of current number."""
        if self.current_expression:
            if self.current_expression.startswith("-"):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = "-" + self.current_expression
        elif self.current_result != "0":
            if self.current_result.startswith("-"):
                self.current_result = self.current_result[1:]
            else:
                self.current_result = "-" + self.current_result
        self._update_display()

    def _update_display(self):
        """Update the display labels."""
        self.expr_label.configure(text=self.current_expression)
        self.result_label.configure(text=self.current_result if self.current_result else "0")

    def _append_bitwise(self, op: str):
        """Append bitwise operator to expression."""
        ops = {"AND": "&", "OR": "|", "XOR": "^", "NOT": "~", "SHL": "<<"}
        if self.current_expression:
            self.current_expression += f" {ops[op]} "
        elif self.current_result != "0":
            self.current_expression = f"{self.current_result} {ops[op]} "

    def _update_base_indicators(self):
        """Update HEX/DEC/OCT/BIN labels in programmer mode."""
        if self.current_mode != "programmer":
            return
        try:
            val = int(float(self.current_result)) if self.current_result not in ["0", "Error", ""] else 0
        except (ValueError, TypeError):
            val = 0

        self.base_hex_label.configure(text=f"HEX: {hex(val).upper()}")
        self.base_dec_label.configure(text=f"DEC: {val}")
        self.base_oct_label.configure(text=f"OCT: {oct(val)}")
        self.base_bin_label.configure(text=f"BIN: {bin(val)}")

    # ==================== MEMORY SYSTEM ====================

    def _memory_action(self, action: str):
        """Handle memory operations (Windows Calculator style with list)."""
        # Get current displayed value
        display_val = self.current_result
        if display_val in ["0", "Error", ""]:
            display_val = "0"

        try:
            current_val = float(display_val)
        except ValueError:
            current_val = 0.0

        if action == "MC":
            # Clear all memory
            self.memory_list = []
            self.selected_memory_index = -1
        elif action == "MR":
            # Recall last saved value or show list
            if self.memory_list:
                idx = self.selected_memory_index if self.selected_memory_index >= 0 else len(self.memory_list) - 1
                self._recall_memory(idx)
        elif action == "M+":
            # Add current value to selected memory entry
            if self.selected_memory_index >= 0 and self.selected_memory_index < len(self.memory_list):
                self.memory_list[self.selected_memory_index] += current_val
            elif self.memory_list:
                self.memory_list[-1] += current_val
                self.selected_memory_index = len(self.memory_list) - 1
            else:
                self.memory_list.append(current_val)
                self.selected_memory_index = 0
        elif action == "M-":
            # Subtract current value from selected memory entry
            if self.selected_memory_index >= 0 and self.selected_memory_index < len(self.memory_list):
                self.memory_list[self.selected_memory_index] -= current_val
            elif self.memory_list:
                self.memory_list[-1] -= current_val
                self.selected_memory_index = len(self.memory_list) - 1
            else:
                self.memory_list.append(-current_val)
                self.selected_memory_index = 0
        elif action == "MS":
            # Store current value as new memory entry
            self.memory_list.append(current_val)
            self.selected_memory_index = len(self.memory_list) - 1

        # Save memory and refresh display
        self._save_memory()
        self._refresh_memory_display()
        self._update_display()

    def _save_memory(self):
        """Save memory list to file."""
        try:
            data = {
                "memory_list": self.memory_list,
                "selected_index": self.selected_memory_index
            }
            with open(self.memory_file, 'w') as f:
                json.dump(data, f)
        except Exception:
            pass

    def _load_memory(self):
        """Load memory list from file."""
        try:
            if os.path.exists(self.memory_file):
                with open(self.memory_file, 'r') as f:
                    data = json.load(f)
                    self.memory_list = data.get("memory_list", [])
                    self.selected_memory_index = data.get("selected_index", -1)
        except Exception:
            self.memory_list = []
            self.selected_memory_index = -1

    # ==================== HISTORY SYSTEM ====================

    def _save_history(self):
        """Save calculation history to file."""
        try:
            history = self.calculator.get_history()
            data = [
                {"expression": expr, "result": res, "timestamp": datetime.now().isoformat()}
                for expr, res in history
            ]
            with open(self.history_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception:
            pass

    def _load_history(self):
        """Load calculation history from file."""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        self.calculator.history.append(
                            (item["expression"], item["result"])
                        )
        except Exception:
            pass

    # ==================== THEME & KEYBOARD ====================

    def _on_theme_changed(self, theme_name: str):
        """Handle theme change."""
        for key, value in THEMES.items():
            if value["name"] == theme_name:
                self.current_theme = key
                break

        self._apply_theme()
        self._setup_ui()

    def _bind_keys(self):
        """Bind keyboard events."""
        self.bind("<Key>", self._on_key_press)
        self.bind("<Return>", lambda e: self._on_button_click("="))
        self.bind("<Escape>", lambda e: self._clear())

    def _on_key_press(self, event):
        """Handle keyboard input."""
        key = event.char

        if key in "0123456789.+-*/()^":
            self._append_text(key)
        elif key == "=":
            self._calculate()
        elif event.keysym == "BackSpace":
            self._backspace()
        elif event.keysym == "Escape":
            self._clear()

        self._update_display()

    def _on_closing(self):
        """Handle window closing."""
        self._save_history()
        self._save_memory()
        self.destroy()


def run_calculator():
    """Run the calculator application."""
    app = CalculatorUI()
    app.protocol("WM_DELETE_WINDOW", app._on_closing)
    app.mainloop()


if __name__ == "__main__":
    run_calculator()
