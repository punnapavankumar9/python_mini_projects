import sys
# sys.getrecursionlimit()
sys.setrecursionlimit(10000)
board = [
    [0, 0, 3, 8, 6, 0, 0, 0, 1],
    [0, 0, 0, 3, 0, 9, 0, 4, 0],
    [0, 4, 0, 0, 1, 0, 2, 0, 8],
    [0, 0, 0, 5, 0, 0, 0, 9, 3],
    [3, 8, 0, 9, 7, 6, 0, 2, 5],
    [9, 2, 0, 0, 0, 8, 0, 0, 0],
    [5, 0, 2, 0, 9, 0, 0, 8, 0],
    [0, 6, 0, 2, 0, 7, 0, 0, 0],
    [1, 0, 0, 0, 8, 3, 4, 0, 0]
]
def solve(bo):
    print(bo)
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i , (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-  -  -  -  -  -  -  -  -  -  -  -  ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else :
                print(str(bo[i][j]) + " ", end="")
print_board(board)
solve(board)
print("solved board is: ")
print_board(board)