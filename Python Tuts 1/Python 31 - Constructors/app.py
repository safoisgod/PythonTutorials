#CONSTRUCTORS are called whenever you create an bject
#like an ARGUMENT and PLACEHOLDERS

class Point:
#we use the initialize function#
#INIT
#you add the components or ATTRIBUTES of the OBJECT
    def __init__(self, x, y):
#TAKE the point.x = 10
#         self.s = x
        self.x = x
        self.y = y

    def link(self):
        print("Point created")

    def move(self):
        print("Point moved")

    def draw(self):
        print("Point drawn")


point = Point(5,13)
print(point_1.x)