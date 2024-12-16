from position import Position

class Keypad:
    def __init__(self, type = 'normal'):
        if type == 'normal':
            self.keypad = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        else:
            self.keypad = [
                [".", ".", "1", ".", "."],
                [".", "2", "3", "4", "."],
                ["5", "6", "7", "8", "9"],
                [".", "A", "B", "C", "."],
                [".", ".", "D", ".", "."]
            ]

    def __getitem__(self, position : Position):
        if position.y < 0 or position.x < 0:
            raise ValueError
        if position.y >= len(self.keypad) or position.x >= len(self.keypad[0]):
            raise ValueError
        if self.keypad[position.y][position.x] == '.':
            raise ValueError
        return self.keypad[position.y][position.x]

    def __setitem__(self, position : Position, value):
        if position.y or position.x < 0:
            raise ValueError
        if position.y >= len(self.keypad) or position.x >= len(self.keypad[0]):
            raise ValueError
        if self.keypad[position.y][position.x] == '.':
            raise ValueError
        self.map[position.y][position.x] = value



def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    return [[chr for chr in line.strip()] for line in lines]

def main():
    instructions = read_input("/Users/plejd/git/AoC2024/2016/day02/input/input.txt")
    keypad = Keypad(type='pro')

    dir_map = {
        'U' : Position(0, -1),
        'L' : Position(-1, 0),
        'R' : Position(1, 0),
        'D' : Position(0, 1),
    }

    digits = []
    pos = Position(1, 1)
    for instruction in instructions:
        for action in instruction:
            dir = dir_map[action]
            try :
                keypad[pos + dir]
            except ValueError :
                continue
            pos = pos + dir
        digits.append(keypad[pos])

    print(digits)



if __name__ == '__main__':
    main()
