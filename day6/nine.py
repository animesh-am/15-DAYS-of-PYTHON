string_list = ['hello', 'how', 'do', 'you', 'do', 'I', 'am', 'doing', 'good']
lst2 = [1, 2, 3, 4, 9]


def is_sorted(lst):
    return lst == sorted(lst)


print(is_sorted(string_list))
print(is_sorted(lst2))
