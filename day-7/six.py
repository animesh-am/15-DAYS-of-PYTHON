string = "banana"

d = {}

for letter in string:
    if letter not in d:
        d[f"{letter}"] = string.count(letter)

print(d)
