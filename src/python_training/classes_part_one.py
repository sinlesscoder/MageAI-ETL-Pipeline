# Creating a Class Definition

class Circle:
    # Init Method: When someone runs the class, it initializes some steps
    def __init__(self, radius: float, circle_name: str):
        # Attribute
        self.radius = radius
        self.circle_name = circle_name
    
    # Circumference Method: Calculate the circumference of the circle
    def circumference(self):
        return 2*self.radius*3.14
    
    # Area Method: Calculate the area of the circle
    def area(self):
        return 2 * self.radius**2 * 3.14
    
    # Summary
    def summary(self):
        circ = self.circumference()
        area = self.area()

        print(f"Circle {self.circle_name} has: \n Circumference: {circ} \n Area: {area}")


# Creating a Circle object with a radius of 15.
circle = Circle(15, 'my_circle')

# Get the Circle object
print(circle)

# Get the radius
print(circle.radius)

# Get the circle name
print(circle.circle_name)

# Get the circumference
print(circle.circumference())

# Get the area
print(circle.area())

# get the summary
circle.summary()