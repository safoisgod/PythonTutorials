def main():
    the_fuel = fuel()
    print(the_perc(the_fuel))


def fuel():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x,y = int(x),int(y)
            if x>y:
                y=0
            return (x / y)*100
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def the_perc(x):
    x = round (x)
    if x <= 10:
        return "E"
    elif x >= 90:
        return "F"
    else:
        return f"{x}%"

main()
