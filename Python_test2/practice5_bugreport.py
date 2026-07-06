
try:
    with open("bug_report.txt", "w")as f:
        f.write("Bug ID:101\n")
        f.write("status: open\n")
        f.write("priority:high\n")
    with open("bug_report.txt", "r")as f:
        content=f.read()
    print(content)
    print(10/0)

except FileNotFoundError:
    print("file is missing")
except ZeroDivisionError:
    print("not divisible")