words = "I started learning Python it was worth it".split(' ')
longest = " "
for word in words:
    if len(word) > len(longest):
        longest = word
print(f"Longest word with {len(longest)} letters is {longest}.")
