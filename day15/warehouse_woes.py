from position import Position
from buffer import Buffer

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    lines = iter(lines)

    map = []
    new_line_found = False
    while not new_line_found:
        line = next(lines)
        if line == '\n':
            new_line_found = True
            continue
        map.append([chr for chr in line.strip()])

    instructions = []
    for line in lines:
        for chr in line.strip():
            instructions.append(chr)

    return map, instructions

class Item:
    def __init__(self, position : Position, buffer : Buffer):
        self.position = position
        self.buffer = buffer

    def draw(self):
        self.buffer[self.position] = self

    def can_move(self, direction : Position):
        item = self.buffer[self.position + direction]
        if item == None:
            return True
        if isinstance(item, Wall):
            return False
        if isinstance(item, Box):
            return item.can_move(direction)

    def move(self, direction : Position):
        new_pos = self.position + direction
        item = self.buffer[new_pos]
        if item != None:
            item.move(direction)
        self.buffer[self.position] = None
        self.position = new_pos
        self.buffer[self.position] = self

    def getGPS(self):
        return self.position.x + self.position.y * 100


class Robot(Item):
    character = '@'

class Wall(Item):
    character = '#'

class Box(Item):
    character = 'O'

def find_assets(warehouse):
    walls = []
    boxes = []
    robot = None

    for y, row in enumerate(warehouse):
        for x, item in enumerate(row):
            if item == '@':
                robot = Position(x, y)
            if item == '#':
                walls.append(Position(x, y))
            if item == 'O':
                boxes.append(Position(x, y))

    return walls, boxes, robot

def main():
    warehouse, instructions = read_input("day15/input/input.txt")

    wall_positions, box_positions, robot_position = find_assets(warehouse)

    buffer = Buffer(len(warehouse), len(warehouse[0]))

    walls = []
    for position in wall_positions:
        wall = Wall(position, buffer)
        wall.draw()
        walls.append(wall)

    boxes = []
    for position in box_positions:
        box = Box(position, buffer)
        box.draw()
        boxes.append(box)

    robot = Robot(robot_position, buffer)
    robot.draw()

    def draw():
        for wall in walls:
            wall.draw()
        robot.draw()
    draw()
    # buffer.show()

    direction = {
        '<' : Position(-1,  0),
        '>' : Position( 1,  0),
        'v' : Position( 0,  1),
        '^' : Position( 0, -1)
    }

    for instruction in instructions:
        if robot.can_move(direction[instruction]):
            robot.move(direction[instruction])

    draw()
    # buffer.show()

    sum = 0
    for box in boxes:
        sum += box.getGPS()
    print(f"Part 1: {sum}")



if __name__ == '__main__':
    main()
