'''
simple algebra lol?

given a race time T, record R and distance covered D:

let p = time spent pressing
let m = time spent moving
let s = constant speed


p + m = T
D = s * m
s = p


therefore D = p * (T - p)

find all integer p such that D > R

D > R
p(T-p) > R
-p2 + Tp > R
0 > p2 - Tp + R
p^2 - Tp + R < 0


therefore, valid p values fall in between the roots for this quadratic equality (assuming there are real roots)

by quadratic formula,

a = 1
b = -T
c = R
'''



from math import sqrt, ceil, floor



def fixed_width_split(string: str, width: int) -> list:
    return [string[i:i + width] for i in range(0, len(string), width)]


def solve_quadratic(a, b, c) -> list:
    d = (b**2) - (4*a*c)
    return (-b-sqrt(d))/(2*a), (-b+sqrt(d))/(2*a)


with open('./6/input.txt', 'r') as f:
    time = [int(num.strip()) for num in fixed_width_split(f.readline()[9:-1], 7)]
    record = [int(num.strip()) for num in fixed_width_split(f.readline()[9:-1], 7)]


product = 1
for T, R in zip(time, record):
    low, high = solve_quadratic(1, -T, R)

    possible_wins = ceil(high) - floor(low) - 1
    print(possible_wins)
    product *= possible_wins

print(product)
