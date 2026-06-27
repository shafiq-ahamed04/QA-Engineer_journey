user = {
    "name" : "shafiq ahamed",
    "age" : 22,
    "phone" : 9944576876
}

print(user["name"])

print(user["age"])

print(user["phone"])

user["city"] = "Chennai"

user["age"] = 23

for key,value in user.items():
    print(key,value)