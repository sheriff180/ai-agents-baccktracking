import constraints

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

solution = []
possible_values=set(range(1,10))


def backtracking(board,domain):
    if constraints.checkFilled(board):
        solution.append(board[:])
        return

    for row_index,row in enumerate(board):
        for col_index,col in enumerate(row):
            pass

