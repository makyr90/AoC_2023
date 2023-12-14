import os

puzzle_data = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_1.txt", "r")
lines = puzzle_data.readlines()


def nums_replacement(val_str: str) -> str:

    repl_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
                 "seven": "7", "eight": "8", "nine": "9", }

    l_val = ""
    index_l = 0
    for idx, letter in enumerate(list(val_str)):
        if index_l == 0:
            l_val += letter
            if letter.isdigit():
                break
            for num_str, num_digit in repl_dict.items():
                if num_str in l_val:
                    l_val = l_val.replace(num_str, num_digit)
                    index_l = idx
                    break

    r_index = 0
    r_val = ""
    for jdx in range(len(val_str)-1, index_l, -1):
        r_val = val_str[jdx] + r_val
        if val_str[jdx].isdigit():
            r_index = jdx
        if r_index == 0:
            for num_str, num_digit in repl_dict.items():
                if num_str in r_val:
                    r_val = r_val.replace(num_str, num_digit)
                    r_index = jdx
                    break
    return l_val+r_val


def find_calibration(val_str: str) -> int:
    digits = []
    for letter in list(val_str):
        if letter.isdigit():
            digits.append(letter)
            break
    for letter in reversed(list(val_str)):
        if letter.isdigit():
            digits.append(letter)
            break

    return int("".join(digits))


calibration_value_part_1 = 0
calibration_value_part_2 = 0

for line in lines:
    line = line.replace("\n", "").strip()
    calibration_value_part_1 += find_calibration(line)
    calibration_value_part_2 += find_calibration(nums_replacement(line))

print("Part 1 answer: {}".format(calibration_value_part_1))
print("Part 2 answer: {}".format(calibration_value_part_2))
