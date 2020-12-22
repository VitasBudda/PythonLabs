import sqlite3

conn = sqlite3.connect('storages.db')
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE storages
#                   (name text, price integer, count integer, 
#                   date DATE, batch_number int, first_name text, last_name text)
#                """)

name = input('name: ')
price = input('price: ')
count = input('count: ')
date = input('date: ')
batch_number = input('batch_number: ')
first_name = input('first_name: ')
last_name = input('last_name: ')

cursor.execute('INSERT INTO storages VALUES (?, ?, ?, ?, ?, ?, ?)', 
    (name, price, count, date, batch_number, first_name, last_name))

conn.commit()

