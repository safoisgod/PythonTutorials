greeting = input("Greeting: ").lower().strip()

if greeting[0:5] == "hello": # the box backet calls out the values of each index, from index 0 to index 5 of the greeting variable and compares it to each index in the str "hello"
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print ("$100")