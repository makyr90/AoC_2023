import os
import copy

puzzle_data = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_3.txt", "r").read().splitlines()

number_indexes = []
symbol_indexes = {}
for r_idx in range(len(puzzle_data)):
    digit_found = False
    for c_idx in range(len(puzzle_data[r_idx])):
        if puzzle_data[r_idx][c_idx].isdigit() and not digit_found:
            number = puzzle_data[r_idx][c_idx]
            digit_found = True
        elif not(puzzle_data[r_idx][c_idx].isdigit()) and digit_found:
            digit_found = False
            if puzzle_data[r_idx][c_idx] != ".":
                symbol_indexes[str(r_idx) + "|" + str(c_idx)] = puzzle_data[r_idx][c_idx]
            if len(number) == 1:
                indexes = [str(r_idx)+"|"+str(c_idx-1)]
            else:
                indexes = [str(r_idx)+"|"+str(c_idx-1 - x) for x in range(len(number)-1, -1, -1)]
            number_indexes.append((number, indexes))
        elif puzzle_data[r_idx][c_idx].isdigit() and digit_found:
            number += puzzle_data[r_idx][c_idx]
        else:
            if puzzle_data[r_idx][c_idx] != ".":
                symbol_indexes[str(r_idx)+"|"+str(c_idx)] = puzzle_data[r_idx][c_idx]
    if digit_found:
        if len(number) == 1:
            indexes = [str(r_idx) + "|" + str(c_idx - 1)]
        else:
            indexes = [str(r_idx) + "|" + str(c_idx - 1 - x) for x in range(len(number) - 1, -1, -1)]
        number_indexes.append((number, indexes))

parts_num_sum = 0
for num_index_pair in number_indexes:
    num = int(num_index_pair[0])
    indexes = num_index_pair[1]
    valid_part = False
    for _index in indexes:
        _index_r, _index_c = _index.split("|")
        for r_idx in range(-1, 2):
            for c_idx in range(-1, 2):
                if str(int(_index_r)+r_idx)+"|"+str(int(_index_c)+c_idx) in symbol_indexes:
                    valid_part = True

    if valid_part:
        parts_num_sum += num

print("Part 1 answer: {}".format(parts_num_sum))

star_indexes = []
for pos, symbol in symbol_indexes.items():
    if symbol == "*":
        star_indexes.append(pos)

indexes_num_dict = {}
for num_index_pair in number_indexes:
    num = int(num_index_pair[0])
    indexes = num_index_pair[1]
    indexes_cp = copy.deepcopy(indexes)
    for index in indexes:
        indexes_num_dict[index] = [num, indexes_cp]

sum_gear_ratios = 0
for star_index in star_indexes:
    _index_r, _index_c = star_index.split("|")
    numbers = []
    seen_indexes = []
    for r_idx in range(-1, 2):
        for c_idx in range(-1, 2):
            check_pos = str(int(_index_r)+r_idx)+"|"+str(int(_index_c)+c_idx)
            if check_pos in indexes_num_dict and check_pos not in seen_indexes:
                numbers.append(indexes_num_dict[check_pos][0])
                seen_indexes.extend(indexes_num_dict[check_pos][1])
    if len(numbers) == 2:
        sum_gear_ratios += numbers[0] * numbers[1]

print("Part 2 answer: {}".format(sum_gear_ratios))
