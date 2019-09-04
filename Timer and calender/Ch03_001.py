import time
t = time.localtime(time.time())
print(t)
# 0-year, 1-month, 2-dayOfMonth, 3-hour, 4-minute, 5-second, 6-weekDay, 7-dayOfYear
print('Current Time: %d:%d:%d' % (t[3],t[4],t[5]))
print('Today: %d/%d/%d' % (t[2],t[1],t[0]))

t1 = time.asctime(t)
print(t1)