from board import Board
from position import Position
from guard import Guard
import time

def print_board(board):
    for row in board:
        for c in row:
            print(f"{c} ", end='')
        print('')


def read_input(input):
    with open(input) as f:
        lines = f.readlines()
    board = [[c for c in line.strip()] for line in lines]
    return board

def get_positions_of_item(board, item):
    return [(x, y) for y, row in enumerate(board) for x, char in enumerate(row) if char == item]

def main():
    # input = read_input("day06/input/example.txt")
    input = read_input("day06/input/input.txt")

    Board.initiate(input)
    Board.show()

    guard_position = Board.get_guard_position()
    Guard.initiate(guard_position)
    while(Board.any_guard):
        Board.move(Guard.patrol())
        Board.show()
        time.sleep(0.005)

    # Board.show()

    print(f"Part 1: {Board.count('X')}")

    pass

if __name__ == '__main__' :
    main()
