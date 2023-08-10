vowels = ['a', 'e', 'i', 'o', 'u']

st = input("Enter a string: ")

i = 0
count = 0

for _ in range(len(st)):
    if i < 5:
        if vowels[i] in st:
            count += st.count(vowels[i])
    i += 1

print("The number of vowels are: ", count)
print(st)
