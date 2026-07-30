# Week-03
# Day-16

# SQL Basics

(1)What is database:
    -Its an place, Where Application stores its data.
    -Think about instagram -> When you create username and password, it saves somewhere , and it is called Database
    EX:
        -Imagine Your College register 
        -Roll NO, Name, Age , Deparment
    -The Database works in the same way as digitally
    -A database is made up of Tables.
    -Each table stores specific data.
        EX:
            Students Table or Employee Table
        
(2)What is SQL?
    -> Stands for Structured Query Language.
    -> SQL is the language used to talk to DB.
    EX:
        *show all students
        *Find one employee
        *Add a customer
        *update salary

(3)Manual Testing Connection
    -> Imagine you register on website after clicking register, the application says -> 'Register Done'
    -> As a manual tester , you will save the message only you dont know if the data was saved

(4)Automation Testing Connection
    -> A QA Engineer checks the DB
    EX:
        userid - ss123
        pass - s@3456
    -If this exist in DB Passed otherwise Failed

    Table -> Everything together
    Column -> Vertical order(Each column stores one type of info)
    Row -> Horizontal order(one row one information)

(5)SELECT Statement:
    -The Most used SQL Command. It means -> Show me the data
    Query-(select entire column)
        SELECT * FROM TableName;
    select one column:
        SELECT Name FROM TableName;
    select multiple column:
        SELECT Name, Salary FROM Employees;
    
(6)WHERE Clause:
    -Suppose you want employees on QA Department
    syntax:
        SELECT * FROM Employees
        WHERE Department = 'QA';

(6) QA Example:
    -> A User Registered you held to verify the record Exists.
    Query:
        SELECT * FROM Users
        WHERE Email = 'shafiq@gmail.com'
    -if row is returend succes, it exists.
    -if no, it is failed, bug found
     -> This is what QA Engineers do.
    Row -> Goes Across(one record)
    column -> Goes down(one field)
    command -> separate the coloumns
    AND -> separates condition you re filter by.

                -----END-----