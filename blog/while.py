class Restaurant():
    def __int__(self,name,cuisine_type):
        self.restaurant_name=name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"the {self.name} serves {self.cuisine_type}")
    def open_restaurant(self):
        print(f"the {self.name} is open")
restaurant = Restaurant('dominos','italian')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
