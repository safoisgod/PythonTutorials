#A program that finds the largest number in a list#

numbers = [2,15,7,34,10,5]
max = 0

for number in numbers:
    if number > max:
        max = number
print(max)

