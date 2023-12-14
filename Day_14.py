import math
import os


def rocks_tilt_west(grid: list[str], swap_dir: bool = False) -> list[str]:

    for idx in range(len(grid)):
        if swap_dir:
            row = list(reversed(list(grid[idx])))
        else:
            row = list(grid[idx])
        for jdx in range(1, len(row)):
            if row[jdx] == "O":
                roll_index = jdx
                for c_idx in range(jdx-1, -1, -1):
                    if row[c_idx] == ".":
                        roll_index = c_idx
                    else:
                        break
                if roll_index != jdx:
                    row[roll_index] = "O"
                    row[jdx] = "."
        if swap_dir:
            grid[idx] = "".join(list(reversed(row)))
        else:
            grid[idx] = "".join(row)

    return grid


def rocks_tilt_up(grid: list[str]) -> list[str]:
    for idx in range(1, len(grid)):
        for jdx in range(len(grid[0])):
            if grid[idx][jdx] == "O":
                roll_index = idx
                for r_idx in range(idx-1, -1, -1):
                    if grid[r_idx][jdx] == ".":
                        roll_index = r_idx
                    else:
                        break
                if roll_index != idx:
                    update_row = list(grid[roll_index])
                    update_row[jdx] = "O"
                    grid[roll_index] = "".join(update_row)
                    update_row2 = list(grid[idx])
                    update_row2[jdx] = "."
                    grid[idx] = "".join(update_row2)
    return grid


def cycle_move(grid: list[str]) -> list[str]:
    north = rocks_tilt_up(grid)
    west = rocks_tilt_west(north)
    south = list(reversed(rocks_tilt_up(list(reversed(west)))))
    east = rocks_tilt_west(south, True)
    return east


grid_p1 = open(os.path.dirname(os.path.realpath(__file__)) + "/data/day_14.txt", "r").read().split("\n")
rocks_tilt_up(grid_p1)
load_p1 = 0
for l_idx, line in enumerate(grid_p1):
    load_p1 += line.count("O") * (len(grid_p1) - l_idx)

print("Part 1 answer: {}".format(load_p1))

grid_p2 = open(os.path.dirname(os.path.realpath(__file__)) + "/data/day_14.txt", "r").read().split("\n")

seen_grids = {tuple(grid_p2)}
all_grids = [(tuple(grid_p2))]

counter = 0
while True:
    counter += 1
    grid_p2 = cycle_move(grid_p2)
    if tuple(grid_p2) in seen_grids:
        break
    seen_grids.add(tuple(grid_p2))
    all_grids.append(tuple(grid_p2))

grid_index = all_grids.index(tuple(grid_p2))
end_grid = all_grids[(1000000000 - grid_index) % (counter - grid_index) + grid_index]

load_p2 = 0
for l_idx, line in enumerate(end_grid):
    load_p2 += line.count("O") * (len(end_grid) - l_idx)

print("Part 2 answer: {}".format(load_p2))
