import numpy as np
import re

def read_input(input):
    with open(input) as f:
        lines = f.readlines()

    # Split character by character
    lines = [[c for c in line.strip()] for line in lines]
    return lines

def shape_of_text(text):
    return (len(text), len(text[0]))

def print_text(text):
    for row in text:
        for c in row:
            print(f"{c} ", end='')
        print('')

def rotate_90_cw(text):
    rows, columns = shape_of_text(text)
    rotated = [['.' for _ in range(rows)] for _ in range(columns)]

    for row, line in enumerate(text):
        for column, character in enumerate(line):
            rotated[column][rows - 1 - row] = character

    return rotated

def rotate_45_cw(text):
    rows, columns = shape_of_text(text)
    output_rows = rows + columns - 1
    rotated = [['.' for _ in range(columns)] for _ in range(output_rows)]

    # Scan Top right triangle
    lengths = [v + 1 for v in range(columns)]
    for i, length in enumerate(lengths):
        for v in range(length):
            x = v
            y = length - v - 1
            c = text[y][x]
            rotated[i][v] = c

    # Scan bottom left
    lengths = lengths[-2::-1]
    for i, length in enumerate(lengths):
        for v in range(length):
            x = columns - 1 - (length - v - 1)
            y = rows - 1 - v
            c = text[y][x]
            rotated[i + rows][v] = c

    return rotated

def count_occurrences(text, word):
    matches = []
    for line in text:
        line = ''.join(line)
        matches.append(re.findall(f"{word}", line))
    n = [1 for match in matches if len(match) != 0]
    return sum(n)

def main():
    sum = 0
    normal = read_input('input/input.txt')
    print_text(normal)
    sum += count_occurrences(normal, 'XMAS')
    sum += count_occurrences(normal, 'SAMX')
    print(sum)

    diagonal_45 = rotate_45_cw(normal)
    print()
    print_text(diagonal_45)
    sum += count_occurrences(diagonal_45, 'XMAS')
    sum += count_occurrences(diagonal_45, 'SAMX')
    print(sum)

    vertical = rotate_90_cw(normal)
    print()
    print_text(vertical)
    sum += count_occurrences(vertical, 'XMAS')
    sum += count_occurrences(vertical, 'SAMX')
    print(sum)

    diagonal_135 = rotate_45_cw(vertical)
    print()
    print_text(diagonal_135)
    sum += count_occurrences(diagonal_135, 'XMAS')
    sum += count_occurrences(diagonal_135, 'SAMX')
    print(sum)

    print(f"Part 1: {sum}")
    # 1209 is to low


if __name__ == '__main__':
    main()
