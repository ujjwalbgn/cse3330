from django.db import connection
import sqlite3

def add_new_customer(customer):
    sql = ''' INSERT INTO customer (Name, Phone)
              VALUES (?,?) '''

    cur = connection.cursor()
    cur.execute(sql,customer)
    cur.commit()

def get_all_customer():
    # cur = connection.cursor()
    # cur.execute('''SELECT * FROM Customer''')
    # result = cur.fetchall()
    #
    connection.row_factory = sqlite3.Row
    c = connection.cursor()
    c.execute('select * from customer')
    result = c.fetchall()
    return result

def get_all_vehicle():
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Vehicle''')
    result = cur.fetchall()
    return result

def add_new_vehicle(vehicle):
    sql = ''' INSERT INTO vehicle (VehicleID, Description, Year, Type, Category)
              VALUES (?,?,?,?,?)'''


    cur = connection.cursor()
    cur.execute(sql,vehicle)
    cur.commit()

def search_available_vehicle(date):
    sql = ''' SELECT  DISTINCT vehicle.vehicleid ,description , year , rate.type, rate.category , rate.Daily 
      FROM vehicle, rental, rate WHERE (vehicle.vehicleid NOT IN (SELECT rental.VehicleID from rental) 
      AND rental.ReturnDate < %s ) AND vehicle.Category = RATE.Category  AND vehicle.Type = rate.Type'''

    cur = connection.cursor()
    cur.execute(sql, [date])
    result = cur.fetchall()
    return result

def add_new_rental(vehicle):
    sql = ''' INSERT INTO rental  (CustID, VehicleID, StartDate, OrderDate, RentalType, Qty, ReturnDate, TotalAmount,
     PaymentDate, returned)
              VALUES (?,?,?,?,?,?,?,?,?,?)'''

    cur = connection.cursor()
    cur.execute(sql,vehicle)
    cur.commit()


