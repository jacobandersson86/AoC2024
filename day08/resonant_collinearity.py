import itertools

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    map = []
    for line in lines:
        row = [chr for chr in line.strip()]
        map.append(row)
    return map

def find_antennas(map):
    antennas = {}
    for y, row in enumerate(map):
        for x, chr in enumerate(row):
            if chr == '.':
                continue

            if chr in antennas:
                antennas[chr].append((x, y))
            else:
                antennas[chr] = [(x, y)]
    return antennas

def find_anti_nodes(positions):
    anti_nodes = []
    for (xa, ya), (xb, yb) in itertools.combinations(positions, 2):
        dx, dy = xb - xa, yb - ya
        anti_nodes.append((xa - dx, ya - dy))
        anti_nodes.append((xb + dx, yb + dy))
    return anti_nodes


def in_map_range(map, position):
    x, y = position
    if x < 0 or y < 0:
        return False
    if x >= len(map[0]) or y >= len(map):
        return False
    return True


def find_all_anti_nodes(map, positions):
    anti_nodes = []
    for (xa, ya), (xb, yb) in itertools.combinations(positions, 2):
        dx, dy = xb - xa, yb - ya

        anti_nodes.append((xa, ya))
        anti_nodes.append((xb, yb))

        # Extend in first direction
        new_pos = (xa - dx, ya - dy)
        while in_map_range(map, new_pos):
            anti_nodes.append(new_pos)
            x, y = new_pos
            new_pos = (x - dx, y - dy)

        new_pos = (xb + dx, yb + dy)
        while in_map_range(map, new_pos):
            anti_nodes.append(new_pos)
            x, y = new_pos
            new_pos = (x + dx, y + dy)

    return anti_nodes

def count_nodes_in_map(map, nodes):
    nodes = [node for node in set(nodes)]
    sum = 0
    for (x, y) in nodes:
        if x < 0 or y < 0:
            continue
        if x >= len(map[0]) or y >= len(map):
            continue
        sum += 1
    return sum

def print_map(map):
    for row in map:
        print(''.join(row))

def add_nodes(map, nodes):
    for (x, y) in nodes:
        map[y][x] = '#'

def main():
    map = read_input("day08/input/input.txt")
    antennas = find_antennas(map)

    anti_nodes = []
    extended_nodes = []
    for frequency in antennas.keys():
        positions = antennas[frequency]
        anti_nodes.extend(find_anti_nodes(positions))
        extended_nodes.extend(find_all_anti_nodes(map, positions))

    n_nodes = count_nodes_in_map(map, anti_nodes)
    print(f"Part 1: {n_nodes}")

    n_nodes = count_nodes_in_map(map, extended_nodes)
    print(len(extended_nodes))
    add_nodes(map, extended_nodes)
    print_map(map)
    print(f"Part 2: {n_nodes}")



if __name__ == '__main__':
    main()
