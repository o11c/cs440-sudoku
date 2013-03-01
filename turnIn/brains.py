#!/usr/bin/env python

from __future__ import print_function, division

import sys
import timeit

import grid

def best_move(g):
    """
        Finds cell with the list number of possibilities
    """
    nn = g.nn
    best = None
    best_cost = nn + 1
    for x in range(nn): # Iterate through all cells
        for y in range(nn):
            if not g[x, y]: # If the cell is empty
                branch_count = len(list(g.neighbors(x, y))) # All possible numbers on (x,y)
                if branch_count == 1: 
                    return x,y
                if branch_count < best_cost:
                    best = x,y
                    best_cost = branch_count # (x,y) with the least number of possibilities
    return best # returns None if all cells are filled

def solve(g):
    """
        Recursive function that fills in sudoku puzzle by the least number of possibilities.
    """
    m = best_move(g)
    if m is None: # Base case: All cells are filled
        return g
    x,y = m

    for gn in g.neighbors(x, y):
        gns = solve(gn)
        if gns is not None:
            return gns
    return None

def main(s):
    s = s.replace('.', ' ')
    for n in [2, 3, 4, 5, 6, 7]:
        nn = n * n
        nnnn = nn * nn
        if len(s) == nnnn:
            break
    else:
        sys.exit('bad size')
        return
    g = grid.Grid(n, s)

    if False:
        print(solve(g))
    else:
        timer = timeit.Timer((lambda: solve(g)))
        # adapt for different possible durations
        for t in [10 ** 0, 10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]:
            dur = timer.timeit(t)
            if dur * t >= 1.0:
                break
        print(dur)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        if sys.stdin.isatty():
            print('Waiting for puzzle(s) from a terminal ...', file=sys.stderr)
        for line in sys.stdin:
            main(line.strip())
