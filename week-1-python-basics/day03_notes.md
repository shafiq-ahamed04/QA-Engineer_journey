# Week-01
# day-03

Python-Operators

(1)What are operators
    operators are the symbols that fill python to perform an action.
        example:
            + -- Add
            - -- Sub
            * -- multiply
            / -- divide
            == -- equal to 
            > -- greater than
            < -- Less than
    Think operators as variables. Such as,
        10+5=15 -- Takes 10 and Add 5 equals to 15.
    
(2)Arithmetic Operations
    1. Addition(+):
        a=10
        b=5 
    print(a+b)                                   Output:
                                                    15
    2.subtraction(-):
        print(a-b)                               Output:
                                                    5
    3.Multiplication(*):
        print(a*b)                               Output:
                                                    50
    4.Divison(/):
        print(a/b)                               Output:
                                                2.0
                Note:Divison is always float
Example:
    Manual Testing:
    <price = 500
    quantity = 2
    exp_price = 1000>
        -As an Manual Tester, you calculate this by own and  verifies it shows correctly.

    Automation testing:
     <price = 500
    quantity = 2
    exp_price = price * Quantity
    print(exp_total)>
        -As an Automation tester, You follow this framework & constanly do Calcualtion  like this.

(3)Comparison Operators:
    Result is always true or false
        1.equal to(==):
         <a = 10, b = 5>
         print(a==b)                            Output:
                                                 False
        2.not equal to(!=):
            print(a!=b)                         Output:
                                                  True
        3.Greter than(>):
            print(a>b)                          Output:
                                                   True
        4.Less than(<):                         
            print(a>b)                         Output:
                                                    False
Example:
    Manual Testing:
        Login Page
            expected message = Login Successful
            actual message = Login sucessful
                so, Tes Passes
    Automation Testing:
            expected_login = "Succesfull"
            actual_login = "Successfull"
        Print(expected_login == actual_login)                    Output;
                                                                    True

(3)Logical Operations:
    -It Combines COnditons and Make Decisions.
        1.AND
            Both conditions must be True
            <age = 22
            is_student = True
            print(age>18 and is_student)>                       Output:
                                                                   True
     Real world QA example:
        login Succeed if both,
            -Username is correct
            -password is correct
        -Both are true , then AND is satisfied.

        2.OR:
            Atleast One condition must be True.
             print(True or False)                         Output:
                                                            True
    Reak world QA example:
        user can login using email and mobile no.
            Email = True
            mobile = False                                 Output:
                                                             True
        3.NOT:
            Reverse the Result
                <is_logged_in = True
                print(not is_logged_in)>                    Output:
                                                             False
                                                             

                         -----END-----                                                             