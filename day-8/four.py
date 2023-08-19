def write_to_file(list_of_sentences):
    with open("new.txt", 'w') as file:
        for sent in list_of_sentences:
            file.write(sent + "\n")


sentences = [
    "The sky is blue.",
    "I love reading books.",
    "Dogs are man's best friend.",
    "Python is a versatile programming language.",
    "The world is a vast place full of mysteries."
]

write_to_file(sentences)
