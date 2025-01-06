from position import Position

class Buffer:
    def __init__(self, height, width):
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
        if self.buffer[position.y][position.x] != value:
            if self.buffer[position.y][position.x] != None and value != None:
                raise ValueError
        self.buffer[position.y][position.x] = value

    def show(self):
        print_buffer = []
        for row in self.buffer:
            for item in row:
                if item == None:
                    print_buffer.append(' ')
                    continue
                print_buffer.append(item.character)
            print_buffer.append('\n')

        print(''.join(print_buffer), end='')

