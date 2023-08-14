names = ['hello', 'java', 'print', 'hello', 'name', 'in', 'java', 'in', 'Python']
unique_list = []
for word in names:
    if word not in unique_list:
        unique_list.append(word)

print(unique_list)
