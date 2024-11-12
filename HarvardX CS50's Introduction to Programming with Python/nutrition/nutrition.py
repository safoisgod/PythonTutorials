dictt = {"apple": 130,
         "avocado": 50,
         "sweet cherries": 100,
         "banana": 110,
         "kiwifruit" : 90,
         "pear" : 100
         }
item = input("Item: ").lower()

for k in dictt:
    if k == item:
        print(f"Calories: {dictt.get(k)}")
    else:
        pass
