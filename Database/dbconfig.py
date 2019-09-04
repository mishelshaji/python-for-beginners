import mysql.connector

dbhost = 'localhost'
user = 'root'
pwd = 'root'
db = 'mishel'

d = mysql.connector.connect(host = dbhost, user = user, passwd = pwd, database = db)
conn = d.cursor()
