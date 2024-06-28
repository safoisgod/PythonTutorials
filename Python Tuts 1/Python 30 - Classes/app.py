#CLASSES are user created methods
#like the dot method, Classes are used to define methods that are USER-DEFINED....lol

#CLASSES use the PascalNamingConvension
#Each word is Capitalised

#CLASSES are used together with the DEF function

class Point:
    def link(self):
        print("Point created")

    def move(self):
        print("Point moved")

    def draw(self):
        print("Point drawn")

#to create an object, we call the class
#then we save that object in a variable

point_1 = Point()
#the objects can have attributes
#such as X and Y
#these attributes may uniquely differential two OBJECTS
point_1.x = 1
point_1.y = 23
print(point_1.x)
point_1.draw()


#more of these OBJECTS can be created with different attributes
point_2 = Point()
point_2.x =19
print(point_2.x)