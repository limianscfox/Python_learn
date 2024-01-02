class Car:
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def red_odometer(self):
        pring(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, capacity):
        self.capacity = 50

class ElectricCar(Car):
    """电动车有别于Car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print(f"This car has a {self.battery_size}-KWH battery")
            
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()