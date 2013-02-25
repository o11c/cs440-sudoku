#!/usr/bin/env python

from __future__ import print_function, division

import sys
import timeit

import grid

def solve(g, x=0, y=0):
    nx = x + 1
    ny = y
    if nx == g.nn:
        nx = 0
        ny = y + 1
        if ny == g.nn:
            # grid will be fully filled
            for gn in g.neighbors(x, y):
                return gn
            return None

    for gn in g.neighbors(x, y):
        gns = solve(gn, nx, ny)
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
        print('Stupid:', dur)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        if sys.stdin.isatty():
            print('Waiting for puzzle(s) from a terminal ...', file=sys.stderr)
        for line in sys.stdin:
            main(line.strip())
