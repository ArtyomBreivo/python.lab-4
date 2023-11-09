#Создать классы Circle (круг), Square (квадрат), Rectangle (прямоугольник)
#для описания плоских геометрических фигур. Реализовать метод нахождения площади фигуры.
#Переопределить метод нахождения площади фигуры.
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    circle = Circle(radius = 5)
    square = Square(side_length = 4)
    rectangle = Rectangle(length=6, width=3)
    print(f"Площадь круга: {circle.area()}")
    print(f"Площадь квадрата: {square.area()}")
    print(f"Площадь прямоугольника: {rectangle.area()}")
