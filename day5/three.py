def count_words(sent):
    count = 0
    sent_list = sent.split(' ')
    for i in sent_list:
        count += 1
    return count


sent = input('Enter a sentence: ')
no_of_words = count_words(sent)
print('Number of words in the sentence = ', no_of_words)
