
def check_result(name, marks):
    if marks >= 50:
        results = "pass"
    else:
        results = "failed"
    print("student: ", name)
    print("marks: ", marks)
    print("results: ", results)    
    print()

check_result("shafiq", 72)
check_result("raj", 45)
check_result("ahamed", 66)


