#exapmle 1
try:
    result = 10/0
except ZeroDivisionError:
    print("the operation fails")
finally:
    print("Done")
    
#example 2
try:
    with open("missing.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("the file is missing")
finally:
    print("check the file name or file is available!")

