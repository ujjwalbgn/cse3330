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


    sql_create_employee_table = """ CREATE TABLE IF NOT EXISTS employee (
                                    id integer PRIMARY KEY,
                                    Fname text Null, 
                                    Minit text Null,
                                    Lname text Null,
                                    EmployeeNumber text Null,
                                    Bdate date Null,
                                    Address text Null,
                                    Sex text Null,
                                    Salary text Null,
                                    SupervisorNumber text Null,
                                    DepaetmentNumber text Null                                     
                                )"""

    sql_create_department_table = """ CREATE TABLE IF NOT EXISTS department (
                                    id integer PRIMARY KEY,
                                    Name text Null, 
                                    Location text Null,
                                    ManagerNumber number Null,
                                    StartDate number Null
                                )"""

    sql_create_deptLocation_table = """ CREATE TABLE IF NOT EXISTS deptLocation (
                                    id integer PRIMARY KEY,
                                    Location text Null
                                    )"""

    sql_create_project_table = """ CREATE TABLE IF NOT EXISTS project (
                                    id integer PRIMARY KEY,
                                    Name text Null,
                                    ProjectNumber text Null,
                                    Location text Null,
                                    DepartmentNumber text Null                                   
                                )"""

    sql_create_works_on_table = """ CREATE TABLE IF NOT EXISTS works_on (
                              EmployeeNumber text Null, 
                              ProjectNumber text Null,
                              hours text Null                                                                  
                            )"""

                       


    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_employee_table)
        create_table(conn, sql_create_department_table)
        create_table(conn, sql_create_deptLocation_table)
        create_table(conn, sql_create_project_table)
        create_table(conn, sql_create_works_on_table)
        
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()