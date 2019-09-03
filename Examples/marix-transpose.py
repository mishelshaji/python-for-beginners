# TRANSPOSE OF A MATRIX
# IMPORTING CODE TO CREATE A MATRIX FROM matrix.py
# WHICH IS LOCATED IN THE SAME DIRECTORY
from Examples import matrix as m

temp = [[0, 0], [0, 0]]
# temp = m.matrix.copy()
print('Transpose of the matrix is:')

rows = len(m.matrix)
cols = len(m.matrix[0])
print(rows, ' ', cols)
for i in range(rows):
    for j in range(cols):
        temp[i][j] = m.matrix[j][i]

# PRINTING THE TRANSPOSE
for i in range(rows):
    for j in range(cols):
        print(temp[i][j], end=" ")
    print()
