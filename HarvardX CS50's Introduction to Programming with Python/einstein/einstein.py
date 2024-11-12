def main():
    m = int(input("m: "))
    calc(m)


def calc(mass):
    c = 300000000
    E = mass * c**2

    print(f"E: {E}")

main()