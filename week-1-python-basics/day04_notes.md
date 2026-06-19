# Week 01
# Day 04

(1)What is String(str):
    It is an text that stores inside a quotes " "
        Example:
            name ="shafiq"
            city = "kumbakonam"
(2)Why String Matters?:
    -Almost,Every Application deals with text like username,password,email,API Responses, error messages, etc..
    -As a tester, You will work with strings everyday.

Manual Testing Correction:
    -using Double Quotes " " or Single Quotes ' '.
        Example:
            name = "shafiq" (or) name = 'shafiq'

(4)String Methods:
    1.Upper()
        -Converts all letters to Uppercase(captial letter)
            Example:
                text = "hello QA"
                print(text.upper())
            Output:
                HELLO QA
    Real World QA Example:
        The Website shows -- Login Successful--full small letters
        -Different Causes may failure:
            <expect = "login sucessfull"
            actual = "LOGIN SUCCESSFUL">
            print(expected.upper()==actual.upper())
    Output:
        True

    2.Lower()
        -Converts eveything to lower case(small letter)
        <text = HELLO QA
        print(text.lower())>

    Output:
        hello qa
    Real QA Example:
        user enters SHAFIQ@gmail.com
        Application saves: shafiq@gmail.com
    -Automation ignores case difference
        <email=SHAFIQ@gmail.com
        print(email.lower())>
    Output:
        shafiq@gmail.com

    3.strip()
        -Removes extra spaces from begin to end
            <text = " hello qa  "
            print(text.strip())>
    Output:
            hello qa

    4.Replace:
        -It replace the text
        <text = "Hello QA"
        print((text.replace("QA", "Automation"))>
    Output:
            Hello Automation

    Real QA Example:
        Testing environment often changes 
            Old:https://test.company.com
            New:https://staging.company.com
            <url = "https://test.company.com"
            print(url.replace("test,"staging")>
        Output:
            https://staging.company.com

    5.Concatenation:
        joining strings(texts)together.
        <print("hello" + " " + "QA" )>
    Output:
        hello QA
    Real QA Example:
        first = "shafiq"
        last = "ahamed"
        full_name = first + " " + last
        print(full_name)
    Output:
        shafiq ahamed
    6.Slicing:
        Slicing means taking one part of a string.
        indexes:
            Hello  QA
            01234 5 67

            <text="Hello QA"
            print(text[0:5])>
        Output:
            hello
    Real QA Example:
        Suppose orderIDs are ORD12345, But we need 12345        
        <print(order[3:8])
    Output:
        12345
    -Automation Engineer use this method for orderIDs, Date, Transaction IDs, API Responses.