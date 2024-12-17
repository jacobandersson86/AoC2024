from position import Position
from maze import Maze
import numpy as np

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
    score = 1
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
                    return None, 0
                # Could walk left
                dir = left[dir]
                score += 1000
                continue

            # Could walk right
            dir = right[dir]
            score += 1000
            continue

        score += 1
        pos += dir

    return pos, score

def check_left_right(nodes, pos, dir):
    neighbors = []
    if pos + right[dir] in nodes:
        neighbors.append((pos + right[dir], 1002))
    if pos + left[dir] in nodes:
        neighbors.append((pos + left[dir], 1002))
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

            neighbor, score = explore_to_next_node(maze, node, dir, nodes)
            if neighbor != None:
                # Handle turning at the start.
                if maze[node] == 'S' and dir != Position(1, 0):
                    score += 1000
                neighbors.append((neighbor, score))
        neighbor_dict[node] = neighbors
    return neighbor_dict

def visit(node, visited : set, neighbors, shortest_path_table):
    node_score, _ = shortest_path_table[node]
    for neighbor, score in neighbors[node]:
        if neighbor in visited :
            continue
        last_score, _ = shortest_path_table[neighbor]
        this_score = score + node_score
        if this_score < last_score:
            shortest_path_table[neighbor] = (this_score, node)
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

def find_shortest_path(nodes, neighbors):
    # Initiate the table
    shortest_path_table = {
        nodes[0] : (0, None)
    }
    for node in nodes[1:]:
        shortest_path_table[node] = (np.inf, None)

    unvisited = set(nodes[1:])
    visited = set()

    visit(nodes[0], visited, neighbors, shortest_path_table)

    while(len(unvisited)):
        next_node = get_next_to_visit(unvisited, shortest_path_table)
        if next_node != None :
            visit(next_node, visited, neighbors, shortest_path_table)
            unvisited.remove(next_node)

    node = nodes[-1]
    path = [node]
    while node != nodes[0]:
        _, node = shortest_path_table[node]
        path.append(node)

    score, _ = shortest_path_table[nodes[-1]]
    return score, path

def main():
    maze = read_input("day16/input/example0.txt")
    maze = Maze(maze)

    nodes = find_nodes(maze)
    neighbors = find_neighbors(maze, nodes)
    score, path = find_shortest_path(nodes, neighbors)

    print(path)

    print(f"Part 1: {score}")

if __name__ == '__main__':
    main()
