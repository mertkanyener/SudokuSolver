import numpy as np


def draw_board(initial):
    for i in range(9):
        print('')
        if i == 3 or i == 6:
            print('------+------+------')
        for j in range(9):
            if j == 3 or j == 6:
                print('|', end='')
            if initial[i][j] == 0:
                print(". ", end='')
            else:
                print(str(initial[i][j]) + ' ', end='')


def string_to_2d(init_str):
    init_str = init_str.replace('\n', '')
    arr = [int(ch) for ch in init_str]
    arr = np.array(arr).reshape(9, 9)
    return arr

def check_move(i, j, arr):

    return True





table = """400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""

init_table = string_to_2d(table)
draw_board(init_table)
