import board
import storage

from kmk.bootcfg import bootcfg

storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "Cw2Usb"
storage.remount("/", readonly=True)

bootcfg(
    sense=board.GP9,
    source=board.GP11,
    midi=False,
    mouse=False,
    storage=False,
    usb_id=('Samux6146', 'Cw2Usb'),
)