class Student:

    def __init__(self, name = "???", group = "???", ID = 0, gpa = 1.0):
        self.name = name
        self.group = group
        self.ID = ID
        self.gpa = gpa

    def __bool__(self):
        return self.gpa >= 2.0

    def __str__(self):
        return f"Student {self.name} have gpa {self.gpa}"
    
    def sayLOL(self):
        print(f"LOL, Я {self.name} моя група {self.group} мой ID {self.ID}")

    def Info(self):
        print("Name: ", self.name)
        print("Group: ", self.group)
        print("ID: ", self.ID)

s1 = Student("Orken", "Nigg", 12, 3.0)

print(bool(s1))
print(str(s1))
if bool(s1):
    print("Nice")
else:
    print("BAD")