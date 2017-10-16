#!/usr/bin/env python3

import random

N = 15

left = [
        0,
        0,
        3,
        3,
        3,
        5,
        5,
        6,
        6,
        8,
        8,
        8,
        8,
        8,
        10,
]

right = [
        4,
        6,
        6,
        7,
        7,
        7,
        7,
        7,
        9,
        9,
        9,
        10,
        12,
        15,
        15,
]

grid = [ ['L' for i in range(N)] for j in range(N) ]
for i in range(N):
    for j in range(left[i], right[i]):
        grid[i][j] = '_'
grid = grid[::-1]

for g in grid:
    print(str(g) + ',')
