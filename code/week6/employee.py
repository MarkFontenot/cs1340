class Employee():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ssn = 1234567

    def get_info(self):
        print(self.name)
        print(self.age)

    def set_ssn(self, new_ssn):
        self.ssn = new_ssn


name = "xinyi"

li = [1, 2, 3, 4]
print(li.index(4))

