import os

pipes_grid = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_10.txt", "r").read().strip().splitlines()
start_letter = "S"


def find_start_pos(grid: list[list]) -> tuple:

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == start_letter:
                return row, col


# BFS
start_r, start_c = find_start_pos(pipes_grid)
queue = [[start_r, start_c, 0]]
visited_nodes = {}
start_val_values = []
while queue:

    node = queue.pop(0)
    node_pos_key = (node[0], node[1], 0)
    visited_nodes[node_pos_key] = node[2]
    neighbours = []
    node_symbol = pipes_grid[node[0]][node[1]]
    if node[0] > 0 and pipes_grid[node[0]-1][node[1]] in ["|", "7", "F"] and \
            pipes_grid[node[0]][node[1]] in ["|", "L", "J", "S"]:
        neighbours.append([node[0] - 1, node[1], node[2] + 1])
        if node_symbol == start_letter:
            start_val_values.append({"|", "L", "J"})
    if node[0] < len(pipes_grid) - 1 and pipes_grid[node[0] + 1][node[1]] in ["|", "L", "J"] and \
            pipes_grid[node[0]][node[1]] in ["|", "7", "F", "S"]:
        neighbours.append([node[0] + 1, node[1], node[2] + 1])
        if node_symbol == start_letter:
            start_val_values.append({"|", "7", "F"})
    if node[1] < len(pipes_grid[0]) - 1 and pipes_grid[node[0]][node[1] + 1] in ["-", "J", "7"] \
            and pipes_grid[node[0]][node[1]] in ["-", "L", "F", "S"]:
        neighbours.append([node[0], node[1] + 1, node[2] + 1])
        if node_symbol == start_letter:
            start_val_values.append({"-", "L", "F"})
    if node[1] > 0 and pipes_grid[node[0]][node[1] - 1] in ["-", "L", "F"] \
            and pipes_grid[node[0]][node[1]] in ["-", "J", "7", "S"]:
        neighbours.append([node[0], node[1] - 1, node[2] + 1])
        if node_symbol == start_letter:
            start_val_values.append({"-", "J", "7"})

    for neighbor in neighbours:
        neighbor_pos = (neighbor[0], neighbor[1])
        if neighbor_pos not in visited_nodes:
            visited_nodes[neighbor_pos] = neighbor[2]
            queue.append(neighbor)

print("Part 1 answer: {}".format(max(visited_nodes.values())))

# Replace start symbol to its correct pipe symbol
start_pipe_val = set.intersection(*start_val_values)
start_val = list(pipes_grid[start_r])
start_val[start_c] = str(list(start_pipe_val)[0])
pipes_grid[start_r] = "".join(start_val)


inside_count = 0
for r_idx in range(len(pipes_grid)):
    for c_idx in range(len(pipes_grid[0])):
        pos = (r_idx, c_idx)
        if pos in visited_nodes:
            continue
        n_crosses = 0
        for jdx in range(c_idx):
            n_pos = (r_idx, jdx)
            if pipes_grid[r_idx][jdx] not in "-7F" and n_pos in visited_nodes:
                n_crosses += 1
        if n_crosses % 2 == 1:
            inside_count += 1
print("Part 2 answer: {}".format(inside_count))
