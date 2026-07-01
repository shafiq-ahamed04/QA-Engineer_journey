# Week 02 
# Day 09

# Python - if-else condition

(1) What is ifelse ?
    -An if else statement allows python to make decision based on a condition.
    -Think of it like this 
        Condition 1 -> true -> execute the code -> 
                        if false -> conditon 2 -> Execute the code.
    Syntax:
        if condition:
            #code
        else:
            #code

(2)manual Testing Connection:
    Suppose, you are testing a login page 
     *correct userid and password -> logged in 
     *wrong userid and password -> invalid login
    - As a manual tester, you observe the result and decide by own.

(3) automation testing connection:
    -It makes the same decision using code.
    </>
        expected = logged in
        actual = logged in
        if expected == actual:
            print("succes")
        else:
            print("failed")
    -This is one of the most comman pattern in Automation frameworks.

(4) if statement:
    example:
        age = 20
        if age > 20:
            print("adult")

    else statement:
        -same code but add else after set if statement. if not execute without else
     example:
        else:
            print("child")

    elif:
        used when there is mulitiple condition.
        example:
            age = 20
        if age >= 18:
            print("adult")
        elif age >=13:
            print ("child)
        else:
            print("teen")
    -python stops checking its condition once it find true condition.

(7)multiple connections:
   -using and 
    username =  true
    password = true
    if username and password:
        print("success")

    -using or
    mobile = true
    email = false
    if mobile or email:
        print("allowed")

    -python runs only one matching block in if-else- elif
         Functions -> Tells the program what to do.
         COnditions -> Tells the program when to do

        
