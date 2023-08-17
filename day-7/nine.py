items = [
    {"id": 1, "quantity": 10, "price": 50},
    {"id": 2, "quantity": 5, "price": 100},
    {"id": 3, "quantity": 8, "price": 75},
    {"id": 4, "quantity": 12, "price": 30},
    {"id": 5, "quantity": 3, "price": 150}
]

total = 0
count = 0
for row in items:
    for value in row.values():
        total += value
        count += 1

print("AVERAGE =", total / count)
