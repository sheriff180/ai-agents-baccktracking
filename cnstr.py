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

# Check row for duplicate number
def isDupRow(board, row, column, choice):
    for cell in range(len(board[row])):
        if cell == column:
            continue

        if board[row][cell] == choice:
            return True 

    return False 

# Check column for duplicate number
def isDupCol(board, row, column, choice):
    for cell in range(len(board)):
        if cell == row:
            continue
        
        if board[cell][column] == choice:
            return True

    return False

