n = int(input("Enter No: "))
"""
if(n%2==0):
	print("Even no.")
if(n%2!=0):
	print("Odd no.")
"""

'''
if(n==0): print("neither Even nor Odd")
else:
	if(n%2==0): print("Even")
	else : print("Odd")
'''

if(n!=0): print('Ur entered non-zero value')
else: print('Ur entered zero')

if(n==0): print('neither Even nor Odd')
elif(n%2==0): print('Even')
else : print('Odd')