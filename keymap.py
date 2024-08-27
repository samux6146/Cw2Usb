import board
import digitalio
from kmk.keys import KC

iambic = [
    [KC.Z, KC.X]
]
straight = [
    [KC.SPC, KC.NO]
]

def get_keymap():
    trig = digitalio.DigitalInOut(board.GP13)
    trig.direction = digitalio.Direction.INPUT
    trig.pull = digitalio.Pull.UP
    sense = trig.value
    trig.deinit()
    if not sense:
        return(straight)
    else:
        return(iambic)