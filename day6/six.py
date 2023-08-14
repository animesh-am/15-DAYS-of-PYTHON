elements = [1, 5, 9, 7, 21, 1, 72, 5, 9, 8, 5]
unique_list = []
for element in elements:
    occurrence = elements.count(element)
    if element not in unique_list:
        unique_list.append(element)
        print(f"{element} occurs {occurrence} times.")
