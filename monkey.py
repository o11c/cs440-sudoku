#!/usr/bin/env python

from __future__ import print_function, division

import sys
import timeit

import grid

def create_order(g):
    ''' Minimize the branching factor one time.
    '''
    nn = g.nn
    sl = []
    for x in range(nn):
        for y in range(nn):
            if not g[x, y]:
                branches = list(g.neighbors(x, y))
                sl.append((len(branches), x, y))
    sl.sort()
    return tuple([(x, y) for bfv,x,y in sl])

def solve(g, l=None):
    if l is None:
        l = create_order(g)
    if not l:
        return g
    x,y = l[0]

    for gn in g.neighbors(x, y):
        gns = solve(gn, l[1:])
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
        print('Monkey:', dur)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        if sys.stdin.isatty():
            print('Waiting for a puzzle from a terminal ...', file=sys.stderr)
        main(sys.stdin.readline().strip())
