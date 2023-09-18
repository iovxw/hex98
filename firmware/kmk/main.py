from kmk.extensions.lock_status import LockStatus
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC, make_key
from kmk.modules.layers import Layers

from kb import KMKKeyboard

keyboard = KMKKeyboard()

class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if self.get_caps_lock():
            keyboard.leds.set_brightness(100, leds=[0])
        else:
            keyboard.leds.set_brightness(0, leds=[0])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Do not forget
        if self.report_updated:
            self.set_lock_leds()
keyboard.extensions.append(LEDLockStatus())

class RGBLayers(Layers):
	last_top_layer = 0
	hues = [(0,0,0), (20,255,255), (69,255,255)]

	def after_hid_send(self, keyboard):
		if keyboard.active_layers[0] != self.last_top_layer:
			self.last_top_layer = keyboard.active_layers[0]
			keyboard.rgb.set_hsv_fill(*self.hues[self.last_top_layer])
keyboard.modules.append(RGBLayers())

# flake8: noqa
# fmt: off
keyboard.keymap = [
    [
        KC.NO,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.NO,
    KC.NO,   KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.DEL,
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
    KC.PGUP, KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        KC.PGDN,   KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,
    KC.HOME, KC.END,  KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.NO,
                          KC.TT(1),           KC.ESC,           KC.LALT, KC.NO,            KC.BSPC,          KC.TT(2),
                                                 KC.LSFT,          KC.LGUI,          KC.LCTL,
                                                     KC.SPC,                    KC.ENT,
    ],[
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
                          KC.TRNS,          KC.TRNS,          KC.TRNS, KC.TRNS,          KC.TRNS,          KC.TRNS,
                                                 KC.TRNS,          KC.TRNS,          KC.TRNS,
                                                     KC.TRNS,                   KC.TRNS,
    ]
]

if __name__ == '__main__':
    keyboard.go()
