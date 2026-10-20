board = [["0"]*9 for n in range(9)]




def checkFilled(board):
    for row in board:
        for column in row:
            if column == "0":
                return False
    return True


def checkRow(row):
    ref = []
    for numbers in row:
        if numbers in ref and numbers != "0":
            return False
        else:
            ref.append(numbers)
    return True

def checkColumn(board,index):
    col=[]
    for row in board:
        col.append(row[index])
    return checkRow(col)

def checkSubGrid(board,row_index,col_index):

    row_start_index=(row_index//3)*3
    col_start_index=(col_index//3)*3
    subgrid_list=[]
    
    for x in range(row_start_index,row_start_index+3):
        for y in range(col_start_index,col_start_index+3):
            elem=board[x][y]
            subgrid_list.append(elem)
    return checkRow(subgrid_list)