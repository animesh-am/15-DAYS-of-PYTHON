import csv

with open('ten.csv','r') as file:
    file.readline()
    data = csv.reader(file)
    total_temp = 0
    count = 0
    for row in data:
        total_temp += float(row[1])
        count += 1
    print("Average temperature = ",total_temp/count)
