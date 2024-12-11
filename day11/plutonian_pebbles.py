import functools

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    pebbles = [int(pebble) for line in lines for pebble in line.strip().split()]
    return pebbles

def append_to_key(key, value, dict):
    try :
        dict[key] += value
    except KeyError as e:
        dict[key] = value
    return key

@functools.lru_cache(maxsize=None)
def apply_rules(pebble):
    if pebble == 0:
        return [1]
    elif len(str(pebble)) % 2 == 0:
        pebble_str = str(pebble)
        l = len(pebble_str) // 2
        right = int(pebble_str[:l])
        left = int(pebble_str[l:])
        return [left, right]
    else:
        pebble *= 2024
        return [pebble]

def blink(pebble_line : dict):
    items = [(pebble, n) for pebble, n in pebble_line.items()]
    for pebble, n in items:
        if n == 0:
            continue

        # Remove the item from this blink
        pebble_line[pebble] -= n

        new_pebbles = apply_rules(pebble)

        for p in new_pebbles:
            append_to_key(p, n, pebble_line)


def print_pebbles(pebble_line):
    length = sum(pebble_line.values())
    print(length, end='')

    if length > 25:
        print()
        return

    line = []
    for pebble, n in pebble_line.items():
        line.extend([pebble] * n)

    print(line)

def main():
    pebbles = read_input("day11/input/input.txt")

    pebble_line = {}
    for pebble in pebbles:
        pebble_line[pebble] = 1

    # print_pebbles(pebble_line)

    for _ in range(75):
        blink(pebble_line)

    print_pebbles(pebble_line)








if __name__ == '__main__':
    main()
