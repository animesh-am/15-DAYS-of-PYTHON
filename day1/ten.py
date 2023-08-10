a, b = input("Enter two integers: ").split()
a = int(a)
b = int(b)
print(f"Before sawp: a={a}, b={b}")

a = a + b
b = a - b
a = a - b
print(f"After sawp: a={a}, b={b}")
