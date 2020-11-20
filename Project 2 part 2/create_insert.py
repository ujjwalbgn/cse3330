#This program create a database and insert data into database

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database"""

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection sucessfull. SQLite3 version "+sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_sql_table):
    try:
        create = conn.cursor()
        create.execute(create_sql_table)
    except Error as e:
        print(e)

def insert_customer (conn, customer):
    sql = ''' INSERT INTO customer ( CustID, Name, Phone)
              VALUES (?,?,?) '''

    try:
        cur = conn.cursor()
        cur.execute(sql,customer)
        conn.commit()
    except Error as e:
        print(e)

def insert_vehicle(conn, vehicle):
    sql = ''' INSERT INTO vehicle (VehicleID, Description, Year, Type, Category)
              VALUES (?,?,?,?,?)'''

    try:
        cur = conn.cursor()
        cur.execute(sql, vehicle)
        conn.commit()
    except Error as e:
        print(e)

def insert_rental(conn, rental):
    sql = ''' INSERT INTO rental (CustID, VehicleID, StartDate, OrderDate, RentalType, Qty, ReturnDate, TotalAmount, PaymentDate)
              VALUES (?,?,?,?,?,?,?,?,?) '''

    try:
        cur = conn.cursor()
        cur.execute(sql, rental)
        conn.commit()
    except Error as e:
        print(e)

def insert_rate(conn, rate):
    sql = ''' INSERT INTO rate (Type, Category, Weekly, Daily)
              VALUES (?,?,?,?)'''

    try:
        cur = conn.cursor()
        cur.execute(sql, rate)
        conn.commit()
    except Error as e:
        print(e)



def main():
    #database Connection
    conn = create_connection(r"CarRental.db")

    sql_create_customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                                    CustID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Name char(15) NOT NULL,
                                    Phone char(14) NOT NULL
                                ) """

    sql_create_vehicle_table = """ CREATE TABLE IF NOT EXISTS vehicle (
                                    VehicleID char(17) PRIMARY KEY,
                                    Description char(15) NOT NULL,
                                    Year int,
                                    Type int NOT NULL,
                                    Category int
                                ) """
    sql_create_rental_table = """ CREATE TABLE IF NOT EXISTS rental (
                                    CustID int NOT NULL,
                                    VehicleID char(17) NOT NULL ,
                                    StartDate char(10) NOT NULL,
                                    OrderDate char(10) NOT NULL,
                                    RentalType int,
                                    Qty int,
                                    ReturnDate char(10) NOT NULL,
                                    TotalAmount float NOT NULL,
                                    PaymentDate char(10),
                                    FOREIGN KEY(CustID) REFERENCES customer(CustID),
                                    FOREIGN KEY(VehicleID) REFERENCES vehicle(VehicleID)
                                ) """
    sql_create_rate_table = """ CREATE TABLE IF NOT EXISTS rate (
                                    Type int NOT NULL,
                                    Category int NOT NULL,
                                    Weekly int NOT NULL,
                                    Daily int NOT NULL,
                                    PRIMARY KEY (Type, Category)
                                )"""



    #create tables
    if conn is not None:

        create_table(conn, sql_create_customer_table)
        create_table(conn, sql_create_vehicle_table)
        create_table(conn, sql_create_rate_table)
        create_table(conn, sql_create_rental_table)


    else:
        print("Error! cannot create the database connection.")


    customer_1 = (201,'A. Parks','(214) 555-0127')
    customer_2 = (202,'S. Patel','(849) 811-6298')
    customer_3 = (203,'A. Hernandez','(355) 572-5385')
    customer_4 = (204,'G. Carver','(753) 763-8656')
    customer_5 = (205,'Sh. Byers','(912) 925-5332')
    customer_6 = (206,'L. Lutz','(931) 966-1775')
    customer_7 = (207,'L. Bernal','(884) 727-0591')
    customer_8 = (208,'I. Whyte','(811) 979-7345')
    customer_9 = (209,'L. Lott','(954) 706-2219')
    customer_10 = (210,'G. Clarkson','(309) 625-1838')
    customer_11 = (211,'Sh. Dunlap','(604) 581-6642')
    customer_12 = (212,'H. Gallegos','(961) 265-8638')
    customer_13 = (213,'L. Perkins','(317) 996-3104')
    customer_14 = (214,'M. Beach','(481) 422-0282')
    customer_15 = (215,'C. Pearce','(599) 881-5189')
    customer_16 = (216,'A. Hess','(516) 570-6411')
    customer_17 = (217,'M. Lee','(369) 898-6162')
    customer_18 = (218,'R. Booker','(730) 784-6303')
    customer_19 = (219,'A. Crowther','(325) 783-4081')
    customer_20 = (220,'H. Mahoney','(212) 262-8829')
    customer_21 = (221,'J. Brown','(644) 756-0110')
    customer_22 = (222,'H. Stokes','(931) 969-7317')
    customer_23 = (223,'J. Reeves','(940) 981-5113')
    customer_24 = (224,'A. Mcghee','(838) 610-5802')
    customer_25 = (225,'L. Mullen','(798) 331-7777')
    customer_26 = (226,'R. Armstrong','(325) 783-4081')
    customer_27 = (227,'J. Greenaway','(212) 262-8829')
    customer_28 = (228,'K. Kaiser Acosta','(228) 576-1557')
    customer_29 = (229,'D. Kirkpatrick','(773) 696-8009')
    customer_30 = (230,'A. Odonnell','(439) 536-8929')
    customer_31 = (231,'K. Kay','(368) 336-5403')

    insert_customer(conn, customer_1)
    insert_customer(conn, customer_2)
    insert_customer(conn, customer_3)
    insert_customer(conn, customer_4)
    insert_customer(conn, customer_5)
    insert_customer(conn, customer_6)
    insert_customer(conn, customer_7)
    insert_customer(conn, customer_8)
    insert_customer(conn, customer_9)
    insert_customer(conn, customer_10)
    insert_customer(conn, customer_11)
    insert_customer(conn, customer_12)
    insert_customer(conn, customer_13)
    insert_customer(conn, customer_14)
    insert_customer(conn, customer_15)
    insert_customer(conn, customer_16)
    insert_customer(conn, customer_17)
    insert_customer(conn, customer_18)
    insert_customer(conn, customer_19)
    insert_customer(conn, customer_20)
    insert_customer(conn, customer_21)
    insert_customer(conn, customer_22)
    insert_customer(conn, customer_23)
    insert_customer(conn, customer_24)
    insert_customer(conn, customer_25)
    insert_customer(conn, customer_26)
    insert_customer(conn, customer_27)
    insert_customer(conn, customer_28)
    insert_customer(conn, customer_29)
    insert_customer(conn, customer_30)
    insert_customer(conn, customer_31)


    vehicle_1 = ('19VDE1F3XEE414842','Acura ILX',2014,1,1)
    vehicle_2 = ('1FDEE3FL6EDA29122',"Ford E 350",2014,6,0)
    vehicle_3 = ('1FDRF3B61FEA87469',"Ford Super Duty Pickup",2015,5,0)
    vehicle_4 = ('1FTNF1CF2EKE54305',"Ford F Series Pickup",2014,5,0)
    vehicle_5 = ('1G1JD5SB3E4240835',"Chevrolet Optra",2014,1,0)
    vehicle_6 = ('1GB3KZCG1EF117132',"Chevrolet Silverado",2014,5,0)
    vehicle_7 = ('1HGCR2E3XEA305302',"Honda Accord",2014,2,0)
    vehicle_8 = ('1N4AB7AP2EN855026',"Nissan Sentra",2014,1,0)
    vehicle_9 = ('1N6BA0EJ9EN516565',"Nissan Titan",2014,5,0)
    vehicle_10 = ('1N6BF0KM0EN101134',"Nissan NV",2014,6,0)
    vehicle_11 = ('1VWCH7A3XEC037969',"Volkswagen Passat",2014,2,1)
    vehicle_12 = ('2HGFB2F94FH501940',"Honda Civic",2015,1,0)
    vehicle_13 = ('2T3DFREV0FW317743',"Toyota RAV4",2015,4,0)
    vehicle_14 = ('3MZBM1L74EM109736',"Mazda 3",2014,1,0)
    vehicle_15 = ('3N1CE2CP0FL409472',"Nissan Versa Note",2015,1,0)
    vehicle_16 = ('3N1CN7APXEK444458',"Nissan Versa",2014,1,0)
    vehicle_17 = ('3VW2A7AU1FM012211',"Volkswagen Golf",2015,1,0)
    vehicle_18 = ('4S4BRCFC1E3203823',"Subaru Outback",2014,4,0)
    vehicle_19 = ('4S4BSBF39F3261064',"Subaru Outback",2015,4,0)
    #vehicle_20 = ('4S4BSELC0F3325370',"Subaru Outback",2015,4,0)
    vehicle_21 = ('4S4BSELC0F3325370',"Subaru Outback",2015,4,0)
    vehicle_22 = ('5J6RM4H90FL028629',"Honda CR-V",2015,4,0)
    vehicle_23 = ('5N1AL0MM8EL549388',"Infiniti JX35",2014,4,1)
    vehicle_24 = ('5NPDH4AE2FH565275',"Hyundai Elantra",2015,1,0)
    vehicle_25 = ('5TDBKRFH4ES26D590',"Toyota Highlander",2014,4,0)
    vehicle_26 = ('5XYKT4A75FG610224',"Kia Sorento",2015,4,0)
    vehicle_27 = ('5XYKU4A7XFG622415',"Kia Sorento",2015,4,0)
    vehicle_28 = ('5XYKUDA77EG449709',"Kia Sorento",2014,4,0)
    vehicle_29 = ('JF1GPAA61F8314971',"Subaru Impreza",2015,1,0)
    vehicle_30 = ('JH4KC1F50EC800004',"Acura RLX",2014,3,1)
    vehicle_31 = ('JH4KC1F56EC000095',"Acura RLX",2014,3,1)
    vehicle_32 = ('JM1BM1V35E1210570',"Mazda 3",2014,1,0)
    vehicle_33 = ('JM3KE4DY4F0441471',"Mazda CX5",2015,4,0)
    vehicle_34 = ('JM3TB3DV0E0015742',"Mazda CX9",2014,4,0)
    vehicle_35 = ('JN8AS5MV0FW760408',"Nissan Rogue Select",2015,4,0)
    vehicle_36 = ('JTEZUEJR7E5081641',"Toyota 4Runner",2014,4,0)
    vehicle_37 = ('JTHBW1GG1F120DU53',"Lexus ES 300h",2015,2,1)
    vehicle_38 = ('JTHCE1BL3F151DE04',"Lexus GS 350",2015,2,1)
    vehicle_39 = ('JTHDL5EF9F5007221',"Lexus LS 460",2015,3,1)
    vehicle_40 = ('JTHFF2C26F135BX45',"Lexus IS 250C",2015,1,1)
    vehicle_41 = ('JTJHY7AX2F120EA11',"Lexus LX 570",2015,4,1)
    vehicle_42 = ('JTJJM7FX2E152CD75',"Lexus GX460",2014,4,1)
    vehicle_43 = ('JTMBFREV1FJ019885',"Toyota RAV4",2015,4,0)
    vehicle_44 = ('KM8SN4HF0FU107203',"Hyundai Santa Fe",2015,4,0)
    vehicle_45 = ('KMHJT3AF1FU028211',"Hyundai Tucson",2015,4,0)
    vehicle_46 = ('KMHTC6AD8EU998631',"Hyundai Veloster",2014,1,0)
    vehicle_47 = ('KNAFZ4A86E5195865',"KIA Sportage",2014,4,0)
    vehicle_48 = ('KNAFZ4A86E5195895',"KIA Forte",2014,1,0)
    vehicle_49 = ('KNAGN4AD2F5084324',"Kia Optima Hybrid",2015,2,0)
    vehicle_50 = ('KNALN4D75E5A57351',"Kia Cadenza",2014,3,0)
    vehicle_51 = ('KNALU4D42F6025717',"Kia K900",2015,3,0)
    vehicle_52 = ('KNDPCCA65F7791085',"KIA Sportage",2015,4,0)
    vehicle_53 = ('WA1LGAFE8ED001506',"Audi Q7",2014,4,1)
    vehicle_54 = ('WAU32AFD8FN005740',"Audi A8",2015,3,1)
    vehicle_55 = ('WAUTFAFH0E0010613',"Audi A5",2014,1,1)
    vehicle_56 = ('WBA3A9G51ENN73366',"BMW 3 Series",2014,1,1)
    vehicle_57 = ('WBA3B9C59EP458859',"BMW 3 Series",2014,1,1)
    vehicle_58 = ('WBAVL1C57EVR93286',"BMW X1",2014,4,1)
    vehicle_59 = ('WDCGG0EB0EG188709',"Mercedes_Benz GLK",2014,1,1)
    vehicle_60 = ('YV440MDD6F2617077',"Volvo XC60",2015,4,1)
    vehicle_61 = ('YV4940NB5F1191453',"Volvo XC70",2015,4,1)

    insert_vehicle(conn, vehicle_1)
    insert_vehicle(conn, vehicle_2)
    insert_vehicle(conn, vehicle_3)
    insert_vehicle(conn, vehicle_4)
    insert_vehicle(conn, vehicle_5)
    insert_vehicle(conn, vehicle_6)
    insert_vehicle(conn, vehicle_7)
    insert_vehicle(conn, vehicle_8)
    insert_vehicle(conn, vehicle_9)
    insert_vehicle(conn, vehicle_10)
    insert_vehicle(conn, vehicle_11)
    insert_vehicle(conn, vehicle_12)
    insert_vehicle(conn, vehicle_13)
    insert_vehicle(conn, vehicle_14)
    insert_vehicle(conn, vehicle_15)
    insert_vehicle(conn, vehicle_16)
    insert_vehicle(conn, vehicle_17)
    insert_vehicle(conn, vehicle_18)
    insert_vehicle(conn, vehicle_19)
    #insert_vehicle(conn, vehicle_20)
    insert_vehicle(conn, vehicle_21)
    insert_vehicle(conn, vehicle_22)
    insert_vehicle(conn, vehicle_23)
    insert_vehicle(conn, vehicle_24)
    insert_vehicle(conn, vehicle_25)
    insert_vehicle(conn, vehicle_26)
    insert_vehicle(conn, vehicle_27)
    insert_vehicle(conn, vehicle_28)
    insert_vehicle(conn, vehicle_29)
    insert_vehicle(conn, vehicle_30)
    insert_vehicle(conn, vehicle_31)
    insert_vehicle(conn, vehicle_32)
    insert_vehicle(conn, vehicle_33)
    insert_vehicle(conn, vehicle_34)
    insert_vehicle(conn, vehicle_35)
    insert_vehicle(conn, vehicle_36)
    insert_vehicle(conn, vehicle_37)
    insert_vehicle(conn, vehicle_38)
    insert_vehicle(conn, vehicle_39)
    insert_vehicle(conn, vehicle_40)
    insert_vehicle(conn, vehicle_41)
    insert_vehicle(conn, vehicle_42)
    insert_vehicle(conn, vehicle_43)
    insert_vehicle(conn, vehicle_44)
    insert_vehicle(conn, vehicle_45)
    insert_vehicle(conn, vehicle_46)
    insert_vehicle(conn, vehicle_47)
    insert_vehicle(conn, vehicle_48)
    insert_vehicle(conn, vehicle_49)
    insert_vehicle(conn, vehicle_50)
    insert_vehicle(conn, vehicle_51)
    insert_vehicle(conn, vehicle_52)
    insert_vehicle(conn, vehicle_53)
    insert_vehicle(conn, vehicle_54)
    insert_vehicle(conn, vehicle_55)
    insert_vehicle(conn, vehicle_56)
    insert_vehicle(conn, vehicle_57)
    insert_vehicle(conn, vehicle_58)
    insert_vehicle(conn, vehicle_59)
    insert_vehicle(conn, vehicle_60)
    insert_vehicle(conn, vehicle_61)

    rental_1 = (203,'JM3KE4DY4F0441471','2019-09-09','2019-05-22',1,4,'2019-09-13',460,'2019-09-09')
    rental_2 = (210,'19VDE1F3XEE414842','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,None)
    rental_3 = (210,'JTHFF2C26F135BX45','2019-05-01','2019-04-15',7,1,'2019-05-08',600,'2019-05-08')
    rental_4 = (210,'JTHFF2C26F135BX45','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,None)
    rental_5 = (210,'WAUTFAFH0E0010613','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,None)
    rental_6 = (210,'WBA3A9G51ENN73366','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,None)
    rental_7 = (210,'WBA3B9C59EP458859','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,None)
    rental_8 = (210,'WDCGG0EB0EG188709','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,None)
    rental_9 = (212,'19VDE1F3XEE414842','2019-06-10','2019-04-15',7,3,'2019-07-01',1800,'2019-06-10')
    rental_10 = (216,'1N6BF0KM0EN101134','2019-08-02','2019-03-15',7,4,'2019-08-30',2740,'2019-08-02')
    rental_11 = (216,'1N6BF0KM0EN101134','2019-08-30','2019-03-15',1,2,'2019-09-01',230,'2019-08-02')
    rental_12 = (221,'19VDE1F3XEE414842','2019-07-01','2019-06-12',7,1,'2019-07-08',600,'2019-07-01')
    rental_13 = (221,'19VDE1F3XEE414842','2019-07-09','2019-06-12',1,2,'2019-07-11',200,'2019-07-01')
    rental_14 = (221,'19VDE1F3XEE414842','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,None)
    rental_15 = (221,'JTHFF2C26F135BX45','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,None)
    rental_16 = (221,'WAUTFAFH0E0010613','2019-07-01','2019-06-12',7,1,'2019-07-08',600,'2019-07-01')
    rental_17 = (221,'WAUTFAFH0E0010613','2019-07-09','2019-06-12',1,2,'2019-07-11',200,'2019-07-01')
    rental_18 = (221,'WAUTFAFH0E0010613','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,None)
    rental_19 = (221,'WBA3A9G51ENN73366','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,None)
    rental_20 = (221,'WBA3B9C59EP458859','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,None)
    rental_21 = (221,'WDCGG0EB0EG188709','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,None)
    rental_22 = (229,'19VDE1F3XEE414842','2019-05-06','2019-04-12',1,4,'2019-06-10',400,'2019-05-06')
    rental_23 = (229,'WAUTFAFH0E0010613','2019-05-06','2019-04-12',1,4,'2019-06-10',400,'2019-05-06')

    insert_rental(conn, rental_1)
    insert_rental(conn, rental_2)
    insert_rental(conn, rental_3)
    insert_rental(conn, rental_4)
    insert_rental(conn, rental_5)
    insert_rental(conn, rental_6)
    insert_rental(conn, rental_7)
    insert_rental(conn, rental_8)
    insert_rental(conn, rental_9)
    insert_rental(conn, rental_10)
    insert_rental(conn, rental_11)
    insert_rental(conn, rental_12)
    insert_rental(conn, rental_13)
    insert_rental(conn, rental_14)
    insert_rental(conn, rental_15)
    insert_rental(conn, rental_16)
    insert_rental(conn, rental_17)
    insert_rental(conn, rental_18)
    insert_rental(conn, rental_19)
    insert_rental(conn, rental_20)
    insert_rental(conn, rental_21)
    insert_rental(conn, rental_22)
    insert_rental(conn, rental_23)

    rate_1 = (1,0,480,80)
    rate_2 = (1,1,600,100)
    rate_3 = (2,0,530,90)
    rate_4 = (2,1,660,110)
    rate_5 = (3,0,600,100)
    rate_6 = (3,1,710,120)
    rate_7 = (4,0,685,115)
    rate_8 = (4,1,800,135)
    rate_9 = (5,0,780,130)
    rate_10 = (5,1,900,150)
    rate_11 = (6,0,685,115)
    rate_12 = (6,1,800,135)

    insert_rate(conn,rate_1)
    insert_rate(conn,rate_2)
    insert_rate(conn,rate_3)
    insert_rate(conn,rate_4)
    insert_rate(conn,rate_5)
    insert_rate(conn,rate_6)
    insert_rate(conn,rate_7)
    insert_rate(conn,rate_8)
    insert_rate(conn,rate_9)
    insert_rate(conn,rate_10)
    insert_rate(conn,rate_11)
    insert_rate(conn,rate_12)



    conn.close()

if __name__ == '__main__':
    main()
