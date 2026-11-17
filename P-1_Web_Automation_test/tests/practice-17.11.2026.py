class TestCase:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def display(self):
        print("Testcase ID:", self.id)
        print("Testcase Name:", self.name)
        print("Testcase Status:", self.status)

test1 = TestCase(101, "Login Test", "PASS")
test2 = TestCase(102, "Signup Test", "FAIL")

test1.display()

print("----------")

test2.display()
