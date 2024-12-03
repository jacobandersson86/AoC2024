import re

def read_input(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    # Flatten lines
    return ''.join(lines)

def part_one(instructions):
    # Find all "mul(a,b)"
    instructions = re.findall('(mul\([0-9]*,[0-9]*\))', instructions)

    # Parse out the numbers
    numbers = [re.findall('([0-9]{1,})', instruction) for instruction in instructions]

    # Count
    sum = 0
    for a, b in numbers:
        sum += int(a) * int(b)

    print(f"Part 1: {sum}")


def main():
    instructions = read_input('input/input.txt')
    # instructions = read_input('input/example.txt')

    part_one(instructions)


if __name__ == '__main__':
    main()
