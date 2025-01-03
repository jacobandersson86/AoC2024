
def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    lines = iter(lines)

    map = []
    new_line_found = False
    while not new_line_found:
        line = next(lines)
        if line == '\n':
            new_line_found = True
            continue
        map.append([chr for chr in line.strip()])

    instructions = []
    for line in lines:
        for chr in line.strip():
            instructions.append(chr)

    return map, instructions


def main():
    warehouse, instructions = read_input("day15/input/example_large.txt")

    print(warehouse)
    print(instructions)

if __name__ == '__main__':
    main()
