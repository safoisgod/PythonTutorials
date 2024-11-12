
def main():
    ask = input("Input: ")
    converted = convert(ask)

    print(f"Output : {converted}")

def convert(tweet):
    the_output = ""
    vowels = ["a","o","e","i","u", "A", "O", "E", "I", "U"]
    for i in tweet:
        if i not in vowels:
            the_output += i

    return the_output

main()

