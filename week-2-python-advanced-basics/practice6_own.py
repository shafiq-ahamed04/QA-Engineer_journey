#variable
name = "shafiq ahamed "
print(name)

#list
names = ["shafiq","zainab","haziq","ishrah","hussain" , "isfa"]
print(names)

#dictionaries
goals = {
    "became a man",
    1234
}

#validator
def test_case1 (exp, act):
    if exp == act:
        return "success"
    else:
        return "failed"
print(test_case1(200,200))
print(test_case1(200,404))
    
#calculator
def add (a,b):
    return a+b

def sub (a,b):
    return a-b

def mul (a,b):
    return a*b

def div (a,b):
    return a/b

number1 = int(input("enter number 1:"))
number2 = int(input("enter number 2:"))

print()
print(add (number1,number2))
print(sub (number1,number2))
print(mul (number1,number2))
print(div (number1,number2))