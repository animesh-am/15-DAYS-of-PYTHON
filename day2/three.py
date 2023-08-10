from four import reverse

st = input("Enter a string: ").lower()

# rev_st = ''
#
# for s in st:
#     rev_st = s + rev_st

if st == reverse(st):
    print("String is Palindrome")
else:
    print("String is not Palindrome")

