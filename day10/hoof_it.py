
from topographic import Topographic
from position import Position
import itertools

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    lines = [[int(v) for v in line.strip()] for line in lines]

    return lines

def take_step(topo : Topographic, position : Position):
    if topo[position] == 9:
        return [position]

    directions = [Position(0, 1), Position(1,0), Position(0, -1), Position(-1, 0)]
    new_positions = [position + direction for direction in directions]

    present_height = topo[position]
    # Remove if outside map or not exactly plus one in height
    correct_height = []
    for i, pos in enumerate(new_positions):
        try:
            height = topo[pos]
        except ValueError:
            continue
        if height == present_height + 1:
            correct_height.append(pos)

    heights = []
    for pos in correct_height:
        heights.extend(take_step(topo, pos))

    return heights


def find_heights_from_head(topo : Topographic, head : Position):
    return take_step(topo, head)


def main():
    lines = read_input("day10/input/example.txt")

    topographic = Topographic(lines)

    trail_heads = topographic.get_trail_heads()
    heights = topographic.get_heights()

    # Start at each trail head and see how many heights can be reached.
    scores = {}
    ratings = {}
    for trail_head in trail_heads:
        found_paths_to_a_height = find_heights_from_head(topographic, trail_head)
        found_heights = set(found_paths_to_a_height)

        score = len(list(found_heights))
        scores[trail_head] = score

        rating = len(found_paths_to_a_height)
        ratings[trail_head] = rating

    print(f"Part 1: {sum(scores.values())}")
    print(f"Part 2: {sum(ratings.values())}")

if __name__ == '__main__':
    main()
