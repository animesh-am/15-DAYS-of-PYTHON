numbers = [1, 9, 20, 85, 0]

min = max = numbers[0]

for i in numbers:
    if i > max:
        max = i

    if max < i:
        min = i

print(max)
print(min)
