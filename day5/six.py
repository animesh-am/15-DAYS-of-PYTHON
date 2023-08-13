def longest_find(sent):
    longest = ''
    sent_list = sent.split(' ')
    for word in sent_list:
        if len(word) > len(longest):
            longest = word
    return longest


words = input("Enter a sentence: ")
print("Longest word = ", longest_find(words))
