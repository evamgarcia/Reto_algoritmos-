from __future__ import annotations
solutions = []

def salvado(board: list[list[int]], row: int, column: int) -> bool:
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True 

def resolver(board: list[list[int]], row:int) -> bool:
    if row >= len(board):
        solutions.append(board)
        printboard(board)
        print()
        return True
    for i in range(len(board)):
        if salvado(board, row, i):
            board[row][i] = 1
            resolver(board, row +1)
            board[row][i] = 0
    return False

def printboard(board: list[list[int]]) -> None:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

n = 4
board = [[0 for i in range(n)] for j in range(n)]
resolver(board, 0)
print("The total number of solutions are: ", len(solutions))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    solutions(10)