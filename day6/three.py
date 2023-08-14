numbers = [1, 5, 9, 0, 7, 21]


def square(values):
    square_list = [x ** 2 for x in numbers]
    return square_list


print(square(numbers))
