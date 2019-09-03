#LARGEST OF TWO NUMBERS
#METHOD 1
a=int(input('Enter first number'))
b=int(input('Enter second number'))
if(a>b):
    print(a)
else:
    print(b)
#METHOD 2
#Takes a list of numbers
print(max(a,b))