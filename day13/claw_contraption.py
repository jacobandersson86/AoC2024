import numpy as np
from position import Position
import re

def read_input(file):
    with open(file) as f:
        data = f.read()

    # Split the data into groups
    groups = data.strip().split("\n\n")

    # Initialize an empty list to store the tuples
    result = []

    # Iterate over each group
    for group in groups:
        # Find all digits in the group
        digits = re.findall(r'\d+', group)
        # Convert the digits to integers
        digits = list(map(int, digits))
        # Create Position objects
        posA = Position(digits[0], digits[1])
        posB = Position(digits[2], digits[3])
        prize = Position(digits[4], digits[5])
        # Store the Position objects in a tuple
        result.append((posA, posB, prize))

    return result

def catch_price(dirA : Position, dirB : Position, target : Position):
    xa, ya = dirA
    xb, yb = dirB
    xt, yt = target

    # Coefficient matrix
    A = np.array([[xa, xb], [ya, yb]])

    # Constant matrix
    B = np.array([xt, yt])

    # Check if determinant is non-zero
    det = np.linalg.det(A)
    if det == 0:
        # Can't catch the price, the determinant is 0, skip!
        return None, None

    # Solve for n and m
    solution = np.linalg.solve(A, B)
    n, m = solution[0], solution[1]

    tolerance = 0.001
    if abs(n - np.rint(n)) > tolerance or abs(m - np.rint(m)) > tolerance:
        # Can't catch the price, not an integer solution, skip!
        return None, None

    # Press a :n times, b : m times
    return np.rint(n).astype(int), np.rint(m).astype(int)


def main():
    machines = read_input("day13/input/input.txt")

    cost = 0
    for button_a, button_b, price in machines:
        n, m = catch_price(button_a, button_b, price)
        if n != None:
            cost += n * 3 + m

    print(f"Part 1: {cost}")

    cost = 0
    for button_a, button_b, price in machines:
        n, m = catch_price(button_a, button_b, price + Position(10000000000000, 10000000000000))
        if n != None:
            cost += n * 3 + m

    print(f"Part 2: {cost}")

if __name__ == '__main__':
    main()
