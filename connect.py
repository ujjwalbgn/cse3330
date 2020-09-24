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

def insert_employee(conn, employee):
    """
    Create a new employee
    :param conn:
    :param employee:
    """

    sql = ''' INSERT INTO employee(Fname,Minit,Lname,EmployeeSSN,Bdate,Address,Sex,Salary,SupervisorSSN,DepartmentNumber)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
              
    try:
        cur = conn.cursor()
        cur.execute(sql, employee)
        conn.commit()
    except Error as e:
        print(e)

def insert_department(conn, department):
    """
    Create a new department
    :param conn:
    :param department:
    """

    sql = ''' INSERT INTO department(DName,Dnumber,ManagerSSN,StartDate)
              VALUES(?,?,?,?) '''
              
    try:
        cur = conn.cursor()
        cur.execute(sql, department)
        conn.commit()
    except Error as e:
        print(e)   

def insert_dept_Location(conn, dept_Location):
     """
    Create a new dept_Location
    :param conn:
    :param dept_Location:
    """
    sql = ''' INSERT INTO department(Dnumber,Dlocation)
              VALUES(?,?) '''

    try:
        cur = conn.cursor()
        cur.execute(sql, dept_Location)
        conn.commit()
    except Error as e:
        print(e)

def insert_project(conn, project):
     """
    Create a new project
    :param conn:
    :param project
    """
    sql = ''' INSERT INTO project(Pname,Pnumber,Plocation,Dnum)
              VALUES(?,?,?,?) '''

    try:
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
    except Error as e:
        print(e)        

def insert_works_on(conn, works_on):
     """
    Create a new works_on
    :param conn:
    :param works_on
    """
    sql = ''' INSERT INTO works_on(Essn,Pno,Hours)
              VALUES(?,?,?) '''

    try:
        cur = conn.cursor()
        cur.execute(sql, works_on)
        conn.commit()
    except Error as e:
        print(e)  


def main():
    #create connection
    conn = create_connection(r"day1.db")

    sql_create_employee_table = """ CREATE TABLE IF NOT EXISTS employee (
                                    Fname varchar(15) Not Null, 
                                    Minit char,
                                    Lname varchar(15) Not Null,
                                    EmployeeSSN char(9) PRIMARY KEY,
                                    Bdate date,
                                    Address varchar(30),
                                    Sex char,
                                    Salary Decimal(10,2),
                                    SupervisorSSN char(9),
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


     #insert Employed 
    employee_1 = ('James', 'E', 'Borg', '888665555', '10-NOV-1927', '450 Stone,Houston,TX', 'M', 55000, None, 1); 
    employee_2 = ('Franklin', 'T', 'Wong', '333445555', '08-DEC-1945', '638 Voss,Houston,TX', 'M', 40000, '888665555', 5)   
    insert_employee(conn, employee_1 )   
    insert_employee(conn, employee_2 )
    
    department_1 = ('Research', 5, '333445555', '22-MAY-1978') 
    insert_department(conn,department_1)

    dept_Location_1 = (1, 'Houston')
    dept_Location_2 = (4, 'Stafford')
    insert_dept_Location(conn, dept_Location_1)
    insert_dept_Location(conn, dept_Location_2)

    project_table_1 = ('ProductX', 1, 'Bellaire', 5)
    project_table_2 = ('ProductY', 2, 'Sugarland', 5)
    insert_project(conn, project_table_1)
    insert_project(conn, project_table_2)

    works_on_1 = ('123456789', 1, 32.5)
    insert_works_on(conn, works_on_1)

    conn.close()

if __name__ == '__main__':
    main()

   
