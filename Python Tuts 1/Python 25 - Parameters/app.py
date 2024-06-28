#this is used to pass information into a define function
#it sets up a parameter for which can be defined in the function
#more than one placeholders can be called
def welcome_address(name):
    print(f"My name is {name}")
    print("I am happy to be here")


print("Welcome Address")
welcome_address("Nana Kwesi Safo")
print("Thank you")

print('''

'''
)
#TAKE
#more than one placeholders can be called
def user_greeting(first_name, last_name):
    print(f"My name is {first_name} {last_name}")
    print("I am happy to be here")

name = input("what is your name?: ")
names = name.split(" ")
first_name = names[0]
last_name = names[1]

user_greeting(first_name, last_name)
print("Thank you")
