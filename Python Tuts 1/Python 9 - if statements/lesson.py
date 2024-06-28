# a propeerty of 1million is to be sold
#if buyer has good credit, he makes downpayment of 10%
#if not he puts down 20%
#print Downpayment

has_good_credit = False
price = 1000000

if has_good_credit:
    print(f"Downpayment is ${price * 0.1}")
else:
    print(f"Downpayment is ${price * 0.2}")

#OR
print('''


''')
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2

print(f"Down payment = ${down_payment}")