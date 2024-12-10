class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Position({self.x}, {self.y})"
