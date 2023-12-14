import os

puzzle_data = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_5.txt", "r").read().split("\n\n")

seeds_p1 = puzzle_data[0].split(":")[1].split()
seeds_p2_ranges = []
seeds_nums = puzzle_data[0].split(":")[1].split()
for idx in range(0, len(seeds_nums)-1, 2):
    seeds_p2_ranges.append((int(seeds_nums[idx]), int(seeds_nums[idx])+int(seeds_nums[idx+1])))

mapping_dicts = []
for data_block in puzzle_data[1:]:
    data_dict = {}
    for row in data_block.split("\n")[1:]:
        _destination, source, _range = row.split()
        source_end = int(source) + int(_range)
        _destination_end = int(_destination) + int(_range)
        data_dict[str(source)+"_"+str(source_end)+"_"+str(_range)] = str(_destination)+"_"+str(
            _destination_end)+"_"+str(_range)
    mapping_dicts.append(data_dict)

location_vals = []
for seed in seeds_p1:
    lookup_val = int(seed)
    for data_dict in mapping_dicts:
        for s_range, d_range in data_dict.items():
            if lookup_val in range(int(s_range.split("_")[0]), int(s_range.split("_")[1])+1):
                range_diff = lookup_val - int(s_range.split("_")[0])
                lookup_val = int(d_range.split("_")[0]) + range_diff
                break
    location_vals.append(lookup_val)

print("Part 1 answer: {}".format(min(location_vals)))

for mapping_dict in mapping_dicts:
    new_mappings = []
    while len(seeds_p2_ranges) > 0:
        seed_start, seed_end = seeds_p2_ranges.pop()
        mapped = False
        for s_range, d_range in mapping_dict.items():
            source_range_start = int(s_range.split("_")[0])
            source_range_end = int(s_range.split("_")[1])
            destination_range_start = int(d_range.split("_")[0])
            destination_range_end = int(d_range.split("_")[1])

            # Compute intersection
            inter_start = max(source_range_start, seed_start)
            inter_end = min(source_range_end, seed_end)
            if inter_end > inter_start:
                offset = destination_range_start - source_range_start
                new_mappings.append((inter_start+offset, inter_end+offset))
                # Not complete intersection, append leftover ranges
                if inter_start > seed_start:
                    seeds_p2_ranges.append((seed_start, inter_start))
                if inter_end < seed_end:
                    seeds_p2_ranges.append((inter_end, seed_end))
                mapped = True
                break
        if not mapped:
            new_mappings.append((seed_start, seed_end))

    seeds_p2_ranges = new_mappings

print("Part 2 answer: {}".format(min([x[0] for x in seeds_p2_ranges])))
