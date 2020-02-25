a_long_str = """
this is a string
second line
third line
"""

class Dog():

    """
    A simple class for a dog
    """
    def __init__(self, name, age):
        self.dog_name = name
        self.dog_age = age

    def sit(self):
        print("The dog is sitting")

    def rollover(self):
        print("the dog is rolling over")

    def get_info(self):
        print(self.dog_name)
        print(self.dog_age)

    def update_age(self, new_age):
        if new_age < 0:
            print("age could not be negative")
        elif new_age < self.dog_age:
            print("the new age must larger or equal to the current age")
        else:
            self.dog_age = new_age

my_dog = Dog("shadow", 8)
# my_dog.get_info()
#
# another_dog = Dog("abc", 9)
# another_dog.get_info()

print(my_dog.dog_age)
my_dog.update_age(9)
print(my_dog.dog_age)

