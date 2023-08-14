list1 = [1, 5, 9]
list2 = [20, 11, 7]
list3 = [x for x in list1]
for i in list2:
    list3.append(i)

print(list3)
