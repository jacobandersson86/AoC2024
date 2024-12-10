from board import Board
from position import Position
from itertools import cycle

class Guard:
    position = Position
    direction = Position
    turning_points = []

    @staticmethod
    def initiate(position : Position):
        Guard.position = position
        Guard.next_direction = cycle([
            Position(0, -1),
            Position(1, 0),
            Position(0, 1),
            Position(-1, 0)
        ])
        Guard.direction = next(Guard.next_direction)

    @staticmethod
    def patrol():
        # Peek what next tile looks like
        next_tile = Board.peek(Guard.position + Guard.direction)
        if next_tile == '#':
            Guard.turning_points.append(Guard.position)
            Guard.direction = next(Guard.next_direction)

        Guard.position += Guard.direction
        return Guard.position
