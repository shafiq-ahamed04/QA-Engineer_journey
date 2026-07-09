# week - 03
# day - 14

# python - OOP

(1)What is oop?
    -Imagine you are the tester, testing a website,it has loginpage,searchpage,cartpage
    -Each page has its own work.Insted of putting everything in one file, we create separate blueprint 
    -the blueprint is called class
(2)real life example:
    -Think about a car, Every car has color, brand, speed . Every car can Start , stop , brake
    -The data and actions are belong together. That exactly what loop does.

(3)Four words:
    Class -> A blueprint | ex: Car
    object -> A real thing from the blueprint | ex: brands of the car(audi,bmw)
    attribute -> A nformation about the object | ex: color , brand ,speed
    method -> An action of the object | ex: start the car (), stop the car()

    python example:
        class Student: -- class
            def student(self): -- defining class
                pass
        student1 - student("shafiq") -- creating and naming the object

(4)__init__(Constructor):
    -Whenever an new object is created ,pyhton runs it automatically.
    example:
        class Student;
            def __init__(self, name):
                self.name = name
        student1 = Student("shafiq")
    ->it assumes the name is shafiq automatically, without giving print or call statement. we have to move another line.

(5)What is self?
    -It refers to the every object and help to useits own data.
    ex:
        self.name -> this objects name
    -If many objects there, without self, it is confused to refer or mention for which object the value passed for.
    
(6)Manual Testing Connection:
    -Imagine you're testing:
Amazon.
Manual Tester thinks:
    -Login Page
    -Search Page
    -Cart Page
    -Payment Page
-> Different pages.Different work.

(7)Automation Testing Connection:
    - we dont write these pages in one file
    -Insted we create class like
        -class Lginpage
        -class Larchpage
        -class Cartpage
        -class Paymentpage
    -each page became one class and every class has its own work

    -for example code and better understanding , Refer the practice file (day-14_oops_basics)

                                -----END-----