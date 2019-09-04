import sqlite3

def Display(cur):
	print('-'*35)
	for (id,it,pr) in cur:
		print("| %5d | %-10s | %10.2f |" % (id,it,pr))
	print('-'*35)

#connect to database
conn = sqlite3.connect('db/db_python')
#creating cursor for query execution
cur = conn.cursor()
menu = '''
	1) Show All
	2) Search
	3) New Record
	4) Update
	5) Delete
	6) Exit
'''
sql_ins = 'insert into stock values(?,?,?)'
sql_up	= 'update stock set item = ?,price = ? where id = ?'
sql_del	= 'delete from stock where id = ?'
sql_sel_all = 'select * from stock'
sql_sel	= 'select * from stock where id = ?'

while(True):
	print(menu)
	ch = int(input('choice ? '))
	if	(ch==1):
		cur.execute(sql_sel_all)
		Display(cur)
	elif(ch==2):
		id = input('Enter Id: ')
		cur.execute(sql_sel,(id))
		Display(cur)
	elif(ch==3):
		id = input('Enter Id: ')
		it = input('Enter Item: ')
		pr = input('Enter Price: ')
		cur.execute(sql_ins,(id,it,pr))
		conn.commit()
		print('saved !!')
	elif(ch==4):
		id = input('Enter Id: ')
		it = input('Enter Item: ')
		pr = input('Enter Price: ')
		cur.execute(sql_up,(it,pr,id))
		conn.commit()
		print('updated !!')
	elif(ch==5):
		id = input('Enter Id: ')
		cur.execute(sql_del,(id))
		conn.commit()
		print('deleted !!')
	elif(ch==6):
		cur.close()
		conn.close()
		break
	else:print('Wrong choice !!!')
print('Have a nice day !!!')