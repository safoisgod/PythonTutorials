#used for situations with multiple conditions
#the logical operators are AND and OR and NOT

#a school system where you need to pay your fees and pass exams to graduate

paid_fees = False
passed_exams = True

if passed_exams and paid_fees:
    print("You are eligible for the 2021 graduation")
elif paid_fees:
    print("You need to write a resit in order to qualify for graduation")
elif passed_exams:
    print("You need to pay fees in full in order to qualify for graduation")
else:
    print("You are not eligible for the 2021 graduation")

print('''


''')
#using OR operator
paid_fees = True
passed_exams = True

if passed_exams and paid_fees:
    print("You are eligible for the 2021 graduation")
elif passed_exams or paid_fees:
    print("Visit the office of the DOS")
else:
    print("You are not eligible for the 2021 graduation")

print('''


''')

#using NOT operator
paid_fees = False
passed_exams = True

if passed_exams and not paid_fees:
    print("Go pay your fees at the administration")
