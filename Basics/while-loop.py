i,n = 1,10
print('break')
while(i<=n):
	if(i==5): break
	print(i);	i+=1

print('continue')
i = 0
while(i<n):
	i+=1
	if(i%2==0): continue
	print(i)

print('pass')
i = 0
while(i<n):
	i+=1
	if(i%2==0): pass
	print(i)