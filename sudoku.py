import numpy as np


def draw_board(board_state):
    for i in range(9):
        print('')
        if i == 3 or i == 6:
            print('------+------+------')
        for j in range(9):
            if j == 3 or j == 6:
                print('|', end='')
            if board_state[i][j] == 0:
                print(". ", end='')
            else:
                print(str(board_state[i][j]) + ' ', end='')


def string_to_2d(init_str):
    init_str = init_str.replace('\n', '')
    arr = [int(ch) for ch in init_str]
    arr = np.array(arr).reshape(9, 9)
    return arr


def string_to_2d_arr(init_str):
    init_str = init_str.replace('\n', '')


def next_free_cell(board_state, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if board_state[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if board_state[x][y] == 0:
                return x, y

    return -1, -1


def check_move(board_state, i, j, move):
    row_ok = all([move != board_state[i][x] for x in range(9)])
    if row_ok:
        column_ok = all([move != board_state[x][j] for x in range(9)])
        if column_ok:
            box_x, box_y = 3 * int(i/3), 3 * int(j/3)
            for x in range(box_x, box_x + 3):
                for y in range(box_y, box_y + 3):
                    if board_state[x][y] == move:
                        return False
            return True
    return False


def solve(board_state, i=0, j=0):
    i, j = next_free_cell(board_state, i, j)
    if i == -1:
        return True
    for move in range(1, 10):
        if check_move(board_state, i, j, move):
            board_state[i][j] = move
            if solve(board_state, i, j):
                return True
            board_state[i][j] = 0
    return False










table = """400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""

table = [[4,0,0,0,0,0,8,0,5],
         [0,3,0,0,0,0,0,0,0],
         [0,0,0,7,0,0,0,0,0],
         [0,2,0,0,0,0,0,6,0],
         [0,0,0,0,8,0,4,0,0],
         [0,0,0,0,1,0,0,0,0],
         [0,0,0,6,0,3,0,7,0],
         [5,0,0,2,0,0,0,0,0],
         [1,0,4,0,0,0,0,0,0]]


#print(init_table)
#draw_board(table)

#print(solve(init_table))
#draw_board(init_table)
#input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
#draw_board(input)

print(solve(table))