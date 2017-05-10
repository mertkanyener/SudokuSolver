import numpy as np


def draw_board(init_str):
    current_state = string_to_2d(init_str)
    for i in range(9):
        print('')
        if i == 3 or i == 6:
            print('------+------+------')
        for j in range(9):
            if j == 3 or j == 6:
                print('|', end='')
            if current_state[i][j] == 0:
                print(". ", end='')
            else:
                print(str(current_state[i][j]) + ' ', end='')

#Convert string to 2d nparray
def string_to_2d(init_str):
    arr = [int(ch) for ch in init_str]
    arr = np.array(arr).reshape(9, 9)
    return arr


def check_row(i, j):
    return i//9 == j//9


def check_col(i, j):
    return (i-j) % 9 == 0


def check_box(i, j):
    return i//27 == j//27 and i % 9//3 == j % 9//3


#Solve sudoku using a DFS
def solve(grid_str):
    i = grid_str.find('0') #find the next free cell
    if i < 0:
        #When there are no 0's left on grid stop searching and print solution
        print('\nSolution:')
        draw_board(grid_str)
        return
    else:
        eliminated = set() #set of eliminated values
        for j in range(81):
            #This is the process of reduction of the possible values
            if check_row(i, j) or check_col(i, j) or check_box(i, j):
                eliminated.add(grid_str[j]) #if current value exists in other units eliminate it
        for number in '123456789':
            if number not in eliminated:
                #Here we can see the DFS property of the algorithm since algorithm dives into the next states after inserting a valid value in the grid string
                grid_str = grid_str[:i] + number + grid_str[i + 1:] #insert the valid value in the string
                solve(grid_str) #go to next state




