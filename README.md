# Python-AbstractClass


# Shape Area Calculator

This Python script demonstrates the use of abstract classes and inheritance to calculate the areas of different shapes.

## Abstract Class

The `Shape` class is an abstract class that defines a blueprint for calculating the area of various shapes. It contains an abstract method `area()` that must be implemented by its subclasses.

## Subclasses

1. **Rectangle**: Represents a rectangle shape. It inherits from the `Shape` class and implements the `area()` method to calculate the area of a rectangle based on its width and height.

2. **Circle**: Represents a circle shape. Similar to the `Rectangle` class, it inherits from the `Shape` class and implements the `area()` method to calculate the area of a circle based on its radius.

## Usage

1. Create instances of the `Rectangle` and `Circle` classes with appropriate parameters (width, height, radius).
2. Call the `area()` method on each instance to calculate the area of the corresponding shape.
3. Print the calculated area.

## Example

```python
rectangle = Rectangle(5, 4)
print("Area of rectangle:", rectangle.area())

circle = Circle(3)
print("Area of circle:", circle.area())

```

Output:

Area of rectangle: 20
Area of circle: 28.26


This README.md provides an overview of the code functionality and usage.
