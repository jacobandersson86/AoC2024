from garden import Garden
from position import Position

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    lines = [[v for v in line.strip()] for line in lines]

    return lines

def search(position : Position, garden : Garden, positions : set, plant : str):
    if position in positions:
        return

    try:
        if garden[position] != plant :
            return
    except ValueError:
        # Outside of map
        return

    positions.add(position)
    garden[position] = ' '

    directions = [Position(1, 0), Position(0, 1), Position(-1, 0), Position(0, -1)]
    for direction in directions:
        search(position + direction, garden, positions, plant)

def find_patch(position, garden):
    plant = garden[position]
    positions = set()
    search(position, garden, positions, plant)
    return plant, positions

def vertical_sort(position : Position):
    return (position.x, position.y)

def count_continuous_fences(fences):
    vertical_left_fence, vertical_right_fence, horizontal_top_fence, horizontal_bottom_fence = fences

    segments = 0
    for vertical, horizontal in [(vertical_left_fence, horizontal_top_fence), (vertical_right_fence, horizontal_bottom_fence)]:
        horizontal = sorted(horizontal)
        segments += 1
        for (x1, y1), (x2, y2) in zip(horizontal, horizontal[1:]):
            if y1 != y2:
                segments += 1
                continue
            if x1 != (x2 - 1):
                segments += 1

        vertical = sorted(vertical, key=vertical_sort)
        segments += 1
        for (x1, y1), (x2, y2) in zip(vertical, vertical[1:]):
            if x1 != x2:
                segments += 1
                continue
            if y1 != (y2 - 1):
                segments += 1

    assert(segments % 2 == 0)
    print(segments)
    return segments


def main():
    garden_map = read_input("day12/input/input.txt")
    garden = Garden(garden_map)

    patches = []
    for position in garden.positions():
        if garden[position] != ' ':
            plant, positions = find_patch(position, garden)
            patches.append(positions)

    fences = []
    for positions in patches:
        vertical_left_fence = []
        vertical_right_fence = []
        horizontal_top_fence = []
        horizontal_bottom_fence = []
        for position in positions:
            # By default 4 fences.
            vertical_directions = [Position(0, -1), Position(0, 1)]
            for dir in vertical_directions:
                # If not a neighbor, add fence
                adjacent_position = dir + position
                if adjacent_position not in positions:
                    # Might look like a type, but you but a horizontal fence towards a vertical neighbor
                    if dir == Position(0, -1):
                        horizontal_top_fence.append(position)
                    else:
                        horizontal_bottom_fence.append(adjacent_position)
            horizontal_directions = [Position(-1, 0), Position(1, 0)]
            for dir in horizontal_directions:
                # If not a neighbor, add fence
                adjacent_position = dir + position
                if adjacent_position not in positions:
                    if dir == Position(-1, 0):
                        vertical_left_fence.append(position)
                    else:
                        vertical_right_fence.append(adjacent_position)
        fences.append((vertical_left_fence, vertical_right_fence, horizontal_top_fence, horizontal_bottom_fence))

    sum_part1 = 0
    sum_part2 = 0
    for positions, fences in zip(patches, fences):
        fence_lenght = sum([len(fence) for fence in fences])
        sum_part1 += len(positions) * fence_lenght
        sum_part2 += len(positions) * count_continuous_fences(fences)

    print(f"Part 1: {sum_part1}")
    print(f"Part 2: {sum_part2}")

if __name__ == '__main__':
    main()
