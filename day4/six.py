area = lambda b, h: (b * h) / 2

breadth, height = input("Enter breadth and height of triangle: ").split()
print(area(int(breadth), int(height)))
