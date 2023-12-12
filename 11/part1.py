import numpy as np
from itertools import combinations

def parse_input_file():
    with open('./11/input.txt', 'r') as f:
        return np.array([list(r) for r in f.read()[:-1].split('\n')])


def expand_cosmos(grid):
    def expand_row(grid):
        expandable = []
        for i, row in enumerate(grid):
            if np.all(row == '.'):
                expandable.append(i + len(expandable))

        for i in expandable:
            grid = np.insert(grid, i, '.', axis=0)

        return grid

    grid = expand_row(grid)
    grid = expand_row(grid.T).T

    return grid


def locate_galaxies(grid):
    indices = np.where(grid == '#')
    coordinates = list(zip(indices[0], indices[1]))
    return coordinates


def taxicab_distance(pair):
    (x1, y1), (x2, y2) = pair

    return abs(x2-x1) + abs(y2-y1)


universe = parse_input_file()
universe = expand_cosmos(universe)
galaxies = locate_galaxies(universe)

sum = 0
for pair in combinations(galaxies, 2):
    sum += taxicab_distance(pair)

print(sum)
