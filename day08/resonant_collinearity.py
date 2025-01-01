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

def main():
    map = read_input("day08/input/input.txt")
    antennas = find_antennas(map)

    anti_nodes = []
    for frequency in antennas.keys():
        positions = antennas[frequency]
        anti_nodes.extend(find_anti_nodes(positions))

    n_nodes = count_nodes_in_map(map, anti_nodes)
    print(f"Part 1: {n_nodes}")


if __name__ == '__main__':
    main()
