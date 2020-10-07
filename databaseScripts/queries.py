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


def getNameSalaries(conn, deptName):

    cur = conn.cursor()
    cur.execute("SELECT Fname, Minit,Lname, Salary FROM employee, department WHERE DName=? and DepartmentNumber = Dnumber ", (deptName,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
            


def getProjNameHours(conn,lastName, firstName):

    cur = conn.cursor()
    cur.execute("SELECT Pname, Hours FROM project,employee, works_on WHERE Lname=? and Fname = ? and EmployeeSSN = Essn and Pno = Pnumber ", (lastName,firstName,))

    rows = cur.fetchall()

    for row in rows:
        print(row)  

def getTotalSalaries(conn, deptName):

    cur = conn.cursor()
    cur.execute("SELECT Salary, Fname FROM (employee JOIN department ON DepartmentNumber = Dnumber)WHERE DName =?", (deptName,))

    rows = cur.fetchall()

    for row in rows:
        print(row)  

def getAllDeptDetails(conn):

    cur = conn.cursor()
    cur.execute("SELECT DName, COUNT (*) FROM (employee JOIN department ON DepartmentNumber = Dnumber)")
    
    rows = cur.fetchall()

    for row in rows:
        print(row)      

def main():
    #create connection
    databaseName = "CSE3330_P1.db"
    conn = connection(databaseName)

    #Enter a department name, and retrieve all the names and salaries of all employees who work in that department.
    # getNameSalaries(conn, "Research")

    #Enter an employee last name and first name and retrieve a list of projects names/hours per week that the employee works on
    # getProjNameHours(conn, "Wong", "Franklin")
    
    #Enter a department name and retrieve the total of all employee salaries who work in the department
    getTotalSalaries(conn, "Research")

    #For each department, retrieve the department name and the number (count) of employees who work in that department. Order the result by number of employees in descending order
    getAllDeptDetails(conn)

if __name__ == '__main__':
    main()
