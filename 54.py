class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getSquare(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getRatio(self):
        return self.getSquare() / self.getPerimeter()
