from position import Position

class Maze:
    def __init__(self, maze):
        self.maze = maze

    def __getitem__(self, position : Position):
        if position.y < 0 or position.x < 0:
            raise ValueError
        if position.y >= len(self.maze) or position.x >= len(self.maze[0]):
            raise ValueError
        if self.maze[position.y][position.x] == '#':
            raise ValueError
        return self.maze[position.y][position.x]

    def __setitem__(self, position : Position, value):
        if position.y or position.x < 0:
            raise ValueError
        if position.y >= len(self.maze) or position.x >= len(self.maze[0]):
            raise ValueError
        if self.maze[position.y][position.x] == '#':
            raise ValueError
        self.maze[position.y][position.x] = value
