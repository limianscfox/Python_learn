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
        
        