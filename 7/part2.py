'''
one key observation:

a joker will always transform into the most frequent card
in other words, add on the number of jokers to most frequent, then J count = 0
'''



from collections import Counter



def transform_jokers(game: dict) -> None:
    for hand in game:
        if not 'J' in hand['hand']: continue
        if hand['hand'] == 'JJJJJ': continue  # edge case

        num_jokers = hand['counter']['J']
        del hand['counter']['J']

        most_common_letter = hand['counter'].most_common(1)[0][0]
        hand['counter'][most_common_letter] += num_jokers

def inplace_sort_by_combo(game: dict) -> None:
    game.sort(key=lambda x: max(x['counter'].values()))


def inplace_sort_by_length(game: dict) -> None:
    game.sort(key=lambda x: len(x['counter']), reverse=True)


def inplace_sort_by_value(game: dict) -> None:
    game.sort(key=lambda x: ['AKQT98765432J'.index(card) for card in x['hand']], reverse=True)


def parse_input_file():
    with open('./7/input.txt', 'r') as f:
        for line in f.readlines():
            hand, bid = line[:-1].split(' ')

            yield (hand, Counter(hand), int(bid))


game = [{'hand': h, 'counter': c, 'bid': b} for h, c, b in parse_input_file()]

transform_jokers(game)
inplace_sort_by_value(game)
inplace_sort_by_length(game)
inplace_sort_by_combo(game)

winnings = 0
for rank, hand in enumerate(game):
    winnings += hand['bid'] * (rank + 1)

print(winnings)
