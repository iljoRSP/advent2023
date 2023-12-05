symbol_coords = set()
all_part_numbers = []
max_col = None
max_row = 0


class PartNumber:
    global max_col
    global max_row

    def __init__(self, head_val: str, head_coords: tuple) -> None:
        self.digit_string = head_val
        self.head_coords = head_coords

    def attach_digit(self, val: str) -> None:
        self.digit_string += val

    def finalise(self) -> None:
        # calculate numerical value
        self.value = int(self.digit_string)

        # calculate surrounding coords
        self.adj_coords = set()

        # defined as the entire row above, entire row below, cell to the right, cell to the left
        # in consideration of the grid edge (technically not needed since we are not indexing into a matrix, but meh)
        x, y = self.head_coords

        left_bound_coord = max(0, x - 1)
        right_bound_coord = min(max_col, x + len(self.digit_string))

        if x > 0:
            self.adj_coords.add((left_bound_coord, y))

        if x < max_col:
            self.adj_coords.add((right_bound_coord, y))

        for u in range(left_bound_coord, right_bound_coord + 1):
                if y > 0:
                    self.adj_coords.add((u, y - 1))
                if y < max_row:
                    self.adj_coords.add((u, y + 1))


# parse grid
with open('./3/input.txt', 'r') as f:
    for row_num, row in enumerate(f.readlines()):
        row = row[:-1]  # drop trailing \n

        if max_col is None: max_col = len(row)
        max_row += 1

        # track significant coords
        col_num = 0
        while col_num < max_col - 1:
            char = row[col_num]

            if char.isnumeric():
                # once a digit is found, build up a new PartNumber, then
                new_part_number = PartNumber(char, tuple([col_num, row_num]))

                # look ahead for the entire number, then
                while col_num < max_col - 1:
                    next_cell = row[col_num + 1]
                    if not next_cell.isnumeric():
                        break

                    new_part_number.attach_digit(next_cell)

                    # keep looking ahead, and also skips that cell for outer loop
                    col_num += 1

                new_part_number.finalise()
                all_part_numbers.append(new_part_number)

            elif char != '.':  # is a symbol
                symbol_coords.add(tuple([col_num, row_num]))

            col_num += 1


# for each part number, check if a symbol intersects with its adjacent cells
schematic_sum = 0

for part_number in all_part_numbers:
    if symbol_coords.intersection(part_number.adj_coords):
        schematic_sum += part_number.value

print(schematic_sum)
