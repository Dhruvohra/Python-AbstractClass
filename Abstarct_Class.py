from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class defining the shape blueprint
    @abstractmethod
    def area(self):  # Abstract method to calculate the area
        pass

class Rectangle(Shape):  # Rectangle class inheriting from Shape
    def __init__(self, width, height):  # Constructor to initialize width and height
        self.width = width
        self.height = height
    
    def area(self):  # Implementation of the area method for rectangles
        return self.width * self.height

class Circle(Shape):  # Circle class inheriting from Shape
    def __init__(self, radius):  # Constructor to initialize radius
        self.radius = radius
    
    def area(self):  # Implementation of the area method for circles
        return 3.14 * self.radius * self.radius

# Usage
rectangle = Rectangle(5, 4)  # Creating a rectangle object
print("Area of rectangle:", rectangle.area())  # Printing the area of the rectangle

circle = Circle(3)  # Creating a circle object
print("Area of circle:", circle.area())  # Printing the area of the circle
