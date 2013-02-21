import node
from grid import *
import itertools
import sys, time
from heapq import *

class MyPriorityQueue:
    """ This is priority queue that organizes objects in the queue in
        this format ( priority value, object ). If "max" is pass as part
        of the constructor, then the priority queue is a max-heap, otherwise,
        it is a min-heap
    """
    def __init__(self,type_of_heap=""):
        self.heap = []
        if type_of_heap == "max":
            self.type_ = -1
        else:
            self.type_ = 1
    def put(self, weight, node):
        heappush(self.heap, ( self.type_*weight, node ) )
    def get(self):
        priority, node = heappop(self.heap)
        return node
    def empty(self):
        return ( len(self.heap) == 0 )
    def __len__(self):
        return len(self.heap)
    def toList(self):
        return  self.heap

def search3x3(rootNode):

    stack = []
    stack.append(rootNode)

    while stack != []:
        node1 = stack.pop()
        node1.state = uniqueCandidate(node1.state)
        if node1.depth == node1.state.nn:
            return node1
        #t = chooseNextSec(node1.state)
        move = []
        action(node1.state, t[0], t[1], move)
        if move != []:
            for n in move:
                newNode = node.Node(n, node1)
                stack.append(newNode)
    return None

def uniqueCandidate(state):

    nn = state.nn

    for x in range(nn):
        for y in range(nn):
            i = 0
            for z in state.neighbors(x, y):
                i += 1
                candidate = z
                if i > 1:
                    break;

            if i == 1:
                return candidate

    return state

def chooseNextSec(state):

    maxCount = 0
    n = state.n

    for x in range(n):
        for y in range(n):
            if not isFilled(state, x, y):
                t3 = x
                t4 = y
                count = numAdj(state, x, y)
                if count > maxCount:
                    maxCount = count
                    t1 = x
                    t2 = y

    if maxCount == 0:
        return (t3, t4)

    return (t1, t2)

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
    """Given a node and sector indecies this function will return a list of
       all posible solution to that sector"""

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
#print str(sudokuBoard[i,j])+" ("+str(i)+", "+str(j)+")"
            if counter > 1:
                return False
    return True

if __name__ == "__main__":
    board = ".94...13..........3...76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8"
             
    sudokuBoard = Grid(3, board)
#print sudokuBoard, '\n'

    """
        x = column
        y = row
    """
    #x = 3
    #y = 6
    #for myb in sudokuBoard.neighbors(x,y):
        #print '\n'
        #print myb
        #print "Row: "+str(checkRow(myb, x,y))
        #print "Col: "+str(checkCol(myb, x,y))
        #print "Valid Sector: " + str(checkSector(myb, x,y))

    #print sudokuBoard[x,y]

    x = []
    t = time.clock()
    n = search3x3(node.Node(sudokuBoard))
    t2 = time.clock()
    print n, '\n'
    print t2 - t, '\n'
