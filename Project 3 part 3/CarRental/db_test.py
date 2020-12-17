
import sqlite3

conn = sqlite3.connect("CarRental.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('select * from customer')
r = c.fetchall()

for i in r:
    print (str(i['CustID']) + '--' + str(i['name'])) 