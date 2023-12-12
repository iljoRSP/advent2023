def parse_input_file():
    with open('./9/input.txt', 'r') as f:
        for line in f.readlines():
            yield [int(d) for d in line[:-1].split(' ')]




def diff_pair(a: int, b: int) -> int:
    return b - a


def diff_pairwise(seq: list) -> list:
    return [diff_pair(*pair) for pair in zip(seq[:-1], seq[1:])]


def diff_to_end(seq: list) -> list:
    while True:
        yield seq
        if (len(set(seq)) == 1 and seq[0] == 0): break

        seq = diff_pairwise(seq)


def propagate_up(diff_history: list):
    diff_history.reverse()
    diff_history[0].append(0)
    stage_n_plus_one_pairs = zip(diff_history[:-1], diff_history[1:])
    for stage_n, stage_plus_one in stage_n_plus_one_pairs:
        stage_plus_one.append(stage_plus_one[-1] + stage_n[-1])

    return diff_history[-1][-1]


sum = 0
for seq in parse_input_file():
    sum += propagate_up([s for s in diff_to_end(seq)])

print(sum)


# can optimise this by only saving the last of every sequence history