r = input('Enter row count')
c = input('Enter col count')
r = int(r)
c = int(c)

m = []
for row in range(r):
    cols = []
    for col in range(c):
        cols.append(input(f"enter no for row: {row} and col{col}"))
    m.append(cols)

for row in range(r):
    for col in range(c):
        print(m[row][col], ' ', end='')
    print()