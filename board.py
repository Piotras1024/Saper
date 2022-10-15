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
        self.board = [[Field(x, y) for y in range(self.height)] for x in range(self.width)]
        return self.board

    def print(self):
        print("y x" + " ".join(map(lambda x: str(x), range(self.width))))
        for y in range(self.height):
            print(f"{y} |" + "|".join(map(lambda x: self.board[y][x].string(self.bombs_around(x, y)), range(len(self.board[y])))) + "|")

    def add_bombs(self, bombs=10):
        while bombs > 0:
            x, y = random.randrange(self.width), random.randrange(self.height)
            if not self.board[y][x].bomb:
                self.board[y][x].add_bomb()
                bombs -= 1

    def bombs_around(self, x, y):
        bombs = 0
        for yy in range(max(y-1, 0), min(y+2, self.height)):
            for xx in range(max(x-1, 0), min(x+2, self.width)):
                if self.board[yy][xx].bomb:
                    bombs += 1
        return bombs

    def uncover_field(self, x, y):
        if not self.board[y][x].uncover():
            return False

        if self.bombs_around(x, y) == 0:
            for yy in range(max(y-1, 0), min(y+2, self.height)):
                for xx in range(max(x-1, 0), min(x+2, self.width)):
                    self.uncover_field(xx, yy)

        return True
