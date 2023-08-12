def mult_table(num):
    for i in range(1, 11):
        print(f'{num} * {i} = {num * i}')


number = int(input("Enter a number: "))
mult_table(number)
