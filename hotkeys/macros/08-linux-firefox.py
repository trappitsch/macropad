# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "Linux Firefox",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, "< Back", [Keycode.CONTROL, "["]),
        (0x400000, "Up", [Keycode.SHIFT, " "]),  # Scroll up
        (0x004000, "Fwd >", [Keycode.CONTROL, "]"]),
        # 2nd row ----------
        (0x462000, "< Tab", [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x400000, "Down", " "),  # Scroll down
        (0x462000, "Tab >", [Keycode.CONTROL, Keycode.TAB]),
        # 3rd row ----------
        (0x000040, "BookMrk", [Keycode.CONTROL, "b"]),
        (0x000040, "Priv", [Keycode.CONTROL, Keycode.SHIFT, "p"]),
        (0x000040, "Pwd", [Keycode.CONTROL, Keycode.SHIFT, "l"]),
        # 4th row ----------
        (
            0x101010,
            "Proton",
            [
                Keycode.CONTROL,
                "t",
                -Keycode.CONTROL,
                "https://mail.proton.me\n",
            ],
        ),
        (
            0x101010,
            "ADS",
            [
                Keycode.CONTROL,
                "t",
                -Keycode.CONTROL,
                "https://ui.adsabs.harvard.edu/\n",
            ],
        ),
        (
            0x101010,
            "Git",
            [Keycode.CONTROL, "t", -Keycode.CONTROL, "https://github.com/login\n"],
        ),
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, "w"]),  # Close window/tab
    ],
}
