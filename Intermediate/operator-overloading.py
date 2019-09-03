class Point:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return "(The result is: {0})".format(self.x)

    def __add__(self, other):
        a = self.x + other.x
        return Point(a)

obj = Point(1)
obj1 = Point(3)
print(obj + obj1)
