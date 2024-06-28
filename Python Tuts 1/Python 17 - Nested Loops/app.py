#nested loops are loops in loops
#generating a set of coordinates

set_1 = range(4)
set_2 = range(4)

for x in set_1:
    for y in set_2:
        print(f"({x},{y})")

#first the code runs line 7 and then for each item in set_1, it picks an item in set_2, then after it is done, it picks the next item in set_1 and runs over or iterates the items in set_2
