def reverse(name):
    reverse_name = ''
    for letter in name:
        reverse_name = letter + reverse_name
    return reverse_name


enter_name = input("Enter the name: ").lower()

if enter_name == reverse(enter_name):
    print('The string is palindrome.')
else:
    print('The string is not palindrome.')
