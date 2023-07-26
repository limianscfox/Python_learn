class User:
    
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        
    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.weight)
    
    def greet_user(self):
        print(f"\nHello {self.last_name.title()} {self.first_name.title()}.")
        

tim = User('tim','zhou',18,72)
tim.describe_user()
tim.greet_user()
