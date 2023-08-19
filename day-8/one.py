with open('file1.txt', mode = 'r') as file:
    f = open('file2.txt', 'w')
    data = file.read()
    print(data)
    f.write(data)
