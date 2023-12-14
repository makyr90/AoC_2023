import os
from collections import Counter

puzzle_data = open(os.path.dirname(os.path.realpath(__file__))+"/data/day_7.txt", "r").read().split("\n")
hands_bids = {}
for line in puzzle_data:
    hand, bid = line.split()
    hands_bids[hand] = [int(bid)]

DECK = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
DECK_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
HEX_MAP = ["D", "C", "B", "A", "9", "8", "7", "6", "5", "4", "3", "2", "1"]


def find_hand_type_score(_hand: str, _joker: bool = False) -> int:

    if _joker:
        if "J" in _hand:
            c = Counter(_hand)
            c["J"] = 0
            max_keys = [k for k, v in c.items() if v == max(c.values())]
            _hand = _hand.replace("J", max_keys[0])

    c = Counter(_hand)
    freqs = list(c.values())
    if 5 in freqs:  # Five of a kind
        return 6
    elif 4 in freqs:  # Four of a kind
        return 5
    elif 3 in freqs and 2 in freqs:  # Full house
        return 4
    elif 3 in freqs:  # Three of a kind
        return 3
    elif freqs.count(2) == 2:  # Two pair
        return 2
    elif freqs.count(2) == 1:  # One pair
        return 1
    elif len(freqs) == 5:  # High card
        return 0
    else:
        print("ERROR")
        return None


def hand_rank_value(_hand: str, _joker: bool = False) -> int:
    if joker:
        deck = DECK_2
    else:
        deck = DECK
    rank_val = ""
    for fig in list(_hand):
        rank_val += str(HEX_MAP[deck.index(fig)])
    return hex(int(rank_val, 16))


all_hands = hands_bids.keys()
for joker in [False, True]:
    for hand in all_hands:
        t_rank = find_hand_type_score(hand, _joker=joker)
        hands_bids[hand].append(t_rank)
        h_rank = hand_rank_value(hand, _joker=joker)
        hands_bids[hand].append(h_rank)

    if joker:
        sorted_hands_bids = {k: v for k, v in sorted(hands_bids.items(), key=lambda item: (item[1][3], item[1][4]))}
    else:
        sorted_hands_bids = {k: v for k, v in sorted(hands_bids.items(), key=lambda item: (item[1][1], item[1][2]))}

    rank_bid_product_sum = 0
    rank_counter = 1
    for k, v in sorted_hands_bids.items():

        rank_bid_product = v[0]*rank_counter
        rank_bid_product_sum += rank_bid_product
        rank_counter += 1
    if not joker:
        print("Part 1 answer: {}".format(rank_bid_product_sum))
    else:
        print("Part 2 answer: {}".format(rank_bid_product_sum))
