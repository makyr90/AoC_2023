import os

sensor_readings = [list(map(int, x.split())) for x in open(os.path.dirname(
    os.path.realpath(__file__))+"/data/day_9.txt", "r").read().split("\n")]


def extrapolate_row(readings: list[int], backward_flag: bool = False) -> int:

    if readings.count(0) == len(readings):
        return 0
    else:
        new_row = [readings[i] - readings[i-1] for i in range(1, len(readings))]
        if backward_flag:
            return readings[0] - extrapolate_row(new_row, True)
        else:
            return readings[-1] + extrapolate_row(new_row)


sum_readings = 0
sum_readings_backward = 0
for row in sensor_readings:
    sum_readings += extrapolate_row(row)
    sum_readings_backward += extrapolate_row(row, True)

print("Part 1 answer: {}".format(sum_readings))
print("Part 2 answer: {}".format(sum_readings_backward))
