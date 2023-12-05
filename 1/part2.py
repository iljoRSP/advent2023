import re

def parse_num_or_word(word: str) -> int:
    if word.isnumeric(): return int(word)

    return {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }[word]

with open('./input.txt', 'r') as f:
    sum = 0

    for line in f.readlines():
        # find first and last occurence of spelt word or digit
        first = re.search(r'\d|zero|one|two|three|four|five|six|seven|eight|nine', line).group()
        last = re.findall(r'(?:.*)(\d|zero|one|two|three|four|five|six|seven|eight|nine)', line)[-1]

        sum += parse_num_or_word(first) * 10 + parse_num_or_word(last)

print(sum)