# reduce has to be imported from the func tools

from functools import reduce

expenses = [
    ("Food", 25),
    ("Drinks", 40)
]

# ideally for calculating the total expense, the below equation may be used

total = 0

for expense in expenses:
    total += expense[1]  # the second index

print(total)

# reduce takes two arguments...
# the first argument is the accumulated value and the second is the new value

total1 = reduce(lambda a, b: a[1] + b[1], expenses)
print(total1)
