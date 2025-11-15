![](images/hex98.webp)

# hex98

 My honeycomb keyboard
 
## Why?

- Minimized learning curve
  - Almost a QWERTY keyboard, with additional thumb keys
- Ergonomics
  - Keys are 60°, keeps wrists straight, see finger placement below
- Six thumb keys
  - Pinky is weak, modifier keys are moved to thumb
- Plenty of keys
  - Move your hands instead of switching layers

## Finger Placement

![](images/finger_placement.svg)

## BOM

| Description      | Qty |
| ---------------- | --- |
| M3*6 FHCS        | 11  |
| MX Switchs       | 98  |
| [YD-RP2040][ali] | 1   |

[ali]: https://www.aliexpress.us/item/3256803817805852.html

## Build guide

Download all step files from `cad/out`, print them

The `keyboard_body` is 306mm*174.73mm, make sure your 3D printer is big enough

`wrist_rest` is optional, print two if you need

![](images/parts.png)

### Hand wiring matrix

Install all switchs:

![](images/switch_installed.webp)

Connect rows

![](images/row.webp)

Trim the diode anode to approximately 5mm

![](images/cut_diode.webp)

Solder the first, and the second

![](images/first_diode.webp)

This is what it looks like from the side:

![](images/diode_side_view.webp)

This method eliminates the need for insulation

Then just repeat it:

![](images/first_column.webp)

![](images/half_column.webp)

![](images/half_column_mirrored.webp)

![](images/matrix.webp)

Note the middle column, several diodes are used merely as wires

Connect the matrix to the board as follows:

![](images/wiring.webp)

Solder the board-side wires first, then you can get creative with the routing

![](images/wiring_finished.webp)

Done

![](images/done.webp)

Note: This build uses keycap_alt and pcb_cover_alt

## Firmware

See [firmware/kmk](firmware/kmk)

## Alternative Keycaps

![](images/alt_keycaps.webp)

## Q&A

### What do these indicator LEDs mean？

![](images/led.jpg)

Power LED is always on

Current Layer RGB is off on default layer, yellow on second layer, green on third layer

Colors can be customized via https://github.com/iovxw/hex98/blob/95d79bd28a6102e14578006c19bc72cac9129d9f/firmware/kmk/code.py#L33-L34

### How to enter dev mode after firmware flashed?

![](images/button.jpg)
