# CREATING A MATRIX
# DO NOT MODIFY. IT MAY BREAK OTHER FILES
r = int(input('Enter the number of rows'))
c = int(input('Enter the number of columns'))
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f'Enter number {j}')))
    matrix.append(row)

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()

# OUTPUT
# 1 2 3
# 4 5 6
# 7 8 9