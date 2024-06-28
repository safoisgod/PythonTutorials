# MAP, FILTER, REDUCE

# map helps user to run a function over each item on the list
# just like using the for loop to iterate over a list, the map() function iterates a particular function over a list
numbers = [1, 2, 3]


def double(a):
    return a * 2


result = map(double, numbers)
# map list to list out output values
print(list(result))

triple = lambda a: a * 3

result2 = map(triple, numbers)
print(list(result2))

# since the lambda function does not require assignment, it can be quoted directly into the map function

result3 = map(lambda a:a*4, numbers)
print(list(result3))