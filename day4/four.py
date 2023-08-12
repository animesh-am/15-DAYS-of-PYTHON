def square(numbers):
    square_list = []
    for num in numbers:
        square_list.append(num ** 2)
    return square_list


values = [1, 9, 5, 11, 0, 70]
print(square(values))
