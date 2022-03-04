import math


class Polygon:  # Abstract class

    def get_area(self):
        raise NotImplementedError()

    def get_sides(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError


class Triangle(Polygon):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(
            semi_perimeter *
            (semi_perimeter - self.side1) *
            (semi_perimeter - self.side2) *
            (semi_perimeter - self.side3)
        )

    def get_sides(self):
        return [self.side1, self.side2, self.side3]

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle(Polygon):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_sides(self):
        return [self.width, self.width, self.height, self.height]

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):

    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length ** 2

    def get_sides(self):
        return [self.length, self.length, self.length, self.length]

    def get_perimeter(self):
        return 4 * self.length
