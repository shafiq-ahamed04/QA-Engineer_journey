# wek 02 
# day 11
# python - Error handling

(1)What is error handling
    -sometimes program encounter errors
    example:
        print(10/0)
    output:
        ZeroDivisionError
    -Normally python stops the entire program.using Error handling make the program to dont stops the entire program or crash , if error happens , handle it and continue.

    syntax:
        try: -> put the code that might cause error 
            #risky code
        except: -> handle the error
            #runs if that error happens
        finally: -> always execute , the error is doesnt matter
            #Runs always

(2)Manual Testing Connection
    -imagine of you are  testing a login page, you click login ,
        ->insted of showing "invalid login"
        -> it crashes the entire application, As a manual tester you report bug.
    
(3)Automation Testing Connection:
    -imagine your scripts tries to open a file.
        </>
            with open ("missing.txt", "r")
                - error - the file doesnt exist
    without error handling:
        ->program crashes
        ->remaining test cases never runs.
    with error handling:
        </>
            try:
                with open("missing.txt", "r")
                except filenotfounderror:
                    print("no file exist")
        -> So Now, the program runs without stopping and crashing. If error happens, it mention the error and doesnt stop or crash.

(4)Catching specific exception
    FileNotFoundError -> missing files
    ZeroDivisionError -> only divisible by zero
    TypeError -> wrong datatype
        -Specific exception makes debugging easier.

    for example and clear understanding, please visit the practice file(day11-error_handling).

                             -----END-----