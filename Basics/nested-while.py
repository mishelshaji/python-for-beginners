#nested loops
import sys
n = int(input('Enter Level: '))
i = 1
while(i<=n):
	j=1
	while(j<=i):
		sys.stdout.write('* ')
		j+=1
	i+=1
	print()