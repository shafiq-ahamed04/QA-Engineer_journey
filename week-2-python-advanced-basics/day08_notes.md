# week - 01 
# day - 08

# Python - Functions

(1)What is function?
    =Its an resuable block of code, that performs a specific task.
    -instead of writing same code again and again, we write it once and call it whenever we need.
    -Think of it like a machine( input -> function -> output)

Syntax:
    def function_name():
    
    def -> keyword, used create a function
    function_name -> name of the function
    () -> paranthese, inside ths they would be parameter
    : -> mandatory at last 

(2)Manual Testing Connection
    Imagine, if you test login page 100 times a day
    steps:
        open -> enter id  -> enter passoword -> click login -> verify result
    -You repeat thi steps for every 100 times.

(3)Automation testing connection:
    Instead of writing the same login code again and again, create one function and use it whenever needed
    example:
        def add(a, b):
    return a + b
result = add (5 , 3)
print(result)
print(result * 2)
print (result / 4)

on fn -> many results 

(4)Defining and calling a Function
    def greet ():
        print ('hello')
    -nothing happens
     def greet ():
        print ('hello')
    greet()---> call it to execute it.

(5) Parameters:
    -This is an input that given to the function.
    example:
        def greet(name):
            print("hello", name)
        greet(shafiq)
        output:
            hello shafiq
        Call again:
            greet(raj)
            the output will be hello raj, same code , with different input(parameter).
        -inside the parameter is called arguement, here the name is parameter and raj is argument
            parameter -> inside the function definition
            arguement -> value passed while calling

(6) Return values
    -some function return value insted of print()
    example:
        def add (a,b):
            return a+b
            result = add (5,3)
        print(result)
        output:
            8

print() VS return()
    </>
        a = 5
        b = 3
            def add(a , b):
                print(a + b)
    -> you cant reuse this again and again

    def add(a , b):
        return a + b
        result(5, 3)
        print(result)

    -> now, the result can be called and used again and again

    print() -> show the output
    return() -> send the value back 

for better understanding , refer practice file(day08_functions.py)

                -----END-----