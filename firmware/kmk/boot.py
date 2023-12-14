import time
import board, digitalio
import neopixel

button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)
pixels = neopixel.NeoPixel(board.NEOPIXEL, n=1, brightness=0.01)
pixels.fill((255, 255, 255))

dev_mode = False
for _ in range(100):
    time.sleep(0.01)
    if not button.value:
        dev_mode = True
        break

if dev_mode:
    pixels.fill((255, 0, 0))
else:
    import storage, usb_cdc

    storage.disable_usb_drive()
    usb_cdc.disable()
