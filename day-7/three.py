d = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
}


def remove(dic, key):
    dic.pop(key, None)
    return dic


key = int(input("Enter the key to remove: "))
print(remove(d, key))
