import math

PI = round(math.pi, 3)

radius = float(input("Enter the radius of circle: "))
area = PI * radius * radius
circumference = 2 * PI * radius
print('Area = ', area)
print('Circumference = ', circumference)
