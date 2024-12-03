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


def part_two(instructions):
    # Find all "mul(a,b)", "do()" and "don't()"
    instructions = re.findall('(mul\([0-9]*,[0-9]*\))|(do\(\))|(don\'t\(\))', instructions)
    instructions = [''.join(instruction) for instruction in instructions]

    count = True
    sum = 0
    for instruction in instructions:
        if (instruction == 'do()'):
            count = True
        elif (instruction == "don\'t()"):
            count = False
        elif (count):
            (a, b) = re.findall('([0-9]{1,})', instruction)
            sum += int(a) * int(b)

    print(f"Part 2: {sum}")


def main():
    instructions = read_input('input/example2.txt')

    part_one(instructions)
    part_two(instructions)


if __name__ == '__main__':
    main()
