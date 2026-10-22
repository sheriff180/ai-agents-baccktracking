import sys
import time
import backtrack
import constraints
import bctrck

# The board that will be filled with the Sudoku puzzle
board = []
# The list that will be filled with the target cells' coordinates
empty_cells = []

# Check appropriate amount of arguments first
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Missing argument or too many arguments. Run with -help for usage.")
    sys.exit(1)

# Store arguments for later use
if len(sys.argv) == 2:
    arg1 = sys.argv[1]

elif len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]


# Check arguments and process
if arg1 == "-help":
    print("Usage: python3 main.py [INPUT] [OPTIONAL OUTPUT].")
    print("Example: python3 main.py quiz1.txt quiz2.txt")
    print("Input must be a .txt file")
    print("If output is not supplied, output will be written to out.txt by default.")
    sys.exit(0)


# Process argv1 (and argv2 if supplied) to check if arugment(s) is valid
if len(sys.argv) == 3:
    f_name1, sep1, ext1 = arg1.partition(".")
    f_name2, sep2, ext2 = arg2.partition(".")

    if f_name1 == "" or ext1 != "txt":
        print("Invalid input, must provide file name and extension (.txt).")
        sys.exit(1)

    if f_name2 == "" or ext2 != ext1:
        print("Invalid output, must provide file name and extension (.txt).")
        sys.exit(1)

elif len(sys.argv) == 2:
    f_name1, sep1, ext1 = arg1.partition(".")

    if f_name1 == "" or ext1 != "txt":
        print("Invalid input, must provide file name and extension (.txt).")
        sys.exit(1)


# Looks up and open file
try:
    with open(arg1, 'r') as file:
        for i, line in enumerate(file):
            row = []
            for c in line:
                if c.isnumeric():
                    row.append(c)
            board.append(row)
                    
except FileNotFoundError:
    print("There is no such file.")
    sys.exit(1)

# We store the empty cells foudn in board list into empty_cells list
for r in range(9):
    for c in range(9):
        if board[r][c] == "0":
            empty_cells.append((r,c))

start_time = time.time()
bctrck.backtrack(board, empty_cells)
if constraints.master_check(board) and constraints.checkFilled(board):
    print("Found a solution ya stinky bum!")
    print("Here it is!")
    print(board)
else:
    print("What the fuck is that?")


print(time.time() - start_time)
