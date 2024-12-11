
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

def blink(pebble_line : dict):
    next_pebble_line = {}

    for pebble, n in pebble_line.items():
        if pebble == 0:
            append_to_key(1, n, next_pebble_line)
        elif len(str(pebble)) % 2 == 0:
            pebble_str = str(pebble)
            l = len(pebble_str) // 2
            right = int(pebble_str[:l])
            left = int(pebble_str[l:])
            append_to_key(right, n, next_pebble_line)
            append_to_key(left, n, next_pebble_line)
        else:
            pebble *= 2024
            append_to_key(pebble, n, next_pebble_line)

    return next_pebble_line

def print_pebbles(pebble_line):
    length = sum(pebble_line.values())
    print(length, end='')

    if length > 6:
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

    print_pebbles(pebble_line)

    for _ in range(75):
        pebble_line = blink(pebble_line)

    print_pebbles(pebble_line)







if __name__ == '__main__':
    main()
