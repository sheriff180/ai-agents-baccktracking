"""
I think—before you look over the rest of the code, Amaan—that it is
important to inform you why I have decided to write a new backtracking
algorithm.

The backtracking algorithm we wrote ran into structural limitations baked
into Python. Looking into CPS-style implementation, I had realized that this
is actually useless. For one, Python actually doesn't do tail-call eliminations.
That is, even if the compiler recognizes a tail-recursive function, it does not
bother to actually optimize it into a non-recursive function, but leaves it
as is. Another thing I have realized is that Python has a limit on recursive
calls. As such, this is possibly why some Sudokus were unsolvable. It could
have been that the algorithm reached a capping limit due to the Sudoku itself
being particularly adversarial against our algorithm.

Therefore, I ultimately decided it was best to attempt at an iterative, manual
manipulation of states, indices, choices, and backtracks in order to make the
most efficient backtracking algorithm possible that REALLY solves Sudoku puzzles—
of course, while keeping your part of the code intact.
"""

# You may delete this comment and all that is above after you have finished reading.
import cnstr

def backtrack(board, empty_cells):
    # We will use this to access empty_cells
    # This is so we know which empty cell we are currently manipulating
    indx = 0

    # We keep going through process until we have finished indexing empty_cells
    while 0 <= indx < len(empty_cells):
        r, c = empty_cells[indx]
        found = False

        for choice in range(int(board[r][c]) + 1, 10):
            if cnstr.isValid(board, r, c, str(choice)):
                board[r][c] = str(choice)
                indx += 1
                found = True
                break

        if not found:
            board[r][c] = '0'
            indx -= 1
