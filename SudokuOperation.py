board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_sudoku(board):
    for i in range(len(board)):
        if i%3 ==0 and i!=0:
            print("-------------------")
        for j in range(len(board[0])):
            if j%3 ==0 and j!=0:
                print("|", end="")
            if j ==8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ",end="")


def empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i,j
    return False

def valid(board, value, position):
    #check the row
    x,y=position
    for i in range(len(board[0])):
        if board[x][i] == value and i!=y:
            return False
    #check the column
    for i in range(len(board[0])):
        if board[i][y] ==value and i!=x:
            return False
    #check the box
    box_x = int(x/3)
    box_y = int(y/3)

    for i in range(box_x*3,box_x*3 +3):
        for j in range(box_y*3,box_y*3+3):
            if board[i][j] == value and (i,j) != (x,y):
                return False
    return True

def sudoku_solver(board):

    position = empty_cell(board)

    if position == False:
        return True

    x, y = position

    for i in range(1,10):
        if(valid(board,i,(x,y))):
            board[x][y]=i
            if (sudoku_solver(board) ==False):
                board[x][y]=0
            else:
                return True
    return False

# print_sudoku(board)
# print("")
sudoku_solver(board)
print_sudoku(board)