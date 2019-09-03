# FLOYD TRIANGLE
limit = int(input("Enter the limit: "))
n = 1
for i in range(1, limit+1):
    for j in range(1, i+1):
        print(n, ' ', end='')  # print on same line
        n += 1
    print('')
