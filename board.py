from field import Field
import random


class Board:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.board = self.clean_board()

    def clean_board(self):
        return [[Field(x, y) for y in range(self.height)] for x in range(self.width)]

    def print_board(self):
        for y in range(self.height):
            print("|".join(map(lambda f: f.string(), self.board[y])))

    def add_bombs(self, bombs=10):
        while bombs > 0:
            x, y = random.randrange(self.width), random.randrange(self.height)
            if not self.board[y][x].bomb:
                self.board[y][x].bomb = True
                bombs -= 1
