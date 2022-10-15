class Field:
    def __init__(self, x, y, bomb=False):
        self.x = x
        self.y = y
        self.uncovered = False
        self.bomb = bomb

    def string(self):
        if self.uncovered:
            if self.bomb:
                return "B"
            return f"_"
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

