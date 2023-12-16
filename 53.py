class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14159 * self.__radius * self.__radius

    def get_circumference(self):
        return 2 * 3.14159 * self.__radius
