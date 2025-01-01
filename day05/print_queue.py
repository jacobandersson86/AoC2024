import re

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    rules = {}
    lines = iter(lines)
    search = True
    while search:
        line = next(lines)
        results = re.findall('(\d+)', line)
        if len(results) :
            if int(results[0]) in rules:
                rules[int(results[0])].add(int(results[1]))
            else :
                rules[int(results[0])] = set([int(results[1])])
        else: search = False

    search = True
    queues = []
    for line in lines:
        results = re.findall('(\d+)', line)
        if len(results) :
            queues.append([int(page) for page in results])

    return rules, queues

def has_correct_ordering(rules, queue):
    queue = queue
    for i, page in enumerate(queue):
        try:
            after = rules[page]
        except KeyError:
            continue
        before = set(queue[:i])
        if after.intersection(before):
            return False

    return True

def main():
    rules, queues = read_input("day05/input/input.txt")

    sum = 0
    for queue in queues:
        if has_correct_ordering(rules, queue) :
            sum += queue[len(queue) // 2]

    print(f"Part 1: {sum}")



if __name__ == '__main__':
    main()
