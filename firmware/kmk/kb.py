import board

from kmk.extensions.led import LED
from kmk.extensions.rgb import RGB
from kmk.extensions.lock_status import LockStatus
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.layers import Layers

from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner


class LEDLockStatus(LockStatus):
    def __init__(self, led):
        self.led = led
        super().__init__()

    def set_lock_leds(self):
        if self.get_caps_lock():
            self.led.set_brightness(100, leds=[0])
        else:
            self.led.set_brightness(0, leds=[0])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Do not forget
        if self.report_updated:
            self.set_lock_leds()


class RGBLayers(Layers):
    last_top_layer = 0

    def __init__(self, rgb, layer_hues):
        self.rgb = rgb
        self.hues = layer_hues
        super().__init__()

    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            self.rgb.set_hsv_fill(*self.hues[self.last_top_layer])


class Hex98(KMKKeyboard):
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
    matrix = MatrixScanner(
        column_pins=col_pins,
        row_pins=row_pins,
        columns_to_anodes=diode_orientation,
        interval=0.05,
    )

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

    led = LED(led_pin=[board.LED], brightness=0)
    KMKKeyboard.extensions.append(led)

    rgb = RGB(pixel_pin=board.RGB, num_pixels=1, val_default=0)
    KMKKeyboard.extensions.append(rgb)

    KMKKeyboard.extensions.append(LEDLockStatus(led))
    KMKKeyboard.modules.append(RGBLayers(rgb, [(0, 0, 0), (20, 255, 255), (69, 255, 255)]))
