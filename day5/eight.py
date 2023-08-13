input_names = ['owl', 'Hero', 'India', 'Ani', 'Orange', 'Umbrella', 'Biology', 'Elephant']


def vowel_count(names):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(5):
        for name in names:
            if name[0].lower() == vowels[i]:
                count += 1
        i += 1

    return count

total = vowel_count(input_names)
print(total)
