from field import Field


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

    def add_bombs(self, number_of_bombs):
        for i in range(number_of_bombs):
            Field(self.width, self.height).bomb = True
        pass
