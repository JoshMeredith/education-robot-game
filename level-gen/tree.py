#!/usr/bin/env python3

import random

random.seed(4920)

N = 15

grid = [ ['L' for i in range(N)] for j in range(N) ]
done = [ [False for i in range(N)] for j in range(N) ]
ddr = [1, 0, -1, 0]
ddc = [0, 1, 0, -1]

def degree(r, c):
    tot = 0
    for (dr, dc) in zip(ddr, ddc):
        nr = r + dr
        nc = c + dc
        if min(nr, nc) >= 0 and max(nr, nc) < N and grid[nr][nc] == '_':
            tot += 1
    return tot

sr = random.randint(0, N-1)
sc = random.randint(0, N-1)
todo = set([(sr, sc)])

while len(todo) > 0:
    (r, c) = todo.pop()
    done[r][c] = True

    if degree(r, c) <= 1:
        grid[r][c] = '_'
        for dr, dc in zip(ddr, ddc):
            nr = r + dr
            nc = c + dc
            if min(nr, nc) >= 0 and max(nr, nc) < N:
                if not done[nr][nc] and degree(nr, nc) <= 1:
                    todo.add((nr, nc))

leaves = [ (r, c) for r in range(N) for c in range(N) if grid[r][c] == '_' and
        degree(r, c) <= 1 ]
leaves = list(map(lambda x: {'row': x[0]+1, 'col': x[1]+1}, leaves))
random.shuffle(leaves)
print(grid)
print(leaves)
