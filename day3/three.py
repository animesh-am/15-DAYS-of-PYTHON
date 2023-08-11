num = int(input("Enter a number: "))

c = 0

for i in range(num):
    if num % (i+1) == 0:
        c += 1

if c <= 2:
    print("The number is prime.")
else:
    print("The number is non-prime.")
