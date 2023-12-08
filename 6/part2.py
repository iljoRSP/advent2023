from math import sqrt, ceil, floor



def solve_quadratic(a, b, c) -> list:
    d = (b**2) - (4*a*c)
    return (-b-sqrt(d))/(2*a), (-b+sqrt(d))/(2*a)


with open('./6/input.txt', 'r') as f:
    time = int(f.readline()[9:-1].replace(' ', ''))
    record = int(f.readline()[9:-1].replace(' ', ''))

low, high = solve_quadratic(1, -time, record)

possible_wins = ceil(high) - floor(low) - 1
print(possible_wins)
