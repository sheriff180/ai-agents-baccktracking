# An attempt at an upgrade (but opinionated) contraints.py

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

# Check sub-grid for duplicate number
"""
Note here that the 'starting cell' is referred to here as a 'door' and the
entire sub-grid is referred to as 'room' as it is my mental model right now.

We offset here the door to explore the rest of the room. If the room does not
already contain the chosen number, then no duplicate is found. Otherwise,
it returns true (since a duplicate is found).
"""
def isDupRoom(board, row, column, choice):
    # First we find the coordinate of the "door"
    door_row = (row//3)*3
    door_col = (column//3)*3

    for r in range(3):
        for c in range(3):
            if (door_row + r) == row and (door_col + c) == column:
                continue

            if board[door_row + r][door_col + c] == choice:
                return True

    return False

def isValid(board, row, column, choice):
    return not isDupRow(board, row, column, choice) and not isDupCol(board, row, column, choice) and not isDupRoom(board, row, column, choice)
