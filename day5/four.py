alphabets = "a b c d e f g h i j k l m n o p  q r s t u v w x y z".split(' ')
alpha = ''
sentence = input("Enter a sentence: ").lower()

def count(sentence):
    c = 0
    for i in range(26):
        if alphabets[i] in sentence:
            c += 1
    return c


if count(sentence) == 26:
    print('Pangram')
else:
    print('Not Pangram')
