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

def search3x3(self, rootNode):
    stack = []
    stack.append(rootNode)

    while stack != []:
        node = stack.pop()
        if node.depth == node.state.nn:
            return node
        #chooseNextSector(node.state, indexX, indexY) call function to determain were to go to next
#mostNonFilledInSector(node)
        action(node.state, indexX, indexY, move)#indexX and Y are the sector coordinates 
        if move != []:
            for n in move:
                newNode = Node(n, node)
                stack.append(newNode)
    return None

def adjacentElement(n, secComponent):
    """
        This function is used by adjacentSector to find the adject x or y coordinates
        of a single coordinate number.
    """
    remainder = secComponent % n
    if remainder != 0:
        index = range(0,secComponent) + range(secComponent+1,n)
    else:
        index = range(1,n)
    return index

def adjacentSector(n, secX, secY):
    """ 
        It creates a list of all adjacent sectors in the sector (secX,secY).
        And it's used in chooseNextSector.
    """
#print (secX,secY)
    columnTuple = zip( [ secX for x in range(0, n-1) ], adjacentElement(n, secY) )
    rowTuple = zip( adjacentElement(n, secX) , [ secY for x in range(0, n-1) ] )
    return rowTuple + columnTuple  

def chooseNextSector(state, secX, secY):
    n = state.n # find boundries
    adjacentSector_ = adjacentSector(n, secX, secY)
    blankSector = []

    for x,y in adjacentSector_: # Getting rid of filled sectors
        if not isFilled(state, x, y):
            blankSector.append( (x,y) )

#print (secX,secY)
    return blankSector
def nonFilledInSector(state):
    n = state.n # find boundries
    allSectors = [( x, y ) for y in range(0,n) for x in range(0,n)]

    blankSector = []
    for x,y in allSectors: # Getting rid of filled sectors
        if not isFilled(state, x, y):
            blankSector.append( (x,y) )
    return blankSector

def mostNonFilledInSector(state, sortby="max"):
    """
        It returns a tuple of a blank sector with the least/most
        number of adjacent blank sectors to it.

        To return tuple with least adjacent number of blanks, "min" has
        to be passed as the second argument. Otherwise, it returns the 
        one with the most blanks.
    """
    availableSector = []
    availableSector = nonFilledInSector(state)
    if availableSector != []:
                myPriQueue = MyPriorityQueue(sortby)
                for sector in availableSector:
                    x,y = sector
                    xy_sectors = chooseNextSector(state, x, y)
                    myPriQueue.put( len( xy_sectors ) , (x,y))
#print myPriQueue.toList()
                return myPriQueue.get()
    else:
        return []

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

    t2 = time.clock()
    print t2 - t, '\n'
