from django.db import connection



def add_new_customer(customer):
    sql = ''' INSERT INTO customer (Name, Phone)
              VALUES (?,?) '''

    try:
        cur = connection.cursor()
        cur.execute(sql,customer)
        cur.commit()
    except:
        print("Error at Insert Customer")


def get_all_customer():
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Customer''')
    result = cur.fetchall()
    return result