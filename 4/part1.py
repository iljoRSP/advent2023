from math import floor

total_score = 0

with open('./4/input.txt', 'r') as f:
    # in this one, since the numbers are spaced out evenly, I'll split based on character count rather than delims. 
    # Mainly to avoid annoying empty strings with 'a  b'.split(' ')
    while line := f.readline():
        # line = ' 18 39  5 97 33 74 70 35 40 72 | 62 23 33 94 18  5 91 74 86 88 82 72 51 39 95 35 44 87 65 15 46 10  3  2 84'

        winning = {int(line[i:i+3]) for i in range(9, 39, 3)}
        scratched = {int(line[u:u+3]) for u in range(42, 117, 3)}

        total_score += floor(2 ** (len(winning.intersection(scratched)) - 1))  # floor as an ugly fix to avoid 2^-1 (from 0 wins) adding a 0.5


print(total_score)