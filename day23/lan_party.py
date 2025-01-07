import re
import networkx as nx
import matplotlib.pyplot as plt

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    connections = [re.findall('(\w+)-(\w+)', line)[0] for line in lines]
    return connections

def main():
    connections = read_input("day23/input/example.txt")

    G = nx.Graph()
    G.add_edges_from(connections)
    cycles_with_t = []
    for cycle in sorted(nx.simple_cycles(G, length_bound = 3)):
        for computer in cycle:
            initial_letter = computer[0]
            if initial_letter == 't':
                cycles_with_t.append(computer)
                break

    for cycle in cycles_with_t:
        print(cycle)

    print(f"Part 1 {len(cycles_with_t)}")

    max_connection = 0
    max_cycle = None
    for cycle in sorted(nx.simple_cycles(G)):
        if len(cycle) > max_connection:
            max_cycle = cycle
            max_connection = len(cycle)

    print(max_cycle)

    # nodes = nx.nodes(G)


    # for node in nodes:
    #     print(node)
    #     print(list(G.edges(node)))


    # # subax1 = plt.subplot(121)
    # nx.draw(G, with_labels=True, font_weight='bold')

    # # print(list(nx.find_cycle(G)))
    # plt.show()



if __name__ == '__main__':
    main()
