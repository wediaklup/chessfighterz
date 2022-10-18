from tkinter.ttk import _Padding
import pygame
import engine

class Opponent:
    def __init__(self, id, name, hp) -> None:
        pass

class Board:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        margX = x
        margY = y

        PADDING = 102

        self.col_coord = {
            "A": margX + PADDING + (0 * 64),
            "B": margX + PADDING + (1 * 64),
            "C": margX + PADDING + (2 * 64),
            "D": margX + PADDING + (3 * 64),
            "E": margX + PADDING + (4 * 64),
            "F": margX + PADDING + (5 * 64),
            "G": margX + PADDING + (6 * 64),
            "H": margX + PADDING + (7 * 64),
        }

        self.row_coord = {
            1: margY + PADDING + (0 * 64),
            2: margY + PADDING + (1 * 64),
            3: margY + PADDING + (2 * 64),
            4: margY + PADDING + (3 * 64),
            5: margY + PADDING + (4 * 64),
            6: margY + PADDING + (5 * 64),
            7: margY + PADDING + (6 * 64),
            8: margY + PADDING + (7 * 64),
        }

        self.field_coords = {
            "A1": (self.col_coord["A"], self.row_coord[1]),
            "A2": (self.col_coord["A"], self.row_coord[2]),
            "A3": (self.col_coord["A"], self.row_coord[3]),
            "A4": (self.col_coord["A"], self.row_coord[4]),
            "A5": (self.col_coord["A"], self.row_coord[5]),
            "A6": (self.col_coord["A"], self.row_coord[6]),
            "A7": (self.col_coord["A"], self.row_coord[7]),
            "A8": (self.col_coord["A"], self.row_coord[8]),

            "B1": (self.col_coord["B"], self.row_coord[1]),
            "B2": (self.col_coord["B"], self.row_coord[2]),
            "B3": (self.col_coord["B"], self.row_coord[3]),
            "B4": (self.col_coord["B"], self.row_coord[4]),
            "B5": (self.col_coord["B"], self.row_coord[5]),
            "B6": (self.col_coord["B"], self.row_coord[6]),
            "B7": (self.col_coord["B"], self.row_coord[7]),
            "B8": (self.col_coord["B"], self.row_coord[8]),

            "C1": (self.col_coord["C"], self.row_coord[1]),
            "C2": (self.col_coord["C"], self.row_coord[2]),
            "C3": (self.col_coord["C"], self.row_coord[3]),
            "C4": (self.col_coord["C"], self.row_coord[4]),
            "C5": (self.col_coord["C"], self.row_coord[5]),
            "C6": (self.col_coord["C"], self.row_coord[6]),
            "C7": (self.col_coord["C"], self.row_coord[7]),
            "C8": (self.col_coord["C"], self.row_coord[8]),

            "D1": (self.col_coord["D"], self.row_coord[1]),
            "D2": (self.col_coord["D"], self.row_coord[2]),
            "D3": (self.col_coord["D"], self.row_coord[3]),
            "D4": (self.col_coord["D"], self.row_coord[4]),
            "D5": (self.col_coord["D"], self.row_coord[5]),
            "D6": (self.col_coord["D"], self.row_coord[6]),
            "D7": (self.col_coord["D"], self.row_coord[7]),
            "D8": (self.col_coord["D"], self.row_coord[8]),

            "E1": (self.col_coord["E"], self.row_coord[1]),
            "E2": (self.col_coord["E"], self.row_coord[2]),
            "E3": (self.col_coord["E"], self.row_coord[3]),
            "E4": (self.col_coord["E"], self.row_coord[4]),
            "E5": (self.col_coord["E"], self.row_coord[5]),
            "E6": (self.col_coord["E"], self.row_coord[6]),
            "E7": (self.col_coord["E"], self.row_coord[7]),
            "E8": (self.col_coord["E"], self.row_coord[8]),

            "F1": (self.col_coord["F"], self.row_coord[1]),
            "F2": (self.col_coord["F"], self.row_coord[2]),
            "F3": (self.col_coord["F"], self.row_coord[3]),
            "F4": (self.col_coord["F"], self.row_coord[4]),
            "F5": (self.col_coord["F"], self.row_coord[5]),
            "F6": (self.col_coord["F"], self.row_coord[6]),
            "F7": (self.col_coord["F"], self.row_coord[7]),
            "F8": (self.col_coord["F"], self.row_coord[8]),

            "G1": (self.col_coord["G"], self.row_coord[1]),
            "G2": (self.col_coord["G"], self.row_coord[2]),
            "G3": (self.col_coord["G"], self.row_coord[3]),
            "G4": (self.col_coord["G"], self.row_coord[4]),
            "G5": (self.col_coord["G"], self.row_coord[5]),
            "G6": (self.col_coord["G"], self.row_coord[6]),
            "G7": (self.col_coord["G"], self.row_coord[7]),
            "G8": (self.col_coord["G"], self.row_coord[8]),

            "H1": (self.col_coord["H"], self.row_coord[1]),
            "H2": (self.col_coord["H"], self.row_coord[2]),
            "H3": (self.col_coord["H"], self.row_coord[3]),
            "H4": (self.col_coord["H"], self.row_coord[4]),
            "H5": (self.col_coord["H"], self.row_coord[5]),
            "H6": (self.col_coord["H"], self.row_coord[6]),
            "H7": (self.col_coord["H"], self.row_coord[7]),
            "H8": (self.col_coord["H"], self.row_coord[8]),
        }

class Game:
    def __init__(self, id, opponent) -> None:
        self.id    = id
        self.opponent = opponent

    def run(self):
        running = True

