from position import Position
from buffer import Buffer
import itertools

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
        self.size = (2, 1)
        self.buffer = buffer

    def draw(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.buffer[self.position + Position(1 * x, 1 * y)] = self

    def can_move(self, direction : Position):
        items = []
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                items.append(self.buffer[self.position + direction + Position(1 * x, 1 * y)])

        if any(items) == False and items[0] == None:
            return [True]

        ret_vals = []
        for item in items:
            if item == self:
                continue
            if isinstance(item, Wall):
                return [False]
            if isinstance(item, Box):
                ret_vals.extend(item.can_move(direction))
        return ret_vals

    def move(self, direction : Position):
        new_pos  = self.position + direction
        new_places = []
        old_places = []
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                new_places.append(Position(new_pos.x + x, new_pos.y + y))
                old_places.append(Position(self.position.x + x, self.position.y + y))


        items = set([self.buffer[place] for place in new_places])
        for item in items:
            if item != None and item != self:
                item.move(direction)

        for place in old_places:
            self.buffer[place] = None
        for place in new_places:
            self.buffer[place] = self
        self.position = new_pos

    def getGPS(self):
        return self.position.x + self.position.y * 100


class Robot(Item):
    character = itertools.cycle(['@'])

    def __init__(self, position, buffer):
        super().__init__(position, buffer)
        self.size = (1, 1)

class Wall(Item):
    character = itertools.cycle(['#'])

class Box(Item):
    character = itertools.cycle(['[', ']'])

def find_assets(warehouse):
    walls = []
    boxes = []
    robot = None

    for y, row in enumerate(warehouse):
        for x, item in enumerate(row):
            if item == '@':
                robot = Position(x * 2, y)
            if item == '#':
                walls.append(Position(x * 2, y))
            if item == 'O':
                boxes.append(Position(x * 2, y))

    return walls, boxes, robot

def main():
    warehouse, instructions = read_input("day15/input/example_large.txt")

    wall_positions, box_positions, robot_position = find_assets(warehouse)

    buffer = Buffer(len(warehouse), len(warehouse[0] * 2))

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
    buffer.show()


    direction = {
        '<' : Position(-1,  0),
        '>' : Position( 1,  0),
        'v' : Position( 0,  1),
        '^' : Position( 0, -1)
    }

    for instruction in instructions:
        if all(robot.can_move(direction[instruction])):
            robot.move(direction[instruction])

    draw()
    buffer.show()

    sum = 0
    for box in boxes:
        sum += box.getGPS()
    print(f"Part 1: {sum}")



if __name__ == '__main__':
    main()
