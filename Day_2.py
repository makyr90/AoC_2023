import os

puzzle_data = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_2.txt", "r")
lines = puzzle_data.readlines()

game_cube_counter = {}
for line in lines:
    game_id = int(line.split(":")[0].split()[1])
    games = line.split(":")[1].split(";")
    game_cube_counter[game_id] = []
    for game in games:
        game_cubes = {"blue": 0, "green": 0, "red": 0}
        for cube_set in game.split(","):
            for cube_color in ["blue", "red", "green"]:
                if cube_set.split()[1] == cube_color:
                    game_cubes[cube_color] += int(cube_set.split()[0])
        game_cube_counter[game_id].append(game_cubes)


sum_ids = 0
for game_id, cube_sets in game_cube_counter.items():
    valid_game = True
    for cube_set in cube_sets:
        if cube_set["green"] > 13 or cube_set["red"] > 12 or cube_set["blue"] > 14:
            valid_game = False
            break
    if valid_game:
        sum_ids += game_id

print("Part 1 answer: {}".format(sum_ids))

sum_powers = 0
for game_id, cube_sets in game_cube_counter.items():
    max_green = max([x["green"] for x in cube_sets])
    max_blue = max([x["blue"] for x in cube_sets])
    max_red = max([x["red"] for x in cube_sets])
    power = max_red * max_blue * max_green
    sum_powers += power

print("Part 2 answer: {}".format(sum_powers))
