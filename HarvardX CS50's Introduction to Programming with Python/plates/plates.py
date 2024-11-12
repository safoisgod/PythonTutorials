import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s)<2 or len(s)>6:
        return False
    elif s[0:2].isdigit():
        return False
    elif not s.isalnum():
        return False

    indexx = len(s)-1
    print (len(s))
    for i in s:
       if i.isdigit():
            if i == "0":
                return False
            indexx = s.index(i)
            break
    for a in s:
        if s.index(a) <= indexx:
            pass
        elif a.isalpha():
                return False

    return True


main()
