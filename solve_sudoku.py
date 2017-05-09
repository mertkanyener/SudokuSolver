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

def reduce_group(group):

    return 0

def reduce(matrix):
    reducing = True


def rows_cols_boxes(matrix):
    res = []




table = """400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""

print(create_matrix(table))

