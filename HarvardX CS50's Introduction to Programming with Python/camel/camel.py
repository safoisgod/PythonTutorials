camelCase = input("camelCase: ")


snake_case = ""
for i in camelCase:
    if i.isupper():
        i = i.lower()
        snake_case += "_" + i
    else:
        snake_case += i
print(snake_case)tw