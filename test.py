import numpy as np


table = """400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""

init_str = table.replace('\n', '')
arr = [int(ch) for ch in init_str]
arr = np.array(arr).reshape(9,9)
print(arr)

a = arr[0].remove(arr[0][6])
print(a)