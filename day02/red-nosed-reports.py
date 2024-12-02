import copy


def sign(v):
    if v >= 0: return 1
    else: return -1


def validate_report(report):
    diff_table = [int(second - first) for first, second in zip(report, report[1:])]

    # Check always change in same direction
    for this, next in zip(diff_table, diff_table[1:]):
        if sign(this) != sign(next):
            return False

    # Check step size
    for this in diff_table:
        if abs(this) < 1 or abs(this) > 3 :
            return False

    return True


def part_one(reports):
    n_good_reports = 0
    for report in reports:
        if validate_report(report):
            n_good_reports += 1
    print(f"Part 1: {n_good_reports}")


def part_two(reports):
    n_good_reports = 0
    for report in reports:
        if validate_report(report):
            n_good_reports += 1
        else:
            # Brute force approach. Try to remove each level one by one
            results = []
            for i, _ in enumerate(report):
                culled = copy.deepcopy(report)
                del culled[i]
                results.append(validate_report(culled))

            if results.count(True) > 0:
                n_good_reports += 1

    print(f"Part 2: {n_good_reports}")


def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    lines = [line.strip().split() for line in lines]
    lines = [[int(v) for v in line] for line in lines]
    return lines


def main():
    # reports = read_input('input/example.txt')
    reports = read_input('input/input.txt')

    part_one(reports)
    part_two(reports)


if __name__ == '__main__':
    main()
