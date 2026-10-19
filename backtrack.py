board = [["0"]*9 for n in range(9)]
print (board)

solution = []

def checkFilled(board):
    for row in board:
        for column in row:
            if column == "0":
                return False
    return True

def backtracking(board):
    if checkFilled(board):
        solution.append(board[:])
        return
    for row in board:
        for column in row:

