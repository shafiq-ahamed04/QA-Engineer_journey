#practice1 -> student list using oop concept:

class Student:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def display(self):
        print(self.name)
        print(self.age)
        print(self.height)
student1 = Student("shafiq", 21, 5.9)
student1.display()
student2 = Student("raj", 20, 5.3)
student2.display()
student3 = Student("ahmed", 21, 6.1)
student3.display()







#QA mini project

class Testcase:
    def __init__(self, testid, testname, status):
        self.testid = testid
        self.testname = testname
        self.status = status
    def display(self):
        print(self.testid)
        print(self.testname)
        print(self.status)
testcase1 = Testcase(101, "Login", "PASSED")
testcase1.display()
testcase2 = Testcase(102, "Search", "FAILED")
testcase2.display()
testcase3 = Testcase(103, "Checkout", "PASSED")
testcase3.display()
