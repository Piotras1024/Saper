from field import Field
import random


class Board:
    def __init__(self, width=8, height=8, bombs=10):
        self.width = width
        self.height = height
        self.bombs = bombs
        self.board = self.clean_board()
        self.add_bombs(self.bombs)

    def clean_board(self):
        return [[Field(x, y) for y in range(self.height)] for x in range(self.width)]

    def print(self):
        print("y x" + " ".join(map(lambda x: str(x), range(self.width))))
        for y in range(self.height):
            print(f"{y} |" + "|".join(map(lambda f: f.string(), self.board[y])) + "|")

    def add_bombs(self, bombs=10):
        while bombs > 0:
            x, y = random.randrange(self.width), random.randrange(self.height)
            if not self.board[y][x].bomb:
                self.board[y][x].add_bomb()
                bombs -= 1



