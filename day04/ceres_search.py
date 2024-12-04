import numpy as np

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

def rotate_90(text):
    # TODO Doesn't rotate, it flips along diagonal (but is this what I want?? )
    rows, columns = shape_of_text(text)
    rotated = [['.' for _ in range(rows)] for _ in range(columns)]

    for i, row in enumerate(text):
        for j, c in enumerate(row):
            rotated[j][i] = c

    return rotated

def rotate_45(text):

    start_points = [[]]


def main():
    normal = read_input('input/example.txt')

    print_text(normal)

    vertical = rotate_90(normal)

    print()
    print_text(vertical)

if __name__ == '__main__':
    main()
