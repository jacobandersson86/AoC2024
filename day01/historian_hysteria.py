import math


def read_input(input):
    with open(input) as f:
        lines = f.readlines()

    lines = [line.strip().split()  for line in lines]

    left = [int(line[0]) for line in lines]
    right = [int(line[1]) for line in lines]

    return left, right


def part_one(left, right):
    distances = [math.fabs(a - b) for (a, b) in zip(left, right)]
    solution = int(sum(distances))
    print(f"Part 1: {solution}")


def part_two(left, right):
    last = 0
    occurrences = {}
    for v in right:
        if v > last :
            last = v
            occurrences[v] = 1
        else:
            occurrences[v] += 1

    sum = 0
    for v in left:
        if v in occurrences:
            sum += v * occurrences[v]
    print(f"Part 2: {sum}")


def main():
    left, right = read_input('input/example.txt')

    left = sorted(left)
    right = sorted(right)

    part_one(left, right)
    part_two(left, right)


if __name__ == '__main__':
    main()
