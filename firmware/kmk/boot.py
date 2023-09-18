import board, digitalio
import time

button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

# Wait pin init
time.sleep(0.1)

# Disable devices only if button is not pressed.
if button.value:
    import storage, usb_cdc

    storage.disable_usb_drive()
    usb_cdc.disable()
