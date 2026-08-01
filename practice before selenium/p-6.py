class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    def display(self):
        print("Employee: ", self.name)
        print("department: ", self.department)
        print("salary: ", self.salary)
        print()
emp1= Employee("shafiq","QA",  25000)
emp1.display()
emp2 = Employee("raj", "Developer", 40000)
emp2.display()
emp3 = Employee("ahamed","Support", 20000)
emp3.display()
