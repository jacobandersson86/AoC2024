from position import Position
import re

class RAM:
    def __init__(self, shape):
        width, height = shape
        self.buffer = [[None for _ in range(width)] for _ in range(height)]

    def __getitem__(self, position : Position):
        if position.y < 0 or position.x < 0:
            raise ValueError
        if position.y >= len(self.buffer) or position.x >= len(self.buffer[0]):
            raise ValueError
        return self.buffer[position.y][position.x]

    def __setitem__(self, position : Position, value):
        if position.y < 0 or position.x < 0:
            raise ValueError
        if position.y >= len(self.buffer) or position.x >= len(self.buffer[0]):
            raise ValueError
        self.buffer[position.y][position.x] = value

    def show(self):
        print_buffer = []
        for row in self.buffer:
            for item in row:
                if item == None:
                    print_buffer.append('.')
                    continue
                print_buffer.append(item)
            print_buffer.append('\n')

        print(''.join(print_buffer), end='')


def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    ram_bytes = []
    for line in lines:
        found = re.findall("(\d+),(\d+)", line)[0]
        x, y = int(found[0]), int(found[1])
        ram_bytes.append(Position(x, y))

    return ram_bytes

def main():
    example = "day18/input/example.txt"
    input = "day18/input/input.txt"
    run = input

    start = Position(0, 0)
    if run == example:
        shape = (7, 7)
        end = (6, 6)
        n = 12
    elif run == input:
        shape = (71, 71)
        end = Position(70, 70)
        n = 1024

    ram_bytes = read_input(run)

    ram = RAM(shape)
    for byte in ram_bytes[:n]:
        ram[byte] = '#'

    ram.show()






if __name__ == '__main__':
    main()
