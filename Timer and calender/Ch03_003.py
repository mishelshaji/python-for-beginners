import time
import sys

print('Use Ctrl+c to stop')
sys.stdout.write('Current Time: ')
while(1):
	t = time.localtime(time.time())
	sys.stdout.write('%2d:%2d:%2d' % (t[3],t[4],t[5]))
	time.sleep(1)
	sys.stdout.flush()
	sys.stdout.write('\b'*8)