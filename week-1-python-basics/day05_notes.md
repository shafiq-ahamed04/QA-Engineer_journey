Week-01
Day-05

python--Lists

(1)What is Lists:
    -A list stores multiple values inside theone variable.
    -it stores values in square braces []          eg:[1,2,3,4,5]
    -the value iniside the [] is called elements.
    -List can be created by numbers, strings and mixed
    i.e:
        1. num = [1,2,3,4,5]
        2. data =  ["shafiq", 22, True]
    -Every item has index
    i.e
        [1,2,3,4,5]
         0 1 2 3 4-- index value

    Example:
        Think of a box as a list with any compartments.
            numbers = [12345]
            -insted of creating 
                num1 = 1
                num2 = 2 etc..
            we can simply write
                numbers=[1,2]

(2)Why lists matters :
    -Application deals with collection of data like username, password, products, orders, test cases, error messages, etc...
    -Lists help us to store all of them together.

(3)Manual testing Conection
    -Suppose you need to test these modules-- Login,search,checkout,payment
    -As a Manual Tester you have to list of modules to test 

(4)Automation testing connection
    -Automation , store them like this
        test_case = ["login, search, checkout, payment"]
    -And , you use this for often.

(5)List methods
    1.append():
        -Add items at the end
        eg:
        number.append(6)
        print (number)                      Output:
                                                [1,2,3,4,5,6]
    2.remove()
        -Remove specific value
        eg:
        number.remove(1)
        print(number)                       Output:
                                                [2,3,4,5,6]
    3.pop()
        -remove the last item
        eg:
        number.pop()
        print(numbers)                      Output:
                                                [2,3,4,5]

    4.sort()
        -order the elements in the elements
        eg:
        numbers = [5,4,3,2,1]
        numbers.sort()
        print(numbers)                      Output:
                                                [1,2,3,4,5]

(6)Loop through lists
    -We can use loops instead of list , like this
        print(numbers[0])
        print(numbers[1])
        print(numbers[2])
    we have to enter without one by one on list like this, insted we use loop
        numbers = [1,2,3,4,5]
        for num in numbers  -------------- means: Take one item from number and store it in num
        print(num)                             Output:
                                                  [1
                                                  2
                                                  3
                                                  4
                                                  5]

(7)why loops matters in QA:
    -So, You have a list of 100 usernames,
    without loops: login(user1) login(user2) login(userx)..
    with loops: for users in user
    print(user)
    - Automation engineer uses loops evertime.

            -----END-----    