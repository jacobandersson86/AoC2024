from position import Position
from maze import Maze
import numpy as np
import copy

directions = [Position(1, 0), Position(0, 1), Position(-1, 0), Position(0, -1)]

right = {
    Position(1, 0) : Position(0, 1),
    Position(0, 1) : Position(-1, 0),
    Position(-1, 0) : Position(0, -1),
    Position(0, -1) : Position(1, 0),
}

left = {
    Position(1, 0) : Position(0, -1),
    Position(0, 1) : Position(1, 0),
    Position(-1, 0) : Position(0, 1),
    Position(0, -1) : Position(-1, 0),
}

def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    return [[chr for chr in line.strip()] for line in lines]

def find_intersection_nodes(maze : Maze):
    y_size, x_size = (len(maze.maze), len(maze.maze[0]))

    # Scan for all intersections
    nodes = []
    start_node = []
    end_node = []
    for y in range(1, y_size - 1):
        for x in range(1, x_size - 1):
            pos = Position(x, y)
            try :
                item = maze[pos]
            except ValueError:
                continue

            # Adding surrounding nodes handles the "turning" and gives a fixed score from node to node.
            surrounding = []
            for dir in directions:
                try :
                    _ = maze[pos + dir]
                except ValueError:
                    continue
                surrounding.append(pos+dir)

            if len(surrounding) > 2 :
                nodes.append(pos)

            if item == 'S' :
                start_node.append(pos)
                continue
            if item == 'E' :
                end_node.append(pos)
                continue

    return start_node + nodes + end_node


def find_nodes(maze: Maze):
    y_size, x_size = (len(maze.maze), len(maze.maze[0]))

    # Scan for all intersections
    nodes = []
    start_node = []
    end_node = []
    for y in range(1, y_size - 1):
        for x in range(1, x_size - 1):
            pos = Position(x, y)
            try :
                item = maze[pos]
            except ValueError:
                continue

            # Adding surrounding nodes handles the "turning" and gives a fixed score from node to node.
            surrounding = []
            for dir in directions:
                try :
                    _ = maze[pos + dir]
                except ValueError:
                    continue
                surrounding.append(pos+dir)

            if item == 'S' :
                start_node.append(pos)
                nodes.extend(surrounding)
                continue
            if item == 'E' :
                end_node.append(pos)
                continue

            if len(surrounding) > 2 :
                nodes.extend(surrounding)

    return start_node + nodes + end_node


def explore_to_next_node(maze, node, dir, nodes):
    nodes = set(nodes)
    pos = node + dir
    # Init to 1 since one step has been taken in the start direction
    distance = 1
    turns = 0
    dead = False

    while pos not in nodes or dead:
        try:
            maze[pos + dir]
        except ValueError:
            # We're walking into a wall. Change direction.
            try:
                maze[pos + right[dir]]
            except ValueError:
                try:
                    maze[pos + left[dir]]
                except ValueError:
                    # Dead end. Not an neighbor
                    return None, 0, 0
                # Could walk left
                dir = left[dir]
                turns += 1
                continue

            # Could walk right
            dir = right[dir]
            turns += 1
            continue

        distance += 1
        pos += dir

    return pos, distance, turns

def check_left_right(nodes, pos, dir):
    neighbors = []
    if pos + right[dir] in nodes:
        neighbors.append((pos + right[dir], 2, 1))
    if pos + left[dir] in nodes:
        neighbors.append((pos + left[dir], 2, 1))
    return neighbors

def find_neighbors(maze: Maze, nodes : list):
    neighbor_dict = {}
    for node in nodes:
        neighbors = []
        for dir in directions:
            try:
                item = maze[node + dir]
            except ValueError:
                continue

            # Check left and right, we might be in an intersection
            close_neighbors = check_left_right(nodes, node + dir, dir,)
            if len(close_neighbors) :
                neighbors.extend(close_neighbors)

            neighbor, distance, turns = explore_to_next_node(maze, node, dir, nodes)
            if neighbor != None:
                # Handle turning at the start.
                if maze[node] == 'S' and dir != Position(1, 0):
                    turns += 1
                neighbors.append((neighbor, distance, turns))
        neighbor_dict[node] = neighbors
    return neighbor_dict

def calc_score(distance, turns):
    return distance + turns * 1000

def visit(node, visited : set, neighbors, shortest_path_table):
    node_score, _ = shortest_path_table[node]
    for neighbor, distance, turns in neighbors[node]:
        score = calc_score(distance, turns)
        if neighbor in visited :
            continue
        last_score, nodes = shortest_path_table[neighbor]
        this_score = score + node_score
        if this_score <= last_score and node not in nodes:
            nodes.append(node)
            shortest_path_table[neighbor] = (this_score, nodes)
    visited.add(node)


def get_next_to_visit(unvisited, shortest_path_table):
    lowest_score = np.inf
    next_node = None
    for node in unvisited:
        score, _ = shortest_path_table[node]
        if score < lowest_score:
            lowest_score = score
            next_node = node
    return next_node

def find_paths(start_node, end_node, path, shortest_path_table):
    node = end_node
    paths = []
    other_paths = None
    while node != start_node:
        _, this_nodes = shortest_path_table[node]
        for other_node in this_nodes[1:]:
            new_path = copy.deepcopy(path)
            new_path.append(other_node)
            other_paths = find_paths(start_node, other_node, new_path, shortest_path_table)
        node = this_nodes[0]
        path.append(node)
    paths.append(path)
    if other_paths:
        paths.extend(other_paths)
    return paths

def find_shortest_path(nodes, neighbors):
    # Initiate the table
    shortest_path_table = {
        nodes[0] : (0, [])
    }
    for node in nodes[1:]:
        shortest_path_table[node] = (np.inf, [])

    unvisited = set(nodes[1:])
    visited = set()

    visit(nodes[0], visited, neighbors, shortest_path_table)

    while(len(unvisited)):
        next_node = get_next_to_visit(unvisited, shortest_path_table)
        if next_node != None :
            visit(next_node, visited, neighbors, shortest_path_table)
            unvisited.remove(next_node)

    start_node = nodes[0]
    end_node = nodes[-1]
    path = [end_node]
    paths = find_paths(start_node, end_node, path, shortest_path_table)

    score, _ = shortest_path_table[nodes[-1]]
    return score, paths

def main():
    maze = read_input("day16/input/input.txt")
    maze = Maze(maze)

    nodes = find_nodes(maze)
    neighbors = find_neighbors(maze, nodes)
    score, paths = find_shortest_path(nodes, neighbors)

    print(f"Part 1: {score}")

    nodes = find_intersection_nodes(maze)
    neighbors = find_neighbors(maze, nodes)
    score, paths = find_shortest_path(nodes, neighbors)

    total_distance = 0
    # Make pairs of all the nodes in the paths
    pairs = set()
    for path in paths:
        for p0, p1 in zip(path, path[1:]):
            pairs.add((p0, p1))

    for node, neighbor in pairs:
        data = neighbors[neighbor]
        distance_to = {position : distance for position, distance, _ in data}
        total_distance += distance_to[node]

    print(f"Part 2: {total_distance}")
    # 501 is to low
    # 540 is to high


if __name__ == '__main__':
    main()
