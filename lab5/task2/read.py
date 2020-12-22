import sqlite3

conn = sqlite3.connect('storages.db')
cursor = conn.cursor()

date = input('date: ')

cursor.execute("""SELECT name FROM storages WHERE price = (SELECT MAX(price) FROM storages WHERE date = ?) AND date = ? """, (date, date))

r = cursor.fetchone()
if r != None:
    r = r[0]

print("Name of most expensive:", r)

cursor.execute("""SELECT sum(price) as sum FROM storages""")

print("Sum of prices: ", cursor.fetchone()[0])