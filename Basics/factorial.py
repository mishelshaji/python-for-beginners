#FACTORIAL OF A NUMBER
a = input("Enter number1")
a=int(a)
factorial=1

if a==1:
    print('Factorial is 1')
elif a<1:
    print('Please enter a valid number')
else:
    for i in range(1, a+1):
        factorial *= i
    print(f'The factorial is {factorial}')