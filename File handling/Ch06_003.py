fo = open('test2.txt','r')
str = fo.read(10)
print('Ist 10 characters: ',str)
pos = fo.tell()
print('Current Position :',pos)

pos = fo.seek(2,0)
print('Rest Current Position :',pos)
str = fo.read(10)
print('again 10 characters from 2nd : ',str)

fo.close()