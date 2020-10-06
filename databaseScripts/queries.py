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
    cur.execute("SELECT SUM(Salary) FROM (employee JOIN department ON DepartmentNumber = Dnumber)WHERE DName =?", (deptName,))

    row = cur.fetchall()

    print(row) 

def main():
    #create connection
    databaseName = "CSE3330_P1.db"
    conn = connection(databaseName)

    #Enter a department name, and retrieve all the names and salaries of all employees who work in that department.
    # getNameSalaries(conn, "Research")

    #Enter an employee last name and first name and retrieve a list of projects names/hours per week that the employee works on
    getProjNameHours(conn, "Wong", "Franklin")
    
    #Enter a department name and retrieve the total of all employee salaries who work in the department
    getTotalSalaries(conn, "Research")

if __name__ == '__main__':
    main()
