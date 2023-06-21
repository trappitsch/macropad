# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "PyCharm",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, "Debug", [Keycode.SHIFT, Keycode.F9]),
        (0x004000, "Run", [Keycode.SHIFT, Keycode.F10]),
        (0x004000, "RunThis", [Keycode.CONTROL, Keycode.SHIFT, Keycode.F10]),
        # 2nd row ----------
        (0x000040, "< Tab", [Keycode.CONTROL, Keycode.PAGE_UP]),
        (0x400000, "RunMenu", [Keycode.ALT, Keycode.SHIFT, Keycode.F10]),
        (0x000040, "Tab >", [Keycode.CONTROL, Keycode.PAGE_DOWN]),
        # 3rd row ----------,
        (0x280046, "Usage", [Keycode.ALT, Keycode.SHIFT, "7"]),
        (0x280046, "Decl", [Keycode.CONTROL, "b"]),
        (0x462000, "Rename", [Keycode.SHIFT, Keycode.F6]),
        # 4th row ----------
        (0x000000, "Black", [Keycode.ALT, Keycode.SHIFT, "B"]),
        (0x202000, "Struct", [Keycode.ALT, "7"]),
        (0x101010, "Sett", [Keycode.CONTROL, Keycode.ALT, "s"]),
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, "w"]),  # Close window/tab
    ],
}
