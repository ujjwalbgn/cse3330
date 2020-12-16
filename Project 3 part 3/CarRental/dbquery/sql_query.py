from django.db import connection

def add_new_customer(customer):
    sql = ''' INSERT INTO customer (Name, Phone)
              VALUES (?,?) '''

    try:
        cur = connection.cursor()
        cur.execute(sql,customer)
        cur.commit()
    except:
        print("Customer")


def get_all_customer():
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Customer''')
    result = cur.fetchall()
    return result

def get_all_vehicle():
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Vehicle''')
    result = cur.fetchall()
    return result

def add_new_vehicle(vehicle):
    sql = ''' INSERT INTO vehicle (VehicleID, Description, Year, Type, Category)
              VALUES (?,?,?,?,?)'''

    try:
        cur = connection.cursor()
        cur.execute(sql,vehicle)
        cur.commit()
    except:
        print("Vehicle")

def add_new_rental(vehicle):
    sql = ''' INSERT INTO rental  (CustID, VehicleID, StartDate, OrderDate, RentalType, Qty, ReturnDate, TotalAmount,
     PaymentDate, returned)
              VALUES (?,?,?,?,?,?,?,?,?,?)'''

    try:
        cur = connection.cursor()
        cur.execute(sql,vehicle)
        cur.commit()
    except:
        print("RENTAL")
#
