import csv

with open('two.csv', 'r') as file:
    file.readline()
    data = csv.reader(file)
    highest_score = 0
    for row in data:
        if int(row[1]) > highest_score:
            highest_score = int(row[1])
    print("Highest score = ", highest_score)

