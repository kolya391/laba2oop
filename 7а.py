class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


width = 12
height = 70

rectangle = Rectangle(width, height)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"Ширина: {width}")
print(f"Высота: {height}")
print(f"Площадь: {area}")
print(f"Периметр: {perimeter}")
