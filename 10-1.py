from numpy import pi


class Shape(object):
    def __init__(self):
        self.s = float()
        self.p = float()


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.r = radius
        self.s = self.r ** 2 * pi
        self.p = self.r * 2 * pi

    def square(self):
        return self.s

    def perimeter(self):
        return self.p


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.l = length
        self.w = width
        self.s = self.l * self.w
        self.p = (self.l + self.w) * 2

    def square(self):
        return self.s

    def perimeter(self):
        return self.p
