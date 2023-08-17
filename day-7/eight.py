items = [
    {"id": 1, "quantity": 10, "price": 50},
    {"id": 2, "quantity": 5, "price": 100},
    {"id": 3, "quantity": 8, "price": 75},
    {"id": 4, "quantity": 12, "price": 30},
    {"id": 5, "quantity": 3, "price": 150}
]

key_entered = input("Enter the key: ")

def sort(values, key):
    print(sorted(values, key = lambda x: x.get(key)))


sort(items, key_entered)
