#an online application that takes the name of the applicant
#if name is less than 5 characters, the program has to prompt the applicant
#if name is moree than 30 characters, the program has to prompt the applicant

name = input("name: ")

if len(name) < 5:
    print("name must be at least 5 characters")
elif len(name) > 30:
    print("name can be a maximum of 30 characters")
else:
    print("Name looks good!!!")