#!/usr/bin/env python
from __future__ import print_function
import node
from grid import *
import itertools
import sys, time
import timeit

def searchNxN(rootNode):

    rootNode.availableSector(nonFilledInSector(rootNode.state ))
    stack = []
    stack.append(rootNode)

    while stack:

        node1 = stack.pop()
        node1.state = findUniqueCandidate(node1.state)

        while node1.state == None:
            if not stack:
                return None
            node1 = stack.pop()
            node1.state = findUniqueCandidate(node1.state)

        if node1.depth == node1.state.nn: #Check for goal state
            return node1

        t = node1.nonFilledInSector[-1]
        move = []
        action(node1.state, t[0], t[1], move)
        if move:
            for n in move:
                newNode = node.Node(n, node1)
                newNode.availableSector(node1.nonFilledInSector[:-1])
                stack.append(newNode)

    return None

def nonFilledInSector(state):
    n = state.n # find boundries
    allSectors = [( x, y ) for y in range(0,n) for x in range(0,n)]
    blankSector = []
    for x,y in allSectors:
        if not isFilled(state, x, y):
            blankSector.append( (x,y) )
    return blankSector 

def findUniqueCandidate(state):

    newState = (state, True)

    while (newState[1]):
        newState = uniqueCandidate(newState[0])
        if newState[0] == None:
            return newState[0]

    return newState[0]

def uniqueCandidate(state):

    nn = state.nn

    for x in range(nn):
        for y in range(nn):
            i = 0
            if state[x, y].i == 0:
                hasOne = 0
                for z in state.neighbors(x, y):
                    i += 1
                    if i > 1:
                        break
                    candidate = z
                    hasOne = 1

                if hasOne == 0:
                    return (None, None)

                if i == 1:
                    return (candidate, True)

    return (state, False)

def sequentialFilledin(state):
    """ picking blank sectors in a sequention manner.
    i.e first, second, third sector and so on"""
    nonFilledin = nonFilledInSector(state)
    if nonFilledin != []:
        return nonFilledin[0]
    else:
        return []

def numAdj(state, secX, secY):

    count = 0
    n = state.n

    for x in range(n):
        if not isFilled(state, x, secY):
            count += 1

    for y in range(n):
        if not isFilled(state, secX, y):
            count += 1

    return count - 2

def action(state, secX, secY, list1):

    if isFilled(state, secX, secY):
        return list1.append(state)

    n = state.n # find boundries
    j = secX * n
    i = secY * n
    jMax = j + n
    iMax = i + n

    goAgain = 0# condition for 

    for col in range(j, jMax): # for every column in the sector
        for row in range(i, iMax):# for every row in the sector
            goAgain = 1
            if state[col, row].i == 0:# if that cell is empyt
                goAgain = 0
                for x in state.neighbors(col, row):# for every posible child
                    if isFilled(x, secX, secY):# if the entire sector is filled in
                        list1.append(x)# appen it to a list
                    else:
                        action(x, secX, secY, list1) #else recursivly call your self
            if goAgain == 0:
                return

def isFilled(state, secX, secY):
    """Given a state and sector cordinates return true if sector is filled in,
       else return false."""
    return (Cell(0) not in reduce(operator.add, state.square(secX, secY)))
    
def isEqual(state1, state2, secX, secY):
    """Given two states of the board check if both are the same."""

    assert state1.n == state2.n # must be of equal size
    square1 = state1.square(secX, secY)
    square2 = state2.square(secX, secY)

    for x, y in itertools.izip(square1, square2):
        for i, j in itertools.izip(x, y):
            if i != j:
                return False
    return True

def checkRow(sudokuBoard,x,y):
    """
        Returns false if element is repeted in the row.
        x = column
        y = row
    """
    n = sudokuBoard.n
    counter = 0
    selectedNum = sudokuBoard[x,y]

    for col in range(n*n):
        if sudokuBoard[col,y] == selectedNum:
            counter = counter + 1
        if counter > 1:
            return False
    return True

def checkCol(sudokuBoard,x,y):
    """
        Returns false if element is repeted in the column.
        x = column
        y = row
    """
    n = sudokuBoard.n
    counter = 0
    selectedNum = sudokuBoard[x,y]

    for row in range(n*n):
        if sudokuBoard[x,row] == selectedNum:
            counter = counter + 1
        if counter > 1:
            return False
    return True

def componentIndex(sudokuBoard, coordinate):
    """
        Given an x or y of an element in the sudoku board,
        it returns x or y coodinate of a sector on the board
    """
    n = sudokuBoard.n
    temp = coordinate/n
    if temp < 1:
        return 0
    elif temp >= 1 and temp < 2:
        return 1
    elif temp >= 2:
        return 2

def checkSector(sudokuBoard, x, y):
    n = sudokuBoard.n
    counter = 0
    selectedNum = sudokuBoard[x,y]

    x_board = componentIndex(sudokuBoard, x)
    y_board = componentIndex(sudokuBoard, y)

    x_sector_range_init = x_board*n
    x_sector_range_end = x_sector_range_init + n

    y_sector_range_init = y_board*n
    y_sector_range_end = y_sector_range_init + n

    for i in range(x_sector_range_init, x_sector_range_end):
        for j in range(y_sector_range_init, y_sector_range_end):
            if sudokuBoard[i,j] == selectedNum:
                counter = counter + 1
            if counter > 1:
                return False
    return True

def main(s):
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
        print( searchNxN(node.Node(sudokuBoard)) )
    else:
        timer = timeit.Timer((lambda: searchNxN(node.Node(sudokuBoard)) ))
        # adapt for different possible durations
        for t in [10 ** 0, 10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]:
            dur = timer.timeit(t)
            if dur * t >= 1.0:
                break
#print('searchNxN:', dur)
        print(dur)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        if sys.stdin.isatty():
            print('Waiting for a puzzle from a terminal ...', file=sys.stderr)
        main(sys.stdin.readline().strip())
