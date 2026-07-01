# week 02
# day 10

# python - File handling

(1)What is file handling
    -It means reading data from a file or write data imto a file.
    -Think of it like a textbook
        read -> Open the book ,read
        write ->open the book, write
        close -> close the textbook
    -pyhton also do same with same files.
syntax:
    open ("fil name.txt", "mode")

(2)manual testing connection:
    Imagine, you finish testing . So you create report.
        test 1: passed 
        test 2: passed
    -You type this manually

(3)Automation testing connection:
    -Here, python writes test automatically.
    example:
        with open("results.txt","w") as f
        f.write ("login test 1 : passed /n")
        f.write ("login test 2 : passed /n")
    -Now, the python creates the report for you!
    -this is most comman in automation testing

(4)Opening an file:
    file = open (test.txt" ,"r")
    using with open:
    prefered method:
        with open("text.txt" , "r") as f:
        print(f.read())
    -why(? -> this automatically close the file after the function is complted without remind it to close.

(5) Writing a file:
    with open ("test.txt", "w") as f:
        f.write("hello QA")
    output:
        Now the file contain the print statement and it deletes the old data.
    same for reading:
        with open("test.txt", "r") as f:
            contect = f.read()
            print(content)

(8)Appending an file:
    if we add a data into a file without deleting or changing the old data.
        example:
            with open("results.txt", "a")
                f.write("add this")

        -refer the practice file("day10_filehandling")for reference


                    -----END-----
        