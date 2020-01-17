import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='jay011089',
    database='testdatabase',
)

mycursor = db.cursor()
#mycursor.execute('CREATE DATABASE testdatabase')  #建立database
#mycursor.execute('CREATE TABLE Person (name VARCHAR(50), age smallint  UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)')  #建立model
#mycursor.execute('insert into Person (name, age) values (%s,%s)', ('jens', 22))  #加入資料
#mycursor.execute('DELETE FROM Person WHERE personID = %s',(1,)) #刪除資料
#db.commit()  #更改資料就要commit

#mycursor.execute('select * from Person')  #取得資料
#mycursor.execute("TRUNCATE TABLE Person")  #清空table
#mycursor.execute('DROP TABLE Person')  #移除table

users = [('jay', '123@gmail.com'), 
('jens', '123456@gmail.com'),
('cool', '789@gmail.com')]

posts = [('ok吧',),
('帥氣',),
('早安',)]


Q1 = 'CREATE TABLE User(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), email VARCHAR(50))'
Q2 = 'CREATE TABLE Post(userID int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES User(id), comment VARCHAR(100), good int DEFAULT 0, bad int DEFAULT 0)'
'''
mycursor.execute(Q1)
mycursor.execute(Q2)
'''
#mycursor.execute('SHOW TABLES')


Q3 = 'INSERT INTO User (name, email) VALUES (%s, %s)'
Q4 = 'INSERT INTO Post (userID, comment) VALUES (%s, %s)'

for x, y in zip(users, posts):
    mycursor.execute(Q3, x)
    lastID = mycursor.lastrowid
    mycursor.execute(Q4, (lastID,) + y)

db.commit()

mycursor.execute('SELECT * FROM Post')

for x in mycursor:
    print(x)