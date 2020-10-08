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
    print("Names and salaries of all employees who work in that department: " +deptName)
    try:
        cur = conn.cursor()
        cur.execute("SELECT Fname, Minit,Lname, Salary FROM employee, department WHERE DName=? and DepartmentNumber = Dnumber ", (deptName,))

        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
            


def getProjNameHours(conn,lastName, firstName):
    print("list of projects names/hours per week that the employee ("+firstName +" "+lastName +") works on")
    try:
        cur = conn.cursor()
        cur.execute("SELECT Pname, Hours FROM project,employee, works_on WHERE Lname=? and Fname = ? and EmployeeSSN = Essn and Pno = Pnumber ", (lastName,firstName,))

        rows = cur.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)  

def getTotalSalaries(conn, deptName):
    print("Retrieve the total of all employee salaries who work in the department : " + deptName)
    cur = conn.cursor()
    cur.execute("SELECT SUM(Salary) FROM (employee JOIN department ON DepartmentNumber = Dnumber)WHERE DName =?", (deptName,))
    try:
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)  

def getAllDeptEmp(conn):
    print("For each department, retrieve the department name and the number (count) of employees who work in that department. Order the result by number of employees in descending order")
    try:
        cur = conn.cursor()
        cur.execute("SELECT DName, COUNT(*) from department INNER JOIN employee ON DepartmentNumber = Dnumber GROUP BY DepartmentNumber, DName ORDER BY COUNT(*) ")
        
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)   

def getSupervisor(conn):
    print("For each employee who is a supervisor, retrieve the employee first and last name and number (count) of employees that are supervised. Order the result in descending order")
    try:
        cur = conn.cursor()
        cur.execute("WITH RECURSIVE SUP_EMP (SupSsn, EmpSsn) AS (SELECT SupervisorSSN, EmployeeSSN FROM employee UNION SELECT E.EmployeeSSN, S.SupSsn FROM EMPLOYEE AS E, SUP_EMP AS S WHERE E.SupervisorSsn = S.EmpSsn) SELECT * FROM SUP_EMP ")
        
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)  

def main():
    #create connection
    databaseName = "CSE3330_P1.db"
    conn = connection(databaseName)

    #Enter a department name, and retrieve all the names and salaries of all employees who work in that department.
    getNameSalaries(conn, "Research")

    #Enter an employee last name and first name and retrieve a list of projects names/hours per week that the employee works on
    getProjNameHours(conn, "Wong", "Franklin")
    
    #Enter a department name and retrieve the total of all employee salaries who work in the department
    getTotalSalaries(conn, "Research")

    #For each department, retrieve the department name and the number (count) of employees who work in that department. Order the result by number of employees in descending order
    getAllDeptEmp(conn)

    # For each employee who is a supervisor, retrieve the employee first and last name and number (count) of employees that are supervised. Order the result in descending order.
    #getSupervisor(conn)


if __name__ == '__main__':
    main()
