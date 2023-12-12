import numpy as np
from itertools import combinations

def parse_input_file():
    with open('./11/input.txt', 'r') as f:
        return np.array([list(r) for r in f.read()[:-1].split('\n')])


def locate_galaxies(grid):
    indices = np.where(grid == '#')
    coordinates = list(zip(indices[0], indices[1]))
    return coordinates


def compute_actual_coordinates(grid):
    indices_stacked = np.indices(grid.shape).transpose(1, 2, 0)  # <- what does this transpose do? truly a numpy readability moment

    return indices_stacked


def expand_cosmos_coordinates(universe, coordinates, scale_factor):
    for ri in range(universe.shape[0]):
        row = universe[ri, :]
        if np.all(row == '.'):
            coordinates[ri:, :, 0] += scale_factor - 1

    for ci in range(universe.shape[1]):
        col = universe[:, ci]
        if np.all(col == '.'):
            coordinates[:, ci:, 1] += scale_factor - 1

    return coordinates


def taxicab_distance_by_coordinates(pair, coordinates):
    gal_a, gal_b = pair

    (x1, y1) = coordinates[gal_a]
    (x2, y2) = coordinates[gal_b]

    return int(abs(x2-x1) + abs(y2-y1))  # cast out of numpy int32


universe = parse_input_file()
galaxies = locate_galaxies(universe)
actual_coordinates = compute_actual_coordinates(universe)
actual_coordinates = expand_cosmos_coordinates(universe, actual_coordinates, 1000000)


sum = 0
for pair in combinations(galaxies, 2):
    sum += taxicab_distance_by_coordinates(pair, actual_coordinates)

print(sum)
