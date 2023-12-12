# inside/outside is based on parity
# per row, starting counting from the left. all these cells are outside
# until, we hit a cell thats part of the loop. all the subsequent cells are now inside
# until, we hit a cell thats part of the loop. all the subsequent cells are now outside
# etc.



from enum import Enum
import regex as re

class Direction(Enum):
    UP      = ( 0, -1)
    DOWN    = ( 0,  1)
    LEFT    = (-1,  0)
    RIGHT   = ( 1,  0)

    @staticmethod
    def opposite(dir):
        match dir:
            case Direction.UP: return Direction.DOWN
            case Direction.DOWN: return Direction.UP
            case Direction.LEFT: return Direction.RIGHT
            case Direction.RIGHT: return Direction.LEFT



class Graph:
    def __init__(self) -> None:
        with open('./10/input.txt', 'r') as f:
            self.symbols = [list(row) for row in f.read().split('\n')]

        self.loop_only = self.__make_is_loop_overlay()


    def __make_is_loop_overlay(self):
        num_rows, num_cols = len(self.symbols), len(self.symbols[0])
        return [['.' for _ in range(num_cols)] for _ in range(num_rows)]


    def __symbol_at(self, coords) -> str:
        x, y = coords
        return self.symbols[y][x]


    def __set_loop_only_at(self, coords, val) -> None:
        x, y = coords
        self.loop_only[y][x] = val



    def __get_adjacents_dir_at(self, coords: tuple) -> set:
        cell = self.__symbol_at(coords)
        return self.__get_adjacents_dir_of(cell)


    def __get_adjacents_dir_of(self, symbol: str) -> set:
        key = {
            '|': {Direction.UP, Direction.DOWN},
            '-': {Direction.LEFT, Direction.RIGHT},
            'L': {Direction.UP, Direction.RIGHT},
            'J': {Direction.UP, Direction.LEFT},
            '7': {Direction.DOWN, Direction.LEFT},
            'F': {Direction.DOWN, Direction.RIGHT},
        }

        if symbol == 'S': return key['-']  # hardcoded :^)
        if symbol == '.': return set()

        return key[symbol]


    def traverse_cycle_marking_loop(self) -> None:
        current_coords = (37, 16)   # position of S, hardcoded :^)
        came_from = Direction.LEFT  # pick to go right first, hardcoded :^)

        while True:
            self.__set_loop_only_at(current_coords, self.__symbol_at(current_coords))

            adjacent_dirs = self.__get_adjacents_dir_at(current_coords)
            next_node_dir = (adjacent_dirs - {came_from}).pop()

            next_coords = tuple(a + b for a, b in zip(current_coords, next_node_dir.value))
            next_from = Direction.opposite(next_node_dir)

            current_coords, came_from = next_coords, next_from

            if self.__symbol_at(current_coords) == 'S':
                return


    def count_parity(self):
        # we have crossed the loop if we cross
        # |
        # F-J
        # L-7

        # everytime we cross the loop, swap parity from inside to outside

        count = 0
        for row in self.loop_only:
            row = ''.join(row)

            # these can be topologically ignored
            row = row.replace('-', '')
            row = row.replace('S', '')  # equal to -
            row = row.replace('F7', '')
            row = row.replace('LJ', '')

            # these are topologically equivalent to vertical lines
            row = row.replace('FJ', '|')
            row = row.replace('L7', '|')

            # split by verticals, take only even numbered chunks (which are the insides)
            chunks = row.split('|')
            insides_only = chunks[1::2]

            # then count
            count += len(''.join(insides_only))

        return count



G = Graph()
G.traverse_cycle_marking_loop()
print(G.count_parity())
