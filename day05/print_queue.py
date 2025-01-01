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

def corrected_queue(rules, queue):
    for i, page in enumerate(queue):
        try:
            after = rules[page]
        except KeyError:
            continue
        before = set(queue[:i])
        if after.intersection(before):
            queue.pop(i)
            queue.insert(i - 1, page)
            corrected_queue(rules, queue)
    return queue

def main():
    rules, queues = read_input("day05/input/input.txt")

    correct_mids = 0
    corrected_mids = 0
    for queue in queues:
        if has_correct_ordering(rules, queue) :
            correct_mids += queue[len(queue) // 2]
        else:
            new_queue = [v for v in reversed(corrected_queue(rules, queue))]
            corrected_mids += new_queue[len(new_queue) // 2]

    print(f"Part 1: {correct_mids}")
    print(f"Part 2: {corrected_mids}")

if __name__ == '__main__':
    main()
