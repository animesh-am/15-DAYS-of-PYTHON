lst1 = [1, 9, 0, 7, 20]
lst2 = [7, 0, 90, 11, 75, 31]


def common(l1, l2):
    return list(set(l1) | set(l2))


print(common(lst1, lst2))
