#list

test_cases = ["login", "search", "checkout"]
print(test_cases)

test_cases.append("logout")
print(test_cases)
test_cases.remove("search")
print(test_cases)
test_cases.sort()
print(test_cases)

for case in test_cases:
    print(case)
