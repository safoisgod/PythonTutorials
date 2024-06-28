# filter does a similar work task compared to map
# however, filter like its name indicates, filters the list

number = range(10)


def isodd(a):
    return a % 2 != 0


result = filter(isodd, number)

print(list(result))


#or again, lamba function can be used to simplify the code

result2 = filter(lambda a: a % 2 == 0, number)
print(list(result2))