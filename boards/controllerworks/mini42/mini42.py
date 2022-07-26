'''
KMK keyboard based on RP2040. Uses Corne-like layout. Has integrated SSD1306
display. Each key monitored by a GPIO with no scanning matrix.

'''

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner

# fmt: off
_KEY_CFG = [
    board.D2, board.D3, board.D4, board.D5, board.D6, board.D7,
    board.D8, board.D9, board.D10, board.D11, board.D12, board.D13,
    board.D14, board.D15, board.D16, board.D17, board.D18, board.D19,
    board.D20, board.D21, board.D22,
]
# fmt: on


class Mini42(KMKKeyboard):
    def __init__(self):
        self.matrix = KeysScanner(_KEY_CFG)
