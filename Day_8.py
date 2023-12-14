import os

import numpy as np


def find_gcd(array):
    num_1 = array[0]
    num_2 = array[1]
    _gcd = gcd(num_1, num_2)
    for idx in range(2, len(array)):
        _gcd = gcd(_gcd, array[idx])

    return _gcd


directions, nodes = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_8.txt", "r").read().split("\n\n")

nodes_map = {}
for node in nodes.split("\n"):
    origin_node = node.split("=")[0].strip()
    l_node = node.split("=")[1].split(",")[0].replace("(", "").strip()
    r_node = node.split("=")[1].split(",")[1].replace(")", "").strip()
    nodes_map[origin_node] = (l_node, r_node)

start_pos = "AAA"
end_pos = "ZZZ"
dir_index = 0
total_moves = 0
while start_pos != end_pos:
    dir_index = dir_index % len(directions)
    dir_val = directions[dir_index]
    start_pos = nodes_map[start_pos][0] if dir_val == "L" else nodes_map[start_pos][1]
    dir_index += 1
    total_moves += 1

print("Part 1 answer: {}".format(total_moves))

starting_nodes = [x for x in nodes_map.keys() if x.endswith("A")]
node_moves = []

for node in starting_nodes:
    start_node = node
    total_moves = 0
    dir_index = 0
    while not start_node.endswith("Z"):
        dir_index = dir_index % len(directions)
        dir_val = directions[dir_index]
        start_node = nodes_map[start_node][0] if dir_val == "L" else nodes_map[start_node][1]
        dir_index += 1
        total_moves += 1
    node_moves.append(total_moves)

print("Part 2 answer: {}".format(np.lcm.reduce(np.array(node_moves))))
