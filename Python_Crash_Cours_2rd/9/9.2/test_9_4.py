class Restaurant:
    
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"\nThe restaurant is {self.restaurant_name},is {self.cuisine_type}")
        
    
    def open_restanurant(self):
        print(f"\nThe {self.restaurant_name} is open")
        
    def set_number_served(self,number_served):
        self.number_served = number_served
    
    def increment_number_served(self,number_served):
        self.number_served += number_served
        
        

restaurant = Restaurant('kfc','kuaican')

print(restaurant.number_served)

restaurant.number_served = 2

print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)