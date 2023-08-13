def reverse_sentence(sent):
    sent_list = sent.split(' ')
    new = " "
    for word in sent_list:
        new = word + " " + new
    return new


words = input("Enter a sentence: ")
print(reverse_sentence(words))
