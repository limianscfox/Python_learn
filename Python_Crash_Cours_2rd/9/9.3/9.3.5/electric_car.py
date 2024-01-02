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

class Battery(car_model):
    """定义电动车电池类"""
    
    def __init__(self, battery_size=75):
        """初始化电瓶属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印电瓶容量"""
        print(f"This car has a {self.battery_size}-KWH battery.")
    
    def get_range(self):
        """判断续航里程"""
        self.car_model = ['] 
        while car_model == 'model s':
            
            
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge!")
        
class ElectricCar(Car):
    """电动车有别于Car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
                
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()