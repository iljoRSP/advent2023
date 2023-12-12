# every symbol connects to a 'prev' and 'next'
# knowing that S is part of a cycle, just go in one direction until we reach S again (no backtracking required)
# keep track of the length of the cycle, then divide by two to find the distance to the midpoint, which is furthest



from enum import Enum

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


    def __symbol_at(self, coords) -> str:
        x, y = coords
        return self.symbols[y][x]


    def __get_adjacents_dir_at(self, coords: tuple) -> set:
        cell = self.__symbol_at(coords)
        key = {
            '|': {Direction.UP, Direction.DOWN},
            '-': {Direction.LEFT, Direction.RIGHT},
            'L': {Direction.UP, Direction.RIGHT},
            'J': {Direction.UP, Direction.LEFT},
            '7': {Direction.DOWN, Direction.LEFT},
            'F': {Direction.DOWN, Direction.RIGHT},
        }

        if cell == 'S': return key['-']  # hardcoded :^)
        if cell == '.': return set()

        return key[cell]


    def traverse_cycle_counting_distance(self) -> int:
        distance_walked = 0
        current_coords = (37, 16)   # position of S, hardcoded :^)
        came_from = Direction.LEFT  # pick to go right first, hardcoded :^)

        while True:
            adjacent_dirs = self.__get_adjacents_dir_at(current_coords)
            next_node_dir = (adjacent_dirs - {came_from}).pop()

            next_coords = tuple(a + b for a, b in zip(current_coords, next_node_dir.value))
            next_from = Direction.opposite(next_node_dir)

            current_coords, came_from = next_coords, next_from
            distance_walked += 1

            if self.__symbol_at(current_coords) == 'S':
                return distance_walked



G = Graph()
print(G.traverse_cycle_counting_distance() / 2)
