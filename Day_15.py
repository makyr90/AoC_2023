import os


def get_hash(_input: str) -> int:
    c_val = 0
    for char in _input:
        c_val += ord(char)
        c_val *= 17
        c_val = c_val % 256
    return c_val


def calc_lens_focus(_input_hashes: list[str]) -> int:
    boxes_dict = {}
    for hs in _input_hashes:
        if "=" in hs:
            label, value = hs.split("=")
            box_id = get_hash(label)
            if box_id not in boxes_dict:
                boxes_dict[box_id] = [(label, value)]
            else:
                if label not in [x[0] for x in boxes_dict[box_id]]:
                    boxes_dict[box_id].append((label, value))
                else:
                    label_index = [x[0] for x in boxes_dict[box_id]].index(label)
                    boxes_dict[box_id][label_index] = (label, value)
        elif "-" in hs:
            label, value = hs.split("-")
            box_id = get_hash(label)
            if box_id in boxes_dict and label in [x[0] for x in boxes_dict[box_id]]:
                label_index = [x[0] for x in boxes_dict[box_id]].index(label)
                boxes_dict[box_id].pop(label_index)
        else:
            print("ERROR")

    focusing_power = 0

    for box_id, lens in boxes_dict.items():
        for l_idx, _len in enumerate(lens):
            focusing_power += (box_id + 1) * (l_idx + 1) * int(_len[1])

    return focusing_power


puzzle_data = open(os.path.dirname(os.path.realpath(__file__)) + "/data/day_15.txt", "r").read().split(",")
print("Part 1 answer: {}".format(sum([get_hash(x.strip()) for x in puzzle_data])))
print("Part 2 answer: {}".format(calc_lens_focus(puzzle_data)))
