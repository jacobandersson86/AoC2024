import re
import itertools

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    equations = []
    for line in lines:
        numbers = re.findall('(\d+)', line)
        equations.append((int(numbers[0]), [int(n) for n in numbers[1:]]))

    return equations


def can_be_solved(solution, numbers):
    n_operations = len(numbers) - 1
    terms = [('+', '*', '||') for _ in range(n_operations)]
    operations = itertools.product(*terms)
    for operators in operations:
        sums = [numbers[0]]
        for operator, number in zip(operators, numbers[1:]):
            if operator == '*':
                sums[-1] *= number
            elif operator == '+':
                sums[-1] += number
            elif operator == '||':
                sums[-1] = int(str(sums[-1]) + str(number))

        if sums[-1] == solution:
            return True
    return False


def main():
    equations = read_input("day07/input/input.txt")

    sum = 0
    for solution, numbers in equations:
        if can_be_solved(solution, numbers):
            sum += solution

    print(f"Part 2 {sum}")


if __name__ == '__main__':
    main()
