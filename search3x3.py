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

def action(node):
    return []

def checkRow(sudokuBoard,x,y):
    """
        Returns false if element is repeted in the row.
        x = column
        y = row
    """
    n = 3
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
    n = 3
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
        it returns x or y coodinate of sector on the board
    """
    n = 3
    temp = coordinate/n
    if temp < 1:
        return 0
    elif temp >= 1 and temp < 2:
        return 1
    elif temp >= 2:
        return 2

def checkSector(sudokuBoard, x, y):
    n = 3
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
    board = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8"
    sudokuBoard = Grid(3, board)
    print sudokuBoard

    """
        x = column
        y = row
    """
    x = 3
    y = 6
    for myb in sudokuBoard.neighbors(x,y):
        print '\n'
        print myb
        print "Row: "+str(checkRow(myb, x,y))
        print "Col: "+str(checkCol(myb, x,y))
        print "Valid Sector: " + str(checkSector(myb, x,y))

    print sudokuBoard[x,y]
