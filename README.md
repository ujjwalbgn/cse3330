## CSE 3330 Database 
This is CSE3330 UTA Database project 

### Getting Started
Before you start make sure you have the Python 3.8 or higher installed in you operating system.<br/>

### Initial Setup 
* Clone the CSE3330 repo:
    * To clone the repo run ```git clone https://github.com/ujjwalbgn/cse3330/ ```
* Navigate into the repository  ```cd cse3330```

### Create Database, Tables amd Insert Data
* To create database (if not present), Create Table and Insert data into table run  ```createInsert.py``` which is located inside <b> databaseScripts</b> folder.<br/>
<i>Rerunning ```createInsert.py``` will generate "UNIQUE constraint failed" error as the script will try to reinsert exisiting data into the database.</i>

### 
Running Database Query
* To run the query run ```queries.py``` which is located inside <b> databaseScripts</b> folder.<br/>
This will print out the results into the command prompt.

* The arguments for the query functions can be changed depending on the needs: <br/>
Example:
    > #Enter a department name, and retrieve all the names and salaries of all employees who work in that department.

   > ```getNameSalaries(conn, "Research")```</br>

    To obtain info about another dept. we can replace ```"Research"``` with name of another dept. lets say ```"Sales"```.   
    >     ```getNameSalaries(conn, "Sales")```</br>