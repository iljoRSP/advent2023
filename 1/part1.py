with open('./1/input.txt', 'r') as input:
    sum = 0
    for line in input.readlines():
        # line = threerznlrhtkjp23mtflmbrzq395three

        first_pointer = 0
        last_pointer = len(line) - 1

        while not line[first_pointer].isnumeric(): first_pointer += 1
        while not line[last_pointer].isnumeric(): last_pointer -= 1

        sum += int(line[first_pointer]) * 10 + int(line[last_pointer])

print(sum)