week 01
day 02

python- Variables and Datatypes

(1) What is variable?
        It is an named container that stores the information to use it later on programming.
    It is called variable
      example:
            name = "raj"
            -- here the name(before the =)is called variable and raj(after =)is called value.
(2)why variable matters
        The computer program need to remember the information like username, password etc,.
    variable allows programms to store and reuse the value.

(3)Manual Testing connection:
        suppose, we testing a login page,
        username: shafiq@123
        password: test@123
    as a manual tester you enter this value manually, if repetiton or changes happens

(4)Automation Testing
        Instead of typing everything again and again, we store them as a variable, and computer does it automatically.if any changes happen in username and password, we chage the value only not the entire scripts.

(5)Assigning Values
        "="- This means stores the value on the right side and value on the left side.


(6)DataTypes
        Different information has different types.
        type-1: String(str)
            -A string is a text
            -It begin and ends with ""(quotes)
        example:
            name = "shafiq_ahamed"

        type-2: Integer(int)
            -An Integer is a Whole Number
            -it includes only numbers. dont need any quotes
        example:
            age = 22

        type-3: Float
            - An Float is the Decimals Numbers
            -Only decimal numbers are included
        example:
            salary = 250000.0688

        type-4: Boolean(bool)
            -Boolean has only two values
                1.True
                2.False
            Note- The value starts with Caps!
        example:
            is_logged_in = True
            is_payment_succes = False
                -Automation Uses Boolean datatype everytime


Real World QA Example:(Login Testing)
    imagine you are working at Amazon and you have to test login page,then the website have 
                -username field
                -password field
                -login button
    Manual Tester :
        1.open website 2.type username and password 3.click login button 4. check results
            Now you can repeat this many time
    Automation Tester:
        write scripts to automate this test, 
            example scripts:
                enter_username("shafiq@123")
                enter_password("test@123")
                click_login
            Now, it test automatically.

                    ------End------
