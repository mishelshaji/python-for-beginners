#nested loops
import sys
n = int(input('Enter Level: '))

for i in range(1,n+1):
	for j in range(1,i+1):
		sys.stdout.write('* ')
	print()
	
for i in range(n+1,0,-1):
	for j in range(1,i+1):
		sys.stdout.write('* ')
	print()