# Cw2Usb
A small adaptor based on an RP2040-Zero microcontroller board, to connect a cw (morse) key to a computer.
Supports both paddles and straight keys without any configuration!

<img src="/Images/setup.png" width="50%" height="50%">

<br>
<br>
<br>


# Why?
Learning cw is not an easy task, this adaptor enables you to train with friends or random pepole online or with [Morse-It](https://apps.apple.com/it/app/morse-it/id284942940) on iphone and ipad ([Lightning adaptor](https://www.apple.com/it/shop/product/MD821ZM/A/adattatore-per-fotocamere-da-lightning-a-usb) required on lightning devices)

<img src="/Images/demo.gif" width="50%" height="50%">

<br>
<br>
<br>


# Components

| Components              | Quantity | Buy |
| ------------------------------ | - | ----------- |
| RP2040-Zero                    | 1 | [Aliexpress](https://www.aliexpress.com/item/1005006060919390.html?spm=a2g0o.productlist.main.1.2202gBdmgBdmwK&algo_pvid=ca51da67-eaf9-4b85-87c1-c4a47e4f0e21&algo_exp_id=ca51da67-eaf9-4b85-87c1-c4a47e4f0e21-0&pdp_npi=4%40dis%21EUR%216.80%211.91%21%21%2152.73%2114.76%21%40211b61bb17245927896378252ecdef%2112000035550922721%21sea%21IT%211890676707%21X&curPageLogUid=jnTx7UaLmlZc&utparam-url=scene%3Asearch%7Cquery_from%3A)         |
| Signal Diodes                  | 2 |  [Aliexpress](https://www.aliexpress.com/item/32465250573.html?spm=a2g0o.productlist.main.1.7702704fFSg6oz&algo_pvid=2ee03842-affe-425c-945a-04e29387264d&algo_exp_id=2ee03842-affe-425c-945a-04e29387264d-0&pdp_npi=4%40dis%21EUR%211.80%211.71%21%21%211.96%211.86%21%4021039cc717245929649286292e4e54%2112000035422362519%21sea%21IT%211890676707%21X&curPageLogUid=EIlYMOsov03D&utparam-url=scene%3Asearch%7Cquery_from%3A) (100pcs)         |
| Female TRS mini jack connector | 1 | [Aliexpress](https://www.aliexpress.com/item/1005005863583101.html?spm=a2g0o.productlist.main.11.28f518b5IVqlr8&algo_pvid=979f6720-57be-4c5f-9c20-94346ba5869f&algo_exp_id=979f6720-57be-4c5f-9c20-94346ba5869f-5&pdp_npi=4%40dis%21EUR%211.53%211.53%21%21%2111.86%2111.86%21%4021039f3e17245931979077665e1d27%2112000034616941985%21sea%21IT%211890676707%21X&curPageLogUid=GMHXKl4PMNry&utparam-url=scene%3Asearch%7Cquery_from%3A)  (10pcs) |

<img src="/Images/top.png" width="50%" height="50%">
<img src="/Images/bottom.png" width="50%" height="50%">
<img src="/Images/connections.png" width="50%" height="50%">

<br>
<br>
<br>


# Firmware
## Setup
1. Installing CircuitPython
    1. Download [CircuitPython](https://circuitpython.org/downloads)
    2. Plug the microcontroller in while holding down the boot select button to enter bootloader mod
    3. Drag the .UF2 file to the root of the microcontroller's usb drive
2. Installing KMK
    1. Download the [KMK zip folder](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/main.zip)
    2. Unzip it
    3. Copy the KMK folder and the doot.py file to the root of the microcontroller's usb drive
    4. Reset the microcontroller by pressing the RESET button
3. Installing the custom Code
    1. Download the [Cw2Usb](https://github.com/samux6146/Cw2Usb) repository
    2. Copy the boot.py, code.py and keymap.py file to the root of the microcontroller's usb drive
    3. Reset the microcontroller by pressing the RESET button
4. You are done!

## Features
1. Booting up the microcontroller with a straight key connected automaticly changes keymap (booting with the dash paddle pressed does the same)
2. Usb drive automatically disabled on boot
3. Booting up the microcontroller with the dot pressed on the cw key mounts the usb drive for updates