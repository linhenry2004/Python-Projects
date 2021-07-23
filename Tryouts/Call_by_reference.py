#Classes and arrays are all call by Call_by_reference
import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius

def main():
    c1 = Circle()
    print('Radius of c1 is %2d and area is %6.2f' %(c1.radius, c1.getArea()))

    c2 = c1
    print('Radius of c2 is %2d and area is %6.2f' %(c2.radius, c2.getArea()))

    c2.setRadius(5)
    print('Radius of c1 is %2d and area is %6.2f' %(c1.radius, c1.getArea()))
    print('Radius of c2 is %2d and area is %6.2f' %(c2.radius, c2.getArea()))

main()
