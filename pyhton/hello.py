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
