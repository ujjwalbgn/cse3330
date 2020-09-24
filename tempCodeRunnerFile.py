
    # sql_create_department_table = """ CREATE TABLE IF NOT EXISTS department (
    #                                 id integer PRIMARY KEY,
    #                                 Name text Null, 
    #                                 Location text Null,
    #                                 ManagerNumber number Null,
    #                                 StartDate number Null
    #                             )"""

    # sql_create_deptLocation_table = """ CREATE TABLE IF NOT EXISTS deptLocation (
    #                                 id integer PRIMARY KEY,
    #                                 Location text Null
    #                                 )"""

    # sql_create_project_table = """ CREATE TABLE IF NOT EXISTS project (
    #                                 id integer PRIMARY KEY,
    #                                 Name text Null,
    #                                 ProjectNumber text Null,
    #                                 Location text Null,
    #                                 DepartmentNumber text Null                                   
    #                             )"""

    # sql_create_works_on_table = """ CREATE TABLE IF NOT EXISTS works_on (
    #                           EmployeeNumber text Null, 
    #                           ProjectNumber text Null,
    #                           hours text Null,                                                                  
    #                         )"""