#!/usr/bin/env python3

# Usage: ./world-one.py big.maze
#
# big.maze format:
# R C
# R lines, each with C characters
# Each character is:
# '*': start
# '$': end
# '_': empty
# '#': wall.
#
# Generates a RxC maze in World 1 according to the given maze file, writing to
# stdout.

import sys

with open('big.maze', 'r') as f:
    R, C = list(map(int, f.readline().split()))
    grid = list(map(lambda x: x.strip(), f.readlines()))
    output = [ [ c for c in list(row) ] for row in grid ]

    assert len(grid) == R
    assert len(grid[0]) == C

    # Check that no wall has degree more than 2.
    ddr = [0, 1, 0, -1]
    ddc = [1, 0, -1, 0]
    wall_mappings = {
            '0000': 'H',
            '0001': 'V',
            '0010': 'H',
            '0100': 'V',
            '1000': 'H',
            '0101': 'V',
            '1010': 'H',
            '1100': 'TL',
            '0110': 'TR',
            '0011': 'BR',
            '1001': 'BL',
            }
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '#':
                output[i][j] = '_'
                if grid[i][j] == '*':
                    sr, sc = i, j
                elif grid[i][j] == '$':
                    er, ec = i, j
                continue
            matches = ''
            for (dr, dc) in zip(ddr, ddc):
                nr = dr + i
                nc = dc + j
                if min(nr, nc) >= 0 and nr < R and nc < C and grid[nr][nc] == '#':
                    matches += '1'
                else:
                    matches += '0'
            assert matches in wall_mappings, "i = %d, j = %d, matches = %s" % (i, j, matches)
            output[i][j] = wall_mappings[matches]
    world = {
            'numRows': R,
            'numCols': C,
            'start': {'x': sc, 'y': sr },
            'startDir': 'Up',
            'goal': {'x': ec, 'y': ec },
            'grid': output
            }
    print(world)
