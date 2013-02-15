import node
from grid import *

def search3x3(self, rootNode):
    stack = []
    stack.append(rootNode)

    while stack != []:
        node = stack.pop()
        if node.depth == node.state.nn:
            return node
        move = action(node)
        if move != []:
            for n in move:
                stack.append(n)
    return None

def action(state, secX, secY, list1):
    """Given a node and sector indecies this function will return a list of
       all posible solution to that sector"""

    n = state.n # find boundries
    j = secX * n
    i = secY * n
    jMax = j + n
    iMax = i + n

    for col in range(j, jMax): # for every column in the sector
        for row in range(i, iMax):# for every row in the sector
            if state[col, row].i == 0:# if that cell is empyt
                for x in state.neighbors(col, row):# for every posible child
                    if checkRow(x, col, row) and checkCol(x, col, row) and checkSector(x, col, row):
                        find = 0
                        for w in list1:
                            if isEqual(x, list1[list1.index(w)]):# if it does not already exist
                                find = 1
                        if find == 0:                        
                            if isFilled(x, secX, secY):# if the entire sector is filled in
                                list1.append(x)# appen it to a list
                            else:
                                action(x, secX, secY, list1) #else recursivly call your self

def isFilled(state, secX, secY):
    """Given a state and sector cordinates return ture if sector is filled in,
       else return false."""

    n = state.n# find boundries
    j = secX * n
    i = secY * n
    jMax = j + n
    iMax = i + n
    count = 0

    for col in range(j, jMax):# for every column
        for row in range(i, iMax):# for ever row
            if state[col, row].i != 0:# if there is not a blank
                count += 1
    
    if count < (n*n):# if the count is less than the number of cells in a sector
        return False
    return True
    
def isEqual(state1, state2):
    """Given two states of the board check if both are the same."""

    assert state1.n == state2.n # must be of equal size

    for x in range(state1.nn):# for every column
        for y in range(state1.nn):# and every row
            if state1[x, y].i != state2[x, y].i:#if one element is out of place return false
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
    print sudokuBoard, '\n'

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
    action(sudokuBoard, 1, 1, x)
    for y in x:
        print y, '\n'
        
    #for x in sudokuBoard.row(0):
        #print x, '\n'