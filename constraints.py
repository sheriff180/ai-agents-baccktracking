board = [["0"]*9 for n in range(9)]


def checkRow(row):
    ref = []
    for numbers in row:
        if numbers in ref and numbers != 0:
            return False
        else:
            ref.append(numbers)
    return True

def checkColumn(board):

