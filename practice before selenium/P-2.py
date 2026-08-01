users = [
    "admin",
    "manager",
    "guest",
    "raj"
]

def login(user):
    for user in users:
        print("Testing login for " + user)
        print("Login sucessful")
        print()
        print("------")
login(users)