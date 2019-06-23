names = ["Dick", "Cock", "Pussy"]
for name in names:
    print(name)
#array in Python


def dicksquare(x):
    return x*x #return a square of the input
for i in range(155):
    print("{} dicksquared is {}".format(i, dicksquare(i))) #append variables to placeholders

#importig a function from another file
from funcs import dicksquare
print (dicksquare(10))


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point (3,5)
print (p.x)
print (p.y)
