class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Position(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y

    def __repr__(self):
        return f"(x:{self.x}, y:{self.y})"

    def __iter__(self):
        return iter((self.x, self.y))

class PositionRange:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __contains__(self, position):
        return (self.top_left.x <= position.x < self.bottom_right.x and
                self.top_left.y <= position.y < self.bottom_right.y)
