class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def display_info(self):
        print(f"{self.__class__.__name__}:")
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())
        print("-------------------------")


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius


# Example usage
triangle = Triangle(6, 8, 6, 8, 10)
rectangle = Rectangle(5, 7)
circle = Circle(4)

triangle.display_info()
rectangle.display_info()
circle.display_info()
