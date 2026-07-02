# week 02
# day 12

# python - Modules and Import

(1)what is modules
    -A module simply a python file that contains code such as functions, variables or classes
    -Insted of writing everything in one file, we spilit code into multiple files.
    -Think of it like this,
        ->math note, sciene note
    -each note contains each subjects,so same in python,
        -> login.py , search.py 
    -each file has specific purpose

    syntax:
        import math -> it imports the entire module
        from math import sqrt -> it imports the specific function we need from this module
         -we have use this for our own model. That is user defined module, the above ones are built in module.
    Example:
        from math import sqrt
            - math is an .py file inside that file , the function is sqrt, so that function only importeed 

(2)Manual Testing connection
    -Imagine your project has many documents. 
        ->login.xlsx
        ->search.xlsx
    -you dont put these in single file, you seperate this for better organization.

(3)Automation Testing Connection
    -imagine every test needs login validation.
        without modules:
            def validate_login(exp , actual):
                return exp == act
    - repeated many times.
        with modules:
            from qahelpers import validate_login
        -now we use it anywhere

(4)Built-in Modules:
    math -> mathematics module
    random.randit ->  points out any random integer
(5)Building own modules:
    -> create file named as file1.py
     inside that file,
        </>
            def login_status(yes, no)
            return yes == no 
    ->save it 
    ->create file named as file2.py
    inside that file , import the function from file.1py
        </>
            from file1 import login_status
            print(login_status(200,200))
        output:
            true

    for better understanding , refer the practice file(day12-modulesandimports.py)
                        -----END-----
