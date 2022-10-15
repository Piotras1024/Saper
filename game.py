from board import Board


class Game:
    def __init__(self):
        self.board = Board()


    def run(self):
        self.board.print()
        while True:
            x, y = self.get_input()
            if self.board.board[y][x].uncover():
                self.board.print()
                if self.board.board[y][x].bomb:
                    print(f"BOOOOM przegrales !!!")
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
