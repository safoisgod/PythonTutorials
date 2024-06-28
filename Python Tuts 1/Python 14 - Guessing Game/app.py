#Using a while loop to build a guessing game
#you have three guesses

secret_number = 3
guess_count = 0

while guess_count != 3:
    guesses = int(input("Guess: "))
    guess_count += 1
    if guesses == secret_number:
        print("Well Done, You guessed right!!!")
        break
else:
    print("You failed!!!")

print("Bye")