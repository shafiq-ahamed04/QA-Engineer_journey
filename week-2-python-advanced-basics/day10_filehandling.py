#write a file
with open ("results.txt", "w") as f:
    f.write("hello, im shafiq ahamed\n")
    f.write("Im an QA Engineer\n")
    f.write("Looking for opportunities\n")

#append a text in file
with open ("results.txt", "a") as f:
    f.write("please give me a job")

    
#read a file
with open ("results.txt", "r") as f:
    content = f.read()
    print(content)





