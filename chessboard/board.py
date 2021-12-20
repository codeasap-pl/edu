#!/usr/bin/env python3
# -*- coding: utf-8; -*-

"""
My winning plan is to move Rh8, exchange rooks on h1,
bring the Queen down to h3 check, then Qg2 mate.
"""

import string
import colored
import random


class C:
    BG_WHITE = (lambda s: "%s%s%s%s%s" % (
        colored.style.BOLD, colored.fore.BLACK, colored.back.WHITE, s, colored.style.RESET))
    BG_BLACK = (lambda s: "%s%s%s%s" % (
        colored.fore.BLACK, colored.back.BLUE, s, colored.style.RESET))
    BOARD = (lambda s: "%s%s%s" % (
        colored.fore.BLUE, s, colored.style.RESET))


class Pieces:
    NAMES = ["K", "Q", "R", "B", "N", "P"]
    TYPES = ["K", "Q", "R", "B", "N", "P"]
    WHITE = ["♔", "♕", "♖", "♗", "♘", "♙"]
    BLACK = ["♚", "♛", "♜", "♝", "♞", "♟"]
    EMPTY = " "


class Board:
    def __init__(self, w=8, h=8):
        self.cols = w
        self.rows = h
        self.col_sym = string.ascii_uppercase[:w]
        self.row_sym = [str(n) for n in range(1, h + 1)]
        self.state = [random.choice(Pieces.WHITE + Pieces.BLACK)
                      for _ in range(w * h)]

    def draw(self):
        print("".center(4), end="")
        for c in range(0, self.cols):
            print(C.BOARD(self.col_sym[c].center(4)), end="")
        print()

        for r in range(self.rows - 1, -1, -1):
            print(C.BOARD(self.row_sym[r].center(4)), end="")
            for c in range(0, self.cols):
                print(self._colorize(r, c, center=4), end="")
            print()

        print("".center(4), end="")
        for c in range(0, self.cols):
            print(C.BOARD(self.col_sym[c].center(4)), end="")
        print()

    def _colorize(self, r, c, /, center=4):
        pc = (self.state[r * self.cols + c] or "")
        pc = pc.center(center)
        r_odd = (r % 2)
        c_odd = (c % 2)
        func = C.BG_WHITE
        if (c_odd and r_odd) or (not c_odd and not r_odd):
            func = C.BG_BLACK
        return func(pc)


if __name__ == "__main__":
    board = Board()
    board.draw()
