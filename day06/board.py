from position import Position
import os
import sys

class Board:
    board = []
    previous_board = []
    any_guard = bool

    def __getitem__(self, position):
        return self.board[position.y][position.x]

    def __setitem__(self, position, value):
        self.board[position.y][position.x] = value

    @staticmethod
    def initiate(input):
        Board.board = input
        Board.previous_board = [[' ' for _ in row] for row in Board.board]
        Board.any_guard = True
        Board.first_show = True

    @staticmethod
    def show():
        if Board.first_show:
            Board.first_show = False
            os.system('clear')

        print("\033[H", end='')

        for y, row in enumerate(Board.board):
            for x, c in enumerate(row):
                if Board.previous_board[y][x] != c:
                    # Move the cursor to the position (y, x)
                    print(f"\033[{y+1};{x*2+1}H{c} ", end='')

        Board.previous_board = [row[:] for row in Board.board]
        # Move the cursor to the position after the last printed character
        print(f"\033[{len(Board.board)+1};1H", end='')

        # Flush the output buffer
        sys.stdout.flush()

    @staticmethod
    def draw(position, item):
        Board.board[position.y][position.x] = item

    @staticmethod
    def get_guard_position():
        return Board._get_positions_of_item('^')[0]

    @staticmethod
    def move(position):
        start = Board.get_guard_position()
        item = Board.board[start.y][start.x]

        Board.board[start.y][start.x] = 'X'  # Leave a trail

        if not position.y in range(len(Board.board)) or not position.x in range(len(Board.board[0])):
            Board.any_guard = False
            return

        Board.board[position.y][position.x] = item

    @staticmethod
    def peek(position):
        if not position.y in range(len(Board.board)) or not position.x in range(len(Board.board[0])):
            return None
        return Board.board[position.y][position.x]

    @staticmethod
    def count(item):
        count = 0
        for row in Board.board:
            for c in row:
                if c == item:
                    count += 1
        return count

    @staticmethod
    def _get_positions_of_item(item):
        return [Position(x, y) for y, row in enumerate(Board.board) for x, char in enumerate(row) if char == item]
