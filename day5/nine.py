enter_string = input("Enter a string: ")


def remove_duplicate(word):
    new = ""
    for i in word:
        if i not in new:
            new = new + i
    return new


print("New string = ", remove_duplicate(enter_string))
