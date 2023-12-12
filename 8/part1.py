directions = ''
graph = dict()

with open('./8/input.txt', 'r') as f:
    directions = list(f.readline()[:-1].replace('L', '0').replace('R', '1'))
    directions = [int(d) for d in directions]
    f.readline()

    for line in f.readlines():
        key, val = line[:-1].split(' = ')
        val = val[1:-1].split(', ')

        graph[key] = val


pointer = 'AAA'
step_count = 0
dir_count = len(directions)

while pointer != 'ZZZ':
    next_dir = directions[step_count % dir_count]

    pointer = graph[pointer][next_dir]

    step_count += 1

print(step_count)