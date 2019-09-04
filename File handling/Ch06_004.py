import sys

fo = open('test1.txt','r')
for v in fo:
	print(v)
	#sys.stdout.write(v)
fo.close()