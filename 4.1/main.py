#Класс Triangle
#Создайте класс Triangle. В нём пропишите 3 (метода) функции.
#Первый метод: проверка на существование треугольника по данным сторонам.
#Второй метод : нахождение площади треугольника. Третий метод: нахождение периметра треугольника.
class Triangle:
    def __init__(self, side1, side2, side3):
     self.side1 = side1
     self.side2 = side2
     self.side3 = side3

    def is_triangle(self):
         if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1:
             return True
         else:
             return False

    def area(self):
          if  self.is_triangle():
             s = (self.side1 + self.side2 + self.side3) / 2
             area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
             return area
          else:
             return "Треугольник не существует"

    def perimeter(self):
        if self.is_triangle():
            return self.side1 + self.side2 + self.side3
        else:
            return "Треугольник не существует"

side1 = 3
side2 = 4
side3 = 2

triangle = Triangle(side1, side2, side3)
if triangle.is_triangle():
    print(f"Площадь треугольника: {triangle.area()}")
    print(f"Периметр треугольника: {triangle.perimeter()}")
else:
    print("Треугольник не существует")




