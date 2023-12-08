from collections import Counter



def inplace_sort_by_combo(game: dict) -> None:
    game.sort(key=lambda x: max(x['counter'].values()))


def inplace_sort_by_length(game: dict) -> None:
    game.sort(key=lambda x: len(x['counter']), reverse=True)


def inplace_sort_by_value(game: dict) -> None:
    game.sort(key=lambda x: ['AKQJT98765432'.index(card) for card in x['hand']], reverse=True)


def parse_input_file():
    with open('./7/input.txt', 'r') as f:
        for line in f.readlines():
            hand, bid = line[:-1].split(' ')

            yield (hand, Counter(hand), int(bid))


# this is abusing that python's inplace sort doesn't reorder any elements that don't need to be moved
#  in effect, I can sort FH/3K and 2P/1P, and then sort it by the highest tuple,
#  and the 'internal' order of the max:3-tuple and max:2-tuples doesn't change

# yes, it's slightly less efficient because I have to sort the entire list thrice, instead of sorting increasingly small lists
# but its ok


game = [{'hand': h, 'counter': c, 'bid': b} for h, c, b in parse_input_file()]

inplace_sort_by_value(game)
inplace_sort_by_length(game)
inplace_sort_by_combo(game)

winnings = 0
for rank, hand in enumerate(game):
    winnings += hand['bid'] * (rank + 1)

print(winnings)
