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


def explore_neighbors(ram : RAM):
    neighbors = dict()
    for y, row in enumerate(ram.buffer):
        for x, item in enumerate(row):
            if item != None:
                continue
            node = Position(x, y)
            node_neighbors = []
            for dir in [Position(0, 1), Position(1, 0), Position(-1, 0), Position(0, -1)]:
                neighbor = node + dir
                try:
                    item = ram[neighbor]
                except ValueError:
                    continue
                if item == None:
                    node_neighbors.append(neighbor)
            neighbors[node] = node_neighbors
    return neighbors


def bfs(start, neighbors, target, ram : RAM):
    visited = {start}
    parents = dict()
    ram[start] = 'O'
    queue = [start]
    found = False
    while not found and len(queue):
        current_node = queue.pop(0)
        for node in neighbors[current_node]:
            if node == target:
                found = True
            if node not in visited:
                queue.append(node)
                visited.add(node)
                parents[node] = current_node
    if not found:
        return None

    node = target
    distance = 0
    while node != start:
        ram[node] = 'O'
        node = parents[node]
        distance += 1
    return distance


def main():
    example = "day18/input/example.txt"
    input = "day18/input/input.txt"
    run = input

    start = Position(0, 0)
    if run == example:
        shape = (7, 7)
        end = Position(6, 6)
        n = 12
    elif run == input:
        shape = (71, 71)
        end = Position(70, 70)
        n = 1024

    ram_bytes = read_input(run)

    for i in range(n, len(ram_bytes)) :
        ram = RAM(shape)
        for byte in ram_bytes[:i]:
            ram[byte] = '#'

        neighbors = explore_neighbors(ram)
        distance = bfs(start, neighbors, end, ram)
        byte = ram_bytes[i - 1]

        if distance == None:
            ram.show()
            print(f'Part 2: {byte}')
            break

        if i == n:
            ram.show()
            print(f"Part 1: {distance}")


if __name__ == '__main__':
    main()
