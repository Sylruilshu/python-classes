
class Circle:

    def __init__(self, a, b, r):         
        self.a = a         
        self.b = b         
        self.r = r

    def area(self):
        area = 3.14 * self.r**2
        return area

    def circumference(self):
        circumference = 2 * 3.14 * self.r
        return circumference

    def test_belongs(self, x, y):
        # Equation of circle: x**2 + y**2 = r**2
        # d^2 = (xp−xc)^2 + (yp−yc)^2
        # Distance between center point (xc, yc) and given point (xp, yp).

        d_squared = (x - self.a)**2 + (y - self.b)**2

        r_squared = self.r**2
    
        if d_squared < r_squared:
            return f"The point ({x}, {y}) is inside the circle"

        if d_squared == r_squared:
            return f"The point ({x}, {y}) is on the circle"

        if d_squared > r_squared:
            return f"The point ({x}, {y}) is outside the circle"


circle = Circle(0, 0, 10)

print(f"The area of the circle is: {circle.area()}")
print(f"The circumference of the circle is: {circle.circumference()}")
print(circle.test_belongs(5, -8))
print(circle.test_belongs(-10, 0))
print(circle.test_belongs(11, 5))