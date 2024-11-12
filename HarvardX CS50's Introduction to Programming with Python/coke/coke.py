price = 50
coin = 0

print(f"Amount Due: {price}")
while coin < price:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        coin += insert_coin

    amount_due = price - coin

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

change_owed = coin - price
print(f"Change Owed: {change_owed}")