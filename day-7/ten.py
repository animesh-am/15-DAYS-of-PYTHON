strings_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "nectarine"]


def unique(list_entered):
    new_list = []
    for item in list_entered:
        st = ""
        for letter in item:
            if letter not in st:
                st = st + letter
        new_list.append(st)
    return new_list


print(unique(strings_list))
