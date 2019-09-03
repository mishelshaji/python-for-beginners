#PRIME OR NOT
num=int(input('Enter a number'))
if num<=1:
    print('Please enter a valid number')
    
for i in range(2,num):
    if(num % i == 0):
        print("The number is not prime number")
        break
else:
    print('The number is a prime number')