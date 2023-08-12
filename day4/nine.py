def leap_check(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return 'Leap Year'
    else:
        return 'Not a Leap Year'


y = int(input("Enter a year: "))
print(y, 'is', leap_check(y))
