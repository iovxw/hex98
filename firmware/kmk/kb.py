import board
import microcontroller

from kmk.extensions.LED import LED
from kmk.extensions.RGB import RGB
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard

from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
    )
    row_pins = (
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP20,
        board.GP21,
        board.GP22,
        board.GP26,
        board.GP27,
    )
    diode_orientation = DiodeOrientation.ROW2COL

    # flake8: noqa
    # fmt: off
    coord_mapping = [
      0,   1,   2,   3,   4,   5,  6,         8,   9,  10,  11,  12,  13,  14,
     15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,
     30,  31,  32,  33,  34,  35,  36,       38,  39,  40,  41,  42,  43,  44,
     45,  46,  47,  48,  49,  50,  51,  52,  53,  54,  55,  56,  57,  58,  59,
     60,  61,  62,  63,  64,  65,  66,       68,  69,  70,  71,  72,  73,  74,
     75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,
               92,       94,       96,       98,      100,      102,
                             110,      112,      114,
                             125,                129,
    ]

    leds = LED(led_pin=[board.LED], brightness=0)
    _KMKKeyboard.extensions.append(leds)

    rgb = RGB(pixel_pin=board.RGB, num_pixels=1, val_default=0)
    _KMKKeyboard.extensions.append(rgb)
