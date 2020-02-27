class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ", " + self.make + ", " + self.model
        return long_name

    def update(self, new_year):
        self.year = new_year

    def get_year(self):
        return self.year

# my_car = Car("BMW", "M3")
# # name = my_car.get_descriptive_name()
# # my_car.update(2020)
#
# print(my_car.get_year())

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")

