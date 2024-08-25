print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP9, board.GP13,)
keyboard.row_pins = (board.GP11,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Iambic
iambic = [
    [KC.Z, KC.X]
]
# Straight
straight = [
    [KC.SPC, KC.NO]
]

keyboard.keymap = iambic

if __name__ == '__main__':
    keyboard.go()