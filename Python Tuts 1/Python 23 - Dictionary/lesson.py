#a prgram that changes digits to corresponding words

phone_number = input(">>>")

numbers ={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "eight",
    "9": "nine"
}
output = ""

for item in phone_number:
    for number in numbers:
        if item == number:
            output += numbers[number] + " "
#adding the quotes at the end spaces the values obtained
print(output)


for number in phone_number:
    output += numbers.get(number, "unknown") + " "
print(output)