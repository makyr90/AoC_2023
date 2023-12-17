import os


def calc_energized_tiles(grid: list[str], init_pos: tuple) -> int:

    directions = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}
    slash_dir_change = {"right": "up", "left": "down", "up": "right", "down": "left"}
    r_slash_dir_change = {"right": "down", "left": "up", "up": "left", "down": "right"}
    beam_pos = [init_pos]

    energized_tiles = set()

    while beam_pos:
        x, y, _dir = beam_pos.pop(0)
        new_x = x + directions[_dir][0]
        new_y = y + directions[_dir][1]

        # new pos out of the grid, skip
        if new_x >= len(grid) or new_x < 0 or new_y >= len(grid[0]) or new_y < 0:
            continue

        grid_val = grid[new_x][new_y]

        # Pass with no direction change
        if grid_val == "." or (grid_val == "|" and _dir in ["up", "down"]) or \
                (grid_val == "-" and _dir in ["left", "right"]):
            if (new_x, new_y, _dir) not in energized_tiles:
                energized_tiles.add((new_x, new_y, _dir))
                beam_pos.append((new_x, new_y, _dir))
        elif grid_val == "/" or grid_val == "\\":
            new_dir = slash_dir_change[_dir] if grid_val == "/" else r_slash_dir_change[_dir]
            if (new_x, new_y, new_dir) not in energized_tiles:
                energized_tiles.add((new_x, new_y, new_dir))
                beam_pos.append((new_x, new_y, new_dir))

        else:
            if grid_val == "|":
                for new_dir in ["up", "down"]:
                    if (new_x, new_y, new_dir) not in energized_tiles:
                        energized_tiles.add((new_x, new_y, new_dir))
                        beam_pos.append((new_x, new_y, new_dir))
            elif grid_val == "-":
                for new_dir in ["left", "right"]:
                    if (new_x, new_y, new_dir) not in energized_tiles:
                        energized_tiles.add((new_x, new_y, new_dir))
                        beam_pos.append((new_x, new_y, new_dir))
            else:
                print("ERROR")

    return len(set([(x[0], x[1]) for x in energized_tiles]))


puzzle_grid = open(os.path.dirname(os.path.realpath(__file__)) + "/data/day_16.txt", "r").read().split("\n")


def beam_best_start(grid: list[str]) -> int:
    config_tiles = []
    # enter from left or right
    for idx in range(len(grid)):
        config_tiles.append(calc_energized_tiles(grid, (idx, -1, "right")))
        config_tiles.append(calc_energized_tiles(grid, (idx, len(grid[0]), "left")))
    # enter from top or bottom
    for jdx in range(len(grid[0])):
        config_tiles.append(calc_energized_tiles(grid, (-1, jdx, "down")))
        config_tiles.append(calc_energized_tiles(grid, (len(grid), jdx, "up")))
    return max(config_tiles)


print("Part 1 answer: {}".format(calc_energized_tiles(puzzle_grid, (0, -1, "right"))))
print("Part 2 answer: {}".format(beam_best_start(puzzle_grid)))
