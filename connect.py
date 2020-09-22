import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection Sucessfull. Running Version SQLite3 " + sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    #create connection
    conn = create_connection(r"day1.db")


    sql_create_employee_table = """ CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    Fname text Null, 
                                    Minit text Null,
                                    Lname text Null,
                                    Bdate date Null,
                                    Address text Null,
                                    Salary text Null,
                                    Sex text Null  
                                )"""

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_employee_table)
        
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()