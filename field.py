class Field:
    def __init__(self, x, y, bomb=False):
        self.x = x
        self.y = y
        self.uncovered = False
        self.bomb = bomb

    def string(self, bombs_around=0):
        if self.uncovered:
            if self.bomb:
                return "B"
            if bombs_around == 0:
                return f"_"
            return str(bombs_around)
        return "x"

    def add_bomb(self):
        if not self.bomb:
            self.bomb = True
            return True
        return False

    def uncover(self):
        if self.uncovered:
            return False
        self.uncovered = True
        return True

