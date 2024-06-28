#used when there are too many variables being used in a single dstring
#eg
first_name = "Nana"
middle_name = "Kwesi"
last_name = "Safo"
age = "20"

print(age * 20)

#ideally, this is how we will write "Nana Kwesi Safo is 20 years old"
#this is string concatenation
output = first_name + ' ' + middle_name + ' ' + last_name + " is " + age + "years old"
print(output)

#instead, to make it much simpler , we use fromattted strings
output_2 = f"{first_name} {middle_name} {last_name} is {age} years old"
print(output_2)

