#Queries

import sqlite3
from sqlite3 import Error

def connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Successfully Connected to SQLite")
        return conn
    except Error as e:
        print("Error while connecting to sqlite")
        print(e)

    return conn



def main():
    databaseName = "P2Part2.db"
    conn = connection(databaseName)

    cur = conn.cursor()
    cur.execute("SELECT count(*) as Total_record FROM customer")

    rows = cur.fetchone()
    print(list(rows))

    #query 1
    #cur = conn.cursor()
    #cur.execute(('''INSERT INTO customer(Name, Phone)
    #                VALUES (?,?)'''),("P.Shishir","(682) 227-5795"))

    #Query 2
    #cur = conn.cursor()
    #cur.execute("""Update customer set Phone = "(837) 721-8965"
    #               where Phone = "(682) 227-5795" """)

    #Query 3
    #cur = conn.cursor()
    #cur.execute("""Update rate set Daily = (Daily + 0.05*Daily)
    #               where Category = 1 """)

    #Query 4a
    #cur = conn.cursor()
    #cur.execute(('''INSERT INTO vehicle(VehicleID, Description, Year, Type, Category)
    #               VALUES (?,?,?,?,?)'''),("5FNRL6H58KB133711","Honda Odyssey",2019,6,1))

    #Query 4b
    #cur = conn.cursor()
    #cur.execute(('''INSERT INTO rate(Type, Category, Weekly, Daily)
    #               VALUES(?,?,?,?)'''),(6,1,800.00,135.00))

    #Query 6
    #cur = conn.cursor()
    #cur.execute(" SELECT c.Name, sum(r.TotalAmount) FROM rental as r, customer as c WHERE (r.CustID = 221 AND c.CustID = 221 AND r.PaymentDate IS NULL ) ")

    #rows = cur.fetchall()
    #print(rows)

    #Query 7
    #cur = conn.cursor()
    #cur.execute("SELECT VehicleID as VIN, Description, Year, Type, Category, Weekly, Daily")

    #Query 8
    #cur = conn.cursor()
    #cur.execute("SELECT sum(TotalAmount) FROM rental WHERE PaymentDate IS NOT NULL ")
    #rows = cur.fetchall()
    #print(rows)

    #Query 9-b
    cur = conn.cursor()
    cur.execute("SELECT c.Name, sum(r.TotalAmount) FROM rental as r,customer as c WHERE r.PaymentDate IS NULL  AND (r.CustId = (SELECT CustID FROM customer WHERE Name = 'J. Brown')) ")

    rows = cur.fetchall()
    print(rows)



    conn.commit()
    cur.close()

if __name__ == '__main__':
    main()
