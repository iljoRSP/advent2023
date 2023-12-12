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


starts = [k for k in graph.keys() if k[-1] == 'A']
shortests = dict()

for start in starts:
    pointer = start
    step_count = 0
    dir_count = len(directions)

    while pointer[-1] != 'Z':
        next_dir = directions[step_count % dir_count]

        pointer = graph[pointer][next_dir]

        step_count += 1

    shortests[start] = step_count


# think of it this way:
# each of these S->G track will cycle every X amount of times
# i most easily picture this as imagining two polygons, most simply a line and a triangle
# start at one of the corners on each, and then travel along the corners, going 1 step at a time simultaneously
# the 'current' corner will fall out of sync, but will eventually resync back on the starting corner
# this will always happen on the LCM

#  (in fact, if you visualise the graph as I did, you'll find that each starting point is on its own cycle
#  (essentially making it this exact problem, just with very large n-gons)

from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def lcm_of_list(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]

    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm(lcm_result, numbers[i])

    return lcm_result

print(lcm_of_list(list(shortests.values())))