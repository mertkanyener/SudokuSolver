import copy


def create_matrix(input_str):
    result_matrix = []
    lines = input_str.split('\n')
    for line in lines:
        matrix_line = []
        for i in line:
            if i == '0':
                matrix_line.append(set(range(1, 10)))
            else:
                matrix_line.append({int(i)})
        result_matrix.append(matrix_line)
    return result_matrix


def rows_cols_boxes(matrix):
    res = []
    for i in range(9):
        res.append(copy.copy(matrix[i]))
    for j in range(9):
        column = []
        for i in range(9):
            column.append(copy.copy(matrix[i][j]))
        res.append(column)
    i, j = 0, 0
    for n in range(9):
        box = []
        if n == 3 or n == 6:
            i += 3
            j = 0
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                box.append(copy.copy(matrix[x][y]))
        res.append(box)
        j += 3
    return res


def reduce_group(group):
    duplicates = []
    reduced = False
    for cell in group:
        if cell not in duplicates:
            duplicates = [i for i in group if i == cell]
            if len(cell) == len(duplicates):
                for i in group:
                    if i not in duplicates:
                        i.difference_update(cell)
                reduced = True
    return reduced

def reduce_groups(groups):
    for group in groups:
        reduce_group(group)
    return False


def reduce(matrix):
    reducing = True
    all_groups = rows_cols_boxes(matrix)
    while reducing:
        reducing = reduce_group(all_groups)


def has_solution(matrix):
    for i in range(9):
        for j in range(9):
            if len(matrix[i][j]) == 0:
                return False
    return True


def check_solution(matrix):
    for i in range(9):
        for j in range(9):
            if len(matrix[i][j]) == 1:
                return False
    return True

def solve(matrix):
    reduce(matrix)
    if not has_solution(matrix):
        return None
    if check_solution(matrix):
        return matrix
    for i in range(9):
        for j in range(9):
            if len(matrix[i][j]) > 1:
                for k in matrix[i][j]:
                    mat_copy = copy.deepcopy(matrix)
                    mat_copy[i][j] = set([k])
                    result = solve(mat_copy)
                    if result != None:
                        return result
    return None







table = """400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""

matrix = create_matrix(table)
res = solve(matrix)
print(res)
