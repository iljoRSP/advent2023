import numpy as np
from itertools import product

grid = []
symbol_coords = []


# parse schematic as a graph and find symbol cells
with open('./3/input.txt', 'r') as f:
    for row_num, row in enumerate(f.readlines()):
        row = row[:-1]
        grid.append(list(row))

        # track coordinates of symbols
        for col_num, char in enumerate(row):
            if char not in list('.0123456789'):
                symbol_coords.append(tuple([row_num, col_num]))

grid = np.array(grid)
max_bound = grid.shape[0]  # assuming grid is a square


# find valid adjacent coords
potential_number_coords = set()
for row, col in symbol_coords:
    adj_rows = [v for v in [row - 1, row, row + 1] if v >= 0 and v < max_bound]
    adj_cols = [v for v in [col - 1, col, col + 1] if v >= 0 and v < max_bound]

    adj_coords = {c for c in product(adj_rows, adj_cols)}.pop((row, col))

    potential_number_coords.union(adj_coords)


# check adjacent coords for digits



# propagate sideways to parse value, then sum
