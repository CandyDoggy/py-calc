"""
Modern Calculator UI using CustomTkinter
Stable, clean interface with multiple themes
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from math_engine.calculator import Calculator, CalculatorError


# Theme configurations
THEMES = {
    "scientific": {
        "name": "Scientific",
        "bg_color": "#0a0e14",
        "card_bg": "#1a2332",
        "button_bg": "#1e2a3a",
        "button_hover": "#2d3f57",
        "accent_color": "#00d4ff",
        "text_color": "#ffffff",
    },
    "minimalistic": {
        "name": "Minimalistic",
        "bg_color": "#0d1117",
        "card_bg": "#161b22",
        "button_bg": "#21262d",
        "button_hover": "#30363d",
        "accent_color": "#58a6ff",
        "text_color": "#ffffff",
    },
    "programmer": {
        "name": "Programmer",
        "bg_color": "#0f0f1a",
        "card_bg": "#1a1a2e",
        "button_bg": "#2d2d44",
        "button_hover": "#3d3d5c",
        "accent_color": "#7c3aed",
        "text_color": "#ffffff",
    },
    "modern": {
        "name": "Modern",
        "bg_color": "#000000",
        "card_bg": "#111111",
        "button_bg": "#1a1a1a",
        "button_hover": "#2a2a2a",
        "accent_color": "#a855f7",
        "text_color": "#ffffff",
    },
    "frutiger_aero": {
        "name": "Frutiger Aero",
        "bg_color": "#006994",
        "card_bg": "#0087C1",
        "button_bg": "#0099cc",
        "button_hover": "#00aaff",
        "accent_color": "#88dd00",
        "text_color": "#ffffff",
    },
}


class CalculatorUI(ctk.CTk):
    """Main Calculator Application."""

    def __init__(self):
        super().__init__()
        
        self.calculator = Calculator()
        self.current_theme = "scientific"
        self.current_expression = ""
        self.current_result = "0"
        
        # Configure window
        self.title("Scientific Calculator")
        self.geometry("500x750")
        self.minsize(450, 700)
        
        # Apply theme
        self._apply_theme()
        
        # Setup UI
        self._setup_ui()
        
        # Bind keyboard events
        self._bind_keys()

    def _apply_theme(self):
        """Apply current theme."""
        theme = THEMES[self.current_theme]
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def _setup_ui(self):
        """Setup the main UI components."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Theme selector
        self._create_theme_selector()
        
        # Display frame
        self._create_display()
        
        # Buttons frame
        self._create_buttons()

    def _create_theme_selector(self):
        """Create theme selection dropdown."""
        theme_frame = ctk.CTkFrame(self, height=50)
        theme_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        theme_frame.grid_propagate(False)
        
        label = ctk.CTkLabel(theme_frame, text="Theme:")
        label.pack(side="left", padx=10, pady=10)
        
        theme_names = [THEMES[k]["name"] for k in THEMES.keys()]
        self.theme_var = ctk.StringVar(value=THEMES[self.current_theme]["name"])
        
        self.theme_combo = ctk.CTkComboBox(
            theme_frame,
            values=theme_names,
            variable=self.theme_var,
            command=self._on_theme_changed,
            width=150
        )
        self.theme_combo.pack(side="right", padx=10, pady=10)

    def _create_display(self):
        """Create the display area."""
        display_frame = ctk.CTkFrame(self, height=180)
        display_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        display_frame.grid_propagate(False)
        display_frame.grid_columnconfigure(0, weight=1)
        
        # Expression label
        self.expr_label = ctk.CTkLabel(
            display_frame,
            text="",
            font=ctk.CTkFont(size=20),
            anchor="e"
        )
        self.expr_label.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 5))
        
        # Result label
        self.result_label = ctk.CTkLabel(
            display_frame,
            text="0",
            font=ctk.CTkFont(size=48, weight="bold"),
            anchor="e"
        )
        self.result_label.grid(row=1, column=0, sticky="ew", padx=15, pady=(5, 15))

    def _create_buttons(self):
        """Create button grid based on current mode."""
        buttons_frame = ctk.CTkFrame(self)
        buttons_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        
        # Configure grid
        for i in range(8):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.grid_columnconfigure(i, weight=1)
        
        self.buttons = {}
        self._create_scientific_layout(buttons_frame)

    def _create_scientific_layout(self, parent):
        """Create scientific calculator button layout."""
        buttons_config = [
            # Row 0: Scientific functions
            [("sin", 0, 0), ("cos", 0, 1), ("tan", 0, 2), ("log", 0, 3), ("ln", 0, 4)],
            # Row 1: More scientific
            [("asin", 1, 0), ("acos", 1, 1), ("atan", 1, 2), ("√", 1, 3), ("x²", 1, 4)],
            # Row 2: Constants and special
            [("π", 2, 0), ("e", 2, 1), ("(", 2, 2), (")", 2, 3), ("^", 2, 4)],
            # Row 3: Numbers and operators
            [("C", 3, 0), ("⌫", 3, 1), ("%", 3, 2), ("÷", 3, 3), ("×", 3, 4)],
            # Row 4: 7-9 and minus
            [("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("-", 4, 3), ("+", 4, 4)],
            # Row 5: 4-6
            [("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("1/x", 5, 3), ("=", 5, 4)],
            # Row 6: 1-3
            [("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("exp", 6, 3)],
            # Row 7: 0 and decimal
            [("0", 7, 0), (".", 7, 1), ("±", 7, 2)],
        ]
        
        for row_data in buttons_config:
            for item in row_data:
                text, row, col = item
                btn = self._create_button(parent, text, row + 3, col)
                self.buttons[text] = btn

    def _create_button(self, parent, text, row, col):
        """Create a calculator button."""
        theme = THEMES[self.current_theme]
        
        # Determine button color based on type
        if text in ["=", "C", "⌫"]:
            fg_color = theme["accent_color"]
            hover_color = self._lighten_color(theme["accent_color"])
        elif text in ["+", "-", "×", "÷", "^", "√", "x²", "1/x", "%", "±"]:
            fg_color = theme["button_bg"]
            hover_color = theme["button_hover"]
        else:
            fg_color = theme["button_bg"]
            hover_color = theme["button_hover"]
        
        btn = ctk.CTkButton(
            parent,
            text=text,
            font=ctk.CTkFont(size=20, weight="bold"),
            fg_color=fg_color,
            hover_color=hover_color,
            command=lambda t=text: self._on_button_click(t),
            height=50,
            corner_radius=8
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
        return btn

    def _lighten_color(self, color: str) -> str:
        """Lighten a hex color."""
        # Simple color lightening
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        factor = 1.2
        r = min(255, int(r * factor))
        g = min(255, int(g * factor))
        b = min(255, int(b * factor))
        
        return f"#{r:02x}{g:02x}{b:02x}"

    def _on_theme_changed(self, theme_name: str):
        """Handle theme change."""
        for key, value in THEMES.items():
            if value["name"] == theme_name:
                self.current_theme = key
                break
        
        self._apply_theme()
        self._setup_ui()

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
            self._append_constant("π")
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
        else:
            self._append_text(text)
        
        self._update_display()

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
        elif key == "*":
            self._append_operator("*")
        elif key == "/":
            self._append_operator("/")
        elif key == "=":
            self._calculate()
        elif event.keysym == "BackSpace":
            self._backspace()
        elif event.keysym == "Escape":
            self._clear()
        
        self._update_display()

    def _on_closing(self):
        """Handle window closing."""
        self.destroy()


def run_calculator():
    """Run the calculator application."""
    app = CalculatorUI()
    app.protocol("WM_DELETE_WINDOW", app._on_closing)
    app.mainloop()


if __name__ == "__main__":
    run_calculator()
