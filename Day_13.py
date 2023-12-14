import os


def count_diffs(_str1: str, _str2: str) -> int:

    return sum([0 if x == z else 1 for x, z in zip(_str1, _str2)])


def find_reflection_index(_pattern: list[str], allowed_dif: int = 0) -> int:
    reflection_index = 0
    for idx in range(len(_pattern)-1):
        if count_diffs(_pattern[idx], _pattern[idx+1]) in [0, allowed_dif]:
            sum_dif = 0
            valid = False
            if count_diffs(_pattern[idx], _pattern[idx + 1]) == allowed_dif:
                sum_dif += allowed_dif
            step = 2
            if idx + step >= len(_pattern) or idx - step + 1 < 0:
                if sum_dif == allowed_dif:
                    valid = True

            while idx+step < len(_pattern) and idx-step+1 >= 0:
                if count_diffs(_pattern[idx+step], _pattern[idx-step+1]) in [0, allowed_dif]:
                    valid = True
                    if count_diffs(_pattern[idx + step], _pattern[idx - step + 1]) == allowed_dif:
                        sum_dif += allowed_dif
                    if sum_dif > allowed_dif:
                        valid = False
                        break
                    step += 1
                    continue
                else:
                    valid = False
                    break
            if valid and sum_dif == allowed_dif:
                reflection_index = idx + 1

    return reflection_index


puzzle_data = open(os.path.dirname(os.path.realpath(__file__)) + "/data/day_13.txt", "r").read().split("\n\n")

total = 0
total_2 = 0
for data in puzzle_data:
    pattern = data.split("\n")
    pattern_cols = ["".join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))]
    total += 100 * find_reflection_index(pattern)
    total += find_reflection_index(pattern_cols)
    total_2 += 100 * find_reflection_index(pattern, 1)
    total_2 += find_reflection_index(pattern_cols, 1)

print("Part 1 answer: {}".format(total))
print("Part 2 answer: {}".format(total_2))
