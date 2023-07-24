# Create a class
class Cat:
    # Initialize with a cat name
    def __init__(self, cat_name):
        self.cat_name = cat_name
    
    def meow(self):
        print(f"{self.cat_name} says meow!")