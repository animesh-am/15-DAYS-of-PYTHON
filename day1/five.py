def func(s):
    rev = ""
    for _ in s:
        rev = _ + rev

    if rev == s:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")


str_enter = input("Enter a string: ")
func(str_enter)
