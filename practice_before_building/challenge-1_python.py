def login(username, password):
    if username == "admin" and password == "1234":
        return "login succesfull"
    else:
        return "Invalid credentials"

print(login("admin", "1234"))
print(login("shafiq", "erty"))
print(login("ahmed", "df56"))