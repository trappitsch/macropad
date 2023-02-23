# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "PyCharm - Debug",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, "Debug", [Keycode.SHIFT, Keycode.F9]),
        (0x004000, "Run", [Keycode.SHIFT, Keycode.F10]),
        (0x004000, "RunThis", [Keycode.CONTROL, Keycode.SHIFT, Keycode.F10]),
        # 2nd row ----------
        (0x400000, "BrkPt", [Keycode.CONTROL, Keycode.F8]),
        (0x101010, "ShowEx", [Keycode.ALT, Keycode.SHIFT, "0"]),
        (0x004000, "Res", [Keycode.F9]),
        # 3rd row ----------
        (0x280046, "StpIn", [Keycode.F7]),
        (0x280046, "StpSmt", [Keycode.SHIFT, Keycode.F7]),
        (0x280046, "RunCur", [Keycode.ALT, Keycode.SHIFT, "9"]),
        # 4th row ----------
        (0x462000, "StpOv", [Keycode.F8]),
        (0x462000, "StpOut", [Keycode.SHIFT, Keycode.F8]),
        (0x000040, "Eval", [Keycode.ALT, Keycode.SHIFT, "8"]),
        # Encoder button ---
        (0x000040, "", [Keycode.CONTROL, "w"]),  # Close window/tab
    ],
}
