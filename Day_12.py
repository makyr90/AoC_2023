import os
from functools import lru_cache


@lru_cache(maxsize=128)
def count_arrangements(record: str, _group_nums: tuple[int], in_block: bool = False) -> int:

    # base case 1
    if len(_group_nums) == 0:
        return 1 if "#" not in record else 0
    # base case 2
    if len(record) == 0:
        return 1 if len(_group_nums) == 0 or (len(_group_nums) == 1 and _group_nums[0] == 0) else 0

    # `.` case
    if record[0] == ".":
        if in_block:
            # End of block
            if _group_nums[0] == 0:
                return count_arrangements(record[1:], _group_nums[1:], False)
            # Invalid arrangement
            else:
                return 0
        # continue with no block
        else:
            return count_arrangements(record[1:], _group_nums, False)
    # `#` case
    elif record[0] == "#":
        # invalid arrangement
        if _group_nums[0] == 0:
            return 0
        # continue block
        else:
            group_nums_cp = list(_group_nums[:])
            group_nums_cp[0] -= 1
            return count_arrangements(record[1:], tuple(group_nums_cp), True)

    # `?` case
    else:
        if in_block:
            # End of block
            if _group_nums[0] == 0:
                return count_arrangements(record[1:], _group_nums[1:], False)
            # Continue block
            else:
                group_nums_cp = list(_group_nums[:])
                group_nums_cp[0] -= 1
                return count_arrangements(record[1:], tuple(group_nums_cp), True)
        else:
            # Reached end of block we need to continue with .
            if _group_nums[0] == 0:
                return count_arrangements(record[1:], _group_nums[1:], False)
            # Either start a new block or not
            else:
                group_nums_cp = list(_group_nums[:])
                group_nums_cp[0] -= 1
                return count_arrangements(record[1:], _group_nums, False) + count_arrangements(
                    record[1:], tuple(group_nums_cp), True)


total_arrangements_p1 = 0
total_arrangements_p2 = 0
puzzle_data = open(os.path.dirname(os.path.realpath(__file__)) + "/data/day_12.txt", "r").read().split("\n")
for line in puzzle_data:
    arrangement, group_nums = line.split()
    group_counts = tuple(map(int, group_nums.split(",")))
    arrangement_p2 = "?".join([arrangement] * 5)
    group_counts_p2 = group_counts * 5
    total_arrangements_p1 += count_arrangements(arrangement, group_counts)
    total_arrangements_p2 += count_arrangements(arrangement_p2, group_counts_p2)

print("Part 1 answer: {}".format(total_arrangements_p1))
print("Part 2 answer: {}".format(total_arrangements_p2))
