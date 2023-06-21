# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "VSCode Debug",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, "Debug", [Keycode.F5]),
        (0x004000, "Run", [Keycode.CONTROL, Keycode.F5]),  # todo
        (0x004000, "RunThis", [Keycode.CONTROL, Keycode.F5]),
        # 2nd row ----------
        (0xff5900, "Stop", [Keycode.F9]),
        (0xff5900, "Rstart", [Keycode.ALT, Keycode.SHIFT, "0"]),
        (0x000040, "Cnsole", [Keycode.CONTROL, Keycode.SHIFT, "Y"]),
        # 3rd row ----------
        (0x280046, "StpOv", [Keycode.F10]),
        (0x280046, "StpIn", [Keycode.F11]),
        (0x280046, "StpOut", [Keycode.SHIFT, Keycode.F11]),
        # 4th row ----------
        (0x400000, "BrkPt", [Keycode.F9]),
        (0x400000, "CondBrk", [Keycode.CONTROL, Keycode.SHIFT, Keycode.F9]),
        (0x400000, "InlBrk", [Keycode.SHIFT, Keycode.F9]),
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, "W"]),  # Close window/tab
    ],
}
