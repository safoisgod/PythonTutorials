def main():
    a = grocery()
    for i in a:
        word = i.upper()
        print (f"{a[i]} {word}")


def grocery():
    the_list = []
    d = {}
    try:
        while True:
            the_input = input()
            the_list.append(the_input)
    except EOFError:
        the_list.sort()
        for i in the_list:
            d.update({str(i): the_list.count(i)})
        return d

main()
