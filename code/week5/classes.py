class Dog():

    def __init__(self, name, age, sex="male"):
        self.name = name
        self.age = age
        self.sex = sex

    def change_age(self, new_age):
        if new_age < 0:
            print("Age could not be negative")
        else:
            self.age = new_age

    def sit(self):
        print("the dog is sitting")

    def roll_over(self):
        print("the dog is rolling over")

    def get_info(self):
        print(self.name)
        print(self.age)


my_dog = Dog("shadow", 9)
print(my_dog.age)
#my_dog.change_age(-10)
my_dog.age = -10
print(my_dog.age)


# my_dog.get_info()

#dog_2 = Dog("abc", 10)



