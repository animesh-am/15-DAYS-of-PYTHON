lst1 = [1, 9, 0, 7, 20]
lst2 = [7, 0, 90, 11, 75, 31]


def common(l1, l2):
    l3 = []
    for item in l1:
        if item in l2:
            l3.append(item)
    return l3


print(common(lst1, lst2))
