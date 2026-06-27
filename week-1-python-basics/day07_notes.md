# Week - 01
# Day- 07

# Python - Loops

(1)What is Loops?
    - A Loops repeats block of code
    -insted of writing 100 test cases manually(i.e, print("hello"),print(hello)...), we use loop
        eg:
            for i in range(5):
                print("hello")

    -for,while -> keyword
    -in -> takes value from sequence
    range() -> Generate numbers
    : -> mandotary after for, which, if
    -Indendation is must 

(2)Manual testing connection
    -suppose,  you have 100 test cases
        ->without loop:
            open-testcase1-testcase2-....testcasen
        -very repetitive

(3)Automation testing connection
    -It repeats code automatically
    eg:
        users = ("user1","user2"..."usern")
            for user in users:
                login(user)
            ->one loop test all user

(4)for loop:
    -used when you know how many times to repeat.
    eg:
        for i in range(5):
            print(i)                                O/P:
                                                        0
                                                        1
                                                        2
                                                        3
                                                        4

    what is 'i'?
        its a variable, 
        iteration: i=0 i=1 i=2...i=n
    -you can name it anything
     eg:
        for number in range:
            print(number)

(5)While loop
    -used when you dont know how exactly how many times to repeat.
    eg:
        count = 0 
        while count < 5:
            print(count)
            count += 1
                -count +=1 --> count=count+1
                -without this , the loop is called infinite loop

(6)Break
    -stops the loops immediatly
    eg:
        for i in range(5):
            if i==5:
                break
                print(i)                                        O/P:
                                                                    0
                                                                    1
                                                                    2
                                                                    3
                                                                    4
        ->when i becomes 5, it breaks the loop.

(7)Continue
    -skips the current iteration
    eg:
        for i in range(5):
            if i==2:
                continue
                print(i)                                        O/P:
                                                                    0
                                                                    1
                                                                    3
                                                                    4
                -The 2 is skipped
            
(8)Nested loop:
    -skips disabled user
    eg:
        for i in range(2):
            for j in range(3)
                print(i,j)                                     O/P:
                                                                  0 0
                                                                  0 1
                                                                  0 2
                                                                  1 0
                                                                  1 1
                                                                  1 2

for better understanding, the practice code is in the practice file(day07_loops.py)
                ----- END -----                                                                    


