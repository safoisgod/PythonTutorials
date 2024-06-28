#program where user enters weight and species unit, the program converts it to other unit

weight = input("Weight: ")
print("Specify whether '(K)g' or '(L)bs'")
unit = input("Unit: ")

if unit.upper() == "K":
    output = f"{int(weight) * 2.205}lbs"
elif unit.upper() == "L":
    output = f"{int(weight) / 2.205}kg"
else:
    output = "Wrong Command!!!"
print(output)