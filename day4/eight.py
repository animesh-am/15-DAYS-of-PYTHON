list1 = [1, 5, 11, 120, 411, 0]
list2 = [92, 2, 12, 7, 5, 0, 111, 90, 11, 420, 1]


def common(l1, l2):
    common_items = []
    for item in l1:
        if item in l2:
            common_items.append(item)
    return common_items


print(common(list1, list2))
