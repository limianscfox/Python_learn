class Car:
    """汽车描述"""
    def __init__(self, make, model, year):
        """初始化"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """返回汽车信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())