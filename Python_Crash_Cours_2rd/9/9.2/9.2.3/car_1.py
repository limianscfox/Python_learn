class Car:
    """汽车描述"""
    def __init__(self, make, model, year):
        """初始化"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100
        
    
    def get_descriptive_name(self):
        """返回汽车信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """设置里程表数值"""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) 
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()