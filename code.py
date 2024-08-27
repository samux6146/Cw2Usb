import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from keymap import get_keymap

keymap = get_keymap()
keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP9, board.GP13,)
keyboard.row_pins = (board.GP11,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = keymap

if __name__ == '__main__':
    keyboard.go()