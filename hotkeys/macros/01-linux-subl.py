# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "SublimeText",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, "Clear", [Keycode.SHIFT, Keycode.F9]),
        (0x004000, "Bld", [Keycode.SHIFT, Keycode.F10]),
        (0x004000, "BldWth", [Keycode.CONTROL, Keycode.SHIFT, Keycode.F10]),
        # 2nd row ----------
        (0x000040, "< Tab", [Keycode.CONTROL, Keycode.PAGE_UP]),
        (0x280046, "cd", [Keycode.CONTROL, Keycode.ALT, "c"]),
        (0x000040, "Tab >", [Keycode.CONTROL, Keycode.PAGE_DOWN]),
        # 3rd row ----------
        (0x462000, "< Jmp", [Keycode.ALT, "-"]),
        (0x280046, "RunPy", [Keycode.CONTROL, Keycode.ALT, "h"]),
        (0x462000, "Jmp >", [Keycode.ALT, Keycode.SHIFT, "-"]),
        # 4th row ----------
        (0x101010, "SpChk", [Keycode.SHIFT, Keycode.CONTROL, "c"]),
        (0x101010, "Discrd", [Keycode.ALT, "d"]),
        (0x101010, "Accpt >", [Keycode.SHIFT, Keycode.ALT, "f"]),
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, "w"]),  # Close window/tab
    ],
}
