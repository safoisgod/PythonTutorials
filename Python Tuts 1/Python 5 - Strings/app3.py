#extra things that can be done with strings
name = "Nana Kwesi Safo"
#calculating number of characters in the string using LEN
#usually used in controlling thew amount of characters that the code can accept
print(len(name))

#the dot operators
#these operators are all case sensite as such strings involve should maintain their cases at all times
#convert characters to Upper case
print(name.upper())

#finding a character in a string
#the case sensitivity returns different figures for N and n as they are seen as two different characters
print(name.find("n"))
print(name.find("N"))
print(name.find("Safo"))

#replacing characters in a string
print(name.replace("Nana", "King"))

#expressing to see in a character is in the variable, NAME
print("Nana" in name)
#returns a BOOLEAN, while FIND returns the index
