class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
rectangle = Rectangle(70, 30)
perimeter = rectangle.calculate_perimeter()
print(perimeter)
