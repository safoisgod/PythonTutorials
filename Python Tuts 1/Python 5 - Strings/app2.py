# indexing the charaters in a string
name = "Nana Kwesi Safo"
# for indexing, as in pinpointing a particular character from a string, the first character is 0
print(name[0])
print(name[7])
# you can also index from the last character by using negatives
print(name[-9])
print(name[-1])

# indexing a couple of characters
print(name[0:6])
#as seen above, python returns the the first character to the 6th ca]haracter without adding the actual 6th index
#leaving out the start will program code to return from the start to the end
print(name[:9])
