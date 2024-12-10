from board import Board
from position import Position
from guard import Guard
from typing import List
import time
import itertools

def read_input(input):
    with open(input) as f:
        lines = f.readlines()
    board = [[c for c in line.strip()] for line in lines]
    return board

def find_possible_locations(points: List[Position]):
    obstacles = []
    last_points = []
    for points in zip(points[:], points[1:], points[2:]):
        x = set([p.x for p in points])
        y = set([p.y for p in points])
        existing_points = set([(p.x, p.y) for p in points])

        # Use itertools to find all combinations of x and y
        new_points = set(itertools.product(x, y))

        # Use difference to find the point.
        diff = new_points.difference(existing_points)
        new_point = next(iter(diff), None)

        # Find if this is a top left, top right, bottom left or bottom right
        corner = str
        if new_point[1] == min(y):
            corner = 'top'
        else:
            corner = 'bottom'
        if new_point[0] == max(x):
            corner = corner + ' right'
        else:
            corner = corner + ' left'

        offset = {
            'top right' : Position(1, 0),
            'top left' : Position(0, -1),
            'bottom right' : Position(0, 1),
            'bottom left' : Position(-1, 0)
        }
        obstacle = Position(new_point[0], new_point[1]) + offset[corner]
        obstacles.append(obstacle)
        last_points.append(points[-1])

        # print(f"Points are {points}, missing corner is {new_point} ({corner}), place obstacle at {obstacle}")

    return obstacles, last_points


def main():
    input = read_input("day06/input/example.txt")
    # input = read_input("day06/input/input.txt")

    Board.initiate(input)
    Board.show()

    guard_position = Board.get_guard_position()
    Guard.initiate(guard_position)
    while(Board.any_guard):
        Board.move(Guard.patrol())
        Board.show()
        time.sleep(0.005)

    places_visited = Board.count('X')

    for p in Guard.turning_points:
        Board.board[p.y][p.x] = '+'

    Board.show()


    # Part 2
    # Take 3 turning points and see if it is possible to add a forth turning point.
    # Since the guard always turns clockwise it means that we can try to but an obstacle
    # at the missing corner and that it is predictable. For example if the bottom right corner
    # is missing, we need to add an obstacle just below the bottom right corner.
    # One can only place the obstacle if:
    # - There is nothing there already.
    # - It is on the board
    # - There is not already an on obstacle on the path between the last point and the
    #   placed obstacle.

    # Find all possible position for an obstacle.
    obstacles, last_points = find_possible_locations(Guard.turning_points)

    # Remove an obstacle if it is an obstacle in between.
    for obstacle, last_point in zip(obstacles, last_points):
        # Iterate all points between and check if there is something between.

    # # Remove obstacles outside of board
    # for obstacle in obstacles:
    #     x, y = (obstacle.x, obstacle.y)


    # Remove obstacles placed where there is already something
    for obstacle in obstacles:
        x, y = (obstacle.x, obstacle.y)
        if Board.board[y][x] == '#':
            del obstacle
        else :
            Board.board[y][x] = 'O'

    Board.show()
    print(f"Part 1: {places_visited}")
    print(len(obstacles))


if __name__ == '__main__' :
    main()
