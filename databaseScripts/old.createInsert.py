#run this python script to create a database and insert data
# Please note that this script is only meant to run once
# running the same insertion script again will create Unique constraint fail errors.

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


def insert_dept_Location(conn, deptLocation):
    """
    Create a new deptLocation
    :param conn:
    :param deptLocation:
    """

    sql = ''' INSERT INTO deptLocation(Dnumber,Dlocation)
               VALUES(?,?) '''

    try:
        cur = conn.cursor()
        cur.execute(sql, deptLocation)
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
    conn = create_connection(r"CSE3330_P1.db")

    sql_create_employee_table = """ CREATE TABLE IF NOT EXISTS employee (
                                    Fname varchar(15) Not Null,
                                    Minit char,
                                    Lname varchar(15) Not Null,
                                    EmployeeSSN char(9) PRIMARY KEY,
                                    Bdate date,
                                    Address varchar(30),
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


     #insert Employed
    employee_1 = ('James', 'E', 'Borg', '888665555', '10-NOV-1927', '450 Stone,Houston,TX', 'M', 55000, None, 1)
    employee_2 = ('Franklin', 'T', 'Wong', '333445555', '08-DEC-1945', '638 Voss,Houston,TX', 'M', 40000, '888665555', 5)
    employee_3 = ('Jennifer', 'S', 'Wallace', '987654321', '20-JUN-1931', '291 Berry,Bellaire,TX', 'F', 43000, '888665555', 4)
    employee_4 = ('Jared', 'D', 'James', '111111100', '10-OCT-1966', '123 Peachtr,Atlanta,GA', 'M', 85000, None, 6)
    employee_5=('Alex', 'D', 'Freed', '444444400', '09-OCT-1950', '4333 Pillsbury,Milwaukee,WI', 'M', 89000, None, 7)
    employee_6=('John', 'C', 'James', '555555500', '30-JUN-1975', '766 Bloomington,Sacramento,CA', 'M', 81000, None, 8)
    employee_7=('John', 'B', 'Smith', '123456789', '09-Jan-1955', '731 Fondren,Houston,TX', 'M', 30000, '333445555', 5)
    employee_8=('Alicia', 'J', 'Zelaya', '999887777', '19-JUL-1958', '3321 Castle,Spring,TX', 'F', 25000, '987654321', 4)
    employee_9=('Ramesh', 'K', 'Narayan', '666884444', '15-SEP-1952', '971 Fire Oak,Humble,TX', 'M', 38000, '333445555', 5)
    employee_10=('Joyce', 'A', 'English', '453453453', '31-JUL-1962', '5631 Rice Oak,Houston,TX', 'F', 25000, '333445555', 5)
    employee_11=('Ahmad', 'V', 'Jabbar', '987987987', '29-MAR-1959', '980 Dallas,Houston,TX', 'M', 25000, '987654321', 4)
    employee_12=('Jon', 'C', 'Jones', '111111101', '14-NOV-1967', '111 Allgood,Atlanta,GA', 'M', 45000, '111111100', 6)
    employee_13=('Justin', None, 'Mark', '111111102', '12-JAN-1966', '2342 May,Atlanta,GA', 'M', 40000, '111111100', 6)
    employee_14=('Brad', 'C', 'Knight', '111111103', '13-FEB-1968', '176 Main St.,Atlanta,GA', 'M', 44000, '111111100', 6)
    employee_15=('Evan', 'E', 'Wallis', '222222200', '16-JAN-1958', '134 Pelham,Milwaukee,WI', 'M', 92000, None, 7)
    employee_16=('Josh', 'U', 'Zell', '222222201', '22-MAY-1954', '266 McGrady,Milwaukee,WI', 'M', 56000, '222222200', 7)
    employee_17=('Andy', 'C', 'Vile', '222222202', '21-JUN-1944', '1967 Jordan,Milwaukee,WI', 'M', 53000, '222222200', 7)
    employee_18=('Tom', 'G', 'Brand', '222222203', '16-DEC-1966', '112 Third St,Milwaukee,WI', 'M', 62500, '222222200', 7)
    employee_19=('Jenny', 'F', 'Vos', '222222204', '11-NOV-1967', '263 Mayberry,Milwaukee,WI', 'F', 61000, '222222201', 7)
    employee_20=('Chris', 'A', 'Carter', '222222205', '21-MAR-1960', '565 Jordan,Milwaukee,WI', 'F', 43000, '222222201', 7)
    employee_21=('Kim', 'C', 'Grace', '333333300', '23-OCT-1970', '667 Mills Ave,Sacramento,CA', 'F', 79000, None, 6)
    employee_22=('Jeff', 'H', 'Chase', '333333301', '07-JAN-1970', '15 Bradbury,Sacramento,CA', 'M', 44000, '333333300', 6)
    employee_23=('Bonnie', 'S', 'Bays', '444444401', '19-JUN-1956', '111 Hollow,Milwaukee,WI', 'F', 70000, '444444400', 7)
    employee_24=('Alec', 'C', 'Best', '444444402', '18-JUN-1966', '233 Solid,Milwaukee,WI', 'M', 60000, '444444400', 7)
    employee_25=('Sam', 'S', 'Snedden', '444444403', '31-JUL-1977', '97 Windy St,Milwaukee,WI', 'M', 48000, '444444400', 7)
    employee_26=('Nandita', 'K', 'Ball', '555555501', '16-APR-1969', '222 Howard,Sacramento,CA', 'M', 62000, '555555500', 6)
    employee_27=('Bob', 'B', 'Bender', '666666600', '17-APR-1968', '8794 Garfield,Chicago,IL', 'M', 96000, None, 8)
    employee_28=('Jill', 'J', 'Jarvis', '666666601', '14-JAN-1966', '6234 Lincoln,Chicago,IL', 'F', 36000, '666666600', 9)
    employee_29=('Kate', 'W', 'King', '666666602', '16-APR-1966', '1976 Boone Trace,Chicago,IL', 'F', 44000, '666666600', 8)
    employee_30=('Lyle', 'G', 'Leslie', '666666603', '09-JUN-1963', '417 Hancock Ave,Chicago,IL', 'M', 41000, '666666601', 8)
    employee_31=('Billie', 'J', 'King', '666666604', '01-JAN-1960', '556 Washington,Chicago,IL', 'F', 38000, '666666603', 8)
    employee_32=('Megan', 'G', 'Jones', '254937381', '02-MAR-1961', '528 Stone CT,Chicago,IL', 'F', 62000, '666666600', 8)
    employee_33=('Jon', 'A', 'Kramer', '666666605', '22-AUG-1964', '1988 Windy Creek,Seattle,WA', 'M', 41500, '666666603', 8)
    employee_34=('Ray', 'H', 'King', '666666606', '16-AUG-1949', '213 Delk Road,Seattle,WA', 'M', 44500, '666666604', 9)
    employee_35=('Gerald', 'D', 'Small', '666666607', '15-MAY-1962', '122 Ball Street,Dallas,TX', 'M', 29000, '666666602', 8)
    employee_36=('Arnold', 'A', 'Head', '666666608', '19-MAY-1967', '233 Spring St,Dallas,TX', 'M', 33000, '666666602', 8)
    employee_37=('Helga', 'C', 'Pataki', '666666609', '11-MAR-1969', '101 Holyoke St,Dallas,TX', 'F', 32000, '666666602', 8)
    employee_38=('Naveen', 'B', 'Drew', '666666610', '23-MAY-1970', '198 Elm St,Philadelphia,PA', 'M', 34000, '666666607', 8)
    employee_39=('Carl', 'E', 'Reedy', '666666611', '21-JUN-1977', '213 Ball St,Philadelphia,PA', 'M', 32000, '666666610', 8)
    employee_40=('Sammy', 'G', 'Hall', '666666612', '11-JAN-1970', '433 Main Street,Miami,FL', 'M', 37000, '666666611', 8)
    employee_41=('Red', 'A', 'Bacher', '666666613', '21-MAY-1980', '196 Elm Street,Miami,FL', 'M', 33500, '666666612', 8)
    employee_42=('Roy', 'C', 'Lewallen', '999999999', '02-MAR-1977', '14 Wynncrest Street,Dallas,TX', 'M', 75500, '666666600', 8)
    employee_43=('John', 'T', 'Ed', '222333444', '18-FEB-1981', '4505 West St,Rochester,NY', 'M', 30000, '555555501', 6)
    employee_44=('Jennifer', 'A', 'Joy', '223344667', '19-MAY-1976', '1204 Main St,Miami,FL', 'F', 45000, '666666613', 8)
    employee_45=('Kim', 'G', 'Ted', '444222666', '15-APR-1968', '3648 Tree Cir,Austin,TX', 'M', 50000, '999999999', 9)
    employee_46=('Juan', 'G', 'Linda', '112244668', '23-JUN-1965', '1210 Apple St,Austin,TX', 'F', 55000, None, 9)
    employee_47=('Jose', 'H', 'Barbara', '343434344', '28-FEB-1955', '905 East St,Kleen,TX', 'F', 35000, '444444400', 6)
    employee_48=('willie', 'D', 'Mary', '234234234', '20-DEC-1961', '101 South St,Arlington,TX', 'F', 12000, '112244668', 9)
    employee_49=('Erin', 'A', 'Maxfield', '242535609', '22-DEC-1971', '123 Copper St,Arlington,TX', 'F', 72000, '555555500', 8)
    employee_50=('Johny', 'C', 'Smith', '122344668', '26-JAN-1972', '1221 Diploma Dr.,Arlington,TX', 'M', 65000, '999999999', 9)
    employee_51=('Sunil', 'D', 'Gupta', '110110110', '01-FEB-2001', '4312 Bowen Rd,Arlington,TX', 'M', 80000, '111111100', 3)
    employee_52=('Penny', 'G', 'Wolowitz', '673466642', '21-JAN-1974', '42 South Blvd,Miami,FL', 'F', 17000, '222333444', 6)
    employee_53=('Michael', 'A', 'Morgan', '636669233', '11-MAY-1984', '26 Sunset Blvd,Miami,FL', 'M', 73500, '666666612', 5)
    employee_54=('Sheldon', 'C', 'Cucuou', '849934919', '22-MAR-1974', '11 Hollywood Blvd,Dallas,TX', 'M', 35500, '888665555', 8)
    employee_55=('Debra', 'T', 'Hall', '202843824', '11-MAR-1983', '45 NY St,Rochester,NY', 'F', 30000, '555555501', 6)
    employee_56=('Jisha', 'A', 'Carpenter', '292740167', '29-MAY-1985', '194 Beachdr,Miami,FL', 'F', 15000, '666666613', 1)
    employee_57=('Gregory', 'G', 'Laurie', '444212096', '15-SEP-1969', '78 Tree Cir,Houston,TX', 'M', 90000, '444444400', 7)
    employee_58=('Lisa', 'G', 'House', '101248268', '29-JUN-1975', '12 Maple St,Austin,TX', 'F', 85000, None, 7)
    employee_59=('Leonard', 'H', 'Moody', '349273344', '09-FEB-1973', '908 Greek Row,Austin,TX', 'M', 45000, '444444400', 7)
    employee_60=('Jake', 'D', 'Sheen', '245239264', '25-DEC-1954', '20 North Co,Arlington,TX', 'M', 52000, '112244668', 6)
    employee_61=('Wilson', 'A', 'Holmes', '242916639', '02-JUN-1971', '21 South Co,Arlington,TX', 'M', 72500, '555555500', 4)
    employee_62=('Cameron', 'D', 'Thirteen', '111422203', '04-MAY-2001', '22 Univ Blvd,Arlington,TX', 'F', 80000, '987987987', 4)
    employee_63=('Joseph', 'K', 'Kirkish', '913323708', '04-MAR-1996', '22 UT Blvd,Austin,TX', 'M', 95000, None, 7)
    employee_64=('Andrea', 'M', 'Sondrini', '614370310', '30-DEC-1996', '1450 Worthington St,Houston,TX', 'F', 65000, '444444401', 5)
    employee_65=('Cindy', 'K', 'Burklow', '432765098', '23-FEB-1984', '2015 Neil Ave,Miami,FL', 'F', 45000, '444444402', 6)
    employee_66=('Zach', 'A', 'Geller', '913353347', '15-AUG-1990', '333 PikeWay,Seattle,WA', 'M', 55000, '444444403', 6)
    employee_67=('Alex', 'C', 'Yu', '001614905', '17-OCT-1980', '626 Mary St,Dallas,TX', 'M', 50000, '444444400', 6)
    employee_68=('Richard', 'T', 'Koelbel', '214370999', '3-APR-1976', '50 Elk St,Chicago,IL', 'M', 85000, '999999999', 4)
    employee_69=('Christina', 'S', 'Hisel', '241625699', '5-JUL-1986', '37 Church Row,Rochester,NY', 'F', 45000, '123456789', 6)
    employee_70=('Percy', 'M', 'Liang', '398172999', '12-JUN-1991', '14 Maple St,Austin,TX', 'M', 55000, None, 9)
    employee_71=('James', 'U', 'Miller', '906218888', '27-MAY-1978', '13 Fifth St,Seattle,WA', 'M', 75000, '999999999', 5)




    insert_employee(conn, employee_1 )
    insert_employee(conn, employee_2 )
    insert_employee(conn, employee_3 )
    insert_employee(conn, employee_4 )
    insert_employee(conn, employee_5 )
    insert_employee(conn, employee_6 )
    insert_employee(conn, employee_7 )
    insert_employee(conn, employee_8 )
    insert_employee(conn, employee_9 )
    insert_employee(conn, employee_10 )
    insert_employee(conn, employee_11 )
    insert_employee(conn, employee_12 )
    insert_employee(conn, employee_13 )
    insert_employee(conn, employee_14 )
    insert_employee(conn, employee_15 )
    insert_employee(conn, employee_16 )
    insert_employee(conn, employee_17 )
    insert_employee(conn, employee_18 )
    insert_employee(conn, employee_19 )
    insert_employee(conn, employee_20 )
    insert_employee(conn, employee_21 )
    insert_employee(conn, employee_22 )
    insert_employee(conn, employee_23 )
    insert_employee(conn, employee_24 )
    insert_employee(conn, employee_25 )
    insert_employee(conn, employee_26 )
    insert_employee(conn, employee_27 )
    insert_employee(conn, employee_28 )
    insert_employee(conn, employee_29 )
    insert_employee(conn, employee_30 )
    insert_employee(conn, employee_31 )
    insert_employee(conn, employee_32 )
    insert_employee(conn, employee_33 )
    insert_employee(conn, employee_34 )
    insert_employee(conn, employee_35 )
    insert_employee(conn, employee_36 )
    insert_employee(conn, employee_37 )
    insert_employee(conn, employee_38 )
    insert_employee(conn, employee_39 )
    insert_employee(conn, employee_40 )
    insert_employee(conn, employee_41 )
    insert_employee(conn, employee_42 )
    insert_employee(conn, employee_43 )
    insert_employee(conn, employee_44 )
    insert_employee(conn, employee_45 )
    insert_employee(conn, employee_46 )
    insert_employee(conn, employee_47 )
    insert_employee(conn, employee_48 )
    insert_employee(conn, employee_49 )
    insert_employee(conn, employee_50 )
    insert_employee(conn, employee_51 )
    insert_employee(conn, employee_52 )
    insert_employee(conn, employee_53 )
    insert_employee(conn, employee_54 )
    insert_employee(conn, employee_55 )
    insert_employee(conn, employee_56 )
    insert_employee(conn, employee_57 )
    insert_employee(conn, employee_58 )
    insert_employee(conn, employee_59 )
    insert_employee(conn, employee_60 )
    insert_employee(conn, employee_61 )
    insert_employee(conn, employee_62 )
    insert_employee(conn, employee_63 )
    insert_employee(conn, employee_64 )
    insert_employee(conn, employee_65 )
    insert_employee(conn, employee_66 )
    insert_employee(conn, employee_67 )
    insert_employee(conn, employee_68 )
    insert_employee(conn, employee_69 )
    insert_employee(conn, employee_70 )
    insert_employee(conn, employee_71 )



    department_1 = ('Research', 5, '333445555', '22-MAY-1978')
    department_3 = ('Administration', 4, '987654321', '01-JAN-1985')
    department_4 = ('Headquarters', 1, '888665555', '19-JUN-1971')
    department_5 = ('Software', 6, '111111100', '15-MAY-1999')
    department_6 = ('Hardware', 7, '444444400', '15-MAY-1998')
    department_7 = ('Sales', 8, '555555500', '01-JAN-1997')
    department_8 = ('HR', 9, '112244668', '01-FEB-1989')
    department_9 = ('Networking', 3, '110110110', '15-MAY-2009')
    department_10 = ('QA', 11, '913323708', '2-FEB-2010')


    insert_department(conn,department_1)
    insert_department(conn,department_3)
    insert_department(conn,department_4)
    insert_department(conn,department_5)
    insert_department(conn,department_6)
    insert_department(conn,department_7)
    insert_department(conn,department_8)
    insert_department(conn,department_9)
    insert_department(conn,department_10)

    dept_Location_1 = (1, 'Houston')
    dept_Location_2 = (4, 'Stafford')
    dept_Location_3 = (5, 'Bellaire')
    dept_Location_4 = (5, 'Sugarland')
    dept_Location_5 = (5, 'Houston')
    dept_Location_6 = (6, 'Atlanta')
    dept_Location_7 = (6, 'Sacramento')
    dept_Location_8 = (7, 'Milwaukee')
    dept_Location_9 = (8, 'Chicago')
    dept_Location_10 = (8, 'Dallas')
    dept_Location_11 = (8, 'Philadephia')
    dept_Location_12 = (8, 'Seattle')
    dept_Location_13 = (8, 'Miami')
    dept_Location_14 = (9, 'Arlington')
    dept_Location_15 = (11, 'Austin')


    insert_dept_Location(conn, dept_Location_1)
    insert_dept_Location(conn, dept_Location_2)
    insert_dept_Location(conn, dept_Location_3)
    insert_dept_Location(conn, dept_Location_4)
    insert_dept_Location(conn, dept_Location_5)
    insert_dept_Location(conn, dept_Location_6)
    insert_dept_Location(conn, dept_Location_7)
    insert_dept_Location(conn, dept_Location_8)
    insert_dept_Location(conn, dept_Location_9)
    insert_dept_Location(conn, dept_Location_10)
    insert_dept_Location(conn, dept_Location_11)
    insert_dept_Location(conn, dept_Location_12)
    insert_dept_Location(conn, dept_Location_13)
    insert_dept_Location(conn, dept_Location_14)
    insert_dept_Location(conn, dept_Location_15)

    project_table_1 = ('ProductX', 1, 'Bellaire', 5)
    project_table_2 = ('ProductY', 2, 'Sugarland', 5)
    project_table_3 = 'ProductZ', 3, 'Houston', 5
    project_table_4 = 'Computerization', 10, 'Stafford', 4
    project_table_5 = 'Reorganization', 20, 'Houston', 1
    project_table_6 = 'Newbenefits', 30, 'Stafford', 4
    project_table_7 = 'OperatingSystem', 61, 'Sacramento', 6
    project_table_8 = 'DatabaseSystems', 62, 'Atlanta', 6
    project_table_9 = 'Middleware', 63, 'Atlanta', 6
    project_table_10 = 'Advertizing', 70, 'Arlington', 9
    project_table_11 = 'InkjetPrinters', 91, 'Milwaukee', 7
    project_table_12 = 'LaserPrinters', 92, 'Milwaukee', 7
    project_table_13 = 'Human1', 95, 'Arlington',9
    project_table_14 = 'SearchEngine', 22, 'Arlington', 6
    project_table_15 = 'MotherBoard', 29, 'Milwaukee', 7
    project_table_16 = 'EntityAnnot', 4, 'Houston', 5
    project_table_17 = 'ConfigMgmt', 11, 'Atlanta',6
    project_table_18 = 'DataMining', 13, 'Sacramento',6

    insert_project(conn, project_table_1)
    insert_project(conn, project_table_2)
    insert_project(conn, project_table_3)
    insert_project(conn, project_table_4)
    insert_project(conn, project_table_5)
    insert_project(conn, project_table_6)
    insert_project(conn, project_table_7)
    insert_project(conn, project_table_8)
    insert_project(conn, project_table_9)
    insert_project(conn, project_table_10)
    insert_project(conn, project_table_11)
    insert_project(conn, project_table_12)
    insert_project(conn, project_table_13)
    insert_project(conn, project_table_14)
    insert_project(conn, project_table_15)
    insert_project(conn, project_table_16)
    insert_project(conn, project_table_17)
    insert_project(conn, project_table_18)

    works_on_1 = ('123456789', 1, 32.5)
    works_on_2 = ('123456789', 2, 7.5)
    works_on_3 = ('666884444', 3, 40.0)
    works_on_4 = ('453453453', 1, 20.0)
    works_on_5 = ('453453453', 2, 20.0)
    works_on_6 = ('333445555', 2, 10.0)
    works_on_7 = ('333445555', 3, 10.0)
    works_on_8 = ('333445555', 10, 10.0)
    works_on_9 = ('333445555', 20, 10.0)
    works_on_10 = ('242535609', 70, 20.0)
    works_on_11 = ('242535609', 62, 20.0)
    works_on_12 = ('999887777', 30, 30.0)
    works_on_13 = ('999887777', 10, 10.0)
    works_on_14 = ('987987987', 10, 35.0)
    works_on_15 = ('987987987', 30, 5.0)
    works_on_16 = ('987654321', 30, 20.0)
    works_on_17 = ('987654321', 20, 15.0)
    works_on_18 = ('888665555', 20, 5.0)
    works_on_19 = ('111111100', 61, 40.0)
    works_on_20 = ('111111101', 61, 40.0)
    works_on_21 = ('111111102', 61, 40.0)
    works_on_22 = ('111111103', 61, 40.0)
    works_on_23 = ('222222200', 62, 40.0)
    works_on_24 = ('222222201', 62, 48.0)
    works_on_25 = ('222222202', 62, 40.0)
    works_on_26 = ('222222203', 62, 40.0)
    works_on_27 = ('222222204', 62, 40.0)
    works_on_28 = ('222222205', 62, 40.0)
    works_on_29 = ('333333300', 63, 40.0)
    works_on_30 = ('333333301', 63, 46.0)
    works_on_31 = ('444444400', 91, 40.0)
    works_on_32 = ('444444401', 91, 40.0)
    works_on_33 = ('444444402', 91, 40.0)
    works_on_34 = ('444444403', 91, 40.0)
    works_on_35 = ('555555500', 92, 40.0)
    works_on_36 = ('555555501', 92, 44.0)
    works_on_37 = ('666666601', 91, 40.0)
    works_on_38 = ('666666603', 91, 40.0)
    works_on_39 = ('666666604', 91, 40.0)
    works_on_40 = ('666666605', 92, 40.0)
    works_on_41 = ('666666606', 91, 40.0)
    works_on_42 = ('666666607', 61, 40.0)
    works_on_43 = ('666666608', 62, 40.0)
    works_on_44 = ('666666609', 63, 40.0)
    works_on_45 = ('666666610', 61, 40.0)
    works_on_46 = ('666666611', 61, 40.0)
    works_on_47 = ('666666612', 61, 40.0)
    works_on_48 = ('666666613', 61, 30.0)
    works_on_49 = ('666666613', 62, 10.0)
    works_on_50 = ('666666613', 63, 10.0)
    works_on_95 = ('999999999', 1, 2.0)
    works_on_51 = ('999999999', 2, 2.0)
    works_on_52 = ('999999999', 3, 4.0)
    works_on_53 = ('999999999', 10, 4.0)
    works_on_54 = ('999999999', 20, 4.0)
    works_on_55 = ('999999999', 30, 4.0)
    works_on_56 = ('999999999', 61, 4.0)
    works_on_57 = ('999999999', 62, 4.0)
    works_on_58 = ('999999999', 63, 4.0)
    works_on_59 = ('999999999', 70, 2.0)
    works_on_60 = ('999999999', 91, 2.0)
    works_on_61 = ('999999999', 92, 1.0)
    works_on_62 = ('999999999', 95, 3.0)
    works_on_63 = ('254937381', 70, 40.0)
    works_on_64 = ('222333444', 91, 10.0)
    works_on_65 = ('223344667', 63, 20.0)
    works_on_66 = ('444222666', 62, 25.0)
    works_on_67 = ('112244668', 95, 40.0)
    works_on_68 = ('343434344', 63, 40.0)
    works_on_69 = ('234234234', 95, 35.0)
    works_on_70 = ('913323708', 92, 33.0)
    works_on_71 = ('636669233', 4, 11.0)
    works_on_72 = ('614370310', 3, 45.0)
    works_on_73 = ('849934919', 95, 23.0)
    works_on_74 = ('432765098', 63, 25.0)
    works_on_75 = ('444212096', 63, 25.0)
    works_on_76 = ('913353347', 22, 30.0)
    works_on_77 = ('292740167', 1, 25.0)
    works_on_78 = ('202843824', 11, 20.0)
    works_on_79 = ('673466642', 22, 4.0)
    works_on_80 = ('101248268', 29, 10.0)
    works_on_81 = ('245239264', 11, 25.0)
    works_on_82 = ('242916639', 4, 5.0)
    works_on_83 = ('906218888', 29, 15.0)
    works_on_84 = ('001614905', 13, 18.0)
    works_on_85 = ('245239264', 10, 25.0)
    works_on_86 = ('349273344', 29, 15.0)
    works_on_87 = ('242916639', 11, 20.0)
    works_on_88 = ('214370999', 10, 35.0)
    works_on_89 = ('111422203', 4, 45.0)
    works_on_90 = ('398172999', 70, 10.0)
    works_on_91 = ('241625699', 61, 4.0)
    works_on_92 = ('122344668', 3, 10.0)
    works_on_93 = ('122344668', 20, 10.0)
    works_on_94 = ('122344668', 30, 25.0)






    insert_works_on(conn, works_on_1)
    insert_works_on(conn, works_on_2)
    insert_works_on(conn, works_on_3)
    insert_works_on(conn, works_on_4)
    insert_works_on(conn, works_on_5)
    insert_works_on(conn, works_on_6)
    insert_works_on(conn, works_on_7)
    insert_works_on(conn, works_on_8)
    insert_works_on(conn, works_on_9)
    insert_works_on(conn, works_on_10)
    insert_works_on(conn, works_on_11)
    insert_works_on(conn, works_on_12)
    insert_works_on(conn, works_on_13)
    insert_works_on(conn, works_on_14)
    insert_works_on(conn, works_on_15)
    insert_works_on(conn, works_on_16)
    insert_works_on(conn, works_on_17)
    insert_works_on(conn, works_on_18)
    insert_works_on(conn, works_on_19)
    insert_works_on(conn, works_on_20)
    insert_works_on(conn, works_on_21)
    insert_works_on(conn, works_on_22)
    insert_works_on(conn, works_on_23)
    insert_works_on(conn, works_on_24)
    insert_works_on(conn, works_on_25)
    insert_works_on(conn, works_on_26)
    insert_works_on(conn, works_on_27)
    insert_works_on(conn, works_on_28)
    insert_works_on(conn, works_on_29)
    insert_works_on(conn, works_on_30)
    insert_works_on(conn, works_on_31)
    insert_works_on(conn, works_on_32)
    insert_works_on(conn, works_on_33)
    insert_works_on(conn, works_on_34)
    insert_works_on(conn, works_on_35)
    insert_works_on(conn, works_on_36)
    insert_works_on(conn, works_on_37)
    insert_works_on(conn, works_on_38)
    insert_works_on(conn, works_on_39)
    insert_works_on(conn, works_on_40)
    insert_works_on(conn, works_on_41)
    insert_works_on(conn, works_on_42)
    insert_works_on(conn, works_on_43)
    insert_works_on(conn, works_on_44)
    insert_works_on(conn, works_on_45)
    insert_works_on(conn, works_on_46)
    insert_works_on(conn, works_on_47)
    insert_works_on(conn, works_on_48)
    insert_works_on(conn, works_on_49)
    insert_works_on(conn, works_on_50)
    insert_works_on(conn, works_on_51)
    insert_works_on(conn, works_on_52)
    insert_works_on(conn, works_on_53)
    insert_works_on(conn, works_on_54)
    insert_works_on(conn, works_on_55)
    insert_works_on(conn, works_on_56)
    insert_works_on(conn, works_on_57)
    insert_works_on(conn, works_on_58)
    insert_works_on(conn, works_on_59)
    insert_works_on(conn, works_on_60)
    insert_works_on(conn, works_on_61)
    insert_works_on(conn, works_on_62)
    insert_works_on(conn, works_on_63)
    insert_works_on(conn, works_on_64)
    insert_works_on(conn, works_on_65)
    insert_works_on(conn, works_on_66)
    insert_works_on(conn, works_on_67)
    insert_works_on(conn, works_on_68)
    insert_works_on(conn, works_on_69)
    insert_works_on(conn, works_on_70)
    insert_works_on(conn, works_on_71)
    insert_works_on(conn, works_on_72)
    insert_works_on(conn, works_on_73)
    insert_works_on(conn, works_on_74)
    insert_works_on(conn, works_on_75)
    insert_works_on(conn, works_on_76)
    insert_works_on(conn, works_on_77)
    insert_works_on(conn, works_on_78)
    insert_works_on(conn, works_on_79)
    insert_works_on(conn, works_on_80)
    insert_works_on(conn, works_on_81)
    insert_works_on(conn, works_on_82)
    insert_works_on(conn, works_on_83)
    insert_works_on(conn, works_on_84)
    insert_works_on(conn, works_on_85)
    insert_works_on(conn, works_on_86)
    insert_works_on(conn, works_on_87)
    insert_works_on(conn, works_on_88)
    insert_works_on(conn, works_on_89)
    insert_works_on(conn, works_on_90)
    insert_works_on(conn, works_on_91)
    insert_works_on(conn, works_on_92)
    insert_works_on(conn, works_on_93)
    insert_works_on(conn, works_on_94)
    insert_works_on(conn, works_on_95)


    conn.close()

if __name__ == '__main__':
    main()
