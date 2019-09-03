#MULTIPLICATION TABLE
a=int(input('Enter a limit'))
b=int(input('Enter a number to multiply'))
for i in range(1, a+1):
    print(f'{i} * {b} = {i*b}')