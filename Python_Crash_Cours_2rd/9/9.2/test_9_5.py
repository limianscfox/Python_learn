class User:
    
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.loging_attempts = 0
        
    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.weight)
    
    def greet_user(self):
        print(f"\nHello {self.last_name.title()} {self.first_name.title()}.")
    
    def increment_login_attempts(self):
        self.loging_attempts += 1
        
    def reset_login_attempts(self):
        self.loging_attempts = 0
        
        
        

tim = User('tim','zhou',18,72)
tim.describe_user()
tim.greet_user()

tim.increment_login_attempts()
print(tim.loging_attempts)

tim.increment_login_attempts()
print(tim.loging_attempts)

tim.increment_login_attempts()
print(tim.loging_attempts)

tim.reset_login_attempts()
print(tim.loging_attempts)