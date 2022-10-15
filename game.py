from board import Board


class Game:
    def __init__(self):
        self.board = Board()

    def run(self):
        self.board.print()
        while True:
            x, y = self.get_input()
            if self.board.uncover_field(x, y):
                self.board.print()
                if self.board.board[y][x].bomb:
                    print(f"BOOOOM przegrales !!!")
                    break
                if self.win():
                    print("WIN")
                    break

    def get_input(self):
        x, y = None, None
        while x is None:
            input_string = input("insert x y:  ")
            input_array = input_string.split(" ")
            if len(input_array) == 2:
                try:
                    x = int(input_array[0])
                    y = int(input_array[1])
                except ValueError:
                    pass
            if x is None or not 0 <= x <= self.board.width or \
                    y is None or not 0 <= y <= self.board.height:
                print("bad coordinates")
                x, y = None, None
        return x, y

    def count_uncover(self):
        uncover_fields = 0
        for y in range(self.board.height):
            for x in range(self.board.width):
                if self.board.board[y][x].uncovered:
                    uncover_fields += 1
        return uncover_fields

    def win(self):
        return (self.board.height * self.board.width) - self.board.bombs == self.count_uncover()
