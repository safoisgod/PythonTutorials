def main():
    time = input("What time is it? ")
    converted = convert(time)
    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")


def convert(time):
    x,y = time.split(":")
    decimal_hours = float(x) + float(y)/60

    return decimal_hours


if __name__ == "__main__":
    main()