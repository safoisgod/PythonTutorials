#there are built in modules for many works in python
#search for PYTHON 3 MODULE INDEX to get acquainted with the various modules in python

#built in modules are not called out like other modules,
#you just import the module

import random

#this RANDOM.RANDOM generates random values from ZERO to ONE
for i in range(3):
    print(random.random())

#RANDOM.RANDINT generates random integers
#RANDINT object requires two positional integers that give the range of ingeres to pick from
for i in range(3):
    print(random.randint(1,6))

#RANDDOM.CHOICE is used to randomly pick strings
countries = ["Ghana", "South Africa", "Nigeria", "Morocco", "Rwanda"]
holiday = random.choice(countries)
print(holiday)

