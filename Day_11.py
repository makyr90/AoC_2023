import os


def find_expansions(_grid: list) -> tuple:

    _expanded_rows = [x for x in range(len(grid)) if "#" not in grid[x]]
    cols = ["".join([grid[row][x] for row in range(len(grid))]) for x in range(len(grid[0]))]
    _expanded_cols = [x for x in range(len(grid[0])) if "#" not in cols[x]]

    return _expanded_rows, _expanded_cols


def find_galaxies_pos(_grid: list) -> dict:

    _galaxies_pos = {}
    for r in range(len(_grid)):
        for c in range(len(_grid[0])):
            if _grid[r][c] == "#":
                _galaxies_pos[len(_galaxies_pos)+1] = [r, c]

    return _galaxies_pos


def galaxies_sum_paths(_galaxies_pos: dict, _expanded_rows: list[int], _expanded_cols: list[int],
                       expansion_val: int = 1) -> int:

    max_galaxy = max(galaxies_pos.keys())
    sum_paths = 0
    for g1 in range(1, max_galaxy):
        for g2 in range(g1 + 1, max_galaxy + 1):
            g1_pos = _galaxies_pos[g1]
            g2_pos = _galaxies_pos[g2]
            for r_idx in range(min(g1_pos[0], g2_pos[0]), max(g1_pos[0], g2_pos[0])):
                sum_paths += expansion_val if r_idx in _expanded_rows else 1
            for c_idx in range(min(g1_pos[1], g2_pos[1]), max(g1_pos[1], g2_pos[1])):
                sum_paths += expansion_val if c_idx in _expanded_cols else 1

    return sum_paths


if __name__ == '__main__':

    grid = [x for x in open(os.path.dirname(
        os.path.realpath(__file__)) + "/data/day_11.txt", "r").read().split("\n")]
    expanded_rows, expanded_cols = find_expansions(grid)
    galaxies_pos = find_galaxies_pos(grid)
    print("Part 1 answer: {}".format(galaxies_sum_paths(galaxies_pos, expanded_rows, expanded_cols, 2)))
    print("Part 2 answer: {}".format(galaxies_sum_paths(galaxies_pos, expanded_rows, expanded_cols, 1000000)))
