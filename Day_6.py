import os
from functools import reduce

puzzle_data = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_6.txt", "r").read().split("\n")
time_ranges = [(int(t), int(r)) for t, r in zip(puzzle_data[0].split(":")[1].split(),
                                                puzzle_data[1].split(":")[1].split())]
time_ranges2 = (int("".join(puzzle_data[0].split(":")[1].split())),
                int("".join(puzzle_data[1].split(":")[1].split())))

win_conf_counts = []
for time_range in time_ranges:
    time, _range = time_range
    winning_conf = 0
    for t in range(1, time+1):
        if t*(time-t) > _range:
            winning_conf += 1
    win_conf_counts.append(winning_conf)

print("Part 1 answer: {}".format(reduce((lambda x, y: x * y), win_conf_counts)))
winning_conf = 0
for t in range(1, time_ranges2[0] + 1):
    if t * (time_ranges2[0] - t) > time_ranges2[1]:
        winning_conf += 1
print("Part 2 answer: {}".format(winning_conf))
