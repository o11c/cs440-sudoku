#!/usr/bin/env python

from __future__ import print_function
import node
from grid import *
import itertools
import sys, time
import timeit

import searchNxN 
import brains 
import monkey
import stupid

def main(s,flag):
    if flag == "-a":
        chosenStrategy = "searchNxN"
        strategy = 0
    elif flag == "-b":
        chosenStrategy = "brains"
        strategy = 1
    elif flag == "-c":
        chosenStrategy = "monkey"
        strategy = 2
    elif flag == "-d":
        chosenStrategy = "stupid"
        strategy = 3
    else:
        sys.stderr.write("Strategy '%s' doesn't exist\n" % flag)
        program_usage()

    #print("Strategy %s was chosen:\n" % chosenStrategy)

    for n in [2, 3, 4, 5, 6, 7]:
        nn = n * n
        nnnn = nn * nn
        if len(s) == nnnn:
            break
    else:
        sys.exit('bad size')
        return
    sudokuBoard = Grid(n, s)
    if False:
        print( strategy(node.Node(sudokuBoard)) )
    else:
        if strategy == 0:
            a = time.clock()
            solvedPuzzle = searchNxN.searchNxN(node.Node(sudokuBoard))
            b = time.clock()

        elif strategy == 1:
            a = time.clock()
            solvedPuzzle = brains.solve(sudokuBoard)
            b = time.clock()

        elif strategy == 2:
            a = time.clock()
            solvedPuzzle = monkey.solve(sudokuBoard)
            b = time.clock()

        elif strategy == 3:
            a = time.clock()
            solvedPuzzle = stupid.solve(sudokuBoard)
            b = time.clock()

        print(solvedPuzzle.board)

def program_usage():
    sys.stderr.write("Usage: %s -flag\n" % sys.argv[0])
    sys.stderr.write(" There are four strategies and their flags are below:\n")
    sys.stderr.write(   "\t searchNxN:\t-a \n"
                        "\t brains:\t-b \n"
                        "\t monkey:\t-c\n"
                        "\t stupid:\t-d\n");
    sys.exit(1)

def flagExit(flag):
    if not (flag == "-a" or flag == "-b" or flag == "-c" or flag == "-d"):
        program_usage()

if __name__ == "__main__":
    if not len(sys.argv) == 2: # Checking if one flag was passed
        program_usage()
    flag = sys.argv[1]
    flagExit(flag) # Checks if flag exists

    if sys.stdin.isatty(): # If puzzle is typed instead of piped into the program
        print('Waiting for a puzzle from a terminal ...', file=sys.stderr)
    for line in sys.stdin:
        main(line.strip(),flag)
