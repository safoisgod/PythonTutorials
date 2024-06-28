#DICTIONARY stores related information with key value pairs
#the KEY VALUE PAIRS can be NAME, CONTACTS, AGE etc

#TAKE
#Customer details

customer ={
    "name": "Nana Kwesi Safo",
    "age": 21,
    "good_customer": True
}

#each KEY VALUE  can be accessed by SQUARE BRACKETS

print(customer["age"])
#USER can use .GET to ask for existence of the value\
print(customer.get("name"))
print(customer.get("birth_day"))
#.GET can also be used to assign a value to the KEY
#TAKE
print(customer.get("location", "Tema"))
#however, new value isnt included in the main dictionary

#to UPDATE
customer["age"] = 23
print(customer)

#to APPEND or ADD new values to the dis=ctionary
customer["location"] = "Tema"
print(customer)