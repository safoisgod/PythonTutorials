#helps in reusing code
#when two codes are similar but have different CLASSES, you use Inheritence

#so, a main class is defined
#and the sub classes inherit from the main class

class Mammal:
    def walk(self):
        print("walk")

class Man(Mammal):
    pass

class Dog(Mammal):
    def bark(self):
        print("bark")

man_1 = Man()
man_1.walk()

dog_1 = Dog()
dog_1.bark()