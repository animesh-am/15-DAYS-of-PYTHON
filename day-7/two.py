d = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    11: 'one',
    12: 'three',
    13: 'three',
}
frequent_item = ''
max_count = 0
d_values = list(d.values())
for item in d_values:
    if d_values.count(item) > max_count:
        max_count = d_values.count(item)
        frequent_item = item

print(frequent_item)
