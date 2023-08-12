def even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


num = int(input('Enter a number: '))
print('The number is', even_odd(num))
