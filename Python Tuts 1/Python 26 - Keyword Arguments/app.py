#with the def function, the parameters are positional
#AS SUCH THE ARGUMENTS POSITIONS ALSO MATTER
#it is refer to as positional argument
#THAT IS, if the ARGUMENTS, NANA and SAFO are interchanged, the program will then recognise NANA as the LAST_NAME and SAFO as the FIRST_NAME

def user_greeting(first_name, last_name):
    print(f"My name is {first_name} {last_name}")
    print("I am happy to be here")

print("Welcome Address")
user_greeting("Safo", "Nana")
print("Thank you")

print('''

''')
#The KEYWORD ARGUMENT, helps to address this
#it aloows the programmer to ASSIGN the placeholder to its corresponding ARGUMENT

def user_greeting(first_name, last_name):
    print(f"My name is {first_name} {last_name}")
    print("I am happy to be here")

print("Welcome Address")
user_greeting(last_name="Safo", first_name="Nana")
print("Thank you")