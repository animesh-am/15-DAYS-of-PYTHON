import csv

with open(file = 'six.csv', mode = 'r') as file:
    specified_product = input("Enter name of product: ")
    file.readline()
    data = csv.reader(file)
    total_sales_revenue = 0
    for row in data:
        if specified_product == row[1]:
            total_sales_revenue += int(row[-1])

    print(f"Total sales revenue for {specified_product} = ", total_sales_revenue)
