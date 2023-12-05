from math import floor

total_score = 0

with open('./4/input.txt', 'r') as f:
    lines = f.readlines()
    copies = [1] * len(lines)

    for curr_card, line in enumerate(lines):
        # number of wins = how many cards ahead get copied
        # number of copies they gain = 1 per copy of this card

        winning = {int(line[i:i+3]) for i in range(9, 39, 3)}
        scratched = {int(line[u:u+3]) for u in range(42, 117, 3)}

        wins = len(winning.intersection(scratched))

        for i in range(curr_card + 1, min(curr_card+wins+1, len(copies))):
            copies[i] += copies[curr_card]

print(sum(copies))