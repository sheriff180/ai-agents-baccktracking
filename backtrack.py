import constraints
import time


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

num_backtrack = 0
search_step = 0

def backtracking(board,domain):
    global num_backtrack
    global search_step

    
    if constraints.checkFilled(board):
        solution.append(board[:])
        
        return True

    for row_index,row in enumerate(board):
        for col_index,col in enumerate(row):

            if board[row_index][col_index] == "0":

                for value in domain:
                    search_step += 1
                    board[row_index][col_index]=value   
                    if constraints.master_check(board):

                        if backtracking(board,domain):
                            return True
                                        
                    board[row_index][col_index]="0"

                num_backtrack += 1
                return False
                 
start_time = time.time()

backtracking(b,possible_values)

exec_t = time.time() - start_time

print(exec_t)
print(num_backtrack)
print(search_step)



