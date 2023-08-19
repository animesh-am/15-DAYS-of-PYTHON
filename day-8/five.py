import csv

with open(file = 'five.csv', mode = 'r') as file:
    file.readline()
    data = csv.reader(file)
    total_salary = 0
    count = 0
    for row in data:
        total_salary += int(row[2])
        count += 1
    print(total_salary / count)
