list1 = [1, 5, 2, 0, 11, 21, 7]
list2 = [0, 7, 8, 3, 9, 22, 1, 21]

common_elements = []

for i in list1:
    if i in list2:
        common_elements.append(i)

print(common_elements)
