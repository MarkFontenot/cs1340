from car import Car, Battery

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(90)
        # self.price = 30000
        self.name = "abcds"

    def get_descriptive_name(self):
        return  "this is a electric car"

    def get_name(self):
        print(self.name.upper())

    def get_battery_info(self):
        return self.battery.describe_battery()


my_tesla = ElectricCar("Tesla", "model s", 2016)
# print(my_tesla.battery)
my_tesla.get_battery_info()

my_tesla.get_name()

# bat = Battery(90)
# bat.describe_battery()