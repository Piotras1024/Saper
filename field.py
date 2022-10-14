class Field:
    def __init__(self, x, y, bomb=False):
        self.x = x
        self.y = y
        self.uncovered = False
        self.bomb = bomb

    def string(self):
        return f"[{self.x},{self.y}, {self.bomb}]"

    def add_bomb(self):
        if not self.bomb:
            self.bomb = True
            return True
        return False
