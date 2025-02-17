import re
import networkx as nx
import matplotlib.pyplot as plt

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    connections = [re.findall('(\w+)-(\w+)', line)[0] for line in lines]
    return connections

def main():
    connections = read_input("day23/input/input.txt")

    G = nx.Graph()
    G.add_edges_from(connections)
    cycles_with_t = []
    for cycle in sorted(nx.simple_cycles(G, length_bound = 3)):
        for computer in cycle:
            initial_letter = computer[0]
            if initial_letter == 't':
                cycles_with_t.append(computer)
                break

    print(f"Part 1: {len(cycles_with_t)}")

    cliques = list(nx.find_cliques(G))
    largest_cliques = next(reversed(sorted(cliques, key=len)))
    print(f"Part 2: {','.join(sorted(largest_cliques))}")

if __name__ == '__main__':
    main()
