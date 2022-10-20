import string
from numpy import row_stack
import pygame
import engine as en
from pygame.sprite import Sprite

class Opponent:
    def __init__(self, id, name, hp) -> None:
        pass

class Board:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        margX = x
        margY = y

        PADDING = 64
        SIDE_SZ = 64

        self.col_coord = {
            "A": margX + PADDING + (0 * SIDE_SZ),
            "B": margX + PADDING + (1 * SIDE_SZ),
            "C": margX + PADDING + (2 * SIDE_SZ),
            "D": margX + PADDING + (3 * SIDE_SZ),
            "E": margX + PADDING + (4 * SIDE_SZ),
            "F": margX + PADDING + (5 * SIDE_SZ),
            "G": margX + PADDING + (6 * SIDE_SZ),
            "H": margX + PADDING + (7 * SIDE_SZ),
        }

        self.row_coord = {
            1: margY + PADDING + (0 * SIDE_SZ),
            2: margY + PADDING + (1 * SIDE_SZ),
            3: margY + PADDING + (2 * SIDE_SZ),
            4: margY + PADDING + (3 * SIDE_SZ),
            5: margY + PADDING + (4 * SIDE_SZ),
            6: margY + PADDING + (5 * SIDE_SZ),
            7: margY + PADDING + (6 * SIDE_SZ),
            8: margY + PADDING + (7 * SIDE_SZ),
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

    def draw_fselector(self, field: str):
        en.draw.img("fieldSelector640.png", *self.field_coords[field])

    def draw_rselector(self, row: str):
        en.draw.img("rowSelector640.png", *self.field_coords[f"{row}1"])

    def draw_fselector_target(self, field: str):
        en.draw.img("targetFieldSelector640.png", *self.field_coords[field])

    def draw_rselector_target(self, row: str):
        en.draw.img("targetRowSelector640.png", *self.field_coords[f"{row}1"])

    def draw(self):
        en.draw.img("board640.png", self.x, self.y)


class Piece:
    def __init__(self, spawn_field) -> None:
        self.col = spawn_field[0]
        self.row = spawn_field[1]

    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def move(start: str, direction: str, amount: str) -> str:
        cols = Piece.cols
        rows = Piece.rows

        st_col = cols.index(start[0])
        st_row = rows.index(start[1])

        col = cols[st_col]
        row = rows[st_row]

        if direction.upper() == "U":
            row = rows[st_row - amount]
        elif direction.upper() == "D":
            row = rows[st_row + amount]
        elif direction.upper() == "R":
            col = cols[st_col + amount]
        elif direction.upper() == "L":
            col = cols[st_col - amount]

        return f"{col}{row}"


class King(Sprite, Piece):
    def __init__(self, spawn_field, black: bool) -> None:
        Sprite.__init__(self)
        Piece.__init__(self, spawn_field)
        self.spawn_field = spawn_field
        self.black = black

    def goto(self, field: str):
        ...


class Queen(Sprite):
    ...


class Rook(Sprite):
    ...


class Bishop(Sprite):
    ...


class Knight(Sprite):
    ...


class Pawn(Sprite):
    ...


class Game:
    def __init__(self, id, opponent) -> None:
        self.id    = id
        self.opponent = opponent

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            board = Board(en.align.centerX(640), en.align.bottom(640))
            board.draw()
            en.draw.img("actWin300.png", 0, en.align.bottom(700))

            for event in pygame.event.get():
                if event.type == pygame.K_DOWN:
                    print("down")
                elif event.type == pygame.K_x:
                    print("x")
                    running = False
                elif event.type == pygame.QUIT:
                    print("quit")
                    running = False

            pygame.display.flip()
            clock.tick(en.RATE)


if __name__ == '__main__':
    print(Piece.move("A4", "D", 3))
