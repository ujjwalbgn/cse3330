#run this python script to create a database and insert data
# Please note that this script is only meant to run once
# running the same insertion script again will create Unique constraint fail errors.

import sqlite3
from sqlite3 import Error
import csv 



def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection Sucessfull. Running Version SQLite3 " + sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_employee(conn):

    sql = ''' INSERT INTO employee(Fname,Minit,Lname,EmployeeSSN,Bdate,Street_Address,City,Zipcode,Sex,Sex,SupervisorSSN,DepartmentNumber)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    
    cur = conn.cursor()
    with open('EntryFiles/EMPLOYEE.csv.csv', "rt") as infile:
        read = csv.reader(infile)
        for row in read:
            try:
                cur.execute(sql, row)
                conn.commit()
            except Error as e:
               print("DEPARTMENT : ")
               print(e)

       


def insert_department(conn):
    sql = ''' INSERT INTO department(DName,Dnumber,ManagerSSN,StartDate)
              VALUES(?,?,?,?) '''

    cur = conn.cursor()
    with open('EntryFiles/DEPARTMENT.csv', "rt") as infile:
        read = csv.reader(infile)
        for row in read:
            try:
                cur.execute(sql, row)
                conn.commit()
            except Error as e:
               print("DEPARTMENT : ")
               print(e)


def insert_dept_Location(conn):

    sql = ''' INSERT INTO deptLocation(Dnumber,Dlocation)
               VALUES(?,?) '''

    cur = conn.cursor()
    with open('EntryFiles/DEPT_LOCATIONS.csv', "rt") as infile:
        read = csv.reader(infile)
        for row in read:
            try:
                cur.execute(sql, row)
                conn.commit()
            except Error as e:
               print("DEPT_LOCATIONS : ")
               print(e)


def insert_project(conn):

    sql = ''' INSERT INTO project(Pname,Pnumber,Plocation,Dnum)
              VALUES(?,?,?,?) '''

    cur = conn.cursor()
    with open('EntryFiles/PROJECT.csv', "rt") as infile:
        read = csv.reader(infile)
        for row in read:
            try:
                cur.execute(sql, row)
                conn.commit()
            except Error as e:
               print("PROJECT : ")
               print(e)


def insert_works_on(conn):

    sql = ''' INSERT INTO works_on(Essn,Pno,Hours)
              VALUES(?,?,?) '''

    cur = conn.cursor()
    with open('EntryFiles/WORKS_ON.csv', "rt") as infile:
        read = csv.reader(infile)
        for row in read:
            try:
                cur.execute(sql, row)
                conn.commit()
            except Error as e:
               print("WORKS_ON : ")
               print(e)


def main():
    #create connection
    conn = create_connection(r"CSE3330_P1.db")

    sql_create_employee_table = """ CREATE TABLE IF NOT EXISTS employee (
                                    Fname varchar(15) Not Null,
                                    Minit char,
                                    Lname varchar(15) Not Null,
                                    EmployeeSSN char(9) PRIMARY KEY,
                                    Bdate date,
                                    Street_Address varchar(30),
                                    City varchar(30),
                                    Zipcode char(5),
                                    Sex char,
                                    Salary Decimal(10,2),
                                    SupervisorSSN char(9) Null,
                                    DepartmentNumber int  Not Null
                                )"""

    sql_create_department_table = """ CREATE TABLE IF NOT EXISTS department (
                                    DName varchar(15) Not Null,
                                    Dnumber int PRIMARY KEY,
                                    ManagerSSN char(9) Not Null,
                                    StartDate date,
                                    UNIQUE(Dname),
                                    FOREIGN KEY(ManagerSSN) REFERENCES employee(EmployeeSSN)
                                )"""

    sql_create_dept_Location_table = """ CREATE TABLE IF NOT EXISTS deptLocation (
                                     Dnumber    INT NOT NULL,
                                     Dlocation    VARVHAR(15) NOT NULL,
                                     PRIMARY KEY (Dnumber, Dlocation)
                                     FOREIGN KEY (Dnumber) REFERENCES department(Dnumber)
                                     )"""

    sql_create_project_table = """ CREATE TABLE IF NOT EXISTS project (
                                     Pname VARCHAR(15) NOT NULL,
                                     Pnumber INT NOT NULL,
                                     Plocation VARCHAR(15),
                                     Dnum  INT NOT NULL,
                                     PRIMARY KEY(Pnumber),
                                     UNIQUE(Pname),
                                     FOREIGN KEY (Dnum) REFERENCES department(Dnumber)
                                 )"""

    sql_create_works_on_table = """ CREATE TABLE IF NOT EXISTS works_on (
                               Essn CHAR(9) NOT NULL,
                               Pno INT    NOT NULL,
                               Hours DECIMAL(3,1) NOT NULL,
                               PRIMARY KEY (Essn, Pno),
                               FOREIGN KEY (Essn) REFERENCES employee(EmployeeSSN),
                               FOREIGN KEY (Pno) REFERENCES project(Pnumber)
                             )"""

    #create tables
    if conn is not None:
        #create projects table
        create_table(conn, sql_create_employee_table)
        create_table(conn, sql_create_department_table)
        create_table(conn, sql_create_dept_Location_table)
        create_table(conn, sql_create_project_table)
        create_table(conn, sql_create_works_on_table)

    else:
        print("Error! cannot create the database connection.")



    insert_employee(conn)
    # insert_department(conn)
    # insert_dept_Location(conn)
    # insert_project(conn)
    # insert_works_on(conn)

    conn.close()


if __name__ == '__main__':
    main()
