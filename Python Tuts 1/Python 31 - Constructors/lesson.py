#define a person with a name attribute and a talk method

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(f"Good morning {self.first_name}")

    def sleep(self):
        print("'snooring😴'")


person_1 = Person("Nana", "Safo")
person_2 = Person("Efua", "Asantewaa")

print(person_2.last_name)
person_2.greet()