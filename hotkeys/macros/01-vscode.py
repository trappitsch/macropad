# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "VSCode",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, "Debug", [Keycode.F5]),
        (0x004000, "Run", [Keycode.CONTROL, Keycode.F5]),
        (0x004000, "RunThis", [Keycode.SHIFT, Keycode.ALT, Keycode.F5]),
        # 2nd row ----------
        (0x000040, "< Tab", [Keycode.CONTROL, Keycode.PAGE_UP]),
        (0xff5900, "RnTsts", [Keycode.CONTROL, Keycode.ALT, "6"]),
        (0x000040, "Tab >", [Keycode.CONTROL, Keycode.PAGE_DOWN]),
        # 3rd row ----------,
        (0x280046, "Refs", [Keycode.SHIFT, Keycode.F12]),
        (0x280046, "Decl", [Keycode.F12]),
        (0x462000, "Rename", [Keycode.F2]),
        # 4th row ----------
        (0x462000, "Refract", [Keycode.CONTROL, Keycode.SHIFT, "R"]),
        (0x202000, "Struct", [Keycode.ALT, Keycode.SHIFT, "7"]),
        (0x101010, "Files", [Keycode.CONTROL, Keycode.SHIFT, "E"]),
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, "W"]),  # Close window/tab
    ],
}
