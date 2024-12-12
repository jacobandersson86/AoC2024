
from typing import List
from position import Position

class Garden:

    def __getitem__(self, position : Position):
        if position.y < 0 or position.x < 0:
            raise ValueError
        if position.y >= len(self.map) or position.x >= len(self.map[0]):
            raise ValueError
        return self.map[position.y][position.x]

    def __setitem__(self, position : Position, value):
        if position.y < 0 or position.x < 0:
            raise ValueError
        if position.y >= len(self.map) or position.x >= len(self.map[0]):
            raise ValueError
        self.map[position.y][position.x] = value

    def __init__(self, map):
        self.map = map

    def find_item(self, searched_item : int) -> List[Position]:
        positions = []
        for y, line in enumerate(self.map):
            for x, item in enumerate(line):
                if item == searched_item:
                    positions.append(Position(x, y))
        return positions

    def positions(self) -> List[Position]:
        return [Position(x, y) for y, row in enumerate(self.map) for x in range(len(row)) ]
