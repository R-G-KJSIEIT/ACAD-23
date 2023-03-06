import mysql.connector
db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     password="root",  # your password
                     db="world") # name of the data base

cur  = db.cursor()
cur.execute("use world")
#cur.execute("create table humans (human_ID varchar(100),Human_Name varchar(100),Human_Rights varchar(100));")
cur.execute("insert into humans(human_ID,Human_Name,Human_Rights) values('H1331','Meow','Poop'")
db.commit()
print("Table created")
str1 = cur.execute ("select * from humans;")
print(str1)

