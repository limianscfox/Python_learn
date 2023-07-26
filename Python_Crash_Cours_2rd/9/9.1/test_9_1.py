class Restaurant:
    
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"\nThe restaurant is {self.restaurant_name},is {self.cuisine_type}")
        
    
    def open_restanurant(self):
        print(f"\nThe {self.restaurant_name} is open")
        

restaurant = Restaurant('kfc','kuaican')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restanurant()
