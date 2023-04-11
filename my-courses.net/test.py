from math import pi


class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def perimeter (self):
        return  2 * pi * self.r


    def area (self):
        return  pi * self.r**2
    

    # form of the cercle equation 
    def formEquation (self, x, y):
        return (x-self.a)**2 + (y-self.b)**2 - self.r**2
    
    # method to test if given point blong to the circle or not 
    def test_belong (self, x, y):
        if (self.formEquation (x, y) == 0):
            print ("the point: (", x, y, ") belongs to the circle C")
        else:
            print ("the point: (", x, y, ") does not belong to the circle C")


# Creating of an instance object
c = Circle (0,0,10)

c.test_belong(5, -8)