days = int(input("Enter number of days: "))

year = int(days / 365)
days = days - year * 365
week = int(days / 7)
days = days - week * 7
st = ''
if year > 0:
    st += f'{year} years '
if week > 0:
    st += f'{week} weeks '
if days > 0:
    st += f'{days} days'
else:
    print('Not a single day was entered.')
print(st)
