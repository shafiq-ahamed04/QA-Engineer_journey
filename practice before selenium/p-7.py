class LoginTest:
    def __init__(self,username,password):
        self.username = username
        self.password = password 

    def run_test(self):
        print ("Running login test...")
        print("username: ", self.username)
        if self.password == "admin123":
            print("Status: passed")
        else:
            print("Status:failed")


login1 = LoginTest("admin", "admin123")
login2 = LoginTest("admin",  "admin345")
login3 = LoginTest("admin", "admin567")

login1.run_test()
print()
login2.run_test()
print()
login3.run_test()
print()

