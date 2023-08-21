import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


def main():
    length = float(input("Enter length of square: "))
    square = Square(length)
    print("Square area =", square.area())
    print("Square perimeter =", square.perimeter())

    radius = float(input("Enter radius of circle: "))
    circle = Circle(radius)
    print("Circle area:", circle.area())
    print("Circle perimeter =", circle.perimeter())


if __name__ == "__main__":
    main()
