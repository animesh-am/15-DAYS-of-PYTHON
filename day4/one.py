numbers = [1, 50, -20, 120, -7, -11, 0, 91]


def sum_positive(nums):
    positive_numbers = [x for x in nums if x >= 0]
    add = 0
    for num in positive_numbers:
        add += num
    return add


print('Sum of +ve = ', sum_positive(numbers))
