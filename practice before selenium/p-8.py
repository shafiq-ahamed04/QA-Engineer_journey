users = [
    {"name": "admin", "password": "123"},
    {"name": "guest", "password": "999"}
]

def validate():
    for u in users:
        print("Checking", u["name"] + "...")  # use u["name"]
        if u["password"] == "123":
            print("PASS")
        else:
            print("FAIL")
        print("----------------")

validate()