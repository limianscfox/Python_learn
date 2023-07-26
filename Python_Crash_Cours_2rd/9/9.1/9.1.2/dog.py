class Dog:
    """Dog 类定义"""
    def __init__(self, name, age):
        """初始化属性name，age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """蹲下"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.") 
print(f"Your dog is {your_dog.age} years old.") 
your_dog.sit()