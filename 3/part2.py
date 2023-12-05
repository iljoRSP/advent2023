pt_gear_coords = set()
all_part_numbers = []
max_col = None


class PartNumber:
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
        # not indexing into matrix, so no care about out-of-bounds coords
        x, y = self.head_coords

        left_bound_coord = x - 1
        right_bound_coord = x + len(self.digit_string)

        self.adj_coords.add((left_bound_coord, y))
        self.adj_coords.add((right_bound_coord, y))

        for u in range(left_bound_coord, right_bound_coord + 1):
            self.adj_coords.add((u, y - 1))
            self.adj_coords.add((u, y + 1))


# parse grid
with open('./3/input.txt', 'r') as f:
    for row_num, row in enumerate(f.readlines()):
        row = row[:-1]  # drop trailing \n

        if max_col is None: max_col = len(row)

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

            elif char == '*':  # potentially a gear
                pt_gear_coords.add(tuple([col_num, row_num]))

            col_num += 1


# for each gear, count number of numbers that it intersects with
touched_gear_count = {k: [] for k in pt_gear_coords}

for part_number in all_part_numbers:
    for touched_gear in pt_gear_coords.intersection(part_number.adj_coords):
        touched_gear_count[touched_gear].append(part_number)

total_sum = 0
for k, v in touched_gear_count.items():
    if len(v) == 2:
        total_sum += v[0].value * v[1].value

print(total_sum)