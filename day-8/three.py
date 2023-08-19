with open("file2.txt", mode = 'r') as file:
    data = file.readlines()
    count_line = len(data)
    count_word = 0
    for i in range(count_line):
        count_word += data[i].count(' ') + 1

    print(data)
    print(count_line, count_word)
