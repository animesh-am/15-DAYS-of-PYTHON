string_list = ['hello', 'how', 'do', 'you', 'do', 'I', 'am', 'doing', 'good']


def sorted_list(input_list):
    new_list = []
    copy_of_input_list = input_list.copy()
    for i in input_list:
        short = [len(x) for x in copy_of_input_list]
        min_length = copy_of_input_list[short.index(min(short))]
        new_list.append(min_length)
        copy_of_input_list.remove(min_length)

    return new_list


print(sorted_list(string_list))
