alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

st = input("Enter a string: ").lower()

c = 0
for i in range(26):
    if alphabets[i] in st:
        c += 1

if c == 26:
    print('The string is a Pangram.')
else:
    print('The string is not Pangram.')
