



b = [
    ["5","3","0","0","7","0","0","0","0"],
    ["6","0","0","1","9","5","0","0","0"],
    ["0","9","8","0","0","0","0","6","0"],
    ["8","0","0","0","6","0","0","0","3"],
    ["4","0","0","8","0","3","0","0","1"],
    ["7","0","0","0","2","0","0","0","6"],
    ["0","6","0","0","0","0","2","8","0"],
    ["0","0","0","4","1","9","0","0","5"],
    ["0","0","0","0","8","0","0","7","9"]
]

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

def checkColumn(board,col_index):
    col=[]
    for row in board:
        col.append(row[col_index])
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


def master_check(board):
    for x,row in enumerate(board):
        if checkRow(row):
            for y,col in enumerate(row):
                if checkColumn(board,y):
                    if checkSubGrid(board,x,y):
                        continue
                    else:
                        return False
                else:
                    return False
        else:
            return False

    return True


