#when you have an exit code of 0, it means programme was successful
#Exit code 1 means programme crashed

#now to prevent errors, you use TRY EXCEPT
#this allows exceptions, where even in the case of a crash, programme still produces
#helps handle errors

#TAKE for instance a programme which requires you to enter an INTEGER
#if the user enders an INVALID value, the program crashes and reports a Value Error

#the TRY EXCEPT function, helps to anticipate errors and create exceptions

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid Value")

#try
#take same code where there has to be a division
try:
    age = int(input("Age: "))
    income = 2000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid Value")
#In the case where the age inputted by user is ZERO, the programme will crash due to the ZeroDivisionError
#to prevent that, we add another EXCEPTION
except ZeroDivisionError:
    print("Age cannot be Zero")
