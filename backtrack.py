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
possible_values=["1","2","3","4","5","6","7","8","9"]


def backtracking(board,domain):
    
    if constraints.checkFilled(board):
        solution.append(board[:])
        
        return True

    for row_index,row in enumerate(board):
        for col_index,col in enumerate(row):

            if board[row_index][col_index] == "0":

                for value in domain:
                    board[row_index][col_index]=value   
                    if constraints.master_check(board):

                        if backtracking(board,domain):
                            return True
                                        
                    board[row_index][col_index]="0"
                return False
                
    
backtracking(b,possible_values)
print(solution[0])