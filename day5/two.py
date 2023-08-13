def reverse(entry):
    reversed_entry = ''
    for letter in entry:
        reversed_entry = letter + reversed_entry

    return reversed_entry


sent = input('Enter a sentence to reverse: ')
reversed_sent = reverse(sent)
print(reversed_sent)
