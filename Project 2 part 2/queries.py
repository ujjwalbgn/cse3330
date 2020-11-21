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
    databaseName = "CarRental.db"
    conn = connection(databaseName)

    cur = conn.cursor()
    cur.execute("SELECT count(*) as Total_record FROM customer")

    rows = cur.fetchone()
    print("No. of Customers : " + str(list(rows)))

    query 1
    cur = conn.cursor()
    cur.execute(('''INSERT INTO customer(Name, Phone)
                   VALUES (?,?)'''),("P.Shishir","(682) 227-5795"))

    Query 2
    cur = conn.cursor()
    cur.execute("""Update customer set Phone = "(837) 721-8965"
                  where Phone = "(682) 227-5795" """)

    Query 3
    cur = conn.cursor()
    cur.execute("""Update rate set Daily = (Daily + 0.05*Daily)
                  where Category = 1 """)

    Query 4a
    cur = conn.cursor()
    cur.execute(('''INSERT INTO vehicle(VehicleID, Description, Year, Type, Category)
                  VALUES (?,?,?,?,?)'''),("5FNRL6H58KB133711","Honda Odyssey",2019,6,1))

    Query 4b
    cur = conn.cursor()
    cur.execute(('''INSERT INTO rate(Type, Category, Weekly, Daily)
                  VALUES(?,?,?,?)'''),(6,1,800.00,135.00))

    Query 5
    cur = conn.cursor()
    cur.execute("Select Distinct vehicle.VehicleID, Description, year, SUM(Julianday(ReturnDate)-Julianday(StartDate)) AS Total_days_rented From vehicle Left Join rental on vehicle.VehicleID=rental.VehicleID where vehicle.Type=1 AND vehicle.Category=1 AND rental.vehicleID NOT IN(Select VehicleID FROM rental WHERE (rental.StartDate Between '2019-06-01' AND '2019-06-20')  OR (rental.ReturnDate Between '2019-06-01' AND '2019-06-20'))Group BY vehicle.VehicleID")
    rows = cur.fetchall()
    print(rows)

    Query 6
    cur = conn.cursor()
    cur.execute(" SELECT c.Name, sum(r.TotalAmount) FROM rental as r, customer as c WHERE (r.CustID = 221 AND c.CustID = 221 AND r.PaymentDate IS NULL ) ")

    rows = cur.fetchall()
    print(rows)

    Query 7
    cur = conn.cursor()
    cur.execute("SELECT v.VehicleID as VIN, v.Description, v.Year, v.Type, v.Category, r.Weekly, r.Daily FROM vehicle as v, rate as r")
    rows = cur.fetchall()
    print(rows)

    Query 8
    cur = conn.cursor()
    cur.execute("SELECT sum(TotalAmount) FROM rental WHERE PaymentDate IS NOT NULL ")
    rows = cur.fetchall()
    print(rows)

    Query 9-a
    cur = conn.cursor()
    cur.execute("

    Query 9-b
    cur = conn.cursor()
    cur.execute("SELECT c.Name, sum(r.TotalAmount) FROM rental as r,customer as c WHERE r.PaymentDate IS NULL  AND (r.CustId = (SELECT CustID FROM customer WHERE Name = 'J. Brown')) ")

    rows = cur.fetchall()
    print(rows)

    Query 10
    cur.execute("SELECT c.Name,StartDate, ReturnDate,TotalAmount FROM (customer as c join rental as r ON c.CustID = r.CustID) WHERE VehicleID = '19VDE1F3XEE414842' AND RentalType = 7 AND PaymentDate is NULL ")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

    Query 11
    cur.execute("SELECT Name FROM customer WHERE CustID NOT IN(SELECT CustID FROM rental) ")
    rows = cur.fetchall()
    print(rows)

    Query 12
    cur.execute("SELECT c.Name, v.Description, r.StartDate, r.ReturnDate,r.TotalAmount FROM (customer as c , rental as r, vehicle as v) WHERE r.PaymentDate = r.StartDate AND c.CustID = r.CustID AND r.VehicleID = v.VehicleID")
    rows = cur.fetchall()
    print(rows)



    #
    # i =0
    # for row in rows:
    #     i = i + 1
    #     print(i)
    #     print(row)



    conn.commit()
    cur.close()

if __name__ == '__main__':
    main()
