import os

puzzle_data = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_4.txt", "r").read().splitlines()

points = 0
card_matches = {}
for card_idx, card in enumerate(puzzle_data):
    winning_numbers = card.split("|")[0].split(":")[1].split()
    numbers = card.split("|")[1].split()
    matches = 0
    count_matches = 0
    for num in numbers:
        if num in winning_numbers:
            count_matches += 1
            if matches == 0:
                matches = 1
            else:
                matches = matches * 2
    card_matches[card_idx+1] = count_matches
    points += matches

print(points)
total_cards = {}

for card, wins in card_matches.items():
    if card not in total_cards:
        total_cards[card] = [1, wins]
    else:
        total_cards[card][0] += 1
    for _ in range(total_cards[card][0]):
        for jdx in range(1, wins+1):
            if card+jdx in card_matches:
                if card+jdx not in total_cards:
                    total_cards[card+jdx] = [1, card_matches[card+jdx]]
                else:
                    total_cards[card + jdx][0] += 1

print(sum([x[0] for _, x in total_cards.items()]))
