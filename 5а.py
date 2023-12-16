class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle = Rectangle(8, 12)
area = rectangle.calculate_area()
print(area)
