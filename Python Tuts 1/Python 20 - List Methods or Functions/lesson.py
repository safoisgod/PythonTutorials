# a PRrogram thatremoves duplocates from a list

list = [1, 43, 43, 12, 7, 1, 23, 19]
new_list = []

for number in list:
    if number not in new_list:
        new_list.append(number)
print(new_list)