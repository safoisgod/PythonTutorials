#produce two random number between 1 and 6
import random

x = random.randint(1,6)
y = random.randint(1,6)

print(f"({x},{y})")

#USING CLASSES

class DiceRoll:
    def roll(self):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return (x, y)

dice_1 = DiceRoll()
print(dice_1.roll())