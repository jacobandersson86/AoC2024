from position import Position, PositionRange
import re
from typing import List
import math

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    robots = []
    for line in lines:
        result = re.findall("p=(\d+),(\d+) v=(-{0,1}\d+),(-{0,1}\d+)", line)[0]
        robots.append((Position(int(result[0]), int(result[1])), Position(int(result[2]), int(result[3]))))

    return robots

def print_restroom(width, height, robots):
    restroom = [['.' for _ in range(width)] for _ in range(height)]

    for (x, y), _ in robots:
        if restroom[y][x] == '.':
            restroom[y][x] = 1
        else:
            restroom[y][x] += 1

    for row in restroom:
        print(''.join(str(element) for element in row))


def main():
    file = "day14/input/input.txt"
    robots = read_input(file)
    if file == "day14/input/input.txt" :
        width, height = (101, 103)
    else :
        width, height = (11, 7)

    print("Initial:")
    print_restroom(width, height, robots)

    elapsed = 0
    for _ in range(10000    ):
        seconds = 1
        board = PositionRange(Position(0, 0), Position(width, height))
        for i, (pos, speed) in enumerate(robots):
            pos = pos + speed * seconds
            pos = Position(pos.x % width, pos.y % height)
            assert(pos in board)
            robots[i] = (pos, speed)

        elapsed += seconds

        sum = 0
        mid = PositionRange(Position(width // 4, height // 4),        Position((width * 3) // 4, (height * 3) // 4))
        for pos, _ in robots:
            if pos in mid:
                sum += 1
        if sum >= (width // 4 * height // 4) / 2 :
            print(f"Part 2: After {elapsed} seconds")
            print_restroom(width, height, robots)

    q0 = PositionRange(Position(0,0),                             Position(width // 2 , height // 2))
    q1 = PositionRange(Position(width // 2 + 1 ,0),               Position(width + 1, height // 2))
    q2 = PositionRange(Position(0, height // 2 + 1),              Position(width // 2, height + 1))
    q3 = PositionRange(Position(width // 2 + 1, height // 2 + 1), Position(width +1, height + 1) )


    zones = []
    for quadrant in [q0, q1, q2, q3]:
        sum = 0
        for pos, _ in robots:
            if pos in quadrant:
                sum += 1
        print(sum)
        zones.append(sum)

    final_sum = math.prod(zones)
    print(f"Part 1 {final_sum}")

if __name__ == '__main__':
    main()
