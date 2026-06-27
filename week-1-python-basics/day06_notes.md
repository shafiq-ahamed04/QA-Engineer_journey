# Week 01
# Day 06

# python - Dictionaries

(1)What is Dictionaries
    -A dictionaries stores data in key value pairs.
    -think of it like an ID card.
        name:raj
        age:22
        email:raj@gmail.com
    -in python, 
        user{
            "name" : "raj",
            "age" : 22,
            "email": "raj@gmail.com"
        }
        -> you dont use index like lists, you use keys here.
        -> {}--curly braces creates dictionary
            inside dictionary
                {
                    "name" : "raj"                
                }
            here,
                ->"name"=key
                ->"raj"=value
                -> : = separates key and value
                -> , = separate different values and keys

(2)Difference b/w list and dictionary
    -list uses [] and accessed by indexes
    -dictionary uses {} and accesed by keys

(3)Manual Testing Connection
    -imagine if you write test cases
        ID : 101
        module : login
        status : passed
        tester : shafiq

    -all the details belong to one test case.
        so, a dictionary is perfect, because each piece of information has a label (key)

(4)Automation Testing Connection
    -The automation framework, stores
     -> user details    -> API responses
     -> Test cases      -> Values
    eg:
        test_case{
            "id" = 1
            "name" = "login"
            "status" = "passed"
        }
    -> insted of reminding index positions, you access values using meaningful keys.

(5) Access values
    user{
        "name" : "raj",
        "age" : "22"       
    }
        print(user["name"])                                         O/P:
                                                                        raj

(6) Add new key
    -user["phone"]=9876543210
        -> then it adds number to the above user variable

(7) Modify Existing values:;
    user[age]=23
    -then it changes to 23 from 22

(8) Loops through Dictionary:
    for key, value in user.items()
        print(key, values)
    ->user.items()-- return all keys inside
    ->for-- loop
    ->key-- stores the keys
    ->value--store the values
    ->:-- mandotary

--> for better understanding, refer the practice code file(day06_dictionaries)

            ----- END -----