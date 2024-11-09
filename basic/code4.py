import math

# Class 1: Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Class 2: Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Class 3: Square
class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Class 4: Triangle
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)
triangle = Triangle(4, 5)

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
print("Square Area:", square.area())
print("Triangle Area:", triangle.area())
