#REVERSE OF A NUMBER
num=copy=int(input('Enter a number'))
res=0
while(num>0):
    temp=num%10
    res=res*10+temp
    num=num//10 # The // stands for floor division
print(res)

#print(10/7) => 1.4285714285714286
#print(10//7) => 1