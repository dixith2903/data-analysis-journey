import tkinter as tk
from tkinter import font
import math

# ─────────────────────────────────────────────
#  COLOUR PALETTE  (Dark + Neon Accent Theme)
# ─────────────────────────────────────────────
BG_MAIN        = "#0D0D0D"   # near-black background
BG_DISPLAY     = "#1A1A2E"   # deep navy display panel
FG_DISPLAY     = "#E0E0E0"   # soft white display text
FG_EXPR        = "#7F8C8D"   # muted expression text

# Button groups
CLR_NUM        = "#16213E"   # number buttons  (dark blue-grey)
CLR_NUM_FG     = "#EAEAEA"
CLR_OP         = "#0F3460"   # operator buttons (medium blue)
CLR_OP_FG      = "#00D4FF"   # neon cyan text
CLR_SPEC       = "#533483"   # special (C, %, ±) (purple)
CLR_SPEC_FG    = "#FFFFFF"
CLR_EQ         = "#E94560"   # equals button    (neon red/pink)
CLR_EQ_FG      = "#FFFFFF"

# Hover colours
CLR_NUM_H      = "#1F2F5A"
CLR_OP_H       = "#1A4A80"
CLR_SPEC_H     = "#6A44A0"
CLR_EQ_H       = "#FF6B81"


# ─────────────────────────────────────────────
#  CALCULATOR CLASS
# ─────────────────────────────────────────────
class Calculator:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_MAIN)

        # State
        self.expression   = ""   # full expression string
        self.result_shown = False
        self.just_evaled  = False

        self._build_ui()
        self._bind_keyboard()

        # Centre on screen
        self.root.update_idletasks()
        w, h = self.root.winfo_width(), self.root.winfo_height()
        sw   = self.root.winfo_screenwidth()
        sh   = self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    # ── UI BUILDER ──────────────────────────────
    def _build_ui(self):
        # ── Display frame ──
        disp_frame = tk.Frame(self.root, bg=BG_DISPLAY, padx=16, pady=12)
        disp_frame.grid(row=0, column=0, sticky="nsew", padx=12, pady=(12, 6))

        self.expr_var   = tk.StringVar(value="")
        self.result_var = tk.StringVar(value="0")

        # Small expression line
        expr_lbl = tk.Label(
            disp_frame, textvariable=self.expr_var,
            bg=BG_DISPLAY, fg=FG_EXPR,
            font=("Consolas", 13), anchor="e", justify="right",
            wraplength=310
        )
        expr_lbl.grid(row=0, column=0, sticky="e")

        # Large result line
        result_lbl = tk.Label(
            disp_frame, textvariable=self.result_var,
            bg=BG_DISPLAY, fg=FG_DISPLAY,
            font=("Consolas", 40, "bold"), anchor="e", justify="right",
            wraplength=310
        )
        result_lbl.grid(row=1, column=0, sticky="e")
        disp_frame.columnconfigure(0, minsize=330)

        # ── Button grid ──
        btn_frame = tk.Frame(self.root, bg=BG_MAIN)
        btn_frame.grid(row=1, column=0, padx=12, pady=(6, 12))

        # Layout: (label, col, row, colspan, bg, fg, hover, action)
        buttons = [
            # Row 1 – special functions
            ("C",   0, 0, 1, CLR_SPEC, CLR_SPEC_FG, CLR_SPEC_H, self._clear),
            ("±",   1, 0, 1, CLR_SPEC, CLR_SPEC_FG, CLR_SPEC_H, self._toggle_sign),
            ("%",   2, 0, 1, CLR_SPEC, CLR_SPEC_FG, CLR_SPEC_H, self._percent),
            ("÷",   3, 0, 1, CLR_OP,   CLR_OP_FG,   CLR_OP_H,   lambda: self._op("/")),

            # Row 2
            ("7",   0, 1, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("7")),
            ("8",   1, 1, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("8")),
            ("9",   2, 1, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("9")),
            ("×",   3, 1, 1, CLR_OP,   CLR_OP_FG,   CLR_OP_H,   lambda: self._op("*")),

            # Row 3
            ("4",   0, 2, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("4")),
            ("5",   1, 2, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("5")),
            ("6",   2, 2, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("6")),
            ("−",   3, 2, 1, CLR_OP,   CLR_OP_FG,   CLR_OP_H,   lambda: self._op("-")),

            # Row 4
            ("1",   0, 3, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("1")),
            ("2",   1, 3, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("2")),
            ("3",   2, 3, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("3")),
            ("+",   3, 3, 1, CLR_OP,   CLR_OP_FG,   CLR_OP_H,   lambda: self._op("+")),

            # Row 5
            ("0",   0, 4, 2, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  lambda: self._digit("0")),
            (".",   2, 4, 1, CLR_NUM,  CLR_NUM_FG,  CLR_NUM_H,  self._dot),
            ("=",   3, 4, 1, CLR_EQ,   CLR_EQ_FG,   CLR_EQ_H,   self._evaluate),
        ]

        for (text, col, row, colspan,
             bg, fg, hover, cmd) in buttons:

            btn = self._make_button(btn_frame, text, bg, fg, hover, cmd)
            btn.grid(
                row=row, column=col, columnspan=colspan,
                padx=5, pady=5, sticky="nsew"
            )
            btn_frame.rowconfigure(row, minsize=72)
            btn_frame.columnconfigure(col, minsize=82)

    def _make_button(self, parent, text, bg, fg, hover_bg, cmd):
        """Create a styled, hover-animated button."""
        btn = tk.Button(
            parent,
            text=text,
            command=cmd,
            bg=bg, fg=fg,
            activebackground=hover_bg,
            activeforeground=fg,
            font=("Consolas", 20, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2",
            width=2,
            height=1,
        )
        # Hover effects
        btn.bind("<Enter>", lambda e, b=btn, c=hover_bg: b.config(bg=c))
        btn.bind("<Leave>", lambda e, b=btn, c=bg:       b.config(bg=c))
        return btn

    # ── KEYBOARD BINDINGS ───────────────────────
    def _bind_keyboard(self):
        bindings = {
            "<Key-0>": lambda e: self._digit("0"),
            "<Key-1>": lambda e: self._digit("1"),
            "<Key-2>": lambda e: self._digit("2"),
            "<Key-3>": lambda e: self._digit("3"),
            "<Key-4>": lambda e: self._digit("4"),
            "<Key-5>": lambda e: self._digit("5"),
            "<Key-6>": lambda e: self._digit("6"),
            "<Key-7>": lambda e: self._digit("7"),
            "<Key-8>": lambda e: self._digit("8"),
            "<Key-9>": lambda e: self._digit("9"),
            "<Key-period>":  lambda e: self._dot(),
            "<Key-plus>":    lambda e: self._op("+"),
            "<Key-minus>":   lambda e: self._op("-"),
            "<Key-asterisk>":lambda e: self._op("*"),
            "<Key-slash>":   lambda e: self._op("/"),
            "<Return>":      lambda e: self._evaluate(),
            "<KP_Enter>":    lambda e: self._evaluate(),
            "<BackSpace>":   lambda e: self._backspace(),
            "<Escape>":      lambda e: self._clear(),
            "<percent>":     lambda e: self._percent(),
        }
        for key, handler in bindings.items():
            self.root.bind(key, handler)

    # ── LOGIC ───────────────────────────────────
    def _get_display(self):
        return self.result_var.get()

    def _set_display(self, val: str):
        # Limit display length and strip unnecessary trailing zeros
        if "." in val:
            val = val.rstrip("0").rstrip(".")
        # Protect against -0
        if val in ("-0", "-0.0", ""):
            val = "0"
        # Truncate long floats
        if len(val) > 14:
            val = val[:14]
        self.result_var.set(val)

    def _digit(self, d: str):
        cur = self._get_display()
        if self.just_evaled:
            # Start fresh after a result, unless chaining with operator
            self.expression = ""
            self.expr_var.set("")
            self.just_evaled = False
            cur = "0"

        if cur == "0" and d != ".":
            cur = d
        else:
            if len(cur) >= 15:
                return
            cur += d

        self.result_var.set(cur)

    def _dot(self):
        cur = self._get_display()
        if self.just_evaled:
            self.expression = ""
            self.expr_var.set("")
            self.just_evaled = False
            cur = "0"

        if "." not in cur:
            self.result_var.set(cur + ".")

    def _op(self, op_char: str):
        """Append the current display value and operator to the expression."""
        cur  = self._get_display()
        self.just_evaled = False

        # Replace last operator if expression ends with one
        if self.expression and self.expression[-1] in "+-*/":
            self.expression = self.expression[:-1]
        else:
            self.expression += cur

        self.expression += op_char

        # Show operator symbol in expression label
        display_op = {"*": "×", "/": "÷", "+": "+", "-": "−"}
        pretty = self.expression.replace("*","×").replace("/","÷").replace("-","−")
        self.expr_var.set(pretty)

        # Reset display to zero for next number input
        self.result_var.set("0")

    def _evaluate(self):
        cur = self._get_display()
        if not self.expression:
            return   # Nothing to evaluate

        full_expr = self.expression + cur
        pretty    = full_expr.replace("*","×").replace("/","÷").replace("-","−")
        self.expr_var.set(pretty + " =")

        try:
            result = eval(full_expr)   # safe: only numbers + +-*/
            if isinstance(result, float):
                if result != result:          # NaN
                    raise ValueError("Not a number")
                if abs(result) == float("inf"):
                    raise ZeroDivisionError
                # Format nicely
                result_str = f"{result:.10f}".rstrip("0").rstrip(".")
            else:
                result_str = str(result)

            self._set_display(result_str)
            self.expression   = result_str   # allow chaining
            self.just_evaled  = True

        except ZeroDivisionError:
            self.result_var.set("÷0 Error")
            self.expression  = ""
            self.just_evaled = False
        except Exception:
            self.result_var.set("Error")
            self.expression  = ""
            self.just_evaled = False

    def _clear(self):
        self.expression  = ""
        self.just_evaled = False
        self.result_var.set("0")
        self.expr_var.set("")

    def _backspace(self):
        if self.just_evaled:
            self._clear()
            return
        cur = self._get_display()
        if len(cur) > 1:
            self.result_var.set(cur[:-1])
        else:
            self.result_var.set("0")

    def _toggle_sign(self):
        cur = self._get_display()
        if cur not in ("0", "Error", "÷0 Error"):
            if cur.startswith("-"):
                self.result_var.set(cur[1:])
            else:
                self.result_var.set("-" + cur)

    def _percent(self):
        cur = self._get_display()
        try:
            val = float(cur) / 100
            self._set_display(str(val))
        except ValueError:
            pass


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
def main():
    root = tk.Tk()

    # ── App icon (in-memory coloured icon using PhotoImage) ──
    icon_data = """
    R0lGODlhEAAQAIAAAAAAAP///yH5BAEAAAEALAAAAAAQABAAAAIjjI+py+0Po5y02ouz3rz7
    D4biSJbmiabqyrbuC8fyTNcFADs=
    """
    try:
        icon = tk.PhotoImage(data=icon_data)
        root.iconphoto(True, icon)
    except Exception:
        pass

    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()