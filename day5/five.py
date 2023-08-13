def remove_vowels(sent):
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = 0
    for _ in range(len(sent)):
        if i < 5:
            if vowels[i] in sent:
                sent = sent.replace(vowels[i], '')
            i += 1
    return sent


sent = input('Enter a sentence:')
new_sent = remove_vowels(sent)
print(new_sent)
