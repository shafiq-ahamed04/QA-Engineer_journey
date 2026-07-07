def api_validate (status_code):
    if status_code == 200:
        return "API PASSED"
    else:
        return "API FAILED"
    
status = int(input("enter status code:"))
print()
print(api_validate(status))

