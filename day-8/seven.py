def sum_all():
    summ = 0
    with open(file = 'seven.txt', mode = 'r') as file:
        data = file.readlines()
        for row in data:
            summ += int(row)
    return summ


print("SUM = ", sum_all())
