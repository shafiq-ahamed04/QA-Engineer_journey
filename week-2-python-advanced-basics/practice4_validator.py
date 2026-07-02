def validate_login(expected, actual):
    if expected == actual:
        return "PASSED"
    else:
        return "FAILED"


# Tests
print(validate_login(200, 200))
print(validate_login(200, 404))

#user validator using var,fn,if-else,comp opt