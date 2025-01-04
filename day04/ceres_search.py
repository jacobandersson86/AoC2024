import numpy as np
import itertools

def read_input(input):
    with open(input) as f:
        lines = f.readlines()

    # Split character by character
    lines = [[c for c in line.strip()] for line in lines]
    return lines

def find_all(text, expr):
    positions = []
    for y, row in enumerate(text):
        if y == 0 or y == len(text) - 1:
            continue
        for x, char in enumerate(row):
            if x == 0 or x == len(text[0]) - 1:
                continue
            if char == expr:
                positions.append((x, y))
    return positions

def get_char(text, pos):
    x, y = pos
    if x < 0 or y < 0:
        return None
    if y >= len(text) or x >= len(text[0]):
        return None

    return text[y][x]

def match_in_any_direction(text, start):
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    sum = 0
    for dx, dy in directions:
        x, y = start
        positions = [(x + dx * (i + 1), y + dy * (i + 1)) for i in range(3)]
        chars = [get_char(text, pos) for pos in positions]
        try:
            expr = ''.join(chars)
        except TypeError:
            continue
        if expr == 'MAS':
            sum += 1
    return sum

def get_expr(text, mid, ds):
    dx, dy = ds
    x, y = mid
    positions = [(x + dx * (i - 1), y + dy * (i - 1)) for i in range(3)]
    chars = [get_char(text, pos) for pos in positions]
    try:
        expr = ''.join(chars)
    except TypeError:
        return None
    return expr

def find_x_shape(text, mid):
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    directions_offset = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
    dir_len = len(directions)
    directions = itertools.cycle(directions)
    directions_offset = itertools.cycle(directions_offset)
    sum = 0
    for _ in range(dir_len):
        ds = next(directions)
        ds90 = next(directions_offset)

        expr = get_expr(text, mid, ds)
        expr90 = get_expr(text, mid, ds90)
        if expr is None or expr90 is None:
            continue
        if expr != 'MAS' or expr90 != 'MAS':
            continue
        sum += 1

    return sum

def main():
    text = read_input("day04/input/input.txt")

    starts = find_all(text, 'X')
    sum = 0
    for start in starts:
        sum += match_in_any_direction(text, start)

    print(f"Part 1: {sum}")

    sum = 0
    mids = find_all(text, 'A')
    for mid in mids:
        sum += find_x_shape(text, mid)

    print(f"Part 2: {sum}")
    #1952 is to high
    #1949 is to high

if __name__ == '__main__':
    main()
